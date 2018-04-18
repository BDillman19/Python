def decreaseRed(picture):
  for px in getPixels(picture):
    value = getRed(px)
    setRed(px, value*0.5)