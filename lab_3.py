
print("----- AREA CALCULATOR -----")
print("1. Square")
print("2. Rectangle")
print("3. Triangle")
print("4. Circle")

choice = int(input("Choose a shape: "))

if choice == 1:
    side = float(input("Enter side: "))
    area = side * side
    print("Area of Square =", area)

elif choice == 2:
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    area = length * breadth
    print("Area of Rectangle =", area)

elif choice == 3:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print("Area of Triangle =", area)

elif choice == 4:
    radius = float(input("Enter radius: "))
    area = 3.14 * radius * radius
    print("Area of Circle =", area)

else:
    print("Invalid choice!")
