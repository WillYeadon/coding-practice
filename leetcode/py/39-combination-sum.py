class Solution:
    def combinationSum(self, candidates, target):
        def backtrack(start, combination, current_sum):
            # for when com found
            if current_sum == target:
                combinations.append(list(combination))
                return
            # gone over so return no append
            if current_sum > target:
                return
            # start the combinations so for [1,2,3] we'll look at all
            # combinations starting with 1 then 2 then 3 this helps to
            # avoid 2,2,1 and 1,2,2 redundancy           
            for i in range(start, len(candidates)):
                # add to current potential combination
                combination.append(candidates[i])
                # hit the backtrack to get either a) added to combinations,
                # b) gone over so return or c) try adding another
                backtrack(i, combination, current_sum + candidates[i])
                # Pop off as now chacked
                combination.pop()
        
        combinations = []
        candidates.sort()
        backtrack(0, [], 0)
        return combinations
