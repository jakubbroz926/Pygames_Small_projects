import cv2
import matplotlib.pyplot as plt


def intro():
    print("""Welcome.
This program will help you change your pictures, by 
adjusting his colors and brightness !!!\n""")

    while True:
        try:
            image = input("At first type the name of the image to the console:")
            cv2.imshow("Your picture", image)
            cv2.waitKey(0)
            cv2.destroyWindow("Your picture")
            print("""In image manipulation you have these possibilities:
                At first you have to decide, if you want to change color or brightness.""")
        except IOError:
            print("""Probably picked image, which is not in this directory or
             you could type incorrect way.
             It should look like this : c/folder/n-folder/image.jpg etc.\n
             """)
        else:
            print("Your picture was picked and is prepared for changes.")
            break
    return image
def choices(img):


def main():
    img = intro()


if __name__ == "__main__":
    main()