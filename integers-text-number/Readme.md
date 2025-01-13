# Number to Word Translation (1-3 Digits)

## Theory

This Python program is designed to convert an integer (up to 3 digits) into its corresponding word representation. The program takes an input number from the user, verifies that it is a valid integer with 1 to 3 digits, and then converts each individual digit into its word form (e.g., `123` becomes `ONE TWO THREE`).

The conversion uses a dictionary where each digit ('0' to '9') is mapped to its word representation (e.g., '0' -> 'ZERO', '1' -> 'ONE', etc.).

## Steps

1. **Dictionary Setup**:
   The program uses a dictionary called `digit_to_word` to map each digit (as a string) to its corresponding word representation in uppercase.
   
   ```python
   digit_to_word = {
       '0': 'ZERO', '1': 'ONE', '2': 'TWO', '3': 'THREE', '4': 'FOUR',
       '5': 'FIVE', '6': 'SIX', '7': 'SEVEN', '8': 'EIGHT', '9': 'NINE'
   }
   ```

2. **Input Validation**:
   The program prompts the user to input an integer. It checks if the input consists of only digits (`isdigit()`) and ensures that the input length is between 1 and 3 characters (i.e., the number should be 1 to 3 digits).

   ```python
   num = input("Enter an integer (up to 3 digits): ")
   if num.isdigit() and 1 <= len(num) <= 3:
       ...
   ```

3. **Conversion of Digits to Words**:
   After validating the input, the program converts the number to a string and maps each digit to its corresponding word using the `digit_to_word` dictionary. It joins the words together with spaces and returns the result.

   ```python
   return ' '.join(digit_to_word[digit] for digit in str(num))
   ```

4. **Output**:
   Finally, the program prints the translated result, where each digit is displayed as its corresponding word.

   ```python
   print(translate_number(num))
   ```

5. **Error Handling**:
   If the user inputs an invalid number (either not an integer or not between 1 to 3 digits), the program will prompt the user to enter a valid integer.

   ```python
   else:
       print("Please enter a valid integer with 1 to 3 digits.")
   ```

## Example

### Input:
```
Enter an integer (up to 3 digits): 578
```

### Output:
```
FIVE SEVEN EIGHT
```

---

### Input:
```
Enter an integer (up to 3 digits): 34
```

### Output:
```
THREE FOUR
```

---

### Input:
```
Enter an integer (up to 3 digits): 1
```

### Output:
```
ONE
```

---

## Conclusion

This program demonstrates a simple approach to converting an integer (up to 3 digits) into its corresponding word form. It leverages a dictionary to efficiently map digits to words and ensures user input is validated for correctness. The output is a string of words representing the digits of the input number, making it suitable for applications where you might need to display numbers in a verbal form.

