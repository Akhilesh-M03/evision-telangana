from PIL import Image

src_path = r"c:\Users\saimo\OneDrive\ドキュメント\Desktop\Projects\evision-telangana\frontend\src\assets\fig.png"
dst_path = r"c:\Users\saimo\OneDrive\ドキュメント\Desktop\Projects\evision-telangana\frontend\src\assets\fig_clean_left.png"

with Image.open(src_path) as im:
    width, height = im.size
    out = im.copy()
    pixels = out.load()
    
    # x = 540 is before the car bumper, so copying this column to the left
    # should cleanly cover all the left text and logo.
    target_x = 540
    
    for y in range(height):
        r, g, b = im.getpixel((target_x, y))
        for x in range(target_x):
            pixels[x, y] = (r, g, b)
            
    out.save(dst_path)
    print("Cleaned left side with target_x = 540")
