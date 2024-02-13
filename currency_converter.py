def usd_to_gbp(amount):
    gbp_rate = 0.77
    gbp_amount = amount * gbp_rate
    return gbp_amount

def usd_to_eur(amount):
    eur_rate = 0.92
    eur_amount = amount * eur_rate
    return eur_amount

def usd_to_cny(amount):
    cny_rate = 6.98
    cny_amount = amount * cny_rate
    return cny_amount

def main():
    usd = float(input("Enter the dollar amount you wish to convert: "))
    currency_type = input("Enter the desired currency (GBP for Pounds, EUR for Euro, or CNY for Yuan): ").upper()
    
    if currency_type == "GBP":
        converted_amount = usd_to_gbp(usd)
        print(f"${usd} in GBP is {converted_amount}.")
    elif currency_type == "EUR":
        converted_amount = usd_to_eur(usd)
        print(f"${usd} in EUR is {converted_amount}.")
    elif currency_type == "CNY":
        converted_amount = usd_to_cny(usd)
        print(f"${usd} in CNY is {converted_amount}.")
    else:
        print("You did not select a valid currency.")

if __name__ == "__main__":
    main()
