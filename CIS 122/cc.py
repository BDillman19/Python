n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
  result = ""
  for word in words:
     result += word
  return result

print join_strings(n)