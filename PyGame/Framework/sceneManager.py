import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Framework.scene import Scene

class SceneManager(Scene) :
    instance = None
    
    def __init__(self) :
        self.isQuit = False
        self.current_scene = None
        self.sceneRecord = dict()

    @classmethod
    def getInstance(cls) :
        if cls.instance is None :
            cls.instance = SceneManager()
        return cls.instance

    def registerScene(self, sceneName, scene) :
        self.sceneRecord[sceneName] = scene

    def registerGameObjects(self, screen, clock) :
        self.screen = screen
        self.clock = clock

    def getScreen(self) :
        return self.screen
    
    def changeScene(self, replaced_scene_name) :
        self.current_scene = self.sceneRecord[replaced_scene_name]
        self.current_scene.__init__(self.screen, self.clock)

    def update(self) :
        self.current_scene.update()

    def render(self) :
        self.current_scene.render()
        
    def setQuit(self, isQuit) :
        self.isQuit = isQuit
