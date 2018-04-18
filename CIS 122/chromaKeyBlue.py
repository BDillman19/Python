def chromaKeyBlue():
  pic = makePicture(pickAFile())
  source = makePicture(pickAFile())
  for px in getPixels(source):
    x = getX(px)
    y = getY(px)
    if (getRed(px) + getGreen(px) < getBlue(px) + 100):
      picpx = getPixel(pic, x, y)
      piccol = getColor(picpx)
      setColor(px, piccol)
  show(source)