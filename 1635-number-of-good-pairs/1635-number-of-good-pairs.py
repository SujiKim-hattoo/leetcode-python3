class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs =[]
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] == nums[j] and i < j:
                    good_pairs.append((i, j))
        return len(good_pairs)

        