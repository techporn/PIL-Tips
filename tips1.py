
def gray(img):
    return img.convert("L")

def gray_a(img):
    return img.convert("LA")

def change_brightness(img, rate):
    return img.point(lambda x: x * rate)

def mosa(path):
    img = Image.open(path)
    gimg = img.filter(ImageFilter.GaussianBlur(4))
    return gimg.resize([x // D for x in img.size]).resize(img.size)
    # gimg.save("{}{}".format(D, path))
    