file = pickAFile()
def increaseVolumeNamed(file):
   sound = makeSound(file)
   for sample in getSamples(sound):
       value = getSampleValue(sample)
       setSampleValue(sample, value* 2)
   play(sound)