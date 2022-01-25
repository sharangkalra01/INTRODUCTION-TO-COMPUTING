''' ASSIGNMENT 2
By= SHARANG KALRA
SID= 21103012 '''

# QUESTION 1

string1="Python is a case sensitive language" #String1
# A)
print("<A>THE LENGTH OF STRING IS",len(string1)) #Function to Find LENGTH OF STRING
# B)
print("<B>THE REVERSED STRING IS ",string1[-1::-1])
# C)
string2=string1[10:26] #STORED a case sensitive IN A NEW STRING
# D)
string2.replace("a case sensitive","object oriented") #REPLACED "a case sensitive" WITH "object oriented"
# E)
print("<E>THE INDEX OF SUBSTRING a is ",string1.find('a'))
# F)
print("<F>THE ORIGINAL STRING AFTER REMOVING WHITESPACES IS",string1.replace(" ",""))
print("\n")

#QUESTION 2

NAME=input("ENTER YOUR NAME")
SID=int(input("ENTER YOUR SID"))
DEPARTMENT=input("ENTER YOUR DEPARTMENT")
CGPA=float(input("ENTER YOUR CGPA"))
print("Hey %s,"%NAME,"Here!")
print("My SID is %d" %SID)
print("I am from %s"%DEPARTMENT,"and my CGPA is %f"%CGPA)
print("\n")

#QUESTION 3

a=56
b=10
#A)     
print("a. ",a&b)
#B)
print("b. ",a|b)
#C)
print("c. ",a^b)
#D) 
print("Left shift both a and b with 2 bits respectively are :",a<<2 ,b<<2)
#E)
print("Right shift a with 2 bits and b with 4 bits respectively are : ",a>>2,b>>4)
print("\n")

#QUESTION 4

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
 
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3
 
print("THE LARGEST NUMBER IS ",largest)
print("\n")

#QUESTION 5

i=input("ENTER A STRING")
if 'name' in i:
    print ("Yes")
else:
    print ("No")
print("\n")

#Question 6

p=int(input("ENTER FIRST SIDE OF TRIANGLE"))
q=int(input("ENTER SECOND SIDE OF TRIANGLE"))
r=int(input("ENTER THIRD SIDE OF TRIANGLE"))
if((p+q)>r and (q+r)>p and (r+p)>q and p>0 and q>0 and r>0): #All sides should be positive and sum of two sides should be greater than third side
    print("Yes")
else:
    print("No")