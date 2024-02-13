# Define the is_triangle function here.
# Return ONLY the boolean result of the evaluation
# I've provided some code to get you started
def is_triangle(a, b, c):
  if (a + b < c) or (b + c < a) or (a + c < b):
    return False
  else:
    return True


# Define your main() function here.
# I've provided some code to get you started here as well
def main():
  side1 = float(input("Enter the length of side 1: "))
  side2 = float(input("Enter the length of side 2: "))
  side3 = float(input("Enter the length of side 3: "))
  triangle = is_triangle(int(side1), int(side2), int(side3))
  if triangle == True:       
    print("Yes, it is a triangle")
  else:
    print("No, it is not a triangle")

# Hmmmm...what's missing down here?

if __name__ == "__main__":
  main()
