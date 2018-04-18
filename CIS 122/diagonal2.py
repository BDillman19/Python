def diagonal2():
  pic = makePicture(pickAFile())
  x = 0
  h = getHeight(pic)
  w = getWidth(pic)
  hyp = sqrt(h^2 + w^2)
  y = h-1
  h = float(h)
  w = float(w)
  dif = int(2*(w/h))
  print dif
  while x < w:
    px = getPixel(pic, x, y)
    setColor(px, white)
    x = x + dif
    y = y - 2
  show(pic)