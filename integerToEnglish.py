# TC: O(1) ==> since set number of digits
# SC: O(1)

class Solution:
    def numberToWords(self, num: int) -> str:
        if num is None: return " "

        if num == 0: return "Zero"

        self.thousands = ["", "Thousand", "Million", "Billion"]

        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        self.below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                         "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

        rtnData = ""

        i = 0

        while num > 0:
            if num % 1000 != 0:
                # get the digits and call helper method
                rtnData = self.helper(num % 1000) + self.thousands[i] + " " + rtnData
            num = num // 1000
            i += 1

        return rtnData.strip()

    def helper(self, num):
        if num == 0: return ""
        if num < 20:
            return self.below_20[num] + " "
        elif num < 100:
            return self.tens[num // 10] + " " + self.helper(num % 10)
        else:
            return self.below_20[num // 100] + " Hundred " + self.helper(num % 100)