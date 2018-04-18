setMediaPath()
def makeCatalog(product, image, price):
  file = open(getMediaPath("catalog.html"), "wt")
  body = """<!DOCTYPE html>
  <html>
  <head>
  <title>Catalog Page for:"""+product+'''</title>
  </head>
  <body>
  <h1>'''+product+""" is the greatest!</h1>
  <p>You are so lucky to have found this page! You have the opportunity to buy """+product+""" for the low, low price of $"""+str(price)+'''.  Just take a look at this beauty!
   <img src="'''+image+'''" height = 100></p>
   <p>Get one today!<p/>
   </body>
   </html>'''
  file.write(body)
  file.close()