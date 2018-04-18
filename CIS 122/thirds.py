def thirds():
  pic = makePicture(pickAFile())
  x = getHeight(pic)
  X1 = x/3
  X2 = 2*x/3
  for px in getPixels(pic):
    z = getY(px)
    r = getRed(px)
    g = getGreen(px)
    b = getBlue(px)
    if z < X1:
      r = r + 50
      g = g + 50
      b = b + 50
      color = makeColor(r, b, g)
      setColor(px, color)
    if X1 < z < X2:
      b = b*.7
      g = g*.7
      color = makeColor(r, b, g)
      setColor(px, color)
    if X2 < z < x:
      r = 255 - r
      g = 255 - g
      b = 255 - b
      color = makeColor(r, b, g)
      setColor(px, color)
  show(pic)