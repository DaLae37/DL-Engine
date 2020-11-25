import pygame

class SimpleImage() :

    centerMode = False

    def __init__(self, directory) :
        self.image = pygame.image.load(directory)
        self.rect = self.image.get_rect()
        self.centerMode = False

    def getInfo(self) :
        return (self.image, self.rect)

    def setPos(self, pos) :
        self.rect.x = pos[0] - ((self.getSize()[0] // 2) if self.centerMode else 0)
        self.rect.y = pos[1] - ((self.getSize()[1] // 2) if self.centerMode else 0)

    def addPos(self, pos) :
        self.rect.x += pos[0]
        self.rect.y += pos[1]

    def getPos(self) :
        return (self.rect.x, self.rect.y)

    def setSize(self, size) :
        if self.centerMode :
            self.addPos((self.getSize()[0] // 2, self.getSize()[1] // 2))
        self.image = pygame.transform.scale(self.image,size)
        self.setPos(self.getPos())

    def getSize(self) :
        return self.image.get_size()

    def setCenterMode(self, centerMode) :
        self.centerMode = centerMode

    def getSurface(self) :
        return self.image

    def setSurface(self, image) :
        self.image = image

    def isCollisionRect(self, pos) :
        left_x = self.getPos()[0]
        left_y = self.getPos()[1]
        right_x = self.getPos()[0] + self.getSize()[0]
        right_y = self.getPos()[1] + self.getSize()[1]

        return left_x <= pos[0] and left_y <= pos[1] and right_x >= pos[0] and right_y >= pos[1]

    def getTag(self) :
        return "SimpleImage"
