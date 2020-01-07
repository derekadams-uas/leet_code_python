class Solution:
    def reverse(self, x: int) -> int:
        num_str = str(x)
        sign_pos = True

        if num_str[0] == '-':
            num_str = num_str[1:]
            sign_pos = False

        num_str_rev = ''.join(reversed(num_str))
        num_rev = int(num_str_rev)

        if (abs(num_rev) <= math.pow(2, 31)):
            if sign_pos:
                return num_rev
            else:
                return num_rev * -1
        else:
            return 0
