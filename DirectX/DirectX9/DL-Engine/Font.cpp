#include "stdafx.h"
#include "Font.h"

Font::Font() {
	color = D3DCOLOR_ARGB(255, 255, 255, 255);

	memset(&desc, 0, sizeof(D3DXFONT_DESC));
	desc.CharSet = HANGUL_CHARSET;
	wcscpy_s(desc.FaceName, TEXT("¸¼Àº °íµñ"));
	desc.Height = 15;
	desc.Width = 15;
	desc.Weight = FW_NORMAL;
	desc.Quality = DEFAULT_QUALITY;
	desc.MipLevels = 1;
	desc.Italic = false;
	desc.OutputPrecision = OUT_DEFAULT_PRECIS;
	desc.PitchAndFamily = FF_DONTCARE;

	D3DXCreateFontIndirect(pd3dDevice, &desc, &pFont);

	SetRect(&rect, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT);
}

Font::~Font() {
	SAFE_RELEASE(pFont);
}

void Font::setText(const char * text) {
	str = (char *) text;
}

void Font::Render() {
	Object::Render();
	pd3dSprite->SetTransform(&mat);
	pFont->DrawTextA(pd3dSprite, str, -1, &rect, DT_TOP | DT_LEFT, color);
}

void Font::setHeight(int height) {
	desc.Height = height;
	D3DXCreateFontIndirect(pd3dDevice, &desc, &pFont);
}

void Font::setWidth(int width) {
	desc.Width = width;
	D3DXCreateFontIndirect(pd3dDevice, &desc, &pFont);
}

void Font::setColor(D3DCOLOR color) {
	this->color = color;
}