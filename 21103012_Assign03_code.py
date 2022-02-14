''' By = SHARANG KALRA
    SID= 21103012
'''

#ASSIGNMENT3
#QUESTION1

name=str(input("ENTER YOUR VALUE: "))
list=name.split() 
dict={} 
if len(list)==1:   #this is the case of single word.
    for i in list[0]:
        if i in dict:
            dict[i]+=1 #if the letter is repeated its value get increased by 1.
        else:
            dict[i]=1
    print(dict)   
else:                   #this is the case of multiple words
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
print("\n")

#QUESTION2

month=int(input("ENTER THE MONTH OF THE YEAR :"))


if(month in[1,3,5,7,8,10,12]):  #The given months in the list has 31 days 
    day=int(input("enter the day :"))
    if(1<=day<=31):
        year=int(input("enter the year: "))
        if(1800<=year<=2025):
            print("Date-",day,"/",month,"/",year)
            if(month==12 and day==31):
                print("Next Date :","1/1/",year+1)  #If the input date is last day of the year , output will be 1 more than the input year.
            elif(day==31):
                print("Next Date :","1/",month+1,"/",year)
            else:
                print("Next Date :",day+1,"/",month,"/",year)
        else:
            print("THE YEAR YOU ENTERRED IS INCORRECT")
    else:
         print("THE DATE YOU ENTERED IS INCORRECT")
elif(month in[4,6,9,11]):  #The months in this list has 30 days.
    day=int(input("enter the day :"))
    if(1<=day<=30):
        year=int(input("enter the year :"))
        if(1800<=year<=2025):
            print("Date-",day,"/",month,"/",year)
            if(day==30):
                print("Next Date :","1/",month+1,"/",year)
            else:
                print("Next Date :",day+1,"/",month,"/",year)
        else:
            print("THE YEAR YOU ENTERED IS INCORRECT")
    else:
         print("THE DATE YOU ENTERED IS INCORRECT")
elif(month==2):  #The month has 28 or 29 days in this case.
    year=int(input("enter the year :"))
    if(1800<=year<=2025):
        day=int(input("enter the day :"))
        if(year%4==0):  #leap year case
            if(1<=day<=29):
                print("Date-",day,"/",month,"/",year)
                if(day==29):
                    print("Next Date :","1/",month+1,"/",year)
                else:
                    print("Next Date :",day+1,"/",month,"/",year)              
            else:
                print("THE DAY YOU ENTERED IS INCORRECT")
        else:
            if(1<=day<=28):   #Non-leap year case
                print("Date-",day,"/",month,"/",year)
                if(day==28):
                    print("Next Date :","1/",month+1,"/",year)
                else:
                    print("Next Date :",day+1,"/",month,"/",year)       
            else:
                print("THE DATE YOU ENTERED IS INCORRECT")     
    else:
        print("THE YEAR YOU ENTERED IS INCORRECT")
else:
    print("THE MONTH OF THE YEAR YOU ENTERED IS INCORRECT")
 

#QUESTION3

list1 = input('Enter elements of a list :')
list2 = list1.split()

print('list: ', list2)


for i in range(len(list2)):
    list2[i] = int(list2[i]) # convert each item to int type
final_list =[(list2[i], list2[i]**2) for i in range(len(list2))] #this 'for' is used to cover every value.

print("The tuples list with number and it's square is :", final_list)

print("\n")  

#QUESTION4  

Grade=int(input("Give your grade points ranging from 4 to 10 :"))
if(Grade==4):
    print("Your Grade is 'D' and Poor Performance")
elif(Grade==5):
    print("Your Grade is 'C' and Below average Performance")
elif(Grade==6):
    print("Your Grade is 'C+' and Average Performance")
elif(Grade==7):
    print("Your Grade is 'B' and Good Performance")
elif(Grade==8):
    print("Your Grade is 'B+' and Very Good Performance")
elif(Grade==9):
    print("Your Grade is 'A' and Excellent Performance")
elif(Grade==10):
    print("Your Grade is 'A+' and Outstanding Performance")
else:
    print("error")

#QUESTION5  

for i in range(6):
    for j in range(i):  #This will produce spaces.
        print(' ', end='')
    for j in range(2*(6-i)-1):  # This will produce characters
        print(chr(65 + j), end='')  #As the value of 'A' is 65 and so on
    print('')

#QUESTION6

Student_ID = int(input("Please enter your SID : "))
name = input("Please enter your name :")
Students = {Student_ID:name}  #created a dictionary with keys as SID and value as name. 

while True: #Loop is created to ask again and again until answer is 'N'.
    Ask_student = input("Do you want to enter another student entry, Please answer in Y or N only :").upper()
    if Ask_student == 'Y':
        Student_ID = int(input("Enter SID: "))
        name = input("Enter Name: ")
        Students[Student_ID] = name
    elif Ask_student == 'N':
        break    #This will made loop to break out , otherwise it won't stop asking.
    else:
        print('Please Answer in Y or N only.')

#A
print(Students)

#B
print({k:v for k,v in sorted(Students.items(), key= lambda x:x[1])})

#C
print({k:v for k,v in sorted(Students.items())})

#D
Student_ID = int(input("Search Name with SID: "))
print(Students[Student_ID])

#QUESTION7

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))
no_of_terms=int(input("ENTER THE NUMBER OF TERMS IN THE SERIES: "))
if no_of_terms <= 0:     #  if the number of terms is valid or not.
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   sum=0
   for i in range(no_of_terms):
       print(fibo(i))
       sum=sum+fibo(i)
#AVERAGE PART       
average=float(sum/no_of_terms)
print("The average is :",average)

#QUESTION8

Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}

#A
new_set=Set1^Set2
print(new_set)

#B
new_set=Set1^(Set2^Set3)
print(new_set)

#C
new_Set=(Set1&Set2)|(Set2&Set3)|(Set1&Set3)
print(new_Set)

#D
new_Set={1,2,3,4,5,6,7,8,9,10}
new_set=new_Set-Set1
print(new_set)

#E
new_set=new_Set-(Set1|Set2|Set3)
print(new_set)
