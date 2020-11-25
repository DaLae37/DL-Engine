#pragma once
#include "Scene.h"
#include "Sprite.h"
//Object
#include "Font.h"
class MainScene : public Scene
{
public :
	MainScene();
	~MainScene();

	Sprite* icon;
	Font* font;

	void Render();
	void Update(float dTime);
};