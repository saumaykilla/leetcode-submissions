class Solution:
    def isPalindrome(self, x: int) -> bool:
        pali = str(x)
        l, r = 0, len(pali) - 1

        while l < r:
            if pali[l] != pali[r]:
                return False
            l += 1
            r -= 1

        return True

        