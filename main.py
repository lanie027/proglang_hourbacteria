a = int(input("Enter the initial count of the bacteria: "))
b = int(input("Enter the number of hours: "))
print("The number of bacteria per hour will be: ")

for i in range(1, a+1):
    print("Hour", i, "=", 2**6*i)