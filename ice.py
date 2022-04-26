import board
import neopixel
import time

nPix = 38

pixels = neopixel.NeoPixel(board.D18, nPix)

def off():
	for i in range (0,nPix):
		pixels[i] = (0, 0, 0)
def bottoms():
	for i in range(0, nPix, 2):
		pixels[i] = (0, 0, 255)
def innermost(col=(255,0,0)):
	for i in range (0,2):
		pixels[i] = col

def innerRing():
	for i in range(2,14):
		pixels[i] = (0, 0, 255)

def outerRing():
	for i in range(14,nPix):
		pixels[i] = (255, 0, 0)


for i in range(255):
	innermost((0,0,i))
	time.sleep(0.01)
outerRing()
