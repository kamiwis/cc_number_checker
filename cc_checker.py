
def main():

    num_str = str(input("Credit card number: "))
    num = int(num_str)
    length = len(num_str)

    # if length does not equal 13, 15, or 16, INVALID number
    if length not in [13, 15, 16]:
        print("INVALID\n")
        return

    else:
        checksum = get_checksum(num, length)
        # if checksum ends in zero, continue checking validity
        if checksum % 10 == 0:
            # if length is 15, check first 2 numbers to see if it's a valid AMEX
            if length == 15:
                if num_str[0:2] == "34" or num_str[0:2] == "37":
                    print("AMEX\n")
                    return
                else:
                    print("INVALID\n")
                    return
            # if length is 16, could be either mastercard or visa
            if length == 16:
                # mastercards with end in 51-55
                if num_str[0:2] in ["51", "52", "53", "54", "55"]:
                    print("MASTERCARD\n")
                    return
                # visas will end in 4
                elif num_str[0] == "4":
                    print("VISA\n")
                    return
                else:
                    print("INVALID\n")
                    return
            # if length is 13, check if its a VISA
            if length == 13:
                if num_str[0] == "4":
                    print("VISA\n")
                    return
                else:
                    print("INVALID\n")
                    return
        else:
            print("INVALID\n")
            return


def get_checksum(num, length):
    string_num = str(num)
    to_multiply = []
    not_multiply = []
    # if length is even, add all even index numbers to the to_multiply list and odd to not_multiply
    if length % 2 == 0:
        for i in range(length):
            if i % 2 == 0:
                to_multiply.append(int(string_num[i]))
            else:
                not_multiply.append(int(string_num[i]))
    # if length is odd, add all odd indexes to the to_multiply list and even to not_multiply
    else:
        for i in range(length):
            if i % 2 == 0:
                not_multiply.append(int(string_num[i]))
            else:
                to_multiply.append(int(string_num[i]))
    # multiply all numbers in to multiply by 2 and replace with product
    for x in range(len(to_multiply)):
        product = (to_multiply[x] * 2)
        to_multiply[x] = product
    sum_to_multiply = 0
    for number in to_multiply:
        if number < 10:
            sum_to_multiply += number
        else:
            sum_to_multiply += int(number / 10) + int(number % 10)
    sum_not_mult = sum(not_multiply)
    total = sum_to_multiply + sum_not_mult
    return total


if __name__ == "__main__":
    main()