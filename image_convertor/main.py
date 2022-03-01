def main():
    print("""Welcome.
This program will help you change your pictures, by 
adjusting his colors and brightness !!!\n""")

    while True:
        try:
            name_of_img = input("At first type the name of the image to the console:")
            img = open(name_of_img)
        except IOError:
            print("""Probably picked image, which is not in this directory or
             you could type incorrect way.
             It should look like this : c/folder/n-folder/image.jpg etc.\n
             """)
        else:
            print("Your picture was picked and is prepared for changes.")
            break


if __name__ == "__main__":
    main()