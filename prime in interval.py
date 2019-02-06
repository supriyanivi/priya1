num = int(input("enter the number"))
sum = 0
temp = num
while temp>0:
digit = temp %10
sum+=digit**3
temp//=10
if num== sum:
print(num,"yes,it is an armstrong number")
else:
print(num,"no,it is not an armstrong number")
