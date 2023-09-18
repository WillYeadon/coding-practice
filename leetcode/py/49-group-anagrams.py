from typing import List
class Solution:
    def counter(self, s):
        ans = {}
        for i in s:
            if i not in ans:
                ans[i] = 1
            else:
                ans[i] += 1
        output = ''
        sorted_ans = {k: ans[k] for k in sorted(ans.keys())}
        for key in sorted_ans.keys():
            output += str(key)
            output += str(sorted_ans[key])
        return output

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counters = []
        for s in strs:
            counters.append([self.counter(s), s])

        groups = {}
        for count in counters:
            if count[0] not in groups:
                groups[count[0]] = [count[1]]
            else:
                groups[count[0]].append(count[1])
        ans = []
        for key in groups.keys():
            ans.append(groups[key])
        return ans
        