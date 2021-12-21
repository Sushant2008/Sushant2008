def reverse(s): 

  str = "" 

  for i in s: 

    str = i + str

  return str

  

s = "Enter a word"

  

  

print (">>> : ",end="") 

print (reverse(s))




###############
while True:
    print ((input("what is your name?\n"))[::-1])
    d=input("retry?\n")
    if d=="y":
        continue
    else:
        break
