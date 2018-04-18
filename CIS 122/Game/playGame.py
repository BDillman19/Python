def playGame():
  location = "Drawbridge"
  showIntroduction()
  while not (location == "Exit"):
    showRoom(location)
    direction = requestString("Which direction?")
    location = pickRoom(direction, location)

def showIntroduction():
  printNow("Welcome to the Adventure castle!")
  printNow("In each room, you will be told")
  printNow(" which directions you can go.")
  printNow("You can move north, south, east, west, upstairs, or downstairs")
  printNow(" by typing that direction.")
  printNow("Type help to replay this introduction.")
  printNow("Type quit or exit to end the program.")

def showRoom(room):
  if room == "Drawbridge":
    showDB()
  if room == "Gate":
    showGate()
  if room == "Courtyard":
    showCourtyard()
  if room == "Kitchen":
    showKitchen()
  if room == "Stables":
    showStables()
  if room == "Hallway":
    showHallway()
  if room == "KR":
    showKR()
  if room == "WR":
    showWR()
  if room == "PR":
    showPR()
  if room == "SKR":
    showSKR()
  
def pickRoom(direction, room):
  if (direction == "quit") or (direction == "exit"):
    printNow("Goodbye!")
    return "Exit"
  if direction == "help":
    showIntroduction()
    return room
  if room == "Drawbridge":
    if direction == "north":
      return "Gate"
  if room  == "Gate":
    if direction == "north":
      return "Courtyard"
  if room == "Courtyard":
    if direction == "west":
      return "Kitchen"
    if direction == "east":
      return "Stables"
    if direction == "upstairs":
      return "Hallway"
    if direction == "south":
      return "Gate"
  if room == "Kitchen":
    if direction == "east":
      return "Courtyard"
  if room == "Stables":
    if direction == "west":
      return "Courtyard"
  if room == "Hallway":
    if direction == "west":
      return "KR"
    if direction == "north":
      return "PR"
    if direction == "east":
      return "SKR"
    if direction == "downstairs":
      return "Courtyard"
  if room == "KR":
    if direction == "east":
      return "Hallway"
    if direction == "south":
      return "WR"
  if room == "WR":
    if direction == "north":
      return "KR"
  if room == "PR":
    if direction == "south":
      return "Hallway"
  if room == "SKR":
    if direction == "west":
      return "Hallway"
      
def showDB():
  printNow("You are on the drawbridge.")
  printNow(" You can go north into the castle.")

def showGate():
  printNow("You are in front of the gate. ")
  printNow("Go north to proceed into the castle.")
  
def showCourtyard():
  printNow("You are in the courtyard. ")
  printNow("You can go east, south, west, or upstairs.")

def showKitchen():
 # show(makePicture('kitchen.jpg'))
  printNow("You are in the kitchen. ")
  printNow("All the surfaces are covered with pots,")
  printNow(" pans, food pieces, and pools of blood.")
  printNow("You think you hear something in the courtyard. ")
  printNow("It's a scraping noise, like something being dragged")
  printNow(" along the floor.")
  printNow("You can go east.")

def showStables():
  printNow("You are in the Stables. ")
  printNow("You can go west.")
  
def showHallway():
  printNow("You are in the Hallway. ")
  printNow("You can go west, north, east, or dowstairs.")

def showWR():
  printNow("You are in the wizard's room. ")
  printNow("You can go north.")

def showKR():
  printNow("You are in the king's room. ")
  printNow("You can go south or east.")

def showPR():
  printNow("You are in the princess room. ")
  printNow("You can go south.")

def showSKR():
  printNow("You are in Sir Knight's Room.")
  printNow("You can go west.")



  