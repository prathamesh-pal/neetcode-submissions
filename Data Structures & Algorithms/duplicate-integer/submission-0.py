class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = []
        for i in nums:
            if i not in num:
                num.append(i)
            else:
                return True
        return False

        