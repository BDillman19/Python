def encode(msgPic, original):
  # Assume msgPic and original have same dimensions
  # First, make all red pixels even
  for pxl in getPixels(original):
    # Using modulo operator to test oddness
    if(getRed(pxl) % 2) == 1:
      setRed(pxl, getRed(pxl) -1)
  # Second, wherever there's black in msgPic
  # make odd the red in the corresponding original pixel
  for x in range(0, getWidth(original)):
    for y in range(0, getHeight(original)):
      msgPxl = getPixel(msgPic, x, y)
      origPxl = getPixel(original, x, y)
      if (distance(getColor(msgPxl), black) < 100.0):
        # It's a message pixel! Make the red value odd.
        setRed(origPxl, getRed(origPxl)+1)
        
def decode(encodedImg):
  # Takes in an encoded image. Return the original message
  message = makeEmptyPicture(getWidth(encodedImg), getHeight(encodedImg))
  for x in range(0, getWidth(encodedImg)):
    for y in range(0, getHeight(encodedImg)):
      encPxl = getPixel(encodedImg, x, y)
      msgPxl = getPixel(message, x, y)
      if(getRed(encPxl) %2) == 1:
        setColor(msgPxl, black)
  return message