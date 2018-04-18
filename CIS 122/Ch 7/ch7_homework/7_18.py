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