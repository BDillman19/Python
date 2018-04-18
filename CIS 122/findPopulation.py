setMediaPath()

def findPopulation():
  state = findState()
  file = open(getMediaPath("state-populations.csv"), "rt")
  lines = file.readlines()
  file.close()
  for line in lines:
    parts = line.split(",")
    if parts[4] == state:
      print "The population of "+state+" is:"
      return int(parts[5])
  return -1
  
def getState():
  inp = requestString("Enter a State")
  cap = inp[0:1]
  cap1 = cap.upper()
  low = inp[1:]
  low1= low.lower()
  state = cap1 + low1
  return state
  
def findState():
  thing = requestString("Enter a state")
  word1 = ""
  word2 = ""
  place = 0
  size = len(thing)
  for letter in thing:
    if letter != " ":
      word1 += letter
      place += 1
    if letter == " ":
      place += 1
      break
  for index in range(place, size):
    if thing[index] != " ":
      word2 += thing[index]
  state = word1 + " " + word2
  return state

      