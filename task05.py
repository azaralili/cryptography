# Task: x = 7^100 mod 13, find x
def mod_calc(base, exp, mod):
    y = 1 #here I consdier y as accumulator
    while exp > 0: #our exponent here is 100
        if exp % 2 == 1: #redusing the exp while its odd
            y = (y * base) % mod
        exp = exp // 2
        base = (base * base) % mod
        print(base, exp, y)
    return y
x = mod_calc(7, 100, 13)
print('The asnwers is 7^100='+str(x)+'mod13')
