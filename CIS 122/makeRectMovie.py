def makeRectMovie(directory):
  for num in range(1,30): #29 frames (1 to 29)
    canvas = makeEmptyPicture(300, 200)
    addRectFilled(canvas, num*10, num*5, 50,50,red)
    #convert number to string
    numStr = str(num)
    if num < 10:
      writePictureTo(canvas, directory+"\\frame0"+numStr+".jpg")
    if num >= 10:
      writePictureTo(canvas, directory+"\\frame"+numStr+".jpg")
  movie = makeMovieFromInitialFile(directory+"\\frame00.jpg");
  return movie
  
# in command type 
# rectM = makeRectMovie("c:\\Temp\\rect")
# then 
# playMovie(rectM)