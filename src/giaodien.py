import pygame
#button go hereee


# initialize game engine
pygame.init()

window_width=500
window_height=500

animation_increment=10
clock_tick_rate=20

# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("Nhận diện khuôn mặt")

dead=False

clock = pygame.time.Clock()

background_image1 = pygame.image.load("bg.png")
resized_background = pygame.transform.scale(background_image1, (window_width, window_height))
while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
	
   
    screen.blit(resized_background, [0, 0])

    pygame.display.flip()
    clock.tick(clock_tick_rate)