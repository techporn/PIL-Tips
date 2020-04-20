from PIL import Image, ImageFilter

def gray(img):
    return img.convert("L")

def gray_a(img):
    return img.convert("LA")

def change_brightness(img, rate):
    return img.point(lambda x: x * rate)

def mosa(img, D=8):
    gimg = img.filter(ImageFilter.GaussianBlur(4))
    return gimg.resize([x // D for x in img.size]).resize(img.size)
    # gimg.save("{}{}".format(D, path))
    

def main():
    filename = "imgs/src.png"
    img = Image.open(filename)
    gray(img).save("imgs/dst_gray.png")
    gray_a(img).save("imgs/dst_gray_a.png")
    change_brightness(img, 1.5).save("imgs/dst_change_brightness.png")
    mosa(img).save("imgs/dst_mosa.png")

if __name__ == "__main__":
    main()