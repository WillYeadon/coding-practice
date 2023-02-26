class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Hash all the letters in the string to get the
        # amount of times they occur
        letters = {}
        for l in s:
            if l not in letters:
                letters[l] = 1
            else:
                letters[l] += 1
        
        # List of relevant values
        # Longest available odd string which will thus sit in
        # the middle of the pallindrome
        middle = 0
        # Total number of idd strings
        odds = 0
        # The total value of all the odd strings e.g. their
        # accumulated length
        oddValues = 0
        # The total value of all the even strings e.g. their
        # accumulated length        
        evens = 0
        
        # Loop through each letter in the string
        for letter in letters:
            # Candidate is the number of times a letter occurred in
            # the string
            candidate = letters[letter]
            # If it occured an even number of times, add it to
            # the evens length
            if (candidate % 2) == 0:
                evens += candidate
            # If it is not even, is it the longest odd encountered
            # thus far?
            elif candidate > middle:
                # If so, add the old odd value to the total odd values
                oddValues += middle
                # Add one to odd count
                odds += 1
                # Update middle to longest odd seen so far                
                middle = candidate
            # If not longest odd seen so far but still an odd
            else:
                # Is this greater than 2? If it is 1, then another 1 length
                # odd has already been picked up as middle else proceed
                if candidate > 2:
                    # Add one to odd count
                    odds += 1
                    # Add this odd length to total odd values
                    oddValues += candidate
        
        # If you have at least one odd
        if odds > 0:
            # Return the total number of evens plus
            # the middle odd number you're using
            # Can also use the odd numbered values - 1 so for
            # c = 5, 'cccccc', can use 4 of those c's as 'cc'
            # at either end. There are #odds odd values so subtract 
            # odds and add oddValues. 
            # However, there is at least one odd value so pick up
            # one too many odds when first assigning middle so 
            # only want (odds - 1) hence add this back on.
            return evens + middle + oddValues - odds + 1
        # Elsewise all evens
        else:
            # Simple case of only even numbers
            return evens
    
x = Solution()
#print(x.longestPalindrome('xxccvvbbnnmm'))
print(x.longestPalindrome('bananas'))
print(x.longestPalindrome('civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'))