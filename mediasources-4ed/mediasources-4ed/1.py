def drivers(speed):
  #what is input and output?
  global reverseDrivers
  global parkedDrivers
  global slowDrivers
  global safeDrivers
  global speeders
  if speed<0:
    reverseDrviers=reverseDrivers+1
  if speed<1:
    parkedDrivers=parkedDrivers+1
  if speed<40:
    slowDrivers=slowDrivers+1
  if speed<=65:
    safeDrivers=safeDrivers+1
  else:
    speeders=speeders+1