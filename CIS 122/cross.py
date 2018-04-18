def cross(pic):
  xMid = getWidth(pic)/ 2
  yMid = getHeight(pic)/ 2
  for px in getPixels(pic):
    if getX(px) == xMid:
      setColor(px, white)
    if getY(px) == yMid:
      setColor(px, white)
  