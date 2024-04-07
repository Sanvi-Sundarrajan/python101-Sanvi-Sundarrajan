largest = None
smallest = None  
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num_ip=int(num)
        if largest is None or num_ip > largest:
              largest = num_ip
        elif smallest is None or num_ip < smallest:
              smallest = num_ip
    except:
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)
