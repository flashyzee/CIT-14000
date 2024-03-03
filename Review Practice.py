def order_capture():
    while True:
        try:
            quantity = int(input("Enter the number of cupcakes sold:"))
            if quantity < 0:
                print("Error: Please enter a positive number.")
            else:
                return quantity
        except ValueError:
            print("Error: Please enter a valid number.")

def subtotal(num):
    if num >= 5:
        return num * 4.00
    else:
        return num * 5.00

def tax_cal(subtotal):
    return subtotal * 0.08 

def total_cal(subtotal, tax):
    return subtotal + tax

def main():
    print("Welcome to Donna's Delights")
    
    num = order_capture()
    my_subtotal = subtotal(num)
    my_tax = tax_cal(my_subtotal)
    my_total = total_cal(my_subtotal, my_tax)
    print(f"You ordered {num}. Your subtotal is ${my_subtotal}, tax is ${my_tax}, and total amount due is ${my_total}")

if __name__ == "__main__":
    main()