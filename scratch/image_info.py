from PIL import Image

img_path = r"c:\Users\saimo\OneDrive\ドキュメント\Desktop\Projects\evision-telangana\frontend\src\assets\fig.png"
with Image.open(img_path) as im:
    print(f"Dimensions: {im.size}")
    print(f"Format: {im.format}")
    print(f"Mode: {im.mode}")
