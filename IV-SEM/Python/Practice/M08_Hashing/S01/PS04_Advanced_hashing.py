class Solution:
    def subarraySum(nums,k):
        count = 0
        pref_sum = 0
        d = {0:1}
        for i in nums:
            pref_sum += i
            complement = pref_sum - k
            if complement in d:
                count += d[complement]
            
            d[pref_sum] = d.get(pref_sum,0) + 1
        return count