import shutil

src = r"c:\Users\saimo\OneDrive\ドキュメント\Desktop\Projects\evision-telangana\frontend\src\assets\fig_clean_both.png"
dst = r"c:\Users\saimo\OneDrive\ドキュメント\Desktop\Projects\evision-telangana\frontend\src\assets\hero.png"

try:
    shutil.copy(src, dst)
    print("Successfully replaced frontend/src/assets/hero.png with our cleaned background!")
except Exception as e:
    print(f"Error: {e}")
