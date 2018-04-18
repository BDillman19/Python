setMediaPath()

def makePage():
  file = open(getMediaPath("generated.html"), "wt")
  file.write("""<!DOCTYPE html>
  
  <html>
  <head> <title> The Simplest Possible Web Page</title>
  </head>
  <body>
  <h1>A Simple Heading</h1>
  <p>some simple text.</p>
  </body>
  </html>""")
  file.close()