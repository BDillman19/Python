def createCollage():
  flower1 = makePicture(pickAFile())
  print flower1
  flower2 = makePicture(pickAFile())
  print flower2
  totY = getHeight(flower1) + getHeight(flower2)
  totX = getWidth(flower1) + getWidth(flower2)
  canvas = makeEmptyPicture(1048, 325)
  print canvas
  #First picture, at left edge
  targetX = 0
  for sourceX in range(0,getWidth(flower1)):
    targetY =0 
    for sourceY in range(0, getHeight(flower1)):
      px = getPixel(flower1, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      setColor(cx, getColor(px))
      targetY = targetY + 1
    targetX = targetX + 1
  #Second picture, 100 pixels over
  targetX = 214
  for sourceX in range(0, getWidth(flower2)):
    targetY = 0
    for sourceY in range(0, getHeight(flower2)):
      px = getPixel(flower2, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      setColor(cx, getColor(px))
      targetY = targetY + 1
    targetX = targetX + 1
  #Third picture, flower1 negative
  negative(flower1)
  targetX = 417
  for sourceX in range(0, getWidth(flower1)):
    targetY = 0
    for sourceY in range(0, getHeight(flower1)):
      px = getPixel(flower1, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      setColor(cx, getColor(px))
      targetY = targetY + 1
    targetX = targetX + 1
  #Fourth picture, flower2 with no blue
  clearBlue(flower2)
  targetX = 631
  for sourceX in range(0, getWidth(flower2)):
    targetY = 0
    for sourceY in range(0, getHeight(flower2)):
      px = getPixel(flower2, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      setColor(cx, getColor(px))
      targetY = targetY + 1
    targetX = targetX + 1
  #fifth picture, decrease red
  negative(flower1)
  decreaseRed(flower1)
  targetX = 833
  for sourceX in range(0, getWidth(flower1)):
    targetY = 0
    for sourceY in range(0, getHeight(flower1)):
      px = getPixel(flower1, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      setColor(cx, getColor(px))
      targetY = targetY + 1
    targetX = targetX + 1
  canvasTot = bigCanvas(canvas)
  show(canvasTot)
  return canvasTot
  


def bigCanvas(smallCanvas):
  bc = makeEmptyPicture(1048, 975)
  
  

def negative(picture):
  for px in getPixels(picture):
    red = getRed(px)
    green = getGreen(px)
    blue = getBlue(px)
    negColor = makeColor(255 - red, 255 - green, 255 - blue)
    setColor(px, negColor)



def clearBlue(picture):
  for px in getPixels(picture):
    setBlue(px, 0)



def decreaseRed(picture):
  for px in getPixels(picture):
    value = getRed(px)
    setRed(px, value*0.5)