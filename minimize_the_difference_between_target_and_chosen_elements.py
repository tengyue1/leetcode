class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        
        min_sum = sum(min(row) for row in mat)
        max_sum = sum(max(row) for row in mat)
        
        if min_sum >= target:
            return min_sum - target
        if max_sum <= target:
            return target - max_sum
        
        s = {0}
        
        for row in mat:
            s = {x + num for num in row for x in s if x + num < 2*target - min_sum}
            
        return min(abs(target - num) for num in s)