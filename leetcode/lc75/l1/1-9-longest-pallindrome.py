class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        for l in s:
            if l not in letters:
                letters[l] = 1
            else:
                letters[l] += 1

        middle = 0
        odds = 0
        oddValues = 0
        evens = 0
        for letter in letters:
            candidate = letters[letter]
            if (candidate % 2) == 0:
                evens += candidate
            elif candidate > middle:
                oddValues += middle
                odds += 1
                middle = candidate
            else:
                if candidate > 2:
                    odds += 1
                    oddValues += candidate
        #print(evens, middle, oddValues, odds)
        #print(evens + middle + oddValues + odds)
        
        if odds > 0:
            return evens + middle + oddValues - odds + 1
        else:
            return evens + middle
    
x = Solution()
print(x.longestPalindrome('bananas'))
print(x.longestPalindrome('civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'))