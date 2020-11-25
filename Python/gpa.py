#Averge calulation
totalvarsum = 0
var = 0
numtest = input("Enter Number Of classes you have taken ")
numpresub = int(numtest)
num = numpresub - 1
while num >= 0:
    print(num)
    varstr = input("Enter average of  ")
    varint = int(varstr)
    num -=1
    var = var + varint
totalvaravr = var / numpresub
print ("your avarge from all your classes is " + str(totalvaravr))
#letter grade calulation
if totalvaravr == 100:
    print("You have an A+!")
elif totalvaravr >= 95:
    print("You have an A!")
elif totalvaravr >= 90:
    print("You have an A-!")
elif totalvaravr >= 89:
    print("You have a B+!")
elif totalvaravr >= 85:
    print("You have a B!")
elif totalvaravr >= 80:
    print("You have a B-!")
elif totalvaravr >= 79:
    print("You have a C+!")
elif totalvaravr >= 75:
    print("You have a C!")
elif totalvaravr >= 70:
    print("You have a C-!")
elif totalvaravr >= 69:
    print("You have a D+!")
elif totalvaravr >= 67:
    print("You have a D!")
elif totalvaravr >= 65:
    print("You have a D-!")
elif totalvaravr <= 65:
    print("You have a F!")
#gpa calculation
x = totalvaravr - 70
y = x * 0.067
z = y + 2
print("Your GPA is " + str(z))
