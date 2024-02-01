 

# Get the number of Shamwowzers the customer would like to order. 

def order_capture(): 

    shamwowzers_num = int(input("Enter the number of Shamwowzers sold: \n")) 

    return shamwowzers_num  

 

# Calculate the subtotal for the number of Shamwowzers ordered 

def subtotal(num): 

    return num * 13.00 

 

# Calculate shipping and handling costs based on the number of Shamwowzers ordered 

def ship_hand(cost): 

    return cost * 3.00 

 

def total_cal(subtotal, ship): 

    return subtotal + ship 

 

def main(): 

    print("Welcome to Shamwowzer, the worlds most absorbent shammy!") 

    num = order_capture() 

    my_subtotal = subtotal(num) 

    my_shiphand = ship_hand(num) 

    my_total = total_cal(my_subtotal, my_shiphand) 

    print(f"You ordered {num}. Your subtotal is ${my_subtotal}, shipping and handling is ${my_shiphand}, and total amount due is ${my_total}") 

 

if __name__ == "__main__": 

    main() 

 

 