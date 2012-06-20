#reversing digits
number=input('Enter the phone number: ')
encNum=0
while number>0:
    rem=number%10
    number=number/10
    encNum=encNum*10 +rem

print encNum



