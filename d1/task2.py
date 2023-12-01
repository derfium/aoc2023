digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits_numerical = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def get_value(string, digits):
    pos = 10000
    val = ""
    for i, digit in enumerate(digits):
        position = string.find(digit)
        if position != -1 and position < pos:
            pos = position
            val = i
    for digit in digits_numerical:
        position = string.find(digit)
        if position != -1 and position < pos:
            pos = position
            val = digit
    return str(val)

        
        
with open("d1/input.txt") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        first = get_value(line, digits)
        
        reversed_digits = [digit[::-1] for digit in digits]
        last = get_value(line[::-1], reversed_digits)
        sum += int(first + last)

    print(sum) # 54019
            
        