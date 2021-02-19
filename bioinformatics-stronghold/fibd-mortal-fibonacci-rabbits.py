n=98
m=18

months=[i for i in range(1,m+1)][::-1]
numbers={}
for month in months:
    numbers[month]=0
numbers[m]=1
print(numbers)
for trig in range(n-1):
    copy=numbers.copy()
    newborn=0
    dead=numbers[1]
    for key in numbers.keys():
        if key==m:
            pass
        elif key==1:
            newborn+=copy[key]
        else:
            newborn+=copy[key]
            numbers[key]=copy[key+1]
    numbers[m]=newborn
    numbers[1]=copy[1]+copy[2]-dead
    print(numbers)
print(sum([numbers[key] for key in numbers.keys()]))
