# sum even-valued fibonacci numbers less than 4,000,000

# as you generate fibonacci numbers add the ones that are even to a sum

fib_sum = 0
fib_prev = 1
fib_cur = 2

while fib_cur < 4000000: 
    if fib_cur % 2 == 0: 
        fib_sum = fib_sum + fib_cur
    
    temp = fib_cur
    fib_cur = fib_cur + fib_prev
    fib_prev = temp

print(fib_sum)