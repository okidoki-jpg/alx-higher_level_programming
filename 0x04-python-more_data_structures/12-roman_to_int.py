#!/ust/bin/python3
def roman_to_int(roman_string):

    if type(roman_string) is not str or roman_string is None:
        return 0
    
    res =  0
    rom_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for idx in range(len(roman_string)):
        i = rom_dict.get(roman_string[idx])
        if (idx < len(roman_string) - 1):
            ii = rom_dict.get(roman_string[idx + 1])
            if ii > i:
                res -= i
            else:
                res += i
        else:
            res += i
    return (res)
