"""var1= 86.9
print (type(var1))"""
#############################
"""print ("Inter your name")
name= input()
print ("Hi,",name) 
while True:
	print ("What do you want to do,", name)
	print ("Press 1 for add (+),", name)
	print ("Press 2 for subs (-),", name)
	print ("Press 3 for multiply (×),",name)
	print ("Press 4 for divide (÷),",name)
	print ("Press 5 for persentage (%),",name)
	print ("Please inter your choise here")
	choise= input()
	if choise== "1":
		print (" Inter first no. ",name)
		input1= input ()
		print (" Inter your second no. ",name)
		input2 = input ()
		b = int(input1) + int(input2) 
		print (" The result is-",end=" ")
		print (b,name)
	elif choise== "2":
		print (" Inter first no. ",name)
		input1= input ()
		print (" Inter your second no. ",name)
		input2 = input ()
		b = int(input1) - int(input2) 
		print (" The result is-",end=" ")
		print (b,name)
	elif choise== "3":
		print (" Inter first no. ",name)
		input1= input ()
		print (" Inter your second no. ",name)
		input2 = input ()
		b = int(input1) * int(input2) 
		print (" The result is-",end=" ")
		print (b,name)
	elif choise== "4":
		print (" Inter first no. ",name)
		input1= input ()
		print (" Inter your second no. ",name)
		input2 = input ()
		b = int(input1) / int(input2) 
		print (" The result is-",end=" ")
		print (b,name)
	elif choise== "5":
		print (" Inter first no. ",name)
		input1= input ()
		print (" Inter your second no. ",name)
		input2 = input ()
		b = int(input1) / int(input2) * 100
		print (" The result is-",end=" ")
		print (b,name)
	else :
		print ("error please check your input",name)
	print("if you want to recalculate please inter y\nif you want to exit the the program please inter n")
	input1000=input()
	if input1000=="y":
		continue
	elif input1000=="n":
		print("by,",name,"See you later.")
		break
	else:
		print("Please check your input")
		break"""


############################


"""print("Welcome")
dict = {"Sushant":"Hello", "Nishant":"Roti"}
print(type(dict))
print(dict[input()])"""

#############################

"""print("Welcome to the Guess The Number Game\n\ninstruction\nYou will get only 9 chance to Guess the number. ")


import random
random_number= random.randint(0,100)
print(random_number)

print("Ok, now Guess the Number")
while (True)<=9:
	number_of_guesses=0
	number_of_guesses=number_of_guesses+1
	
	no=random_number
	
	a=int(input ())
	

	if number_of_guesses>=9:
		print("Game Over\nYou took full of 9 guesses and you have not guessed.")
		print("\nif you want to play again please inter y \nIf you want to quit the game please inter n:")
		r=input()
		if r=="y":
			print("Ok, now Guess the Number")
			continue
		elif r=="n": break
		else:
			print ("Please check your input")
			break
		break
	elif a<no:
		print("Please inter greater number")
		continue
	elif a>no:
		print("Please inter smaller number")
		continue
	elif a==no:
		print("You guessed the number")
		print("You took",number_of_guesses,"chances")

		print("if you want to play again please inter y \nIf you want to quit the game please inter n:")
		r=input()
		if r=="y":
			print("Ok, now Guess the Number")
			random_number= random.randint(0,100)
			print(random_number)
			continue
		elif r=="n":
			break"""

#############################

"""print("Welcome to (Snake, Water, Gun) game\nInstruction: \nYou have only 10 chance \nYou have to chose one of the following:\ni)Snake\nii)Water\niii)Gun\n\nOk, let's start the game")
number_he_has_played=1
import random
while True:
	list =("Snake","Water","Gun")
	random_number= random.choice(list)
	
	
	s="snake"
	w="water"
	g="gun"
	
	a=input()
	print("computer chose", random_number)
	number_he_has_played= number_he_has_played+1
	if number_he_has_played == 11:
		break
	if a == s and random_number== "Snake":
		print ("Tie")
		print(" ")
		continue
	elif a == w and random_number== "Snake":
		print ("Computer Won")
		print(" ")
		continue
	elif a == g and random_number== "Snake":
		print ("You Win")
		print(" ")
		continue
	elif a == s and random_number== "Water":
		print ("You Win")
		print(" ")
		continue
	elif a == w and random_number== "Water":
		print ("Tie")
		print(" ")
		continue
	elif a == g and random_number== "Water":
		print ("Tie")
		print(" ")
		continue
	elif a == s and random_number== "Gun":
		print ("Computer Win")
		print(" ")
		continue
	elif a == w and random_number== "Gun":
		print ("Tie")
		print(" ")
		continue
	elif a == g and random_number== "Gun":
		print ("Tie")
		print(" ")
		continue
	else:
		print("Please check your input")
		print("You chose ", a)
		break"""

##############################
"""while True:
	a= (int(input("How many rows do you want: ")))
	b= (int(input("Please inter 1 or 2: ")))
	count=0
	if (b)==1:
		while (count<=a):
			print("*"*count)
			count=count+1

	if (b)==2:
		count=a
		while (count!=0):
			print("*"*count)
			count=count-1"""

############################
"""a= (int(input("How many rows do you want: ")))
b= (int(input("Please inter 1 or 2: ")))
count=0
no =0
if (b)==1:
	while (count<=a):
		print((str(no))*count)
		count=count+1
		no=no+1
if(b)==2:
	a=a+1
	count=a
	while (count!=0):
		print((str(no))*count)
		count=count-1
		no=no+1"""

##############################


while True:
	input1=(str(input("What do you want to do:\n1. Read\n2. Write\n\n")))
	if input1=="1":
		input2=input("\nFor whome do you want to read:\n1. Harry\n2. Rohan\n3. Sushant\n\n")
		if input2=="1":
			while True:
				input3=input("\nFor what do you want to read:\n1. Exercise\n2. Food\n\n")
				if input3=="1":
					f=open("Harry.Exercise.txt")
					print("\n",f.read(),"\n")
					f.close()
					break
				elif input3=="2":
					f=open("Harry.Food.txt")
					print("\n",f.read(),"\n")
					f.close()
					break
				else:
					print("\nPlease check your input")
					continue