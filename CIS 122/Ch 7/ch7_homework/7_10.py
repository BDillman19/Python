def neutral():
  sound = makeSound(pickAFile())
  count = 0
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value == 0:
      count += 1
  print count