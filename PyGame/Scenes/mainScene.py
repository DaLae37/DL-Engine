import pygame
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Framework.scene import Scene
from Framework.sceneManager import SceneManager
from Framework.soundManager import SoundManager

class MainScene(Scene) :

    simpleImage_list = []

    def __init__(self, screen, clock) :
        self.screen = screen
        self.clock = clock

        self.load_resources()

    def update(self) :
        for si in self.simpleImage_list :
            self.screen.blit(si.getSurface(), si.getPos())

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                SceneManager.getInstance().isQuit = True
                return

            if event.type == pygame.MOUSEBUTTONDOWN :
                if self.chessButton.isCollisionRect(pygame.mouse.get_pos()) :
                    print("마우스 버튼 클릭")
                    return

    def load_resources(self) :
        SoundManager.getInstance().load_music("Resources/Sounds/BGM.mp3")
