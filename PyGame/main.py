import pygame

from Framework.sceneManager import SceneManager
from Framework.simpleImage import SimpleImage

from Scenes.mainScene import MainScene

if __name__ == '__main__' :
    pygame.init()
    pygame.display.set_caption("DL-Engine")
    pygame.display.set_icon(SimpleImage("Resources/Images/Icon/icon.png").getSurface())
    pygame.mixer.pre_init(44100, 16, 2, 4096) #Frequency, Size, Channels, BufferSize

    screen = pygame.display.set_mode((720, 720))
    clock = pygame.time.Clock()
    run = True
    
    SceneManager.getInstance().registerGameObjects(screen, clock)
    SceneManager.getInstance().registerScene("MainScene", MainScene(screen,clock))
    SceneManager.getInstance().changeScene("MainScene")

    while run:
        SceneManager.getInstance().update()
        
        pygame.display.flip()
        clock.tick(144)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        if SceneManager.getInstance().isQuit :
            run = False

    pygame.quit()
