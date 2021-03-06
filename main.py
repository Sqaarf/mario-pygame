import pygame

pygame.init()

win = pygame.display.set_mode((600,400))
pygame.display.set_caption('Mario')

img_path = './assets/'
bg = pygame.image.load(img_path+'bg.png')

mario_right = [pygame.image.load(img_path+"w_0.png").convert_alpha(),
	       pygame.image.load(img_path+"w_0.png").convert_alpha(),
               pygame.image.load(img_path+"w_1.png").convert_alpha(),
               pygame.image.load(img_path+"w_1.png").convert_alpha(),
               pygame.image.load(img_path+"w_2.png").convert_alpha(),
               pygame.image.load(img_path+"w_2.png").convert_alpha(),
               pygame.image.load(img_path+"w_3.png").convert_alpha(),
               pygame.image.load(img_path+"w_3.png").convert_alpha()]

mario_left = [pygame.image.load(img_path+"wl_0.png").convert_alpha(),
              pygame.image.load(img_path+"wl_0.png").convert_alpha(),
              pygame.image.load(img_path+"wl_1.png").convert_alpha(),
              pygame.image.load(img_path+"wl_1.png").convert_alpha(),
              pygame.image.load(img_path+"wl_2.png").convert_alpha(),
              pygame.image.load(img_path+"wl_2.png").convert_alpha(),
              pygame.image.load(img_path+"wl_3.png").convert_alpha(),
              pygame.image.load(img_path+"wl_3.png").convert_alpha()]

rindex = 0
lindex = 0
is_right = True
vel = 5

FPS = 30 #Change if you want to speed up the animation
run = True

x = 0
y = 323
hitbox = mario_right[0].get_rect() #All images have the same dimensions

def commands():
    global run, x, y, rindex, lindex, is_right
    keys = pygame.key.get_pressed()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
    
    if keys[pygame.K_RIGHT]:
        is_right = True
        x += vel
        rindex += 1
    if not keys[pygame.K_RIGHT]:
        rindex = 0

        if keys[pygame.K_LEFT]:
            is_right = False
            x -= vel
            lindex += 1
        if not keys[pygame.K_LEFT]:
            lindex = 0
        
def render():
    global rindex, lindex
    win.blit(bg,(0, 0))
    if is_right:
        win.blit(mario_right[rindex], (x,y))
        if rindex >= len(mario_right) - 1:
            rindex = 0
    else:
        win.blit(mario_left[lindex], (x,y))
        if lindex >= len(mario_left) - 1:
            lindex = 0
    

while run:
    pygame.time.Clock().tick(FPS)
    commands()
    render()
    #print(hitbox)
    pygame.display.update()

pygame.quit()
