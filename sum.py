# Keep adding numbers until 0 is entered
a = 1
s = 0
print("Enter numbers to add to the sum.")
print("Enter 0 to quit.")
while a != 0:
    print("Current Sum:", s)
    a = float(input("Number? "))
    s = s + a
print("Total sum =", s)