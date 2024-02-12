def function(a,b):
    s = (i**2 for i in range(a,b+1))
    for i in s:
        print(i)

a = int(input())
b = int(input())
function(a,b)
