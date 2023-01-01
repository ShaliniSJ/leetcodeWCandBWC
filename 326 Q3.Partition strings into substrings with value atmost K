class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        ans = 0
        pre = ""
        for w in s:
            if int(pre+w) <= k:
                pre += w
            else:
                if not pre:
                    return -1
                if int(pre) <= k:
                    ans += 1
                else:
                    return -1
                pre = w
        if pre:
            if int(pre) <= k:
                ans += 1
            else:
                return -1
        return ans
