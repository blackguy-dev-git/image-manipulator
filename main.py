import numpy as np
from PIL import Image
img = Image.open(r"C:\Users\moiz3\image maniuplator\56afaa04bf2745345b714ed273cef7ea.jpg")
img_arr = np.array(img)
def conver_gray():
    def grav(i):
        g1 = i[0]*0.299
        g2 = i[1]*0.587
        g3 = i[2]*0.114
        gra = g1+g2+g3
        return gra
    gray_arr = np.zeros((img_arr.shape[0], img_arr.shape[1]), dtype=np.uint8)

    for row in range(img_arr.shape[0]):
        for i in range(img_arr.shape[1]):
            gray_arr[row, i] = grav(img_arr[row, i])

            gray_img = Image.fromarray(gray_arr)
            gray_img.save("grav.png")
            gray_img.show()

def brightness():
    def bright(f):
        b1 = f[0] + 50
        b2 = f[1] + 50
        b3 = f[2] + 50
        return np.clip([b1, b2, b3], 0, 255)

    bri_arr = np.zeros(img_arr.shape, dtype=np.uint8)

    for row in range(img_arr.shape[0]):
        for f in range(img_arr.shape[1]):
            bri_arr[row, f] = bright(img_arr[row, f])

    bright_img = Image.fromarray(bri_arr)
    bright_img.save("bright.png")
    bright_img.show()
def inversion():
    def inverse(u):
        inv1 = 255 - u[0]
        inv2 = 255 - u[1]
        inv3 = 255 - u[2]
        return np.clip([inv1,inv2,inv3], 0, 255)
    inve_arr = np.zeros(img_arr.shape, dtype=np.uint8)
    for row in range(img_arr.shape[0]):
            for u in range(img_arr.shape[1]):
                inve_arr[row,u] = inverse(img_arr[row,u])
    invers_img = Image.fromarray(inve_arr)
    invers_img.save("inverse.png")
    invers_img.show()
inversion()
def flip():
    flipped_arr = np.flip(img_arr, axis=1)
    flipped_img = Image.fromarray(flipped_arr)
    flipped_img.save("flipped.png")
    flipped_img.show()
inp = input("enter what function u want to perfome on image")
if inp == "gray":
    conver_gray()
elif inp == "bright":
    brightness()
elif inp == "inverse":
    inversion()
elif inp == "flip":
    flip()   
