def bullseye():
  canvas = makeEmptyPicture(401, 401)
  addArcFilled(canvas, 150, 150, 100, 100, 0, 180, red)
  addArcFilled(canvas, 150, 150, 100, 100, 0, -180, red)
  addArc(canvas, 100, 100, 200, 200, 0, 180, red)
  addArc(canvas, 100, 100, 200, 200, 0, -180, red)
  addArc(canvas, 50, 50, 300, 300, 0, 180, red)
  addArc(canvas, 50, 50, 300, 300, 0, -180, red)
  explore(canvas)