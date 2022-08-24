# var_a
a = int(input("Variable a: "))

# var_b
b = int(input("Variable b: "))

# operation
sum = 0
for n in range(a, b+1):
    if n % 2 == 1:
        sum += n
    else:
        continue

# print result
print(sum)
