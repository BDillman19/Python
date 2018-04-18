def negToZero():
  sound = makeSound(pickAFile())
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value < 0:
      setSampleValue(sample, 0)
  play(sound)