# TC = O(n)
# SC = O(1)

class Solution:
    def calculate(self, s: str) -> int:
        if s is None or len(s) == 0: return 0

        # initialize variables
        lastSign = '+'
        num = 0
        calc = 0
        tail = 0

        # trim spaces
        s = s.strip()

        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = (num * 10) + int(c)
            if (not c.isdigit() and c != ' ') or (i == len(s) - 1):
                if lastSign == '+':
                    calc = calc + num
                    tail = +num
                elif lastSign == '-':
                    calc = calc - num
                    tail = -num
                elif lastSign == '*':
                    calc = calc - tail + (tail * num)
                    tail = tail * num
                else:
                    calc = calc - tail + (tail // num)
                    tail = (tail) // num
                lastSign = c
                num = 0

        return calc