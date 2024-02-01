import math 

#Define a function named cal_area_value 

def cal_area_value(radius): 

  return  3.14 * radius ** 2 

  return area 

 

#Summation and Product of Two Numbers 

 

def sum_and_multi(num1, num2): 

  result1 = num1 + num2 

  result2 = num1 * num2 

  return result1, result2 

  print(result1, result2) 

 

#Main Function Implementation 

def main(): 

  num1 = int(input("Enter the first number: ")) 

  num2 = int(input("Enter the second number: ")) 

  sqrt_value = math.sqrt(float(num1)) 

  area_value = cal_area_value(float(num2)) 

  my_sum, my_product = sum_and_multi(sqrt_value,  area_value) 

  print(f"The sum of your numbers is {my_sum}, and the product of your number is {my_product}") 

 

if __name__ == "__main__": 

  main() 

 