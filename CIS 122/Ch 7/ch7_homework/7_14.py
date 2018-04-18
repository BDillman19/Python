def increaseVolume3(sound, place):
  samples = getSamples(sound)
  for index in range(len(samples)):
    sample = sample[index]
    value = getSampleValue(sample)
    setSampleValue(sample, value * 2)
  writeSoundTo(place)