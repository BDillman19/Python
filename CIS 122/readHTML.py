import urllib
def readHTML():
  connect = urllib.urlopen("https://cobra.parkland.edu")
  lines = connect.readlines()
  connect.close()
  for line in lines:
    if "<h1>" in line or "<h2>" in line or "<h3>" in line or "<h4>" in line or "<h5>" in line or "<h6>" in line:
      print line