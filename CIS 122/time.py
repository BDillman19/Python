
"""Bryce Dillman"""
#This function will tell you the time it takes to travel a number of hours going a certain speed
def time(): 
  #get the distance travelled
  d = input("how far are you going")
  #get the speed at which you are travelling
  s = input("how fast are you going")
  #find number of hours
  h = int(d/s)
  #get miles left after number of hours
  x = d*h - s
  #make x and s float values instead of int values
  x = float(x)
  s = float(s)
  #get remainder of minutes
  y = x/s
  #turn remainder into a minute value
  m = int(y*60)
  
  print("time(hrs: min)")
  print(h, m)