def posterize(picture):
  for p in getPixels(picture):
    setRed(p, pickPosterizeValue(getRed(p)))
    setGreen(p, pickPosterizeValue(getGreen(p)))
    setBlue(p, pickPosterizeValue(getBlue(p)))
  show(picture)
    
def pickPosterizeValue(current):
  if(current < 64):
    return 31
  if(current > 63 and current < 128):
    return 95
  if(current > 127 and current < 192):
    return 159
  if(current > 191 and current < 256):
    return 223