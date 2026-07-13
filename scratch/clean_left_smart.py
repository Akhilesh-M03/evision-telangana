from PIL import Image

src_path = r"c:\Users\saimo\OneDrive\ドキュメント\Desktop\Projects\evision-telangana\frontend\src\assets\fig.png"
dst_path = r"c:\Users\saimo\OneDrive\ドキュメント\Desktop\Projects\evision-telangana\frontend\src\assets\fig_clean_left.png"

with Image.open(src_path) as im:
    width, height = im.size
    out = im.copy()
    pixels = out.load()
    
    for y in range(height):
        if y < 580:
            # Sky region: text goes further right (up to x=760)
            target_x = 760
        else:
            # Ground/car region: avoid stretching the car bumper
            target_x = 540
            
        r, g, b = im.getpixel((target_x, y))
        for x in range(target_x):
            pixels[x, y] = (r, g, b)
            
    out.save(dst_path)
    print("Cleaned left side using smart height splitting!")
