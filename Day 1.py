msg="hello world"
print(msg)
#=hello world


msg=2+2
print(msg)
#=4


msg=int(7/5)
print(msg)
#=1


msg=int(2**3)
print(msg)
#=8


msg=0.1+0.2-0.3
print(msg)
#=5.5532e-17


msg = 3
print(msg)
#=3


#typr of data type used
msg=3.2
print(type(msg))
#=float


#string
msg = 'a'
print(msg)
#=a


msg="I'm going on a \nrun"
print (msg)
#=I'm going on a 
#run

#length of a string
print(len('hello'))  
#=5

#INDEXING AND SLICING
msg="hello"
print(msg[1])  #indexing
print('Hello'[3])
#=e
#=l


msg="This is me learning"
print(msg[1:4])   #slicing
#=his
print(msg[2:9:2]) #slicing last 2 means jump to 2 steps
#=i sm
print(msg[::-1])  #reversing the string
#=gninrael em si sihT

msg="Hello"
last_letter="ello"
print('b'+last_letter)  #string concatenation
#=bello
print(msg*10)  
#=HelloHelloHelloHelloHelloHelloHelloHelloHelloHello


msg="Hello World"
print(msg.upper())  #to print all letters in upppercase 
print(msg.lower())
print(msg.split())  #split string as per white spaces
print(msg.split('l'))  #split string as per l spaces

print("-".join(msg))  ##Important



String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)
  
# Updating a character of the String
## As python strings are immutable, they don't support item updation directly
### there are following two ways
#1
list1 = list(String1)
list1[2] = 'p'
String2 = ''.join(list1)
print("\nUpdating character at 2nd Index: ")
print(String2)
  
#2
String3 = String1[0:2] + 'p' + String1[3:]
print(String3)


#del String3
#print(String3) #deleting a string


msg= "I'm a good learner it seems \"right\"?" #escaping double qoutes
print(msg)
msg= 'I\'m a good learner it seems "right"?' #escaping single quotes
print(msg)

#STRING FORMATTING

print('Hello{}'.format(msg))

print('Hello {Sen1} {Sen2} {Name}'.format(Name='Chirag',Sen2='Name is',Sen1='My'))     #String Formatting

result=100/555

print(result)
print("The result was {r:1.4f}".format(r=result))  
print("The result was {r:10.4f}".format(r=result))  #FLOAT FORMATTING
result=104.234664
print("The result was {r:1.4f}".format(r=result))

print(f"The result was {result}")    ##New way to use inside output variable