# Pro/g/ramming challenge # 83
# Simple paint program
import pygame, sys
from pygame.locals import *

def isFile(fileName):
    pass
    
def openImage(fileName):
    pass
    
def createImage(fileName):
    pass
    
def renderImage(imageObject):
    pass
    
def mouseInput(sysInput):
    pass
    
class paintCursor(object):
    def __init__(self):
        pass
    def color(self):
        pass
    def draw(self, imageObject, (x,y)):
        pass
        
def saveFile(imageObject):
    pass
    
def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Ruggles Paint')
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()
    
if __name__ == '__main__': main()
