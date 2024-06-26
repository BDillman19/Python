def slowSunset(directory):
  #outside the loop!
  setMediaPath()
  canvas = makePicture("rotoroa.jpg")
  for num in range(1,100): #99 frames
    printNow("Frame number: "+ str(num))
    makeSunset(canvas)
    #now, write out the frame
    writeFrame(num, directory, canvas)
  movie = makeMovieFromInitialFile(directory+"\\frame001.jpg")
  return movie
  
def makeSunset(picture):
  for p in getPixels(picture):
    value = getBlue(p)
    setBlue(p, int(value*.99))
    value = getGreen(p)
    setGreen(p, int(value*.99))
    
def writeFrame(num, dir, pict):
  numStr = str(num)
  if num < 10:
    writePictureTo(pict, dir+"//frame00"+numStr+".jpg")
  if num >= 10 and num < 100:
    writePictureTo(pict, dir+"//frame0"+numStr+".jpg")
  if num >= 100:
    writePictureTo(pict, dir+"//frame"+numStr+".jpg")