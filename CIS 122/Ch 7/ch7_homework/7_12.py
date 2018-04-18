def fauxIncreaseVolume(sound, increment):
  file = makeSound(sound)
  for sample in getSamples(file):
    value = getSampleValue(sample)
    value = value + increment
  play(file)