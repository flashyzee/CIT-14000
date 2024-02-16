def get_usd():
    while True:
        try:
            n = float(input("Enter the dollar amount you wish to convert: "))
            if n > 0:
                return n
            else:
                print("Entry must be greater than 0")
        except ValueError:
            print("You did not enter a number")


def get_currency():
    while True:
        currency = input("Enter the desired currency (GBP for Pounds, EUR for Euro, or CNY for Yuan, ₦ for Naira): ").upper()
        if currency in ["GBP", "EUR", "CNY", "₦"]:
            return currency
        else:
            print("You did not enter a valid currency type")


def usd_to_gbp(amount):
    return amount * 0.77
  

def usd_to_naira(amount):
  naira_rate = 15185.0
  naira_amount = amount * naira_rate
  return naira_amount


def usd_to_eur(amount):
    return amount * 0.92


def usd_to_cny(amount):
    return amount * 6.98


def main():
    amount = get_usd()
    currency_type = get_currency()

    if currency_type == "GBP":
        converted_amount = usd_to_gbp(amount)
        print(f"${amount} in GBP is {converted_amount}.")
    elif currency_type == "EUR":
        converted_amount = usd_to_eur(amount)
        print(f"${amount} in EUR is {converted_amount}.")
    elif currency_type == "CNY":
        converted_amount = usd_to_cny(amount)
        print(f"${amount} in CNY is {converted_amount}.")
    elif currency_type == "₦":
      converted_amount = usd_to_naira(amount)
      print(f"${amount} in ₦ is {converted_amount}.")
    else:
        print("You did not select a valid currency.")


if __name__ == "__main__":
    main()
