# You should sort the array silly!!!

class Solution:
    def remove(self, arr):
        if not arr:
            return 0, arr
        m = min(arr)
        for a in range(len(arr)):
            if arr[a] == m:
                return arr[a], arr[:a] + arr[a + 1:]
        return 0, arr

    def numberGame(self, nums):
        ans = []
        arr = nums
        a, b = 0, 0
        while len(arr) > 1:
            a, arr = self.remove(arr)
            b, arr = self.remove(arr)
            ans.append(b)
            ans.append(a)
        return ans