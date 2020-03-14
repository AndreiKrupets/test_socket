fib1 = 0
fib2 = 1
summ_even = 0
lst_even = [0,1]
with open('fibonacci.txt', 'a') as file:
    while fib2 < 4000000:
        fib1, fib2 = fib2, fib1 + fib2
        file.write(str(fib1) + ',')
        if fib2 % 2 == 0:
            summ_even += fib2
        else:
            continue
    file.write('the sum of the even digit in limit 4kk ==  ' +str(summ_even))



