def makeCollage():
  canvas = makeEmptyPicture(812, 600)
  src = makePicture(pickAFile())
  
  targetX = 0
  for sourceX in range(0,getWidth(src)):
    targetY =0 
    for sourceY in range(0, getHeight(src)):
      px = getPixel(src, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      setColor(cx, getColor(px))
      targetY = targetY + 1
    targetX = targetX + 1
  negative(src)
  targetX = 203
  for sourceX in range(0, getWidth(src)):
    targetY = 0
    for sourceY in range(0, getHeight(src)):
      px = getPixel(src, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      setColor(cx, getColor(px))
      targetY = targetY + 1
    targetX = targetX + 1
  negative(src)
  increaseBlue(src)
  targetX = 406
  for sourceX in range(0, getWidth(src)):
    targetY = 0
    for sourceY in range(0, getHeight(src)):
      px = getPixel(src, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      setColor(cx, getColor(px))
      targetY = targetY + 1
    targetX = targetX + 1
  undoIncreaseBlue(src)
  decreaseRed(src)
  targetX = 609
  for sourceX in range(0, getWidth(src)):
    targetY = 0
    for sourceY in range(0, getHeight(src)):
      px = getPixel(src, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      setColor(cx, getColor(px))
      targetY = targetY + 1
    targetX = targetX + 1
  undoDecreaseRed(src)
  targetX = 203
  for sourceX in range(0,getWidth(src)):
    targetY =300 
    for sourceY in range(0, getHeight(src)):
      px = getPixel(src, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      setColor(cx, getColor(px))
      targetY = targetY + 1
    targetX = targetX - 1
  negative(src)
  targetX = 406
  for sourceX in range(0, getWidth(src)):
    targetY = 300
    for sourceY in range(0, getHeight(src)):
      px = getPixel(src, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      setColor(cx, getColor(px))
      targetY = targetY + 1
    targetX = targetX - 1
  negative(src)
  increaseBlue(src)
  targetX = 609
  for sourceX in range(0, getWidth(src)):
    targetY = 300
    for sourceY in range(0, getHeight(src)):
      px = getPixel(src, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      setColor(cx, getColor(px))
      targetY = targetY + 1
    targetX = targetX - 1
  undoIncreaseBlue(src)
  decreaseRed(src)
  targetX = 811
  for sourceX in range(0, getWidth(src)):
    targetY = 300
    for sourceY in range(0, getHeight(src)):
      px = getPixel(src, sourceX, sourceY)
      cx = getPixel(canvas, targetX, targetY)
      setColor(cx, getColor(px))
      targetY = targetY + 1
    targetX = targetX - 1
  undoDecreaseRed(src)
  show(canvas)
  
  
def negative(picture):
  for px in getPixels(picture):
    red = getRed(px)
    green = getGreen(px)
    blue = getBlue(px)
    negColor = makeColor(255 - red, 255 - green, 255 - blue)
    setColor(px, negColor)
    
    
def increaseBlue(picture):
  for px in getPixels(picture):
    b = getBlue(px)
    setBlue(px, b*1.5)
    

def undoIncreaseBlue(picture):
  for px in getPixels(picture):
    b = getBlue(px)
    setBlue(px, b/1.5)

 
   
def decreaseRed(picture):
  for px in getPixels(picture):
    value = getRed(px)
    setRed(px, value*0.5)
    
def undoDecreaseRed(picture):
  for px in getPixels(picture):
    value = getRed(px)
    setRed(px, value/0.5)
