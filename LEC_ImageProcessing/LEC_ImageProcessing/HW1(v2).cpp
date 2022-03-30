#include <iostream>
#include <fstream>
#include <Windows.h>
#include <math.h>

using namespace std;

// Proto type
void genRaw(unsigned char* imageBuffer);
int smoothRamp(int col);
double equation(int col, double x1, double y1, double x2, double y2);

// Main
int main() {
	int imageSize = 512;
	int bright;

	unsigned char imageBuffer[512][512];

	for (int col = 0; col < imageSize; col++) {
		bright = smoothRamp(col);
		for (int row = 0; row < imageSize; row++) {
			imageBuffer[row][col] = bright;
		}
	}

	// 파일 저장_raw 파일
	FILE* fp;
	fopen_s(&fp, "HW1-1(v6).raw", "wb");
	fwrite(imageBuffer, sizeof(unsigned char), imageSize * imageSize, fp);
	fclose(fp);

	// Header 지정
	BITMAPFILEHEADER fh;
	BITMAPINFOHEADER ih;
	RGBQUAD rgb[256];
	for (int i = 0; i < 256; i++)
	{
		rgb[i].rgbBlue = i;
		rgb[i].rgbGreen = i;
		rgb[i].rgbRed = i;
		rgb[i].rgbReserved = 0;
	}
	memset(&fh, 0, sizeof(BITMAPFILEHEADER));
	memset(&ih, 0, sizeof(BITMAPINFOHEADER));
	memset(&rgb, 0, sizeof(RGBQUAD) * 256);
	fh.bfOffBits = 1078; // RGBQUAD + InfoHeader + FileHeader only 8bit mode if 24bit == 54; 40+ 14;

	fh.bfSize = imageSize * imageSize + sizeof(RGBQUAD) * 256 + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);
	fh.bfType = 19778;

	ih.biBitCount = 8;
	ih.biHeight = imageSize;
	ih.biPlanes = 1;
	ih.biSize = 40;
	ih.biSizeImage = imageSize * imageSize;
	ih.biWidth = imageSize;
	ih.biXPelsPerMeter = 0;
	ih.biYPelsPerMeter = 0;

	// 파일 저장_bmp파일
	fopen_s(&fp, "HW1-2.bmp", "wb");
	fwrite(&fh, sizeof(BITMAPFILEHEADER), 1, fp);
	fwrite(&ih, sizeof(BITMAPINFOHEADER), 1, fp);
	fwrite(rgb, sizeof(RGBQUAD), 256, fp);
	fwrite(imageBuffer, sizeof(unsigned char), imageSize * imageSize, fp);
	fclose(fp);

	return 0;
}


int smoothRamp(int col) {
	double brightness;
	if (col < 100)
		brightness = 120;
	else if (col < 200)
		brightness = equation(col, 100, 120, 200, 135);
	else if (col < 280)
		brightness = equation(col, 200, 135, 280, 225);
	else if (col < 300)
		brightness = equation(col, 280, 225, 300, 235);
	else
		brightness = 240;

	return (int)brightness;
}

double equation(int col, double x1, double y1, double x2, double y2) {
	return ((y2 - y1) / (x2 - x1)) * (col - x1) + y1;
}