import pygame


def main():
    pygame.init()
    logo = pygame.image.load("mage_logo.jpg")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Tournament of mages")
    screen = pygame.display.set_mode((1280,640))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()