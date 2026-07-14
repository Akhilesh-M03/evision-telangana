import os
import joblib
import pandas as pd
import shap
import matplotlib.pyplot as plt
import numpy as np

# Import data processing from the training script
import sys
sys.path.append(os.path.dirname(__file__))
from train_model import load_and_prepare_data, split_data

def generate_shap_explanations():
    data_path = '../data/processed/ml_training_dataset.csv'
    model_path = '../models/best_model.joblib'
    models_dir = '../models'
    
    if not os.path.exists(model_path):
        print(f"Error: Model not found at {model_path}. Please run train_model.py first.")
        return
        
    print("Loading model and data...")
    model = joblib.load(model_path)
    df = load_and_prepare_data(data_path)
    X_train, y_train, X_test, y_test, test_df = split_data(df)
    
    print("Computing SHAP values...")
    # Use TreeExplainer for tree-based models like XGBoost/Random Forest
    explainer = shap.TreeExplainer(model)
    shap_values = explainer(X_test)
    
    print("Generating SHAP summary plot...")
    plt.figure(figsize=(10, 8))
    shap.summary_plot(shap_values, X_test, show=False)
    plt.tight_layout()
    plot_path = os.path.join(models_dir, 'shap_summary.png')
    plt.savefig(plot_path, dpi=300)
    plt.close()
    
    print(f"SHAP summary plot saved to {plot_path}")
    
    # Calculate average absolute SHAP values to rank features
    # shap_values.values is a 2D numpy array of shape (n_samples, n_features)
    mean_abs_shap = np.abs(shap_values.values).mean(axis=0)
    shap_df = pd.DataFrame({
        'feature': X_test.columns,
        'mean_abs_shap': mean_abs_shap
    }).sort_values(by='mean_abs_shap', ascending=False)
    
    shap_csv_path = os.path.join(models_dir, 'shap_feature_importance.csv')
    shap_df.to_csv(shap_csv_path, index=False)
    print(f"SHAP feature importances saved to {shap_csv_path}")
    
    # Print summary
    print("\nTop 10 features by SHAP value magnitude:")
    print(shap_df.head(10).to_string(index=False))

if __name__ == "__main__":
    generate_shap_explanations()
