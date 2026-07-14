import pandas as pd
import numpy as np
import json
import joblib
import os
from sklearn.model_selection import TimeSeriesSplit, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import warnings

warnings.filterwarnings('ignore')

def load_and_prepare_data(filepath):
    df = pd.read_csv(filepath)
    
    # Sort chronologically and by location
    df = df.sort_values(by=['latitude', 'longitude', 'year', 'month'])
    
    # Create target (Option B: Forecast next month's demand)
    df['target'] = df.groupby(['latitude', 'longitude'])['units'].shift(-1)
    
    # Drop rows where target is NaN (the last month for each district)
    df = df.dropna(subset=['target'])
    
    # Drop features that would cause target leakage or aren't useful for regression
    leakage_cols = ['units', 'cumulative_units']
    df = df.drop(columns=[col for col in leakage_cols if col in df.columns])
    
    # Sort strictly chronologically for the train/test split
    df = df.sort_values(by=['year', 'month'])
    
    return df

def split_data(df, train_ratio=0.8):
    # Chronological split
    split_index = int(len(df) * train_ratio)
    
    train_df = df.iloc[:split_index]
    test_df = df.iloc[split_index:]
    
    # Features and targets
    X_train = train_df.drop(columns=['target'])
    y_train = train_df['target']
    
    X_test = test_df.drop(columns=['target'])
    y_test = test_df['target']
    
    return X_train, y_train, X_test, y_test, test_df

def train_and_evaluate():
    data_path = '../data/processed/ml_training_dataset.csv'
    models_dir = '../models'
    
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)
        
    print("Loading and preparing data...")
    df = load_and_prepare_data(data_path)
    
    print("Splitting data chronologically...")
    X_train, y_train, X_test, y_test, test_df = split_data(df)
    
    print(f"Train size: {len(X_train)}, Test size: {len(X_test)}")
    
    tscv = TimeSeriesSplit(n_splits=5)
    
    models = {
        'RandomForest': {
            'estimator': RandomForestRegressor(random_state=42),
            'param_grid': {
                'n_estimators': [50, 100, 200],
                'max_depth': [None, 10, 20],
                'min_samples_split': [2, 5, 10]
            }
        },
        'XGBoost': {
            'estimator': XGBRegressor(random_state=42, objective='reg:squarederror'),
            'param_grid': {
                'n_estimators': [50, 100, 200],
                'max_depth': [3, 6, 9],
                'learning_rate': [0.01, 0.1, 0.2]
            }
        }
    }
    
    best_models = {}
    metrics = {}
    
    for name, config in models.items():
        print(f"Training {name}...")
        grid = GridSearchCV(
            estimator=config['estimator'],
            param_grid=config['param_grid'],
            cv=tscv,
            scoring='neg_mean_squared_error',
            n_jobs=-1
        )
        grid.fit(X_train, y_train)
        
        best_model = grid.best_estimator_
        best_models[name] = best_model
        
        # Evaluate
        predictions = best_model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, predictions))
        mae = mean_absolute_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        
        metrics[name] = {
            'rmse': rmse,
            'mae': mae,
            'r2': r2,
            'best_params': grid.best_params_
        }
        
        print(f"{name} Results - RMSE: {rmse:.2f}, MAE: {mae:.2f}, R2: {r2:.2f}")

    # Select best model based on RMSE
    best_model_name = min(metrics, key=lambda k: metrics[k]['rmse'])
    final_best_model = best_models[best_model_name]
    print(f"\nBest Model: {best_model_name}")
    
    # Save best model
    joblib.dump(final_best_model, os.path.join(models_dir, 'best_model.joblib'))
    
    # Save metrics
    with open(os.path.join(models_dir, 'metrics.json'), 'w') as f:
        json.dump(metrics, f, indent=4)
        
    # Feature importance
    if best_model_name == 'RandomForest':
        importances = final_best_model.feature_importances_
    else:
        importances = final_best_model.feature_importances_
        
    fi_df = pd.DataFrame({
        'feature': X_train.columns,
        'importance': importances
    }).sort_values('importance', ascending=False)
    
    fi_df.to_csv(os.path.join(models_dir, 'feature_importance.csv'), index=False)
    
    # Generate Report
    report_path = os.path.join(models_dir, 'training_report.md')
    with open(report_path, 'w') as f:
        f.write("# ML Training Report\n\n")
        f.write("## Overview\n")
        f.write("This report documents the results of training the EV charging demand forecasting model. ")
        f.write("Based on architectural review, the model is designed to forecast **next month's demand** (Option B).\n\n")
        
        f.write("## Dataset Changes\n")
        f.write("- **Target Definition:** `target = units.shift(-1)` per district.\n")
        f.write("- **Rows Removed:** The final observation for each of the 32 districts was dropped due to missing shifted targets.\n")
        f.write("- **Data Split:** A chronological split (80% train, 20% test) was used instead of random shuffling to prevent temporal data leakage.\n\n")
        
        f.write("## Model Comparison\n")
        f.write("| Model | RMSE | MAE | R² |\n")
        f.write("|---|---|---|---|\n")
        for name, res in metrics.items():
            f.write(f"| {name} | {res['rmse']:.2f} | {res['mae']:.2f} | {res['r2']:.4f} |\n")
            
        f.write(f"\n## Recommendation\n")
        f.write(f"**{best_model_name}** achieved the lowest RMSE and is recommended as the production model.\n")
        
    print("Pipeline complete.")

if __name__ == "__main__":
    train_and_evaluate()
