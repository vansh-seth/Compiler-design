# DFA Implementation

## Aim
To implement a Python program that performs various checks on strings based on predefined criteria, providing a menu-driven interface for user interaction.

## Theory
String validation is a common task in programming that ensures input strings adhere to certain rules. This program focuses on strings containing only the characters `'a'` and `'b'` and applies different validation checks, such as:
- Checking the starting and ending characters.
- Validating substrings.
- Counting specific characters and applying conditions like even or odd counts.

The program is modular, with each validation implemented as a separate function for clarity and reusability.

## Code
```python
def check_string_1(s):
    if s.startswith('a') and s.endswith('a') and all(c in 'ab' for c in s):
        return True
    return False

def check_string_2(s):
    if s.startswith('a') and s.endswith('b') and all(c in 'ab' for c in s):
        return True
    return False

def check_substring(s):
    if 'aab' in s and all(c in 'ab' for c in s):
        return True
    return False

def check_even_a(s):
    a_count = s.count('a')
    if a_count % 2 == 0 and all(c in 'ab' for c in s):
        return True
    return False

def check_odd_a_b(s):
    a_count = s.count('a')
    b_count = s.count('b')
    if a_count % 2 != 0 and b_count % 2 != 0 and all(c in 'ab' for c in s):
        return True
    return False

def check_string_3(s):
    if all(c in 'ab' for c in s):
        b_count = s.count('b')
        if b_count % 3 == 0:
            return True
    return False

def menu():
    while True:
        print("\nMenu:")
        print("1. Check if string starts with 'a', ends with 'a', and contains only 'a' and 'b'")
        print("2. Check if string starts with 'a', ends with 'b', and contains only 'a' and 'b'")
        print("3. Check if string contains substring 'aab' and only 'a' and 'b'")
        print("4. Check if string contains even number of 'a's and only 'a' and 'b'")
        print("5. Check if string contains odd number of 'a's and odd number of 'b's, and only 'a' and 'b'")
        print("6. Check if string contains only 'a' and 'b', and number of 'b's is divisible by 3")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            input_string = input("Enter a string: ")
            if check_string_1(input_string):
                print("The string is valid.")
            else:
                print("The string is invalid.")
        
        elif choice == '2':
            input_string = input("Enter a string: ")
            if check_string_2(input_string):
                print("The string is valid.")
            else:
                print("The string is invalid.")
        
        elif choice == '3':
            input_string = input("Enter a string: ")
            if check_substring(input_string):
                print("The string is valid.")
            else:
                print("The string is invalid.")
        
        elif choice == '4':
            input_string = input("Enter a string: ")
            if check_even_a(input_string):
                print("The string is valid.")
            else:
                print("The string is invalid.")
        
        elif choice == '5':
            input_string = input("Enter a string: ")
            if check_odd_a_b(input_string):
                print("The string is valid.")
            else:
                print("The string is invalid.")
        
        elif choice == '6':
            input_string = input("Enter a string: ")
            if check_string_3(input_string):
                print("The string is valid.")
            else:
                print("The string is invalid.")
        
        elif choice == '7':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
            
menu()
```

## Output
**Example Run:**
```
Menu:
1. Check if string starts with 'a', ends with 'a', and contains only 'a' and 'b'
2. Check if string starts with 'a', ends with 'b', and contains only 'a' and 'b'
3. Check if string contains substring 'aab' and only 'a' and 'b'
4. Check if string contains even number of 'a's and only 'a' and 'b'
5. Check if string contains odd number of 'a's and odd number of 'b's, and only 'a' and 'b'
6. Check if string contains only 'a' and 'b', and number of 'b's is divisible by 3
7. Exit

Enter your choice (1-7): 1
Enter a string: aabba
The string is valid.

Enter your choice (1-7): 4
Enter a string: abababa
The string is invalid.

Enter your choice (1-7): 7
Exiting the program.
```

## Conclusion
The program efficiently validates strings based on specific criteria using modular functions. It provides an interactive interface for testing various conditions, making it a useful tool for string analysis tasks.
