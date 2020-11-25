import pygame
import time
from pygame import Surface
from pygame.color import Color
from pygame.sprite import Sprite

class Animation(Sprite) :
    def __init__(self, images, frames):
        Sprite.__init__(self)
        self.clock = pygame.time.Clock()

        self.images = list()
        self.frames = frames
        self.beforeTime = 0

        for i in images :
            self.images.append(pygame.image.load(i))

        self.image_count = len(images)
        self.current_frame = 0
        self.image = self.images[self.current_frame]

        self.rect = pygame.Rect(0, 0, self.image.convert().get_width(), self.image.convert().get_height())

    def update(self):
        if time.time() - self.beforeTime > 1 / self.frames :
            if self.current_frame is self.image_count -1 :
                self.current_frame = 0
            else:
                self.current_frame += 1
            self.image = self.images[self.current_frame]
            self.beforeTime = time.time()

    def setPos(self, pos) :
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def addPos(self, pos) :
        self.rect.x += pos[0]
        self.rect.y += pos[1]

    def getPos(self) :
        return (self.rect.x, self.rect.y)

    def getSize(self) :
        return self.image.get_size()

    def getSurface(self) :
        return self.image

    def isCollisionRect(self, pos) :
        left_x = self.getPos()[0]
        left_y = self.getPos()[1]
        right_x = self.getPos()[0] + self.getSize()[0]
        right_y = self.getPos()[1] + self.getSize()[1]

        return left_x <= pos[0] and left_y <= pos[1] and right_x >= pos[0] and right_y >= pos[1]

    def getTag(self) :
        return "Animation"
