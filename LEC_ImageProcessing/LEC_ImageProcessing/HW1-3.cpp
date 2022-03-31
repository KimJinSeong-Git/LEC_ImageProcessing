#include <iostream>
#include <fstream>
#include <Windows.h>
#include <math.h>

using namespace std;

// Proto type
int smoothRamp(int col);
double equation(int col, double x1, double y1, double x2, double y2);

// Main
int main() {
	int imageSize = 512;

	unsigned char imageBuffer[512][512];
	unsigned char tempBuffer[512][512];


	FILE* rawfile;
	fopen_s(&rawfile, "HW1-1.raw", "rb");
	fread(imageBuffer, sizeof(char), imageSize * imageSize, rawfile);

	for (int row = 0; row < imageSize; row++) {
		for (int col = 0; col < imageSize; col++) {
			tempBuffer[col][imageSize - row] = imageBuffer[row][col];
		}
	}

	// 비트맵 헤더 추가
	char inputImage[50] = "lena_bmp_512x512_new.bmp";
	FILE* infile;

	fopen_s(&infile, inputImage, "rb"); // "Read Binary"

	BITMAPFILEHEADER HF; //파일정보 선언(C에 내장되어 있음)
	BITMAPINFOHEADER IF; //영상정보 선언
	RGBQUAD hRGB[256];

	fread(&HF, sizeof(BITMAPFILEHEADER), 1, infile);
	fread(&IF, sizeof(BITMAPINFOHEADER), 1, infile);
	fread(hRGB, sizeof(RGBQUAD), 256, infile);

	// BMP로 저장
	FILE* outfile;
	fopen_s(&outfile, "HW1-3.bmp", "wb");
	fwrite(&HF, sizeof(BITMAPFILEHEADER), 1, outfile);
	fwrite(&IF, sizeof(BITMAPINFOHEADER), 1, outfile);
	fwrite(hRGB, sizeof(RGBQUAD), 256, outfile);
	fwrite(tempBuffer, sizeof(unsigned char), imageSize * imageSize, outfile);
	fclose(rawfile);
	fclose(outfile);
	fclose(infile);

	return 0;
}