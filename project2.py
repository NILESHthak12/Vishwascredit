while True:
    num = int(input("Enter a Number: "))
    for i in range(1,11):
        print(f"{num}*{i}={num*i}")
    result =input("Do you want to continue(y/n):")
    if result != 'y':
        break
    
    
x=5
y=6
print(x+y)