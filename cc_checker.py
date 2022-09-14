
def main():
    # Get user input for credit card number as a string.
    num_str = str(input("Credit card number: "))
    # Convert user input to an int in order to be able to calculate checksum.
    num = int(num_str)
    # Get length of credit card number.
    length = len(num_str)

    # If length does not equal 13, 15, or 16, CC number cannot be a valid AMEX, MASTERCARD, or VISA, return INVALID.
    if length not in [13, 15, 16]:
        print("INVALID\n")
        return

    # If length does equal 13, 15, or 16, continue checking validity.
    else:
        # Use get_checksum function to calculate checksum.
        checksum = get_checksum(num, length)
        # If checksum ends in zero, continue checking validity.
        if checksum % 10 == 0:
            # If length is 15, check first 2 digits. If they match 34 or 37, card number is a valid AMEX.
            if length == 15:
                if num_str[0:2] == "34" or num_str[0:2] == "37":
                    print("AMEX\n")
                    return
                else:
                    print("INVALID\n")
                    return
            # If length is 16, CC number could be either MASTERCARD or VISA.
            if length == 16:
                # Check first two digits, if they match 51-55, card number is a valid MASTERCARD.
                if num_str[0:2] in ["51", "52", "53", "54", "55"]:
                    print("MASTERCARD\n")
                    return
                # Check first digit, if it is 4, card number is a valid VISA.
                elif num_str[0] == "4":
                    print("VISA\n")
                    return
                else:
                    print("INVALID\n")
                    return
            # If length is 13, check if card number is a valid VISA.
            if length == 13:
                # Check first digit, if it is 4, card number is a valid VISA.
                if num_str[0] == "4":
                    print("VISA\n")
                    return
                else:
                    print("INVALID\n")
                    return
        # If card number does not pass the above tests, the card number is invalid.
        else:
            print("INVALID\n")
            return


# Function to calculate checksum of credit card number using Luhn's algorithm.
def get_checksum(num, length):
    # Convert int credit card number to str in order to be able to loop through digits.
    string_num = str(num)
    # Instantiate a list that will include all digits that are to be multiplied by 2.
    to_multiply = []
    # Instantiate a list of all other numbers that will not be multiplied by 2.
    not_multiply = []
    # If length of credit card number is even:
    # Add all even index digits to the to_multiply list and odd index digits to not_multiply.
    if length % 2 == 0:
        for i in range(length):
            if i % 2 == 0:
                to_multiply.append(int(string_num[i]))
            else:
                not_multiply.append(int(string_num[i]))
    # If length of credit card number is odd:
    # Add all odd index digits to the to_multiply list and even index digits to not_multiply.
    else:
        for i in range(length):
            if i % 2 == 0:
                not_multiply.append(int(string_num[i]))
            else:
                to_multiply.append(int(string_num[i]))
    # Multiply all numbers in to_multiply by 2 and them with their product.
    for x in range(len(to_multiply)):
        product = (to_multiply[x] * 2)
        to_multiply[x] = product
    # Instantiate sum of all individual digits in to_multiply list.
    sum_to_multiply = 0
    # Loop through all items in to_multiply.
    for number in to_multiply:
      # If number is single digit, add digit to sum_to_multiply.
      if number < 10:
        sum_to_multiply += number
        # If number is more than one digit, split digits and individually add to sum_to_multiply.
      else:
          sum_to_multiply += int(number / 10) + int(number % 10)
    # Find sum of not_multiply list.
    sum_not_mult = sum(not_multiply)
    return sum_to_multiply + sum_not_mult


if __name__ == "__main__":
    main()