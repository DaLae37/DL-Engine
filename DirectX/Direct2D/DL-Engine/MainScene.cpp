#include "stdafx.h"
#include "MainScene.h"

MainScene::MainScene() {
	icon = new Sprite(L"Resources/Images/icon.png");
	AddObject(icon);
	icon->setPos(10, 10);
	icon->setRotation(20);
	icon->setRotationCenter(icon->getWidth() / 2, icon->getHeight() / 2);
	icon->setScale(0.5f, 0.5f);
}

MainScene::~MainScene() {

}

void MainScene::Render() {
	icon->Render();
}

void MainScene::Update(float dTime) {
	Scene::Update(dTime);
}