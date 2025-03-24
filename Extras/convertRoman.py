def romanToInt(s: str) -> int:
        r = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        res = 0
        n = len(s)
        for i in range(n):
            if i + 1 < n and r[s[i]] < r[s[i+1]]:
                res -= r[s[i]]
            else:
                res += r[s[i]]
        return res
def intToRoman(num: int) -> str:
        r = [
            ['M', 1000],
            ['CM', 900],
            ['D', 500],
            ['CD', 400],
            ['C', 100],
            ['XC', 90],
            ['L', 50],
            ['XL', 40],
            ['X', 10],
            ['IX', 9],
            ['V', 5],
            ['IV', 4],
            ['I', 1]
        ]
        res = ''
        for sym, val in r:
            if num // val :
                count = num // val
                res += (sym * count)
                num = num % val
        return res
        
def convertRoman(input):
    if input.isdigit():
        return intToRoman(int(input))
    elif isinstance(input, str):
        return romanToInt(input)
    else:
        raise ValueError("Input must be a string representing an integer or a Roman numeral")
print(convertRoman("III")) # 3
print(convertRoman("4")) # IV