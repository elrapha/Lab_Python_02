theInput = raw_input("Enter an integer: ")
#Your code here
theInput=int(theInput)

if theInput % 2 == 0:
    print "even"
else:
    print "odd"

print "\n"
print "------------------------------------------------"
print "\n"

primSchAge=6
legalVotnAge=18
presidentAge=40
retireAge=60

personsAge = input('Enter an age: ')

if personsAge < primSchAge:
    print 'Too young'
elif personsAge >= legalVotnAge :
    print 'Remember to vote'
elif personsAge>=presidentAge:
    print 'Vote for me'
elif personsAge < presidentAge:
    print "You can't be president"
elif personsAge>=retireAge:
    print 'Too old'            
     
print "\n"
print "------------------------------------------------"
print "\n"

i=40
while i>0:
    i=i-1
    if i%3==0:
        print i        

print "\n"
print "------------------------------------------------"
print "\n"

for i in range(6,30,1):
    if i%2!=0 and i%3!=0 and i%5!=0:
        print i

print "\n"
print "------------------------------------------------"
print "\n"
n=1
while (79*n)%97 != 1:
    n=n+1
print 'n is= ', n


























