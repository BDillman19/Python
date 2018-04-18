def increaseVolume(sound):
   for sample in getSamples(sound):
       value = getSampleValue(sample)
       setSampleValue(sample, value* 2)
##################################################
def decreaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * .5)
##################################################
def increaseVolume2(sound):
  samples = getSamples(sound)
  for index in range(len(samples)):
    sample = samples[index]
    value = getSampleValue(sample)
    setSampleValue(sample, value * 2)
##################################################

def changeVolume(sound, factor):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * factor)
##################################################    
def normalize(sound):
  largest = 0
  for s in getSamples(sound):
    largest = max(largest, getSampleValue(s))
  multiplier = 32767.0 / largest
  print "Largest sample value in original sound was", largest
  print "multiplier is", multiplier
  
  for s in getSamples(sound):
    louder = multiplier * getSampleValue(s)
    setSampleValue(s, louder)
##################################################
def onlyMaximize(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value >= 0:
      setSampleValue(sample, 32767)
    if value < 0:
      setSampleValue(sample, -32768)
##################################################
