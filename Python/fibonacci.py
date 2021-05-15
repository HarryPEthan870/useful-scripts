terms_l = []
terms = int(input("enter what term number you want: "))
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
for num in range(terms):
    terms_l.append(fibonacci(num))
    print(terms_l)
print(terms_l[terms-1])

