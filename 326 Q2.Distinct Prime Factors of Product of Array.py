#MINE
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        nums = set(nums)
        c = 2
        pro = 1
        sets = []
        for i in nums:
                pro =pro *(i)
        while(pro>1):
            if pro%c == 0:
                sets.append(c)
                pro = int(pro//c)
            else :
                c += 1
        return len(set(sets))
