import pygame
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class CameraManager() :
    isFollowing = False
    followedObject = None
    instance = None
    cameraX = 0
    cameraY = 0
    dX = 0
    dy = 0
    def update(self) :
        if self.isFollowing and self.followedObject.getIsMove() is True :
            x = self.followedObject.getPos()[0]
            y = self.followedObject.getPos()[1]
            self.addCameraPos((x - self.dX, y - self.dY))
            self.dX = x
            self.dY = y
            if self.getCameraPos()[1] > 0 :
                self.setCameraPos((self.getCameraPos()[0],0))

    @classmethod
    def getInstance(cls) :
        if cls.instance is None :
            cls.instance = CameraManager()
        return cls.instance

    def setCameraPos(self, pos) :
        self.cameraX = pos[0]
        self.cameraY = pos[1]

    def addCameraPos(self, pos) :
        self.cameraX += pos[0]
        self.cameraY += pos[1]

    def getCameraPos(self) :
        return (self.cameraX, self.cameraY)

    def setFollowedObject(self, obj) :
        self.followedObject = obj
        x = self.followedObject.getPos()[0]
        y = self.followedObject.getPos()[1]
        self.dX = x
        self.dY = y
        self.isFollowing = True

    def releaseObject(self) :
        self.followedObject = None
        self.isFollowing = False
