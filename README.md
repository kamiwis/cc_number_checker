# cc_number_checker
Command-line program that checks the validity of credit card numbers by using Luhn’s Algorithm in conjunction with known credit card number lengths for AMEX, MASTERCARD, and VISA. This program was created as a project for CS50's Introduction to Computer Science course on EdX.

### Functionality
This program was made to be used through your terminal.

To use the credit card number checker: use `python3 cc_checker.py`

You will then be prompted for a credit card number. Enter a credit card number, excluding any spaces or hyphens. 

The program will then either return the credit card issuer if the credit card number is valid, or return "INVALID."


#### Ideas for improvements and changes
- Incorporate other major credit card issuers like DISCOVER.
- Incorporate any additional standards that AMEX, MASTERCARD, and VISA have.
- Add functionality that allows user to input numbers with hyphens or spaces. The program will parse the given input, remove then spaces or additional characters and return an integer value that corresponds to the credit card number before continuing with the test. 
- Instead of instantiating new variable `string_num` within `get_checksum()`, add `num_str` as another argument to reduce space.


