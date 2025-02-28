def translate_number(num):
    digit_to_word = {
        '0': 'ZERO', '1': 'ONE', '2': 'TWO', '3': 'THREE', '4': 'FOUR',
        '5': 'FIVE', '6': 'SIX', '7': 'SEVEN', '8': 'EIGHT', '9': 'NINE'
    }
    return ' '.join(digit_to_word[digit] for digit in str(num))
num = input("Enter an integer (up to 3 digits): ")
if num.isdigit() and 1 <= len(num) <= 3:
    print(translate_number(num))
else:
    print("Please enter a valid integer with 1 to 3 digits.")
