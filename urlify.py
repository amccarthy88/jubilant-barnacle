def URLify(string):
  strlist = [*string]
  urlstr = ""
  for i in strlist:
    if i != " ":
      urlstr += i
    else:
      urlstr += "%20"
  return urlstr

print(URLify("mr john smith"))
