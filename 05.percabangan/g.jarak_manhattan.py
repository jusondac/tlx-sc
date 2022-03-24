# jarak manhattan formula
# res = |x1-x2| + |y1-y2|
num = input('')
x1,y1,x2,y2 = [int(x) for x in num.split(' ')]
num = abs(x1 - x2) + abs(y1 - y2)
print(num)
