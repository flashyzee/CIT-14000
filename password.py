def main():
    password = input('Please enter a string to encode: ')
    password = password.upper()
    
    # Remove all spaces
    password = password.replace(" ", "")
    
    # Replace all E's with 3's
    password = password.replace("E", "3")
    
    # Replace all S's with 5's
    password = password.replace("S", "5")
    
    # Reverse the password
    password = password[::-1]
    
    # Print the user's new password to the screen
    print(password)

if __name__== "__main__":
    main()
