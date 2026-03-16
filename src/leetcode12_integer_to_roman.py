def int_to_roman(num: int) -> str:
    roman_numerals = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }
    result = ""
    for key, value in roman_numerals.items():
        while num >= value:
            result += key
            num -= value
    return result

if __name__ == "__main__":
    print(int_to_roman(4))
