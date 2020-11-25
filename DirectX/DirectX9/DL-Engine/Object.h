#pragma once
#include <d3dx9.h>
#include <list>

class Object
{
protected:
	Object* parent;

	D3DXMATRIX mat;
	D3DXVECTOR2 pos;

	D3DXVECTOR2 scalingCenter;
	D3DXVECTOR2 scale;

	D3DXVECTOR2 rotationCenter;
	float rotation;

	RECT rect;

	std::list<Object*> childList;

public:
	Object();
	~Object();

	virtual void Render();
	virtual void Update(float dTime);

	void AddChild(Object* child);
	void RemoveChild(Object* child);

	bool IsCollisionRect(Object* object);
	bool IsPointInRect(D3DXVECTOR2 p);

	D3DXMATRIX getMat();
	D3DXVECTOR2 getPos();
	RECT getRect();

	float getPosX();
	float getPosY();
	float getRotation();

	void setParent(Object* parent);
	void setPos(D3DXVECTOR2 pos);
	void setScale(D3DXVECTOR2 scale);
	void setScalingCenter(D3DXVECTOR2 scaleCenter);
	void setRotation(float rotation);
	void setRotationCenter(D3DXVECTOR2 rotationCenter);

	template<typename PX, typename PY>
	void setPos(PX posX, PY posY) {
		pos.x = posX;
		pos.y = posY;
	}

	template<typename SX, typename SY>
	void setScale(SX scaleX, SY scaleY) {
		scale.x = scaleX;
		scale.y = scaleY;
	}

	template<typename SCX, typename SCY>
	void setScalingCenter(SCX scaleCenterX, SCY scaleCenterY) {
		scalingCenter.x = scaleCenterX;
		scalingCenter.y = scaleCenterY;
	}

	template<typename RCX, typename RCY>
	void setRotationCenter(RCX rotationCenterX, RCY rotationCenterY) {
		rotationCenter.x = rotationCenterX;
		rotationCenter.y = rotationCenterY;
	}
};