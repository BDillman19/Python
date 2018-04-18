#CH7 Homework Problems
############################################
#7.2
#Converting to 2's complement
#-9 = 11110111
#4  = 00000100
#-27= 11100101

############################################
#7.6
file = pickAFile()
def increaseVolumeNamed(file):
   sound = makeSound(file)
   for sample in getSamples(sound):
       value = getSampleValue(sample)
       setSampleValue(sample, value* 2)
   play(sound)
   
############################################
#7.8
def negToZero():
  sound = makeSound(pickAFile())
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value < 0:
      setSampleValue(sample, 0)
  play(sound)
  
############################################
#7.10
def neutral():
  sound = makeSound(pickAFile())
  count = 0
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value == 0:
      count += 1
  print count
  
############################################
#7.12
def fauxIncreaseVolume(sound, increment):
  file = makeSound(sound)
  for sample in getSamples(file):
    value = getSampleValue(sample)
    value = value + increment
  play(file)
  
############################################
#7.14
def increaseVolume3(sound, place):
  samples = getSamples(sound)
  for index in range(len(samples)):
    sample = sample[index]
    value = getSampleValue(sample)
    setSampleValue(sample, value * 2)
  writeSoundTo(place)
  
############################################
#7.18
def sprinkles():
  sound = makeSound(pickAFile())
  count = 0
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if count % 3 == 0:
      if value >= 0:
        setSampleValue(sample, 32767)
      if value < 0:
        setSampleValue(sample, -32768)
    count += 1
  explore(sound)