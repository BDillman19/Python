import urllib
def readHTML():
  connect = urllib.urlopen("https://cobra.parkland.edu")
  lines = connect.readlines()
  connect.close()
  for line in lines:
    if "<h1>" in line or "<h2>" in line or "<h3>" in line or "<h4>" in line or "<h5>" in line or "<h6>" in line:
      print line

##################################################################################################################

def pullSound():
  setMediaPath()
  connect = urllib.urlopen("http://www.thesoundarchive.com/caddyshack/augusta.wav")
  lines = connect.read()
  connect.close()
  file = open(getMediaPath("caddyshack.wav"), "wb")
  file.write(lines)
  file.close()

##################################################################################################################

def thumbnail():
  setMediaPath()
  connect = urllib.urlopen("http://img.picturequotes.com/2/385/384312/60-of-the-time-it-works-every-time-quote-1.jpg")
  lines = connect.read()
  connect.close()
  file = open(getMediaPath("code.jpg"), "wb")
  file.write(lines)
  file.close()