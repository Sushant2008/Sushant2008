def reverse(s): 

  str = "" 

  for i in s: 

    str = i + str

  return str

  

s = "Enter a word"

  

  

print (">>> : ",end="") 

print (reverse(s))
