from PIL import Image

src_path = r"c:\Users\saimo\OneDrive\ドキュメント\Desktop\Projects\evision-telangana\frontend\src\assets\fig.png"
dst_path = r"c:\Users\saimo\OneDrive\ドキュメント\Desktop\Projects\evision-telangana\frontend\src\assets\fig_clean_both.png"

with Image.open(src_path) as im:
    width, height = im.size
    out = im.copy()
    pixels = out.load()
    
    # 1. Clean the left side text
    for y in range(height):
        if y < 580:
            target_x_left = 760
        else:
            target_x_left = 540
            
        r, g, b = im.getpixel((target_x_left, y))
        for x in range(target_x_left):
            pixels[x, y] = (r, g, b)
            
    # 2. Clean the right side cards (below the top leaves)
    # Cards start around y=150 and go down.
    # The charger ends around x=1230, so x=1245 is a clean background column.
    target_x_right = 1245
    for y in range(height):
        if y >= 150:
            r, g, b = im.getpixel((target_x_right, y))
            for x in range(target_x_right, width):
                pixels[x, y] = (r, g, b)
                
    out.save(dst_path)
    print("Cleaned both left and right sides successfully!")
