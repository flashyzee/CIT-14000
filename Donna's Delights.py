def order_capture():
    my_cakes = int(input("Enter the number of cupcakes sold: "))
    return my_cakes

def subtotal(num):
    return num * 4.00

def tax_cal(subtotal):
    return subtotal * 0.08 

def total_cal(subtotal, tax):
    return subtotal * tax

def main():
    print("Welcome to Donna's Delights")
    num = order_capture()
    my_subtotal = subtotal(num)
    my_tax = tax_cal(my_subtotal)
    my_total = total_cal(my_subtotal, my_tax)
    print(f"You ordered {num}. Your subtotal is ${my_subtotal}, tax is ${my_tax}, and total amount due is ${my_total} : ")

if __name__ == "__main__":
    main()


