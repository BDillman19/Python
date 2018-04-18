def diagonal():
  pic = makePicture(pickAFile())
  x = 0
  y = getHeight(pic)-1
  print getHeight(pic)
  print y
  z = getWidth(pic)
  while x < z:
    px = getPixel(pic, x, y)
    setColor(px, white)
    x = x +1
    y = y -1
  show(pic)