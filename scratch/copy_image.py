import shutil
import os

src = r"c:\Users\saimo\Documents\Fig.png"
dst = r"c:\Users\saimo\OneDrive\ドキュメント\Desktop\Projects\evision-telangana\frontend\src\assets\fig.png"

# Ensure destination directory exists
os.makedirs(os.path.dirname(dst), exist_ok=True)

try:
    shutil.copy(src, dst)
    print("Success: Copied Fig.png to frontend/src/assets/fig.png")
except Exception as e:
    print(f"Error: {e}")
