# Pro/g/ramming challenge # 83
# Simple paint program
import pygame, sys
from pygame.locals import *

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Ruggles Paint')
    
    try:
        imageName = sys.argv[1]
    except IndexError:
        print "Please supply a name for the image file"
        raise IndexError
        
    try:
        imgSurf = pygame.image.load(imageName)
        DISPLAYSURF.blit(imgSurf, (0,0))
    except pygame.error:
        print "Image does not exist"
    
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    mouseColor = RED
    
    while True:
        for event in pygame.event.get():
        
            # if rmb is pushed, save image
            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                pygame.image.save(DISPLAYSURF, imageName)
                print "Image Saved", imageName
            
            # if lmb is held down
            if pygame.mouse.get_pressed()[0]:
                mouseX, mouseY = pygame.mouse.get_pos()
                pixArray = pygame.PixelArray(DISPLAYSURF)
                pixArray[mouseX][mouseY] = mouseColor
                del pixArray
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()
    
if __name__ == '__main__': main()
