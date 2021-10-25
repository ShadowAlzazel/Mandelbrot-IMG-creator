from PIL import Image, ImageDraw
import time

max_iterations = 80

#Image Dimensions
p = 40 
width = (3 * p) * 100
height = (2 * p) * 100

#Interval Coordinates
r_min = -2
r_max = 1
i_min = -1
i_max = 1

#Mandelbrot Function
def mandelbrotFunc(x, y):
    z = 0
    n = 0 
    c = complex(r_min + (x / width) * (r_max - r_min), i_min + (y / height) * (i_max - i_min))

    while abs(z) <= 2 and n < max_iterations:
        z = z*z + c
        n += 1
    return n

#Get Color of the Pixel Function
def colorOfPixelFunc(x, y):
    pixelColor = list((newMandelbrot.getpixel((x, y))))

    if pixelColor[0] == 0:
        return False
    elif pixelColor[0] <= 200:
        return True 
    else:
        return False

#Plot the Pixel Function
def plotPixelFunc(x, y):
    complexPixel = mandelbrotFunc(x, y)
    color = 255 - int(complexPixel * 255 / max_iterations)
    draw.point([x, y], (color, color, color)) 


#Timer start
start = time.time()
print("Time Started:", time.ctime(start))

#Loop the Image
oldMandelbrot = Image.open('MandelbrotIMGRES30.png')
newMandelbrot = oldMandelbrot.resize((width, height))
draw = ImageDraw.Draw(newMandelbrot)

for x in range(0, width):
    for y in range(0, height):
        if x > 1 and x < (width - 1) and y > 1 and y < (height - 1):
            if colorOfPixelFunc(x, y) == True:
                plotPixelFunc(x, y)
        else: 
            plotPixelFunc(x, y)

#Timer stop
finish = time.time()
print("Time Finished:", time.ctime(finish))
print("Time Elapsed in seconds:", ((((finish - start) * 100) // 1) / 100))

#Show and Save Image
newMandelbrot.show()
newMandelbrot.save('MandelbrotIMGRES40.png', 'PNG')