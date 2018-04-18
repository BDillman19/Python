def midterm():
  #For the picture, choose Arch, then BigBen, then BlueShrub
  #Creating an empty canvas large enough for the src pictures
  canvas = makeEmptyPicture(1920, 1430)
  src1 = makePicture(pickAFile())
  srcC1 = makeEmptyPicture(360,480)
  copy(src1, srcC1, 0, 0)
  src2 = makePicture(pickAFile())
  src3 = makePicture(pickAFile())
  srcC3 = makeEmptyPicture(640, 480)
  copy(src3, srcC3, 0, 0)
  
  edge(src1)
  targetX = 0
  for sourceX in range(0,getWidth(src1)):
    targetY =0 
    for sourceY in range(0, getHeight(src1)):
      px = getPixel(src1, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      setColor(cx, getColor(px))
      targetY = targetY + 1
    targetX = targetX + 1
  
  
  #normal picture
  targetX = 360
  for sourceX in range(0,getWidth(srcC1)):
    targetY =0 
    for sourceY in range(0, getHeight(srcC1)):
      px = getPixel(srcC1, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      setColor(cx, getColor(px))
      targetY = targetY + 1
    targetX = targetX + 1
  
  #mirroring the picture
  targetX = 1080
  for sourceX in range(0,getWidth(srcC1)):
    targetY = 0
    for sourceY in range(0, getHeight(srcC1)):
      px = getPixel(srcC1, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      setColor(cx, getColor(px))
      targetY = targetY + 1
    targetX = targetX - 1
  
  negative(src2)
  targetX = 0
  for sourceX in range(0,getWidth(src2)):
    targetY =480 
    for sourceY in range(0, getHeight(src2)):
      px = getPixel(src2, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      setColor(cx, getColor(px))
      targetY = targetY + 1
    targetX = targetX + 1
  #recall negative to undo itself
  negative(src2)
  
  #normal Picture
  targetX = 200
  for sourceX in range(0,getWidth(src2)):
    targetY =480 
    for sourceY in range(0, getHeight(src2)):
      px = getPixel(src2, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      setColor(cx, getColor(px))
      targetY = targetY + 1
    targetX = targetX + 1
    
  posterize(src2)
  targetX = 400
  for sourceX in range(0,getWidth(src2)):
    targetY =480 
    for sourceY in range(0, getHeight(src2)):
      px = getPixel(src2, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      setColor(cx, getColor(px))
      targetY = targetY + 1
    targetX = targetX + 1
  
  grayScale(src3)
  targetX = 0
  for sourceX in range(0,getWidth(src3)):
    targetY =950 
    for sourceY in range(0, getHeight(src3)):
      px = getPixel(src3, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      setColor(cx, getColor(px))
      targetY = targetY + 1
    targetX = targetX + 1
  
  #normal picture
  targetX = 640
  for sourceX in range(0,getWidth(srcC3)):
    targetY =950 
    for sourceY in range(0, getHeight(srcC3)):
      px = getPixel(srcC3, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      setColor(cx, getColor(px))
      targetY = targetY + 1
    targetX = targetX + 1
    
  makeLight(srcC3)
  targetX = 1280
  for sourceX in range(0,getWidth(srcC3)):
    targetY =950 
    for sourceY in range(0, getHeight(srcC3)):
      px = getPixel(srcC3, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      setColor(cx, getColor(px))
      targetY = targetY + 1
    targetX = targetX + 1
  
  
  show(canvas)


def edge(source):
  for px in getPixels(source):
    x = getX(px)
    y = getY(px)
    if y < getHeight(source) -1 and x < getWidth(source) -1:
      sum = getRed(px)+getGreen(px)+getBlue(px)
      botrt = getPixel(source, x+1, y+1)
      sum2 = getRed(botrt) + getGreen(botrt) + getBlue(botrt)
      diff = abs(sum2 - sum)
      newColor = makeColor(diff, diff, diff)
      setColor(px, newColor)
      
def negative(picture):
  for px in getPixels(picture):
    red = getRed(px)
    green = getGreen(px)
    blue = getBlue(px)
    negColor = makeColor(255 - red, 255 - green, 255 - blue)
    setColor(px, negColor)
 
def posterize(picture):
  for p in getPixels(picture):
    setRed(p, pickPosterizeValue(getRed(p)))
    setGreen(p, pickPosterizeValue(getGreen(p)))
    setBlue(p, pickPosterizeValue(getBlue(p)))
    
def pickPosterizeValue(current):
  if(current < 64):
    return 31
  if(current > 63 and current < 128):
    return 95
  if(current > 127 and current < 192):
    return 159
  if(current > 191 and current < 256):
    return 223
  
def grayScale(picture):
  for px in getPixels(picture):
    r1 = getRed(px)
    g1 = getGreen(px)
    b1 = getBlue(px)
    intensity = (getRed(px)+getGreen(px)+getBlue(px))/3
    setColor(px, makeColor(intensity, intensity, intensity))
    
def makeLight(picture):
  for px in getPixels(picture):
    color = getColor(px)
    color = makeLighter(color)
    setColor(px, color)

def copy(source, target, targX, targY):
  targetX = targX
  for sourceX in range(0, getWidth(source)):
    targetY = targY
    for sourceY in range(0, getHeight(source)):
      px = getPixel(source, sourceX, sourceY)
      tx = getPixel(target, targetX, targetY)
      setColor(tx, getColor(px))
      targetY = targetY+1
    targetX = targetX+1