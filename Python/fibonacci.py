import functools
terms_l = []
terms = int(input("enter what term number you want: "))
@functools.lru_cache
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
for num in range(terms):
    terms_l.append(fibonacci(num))
    print(terms_l)
print(terms_l[terms-1])

