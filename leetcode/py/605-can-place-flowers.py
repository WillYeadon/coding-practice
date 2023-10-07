class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        zeroGroups = []
        running = 0
        flowerbed = [0] + flowerbed + [0]
        for i in flowerbed:
            if i == 0:
                running += 1
            else:
                zeroGroups.append(running)
                running = 0
        if (running != 0) : zeroGroups.append(running)
        total = [max((j - 1) // 2, 0) for j in zeroGroups]
        return sum(total) >= n