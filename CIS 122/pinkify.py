def pinkify():
  pic = makePicture(pickAFile())
  for px in getPixels(pic):
    if getRed(px) > 100:
      if getGreen(px) > 100:
        if getBlue(px) > 100:
          setColor(px, pink)
  show(pic)