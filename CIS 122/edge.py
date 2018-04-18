def posterize():
  for px in getPixels(pic):
    r = getRed(px)
    g = getGreen(px)
    b = getBlue(px)
    if r > 180:
      setColor(px, red)
    elif b > 180:
      setColor(px, blue)
    elif g > 180:
      setColor(px, green)
    else: 
      setColor(px, black)