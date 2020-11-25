#include "stdafx.h"
#include "MainScene.h"

MainScene::MainScene() {
	icon = new Sprite("Resources/Images/icon.png");
	AddObject(icon);
	icon->setPos(0, 0);

	font = new Font();
	font->setText("¾È³çÇÏ¼¼¿ä");
	font->setPos(0, 0);
	font->setWidth(10);
	font->setHeight(20);
	font->setColor(D3DCOLOR_ARGB(255, 0, 0, 0));
}

MainScene::~MainScene() {

}

void MainScene::Render() {
	icon->Render();
	font->Render();
}

void MainScene::Update(float dTime) {
	Scene::Update(dTime);
}