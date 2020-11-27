#Averge calulation
totalvarsum = 0
var = 0
numtest = input("Enter Number Of classes you have taken ")
numpresub = int(numtest)
num = numpresub - 1
while num >= 0:
    varstr = input("Enter average of a class ")
    varint = int(varstr)
    num -=1
    var = var + varint
totalvarvar = var / numpresub
totalvaravr = round(totalvarvar,2)
#letter grade calulation
def letter_grade():
    if totalvaravr == 100:
        f.write("\nYou have an A+!")
    elif totalvaravr >= 95:
        f.write("\nYou have an A!")
    elif totalvaravr >= 90:
        f.write("\nYou have an A-!")
    elif totalvaravr >= 89:
        f.write("\nYou have a B+!")
    elif totalvaravr >= 85:
        f.write("\nYou have a B!")
    elif totalvaravr >= 80:
        f.write("\nYou have a B-!")
    elif totalvaravr >= 79:
        f.write("\nYou have a C+!")
    elif totalvaravr >= 75:
        f.write("\nYou have a C!")
    elif totalvaravr >= 70:
        f.write("\nYou have a C-!")
    elif totalvaravr >= 69:
        f.write("\nYou have a D+!")
    elif totalvaravr >= 67:
        f.write("\nYou have a D!")
    elif totalvaravr >= 65:
        f.write("\nYou have a D-!")
    elif totalvaravr <= 65:
        f.write("\nYou have a F!")
#gpa calculation
x = totalvaravr - 70
y = x * 0.067
z = y + 2
zv2 = str(z)
gpa = round(zv2,3)
#export to file var
def export_grades():
    f.write("your average from all your classes is " + str(totalvaravr))
    letter_grade()
    f.write("\nYour GPA is " + gpa)
#export to file
f = open("grades.txt", "w")
export_grades()
#print
f.close()
f = open("grades.txt", "r")
print(f.read())