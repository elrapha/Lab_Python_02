
entry=input('Enter the phone number: ')
number=entry
# Find out the weitht of the number in tens
numWeight=1
nines=9
while True:
    if number>nines:
        nines=nines*10 +9
    else:
        numWeight=nines/10+1
        break
    
#Compute the modular number conversion
num=number
newNum=0 #initialize the new number
while num>0:
    d=num/numWeight
    denc= ((d + 7) % 10)
    num=num%numWeight
    numWeight=numWeight/10
    newNum=newNum*10 + denc # form new number

number=newNum    
encNum=0
while number>0:
    rem=number%10
    number=number/10
    encNum=encNum*10 +rem

print entry," ==> ",newNum," ==> ",encNum



