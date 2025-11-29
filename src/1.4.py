import string

alphabet = [x for x in string.digits] + [x for x in string.ascii_uppercase]

def sym_to_num(sym: chr):
    try:
       return alphabet.index(sym)
    except:
       print("Invalid value!")

def to_hex(num: str, base: int):
    res = 0
    for i in range(len(num)):
        res += sym_to_num(num[len(num) - i - 1]) * base ** i
    return res

def to_any(dec: int, base: int):
    if dec == 0: return '0'
    res = ""
    while dec > 0:
        print(dec % base)
        res = alphabet[(dec % base)] + res
        dec //= base
    return res


# ---------------------------- INPUT -------------------------
num = input("Value: ").upper()
cur_base = int(input("Cur base: "))
nec_base = int(input("Necessery base: "))

print(to_hex(num, cur_base))
print(f"Res: {to_any(to_hex(num, cur_base), nec_base)}")
