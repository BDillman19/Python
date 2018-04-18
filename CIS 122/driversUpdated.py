def drivers():
  x = 0
  reverseDrivers = 0
  parkedDrivers = 0
  slowDrivers = 0
  safeDrivers = 0
  speeders = 0
  while x < 15:
    speed =  getSpeed()
    x += 1
    if speed < 0:
      reverseDrivers += 1
    elif 0 < speed < 1:
      parkedDrivers +=1
    elif 1 < speed < 40:
      slowDrivers +=1
    elif 40 < speed <= 65:
      safeDrivers += 1
    else:
      speeders += 1
  print "reverse drivers = " 
  print reverseDrivers
  print "parked drivers = "
  print parkedDrivers
  print "slow drivers = "
  print slowDrivers
  print "safe drivers = "
  print safeDrivers
  print "speeders = "
  print speeders
  
def getSpeed():
  s = raw_input("Enter the speed ")
  s = int(s)
  return s