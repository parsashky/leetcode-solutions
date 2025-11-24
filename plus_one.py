def plus_one():
    digits = [4,2,4,1]
    digits.reverse()
    
    digits[0] += 1  

    b = 0
    for i in range(len(digits)):
        if digits[i] >= 10:
            a = (digits[i] % 10) + b
            digits[i] = a
            b = 1
    if b == 1:
        digits.append(1)

    digits.reverse()
    return digits

print(plus_one())
