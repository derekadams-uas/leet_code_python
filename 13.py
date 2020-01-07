class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': -2,
            'IX': -2,
            'XL': -20,
            'XC': -20,
            'CD': -200,
            'CM': -200
        }

        total = 0
        for key in symbols.keys():
            key_count = s.count(key)
            total += (key_count * symbols[key])

        return total
