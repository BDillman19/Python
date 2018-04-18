import random
def listToPicture():
  list = randomList()
  picture = makePicture(getMediaPath("640x480.jpg"))
  for p in list:
    if p[0] <= getWidth(picture) and p[1] <= getHeight(picture):
      setColor(getPixel(pcture, p[0], p[1]), makeColor(p[2], p[3], p[4]))
  show(picture)
  return picture
  
def randomList():
  list = []
  x = 0
  while x < 500:
    ran = random.random() *1000
    x += 1
    list.append(ran)
  return list