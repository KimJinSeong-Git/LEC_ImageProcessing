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
	int bright;

	unsigned char imageBuffer[512][512];

	for (int col = 0; col < imageSize; col++) {
		bright = smoothRamp(col);
		for (int row = 0; row < imageSize; row++) {
			imageBuffer[row][col] = bright;
		}
	}

	// 파일 저장_raw 파일
	FILE* rawfile;
	fopen_s(&rawfile, "HW1-1(v7).raw", "wb");
	fwrite(imageBuffer, sizeof(unsigned char), imageSize * imageSize, rawfile);
	//fclose(fp);
	

	// 비트맵 이미지로 만들기
	char inputImage[50] = "lena_bmp_512x512_new.bmp";//"F:/github\/LEC_ImageProcessing/LEC_ImageProcessing/LEC_ImageProcessing/lena_bmp_512x512_new.bmp";
	FILE* infile;

	fopen_s(&infile, inputImage, "rb"); // "Read Binary"

	BITMAPFILEHEADER HF; //파일정보 선언(C에 내장되어 있음)
	BITMAPINFOHEADER IF; //영상정보 선언
	RGBQUAD hRGB[256];

	fread(&HF, sizeof(BITMAPFILEHEADER), 1, infile);
	fread(&IF, sizeof(BITMAPINFOHEADER), 1, infile);
	fread(hRGB, sizeof(RGBQUAD), 256, infile);

	BYTE* lpImg = new BYTE[IF.biSizeImage]; 
	fread(lpImg, sizeof(char), imageSize * imageSize, rawfile);

	FILE* outfile;
	fopen_s(&outfile, "HW1-2(v3).bmp", "wb");
	fwrite(&HF, sizeof(BITMAPFILEHEADER), 1, outfile);
	fwrite(&IF, sizeof(BITMAPINFOHEADER), 1, outfile);
	fwrite(hRGB, sizeof(RGBQUAD), 256, outfile);
	fwrite(imageBuffer, sizeof(unsigned char), imageSize * imageSize, outfile);
	fclose(outfile);

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