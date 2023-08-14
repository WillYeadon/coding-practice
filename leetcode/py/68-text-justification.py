class Solution:
    def lineCreate(self, words, maxWidth):
        run = [] # To store the words for the current line
        runLength = 0 # The total length of the current line
        count = 0 # The count of words added to the current line
        for i in words:
            # If it's not the first word, we need an additional space
            additional_space = 1 if run else 0
            # Check if adding the next word exceeds the maxWidth
            if (runLength + len(i) + additional_space) <= maxWidth:
                run.append(i) # Add the word to the current line
                runLength += len(i) + additional_space # Update the line length
                count += 1
            else:
                break
        return run, words[count:] # Return the current line and remaining words

    def spaceBulker(self, passage, maxWidth):
        words = passage.split() # Split the line into words
        # If there is only one word in the line, fill with spaces
        if len(words) == 1:
            return passage + ' ' * (maxWidth - len(passage))

        spaces = len(words) - 1 # Number of spaces between words
        # Calculate required spaces to reach maxWidth
        required_spaces = maxWidth - len(passage) + spaces

        # Distribute the required spaces evenly among the spaces between words
        for i in range(spaces):
            # If there's a remainder, distribute it to the leftmost spaces
            words[i] += ' ' * (required_spaces // spaces + (i < required_spaces % spaces))

        return ''.join(words) # Join the words with the spaces

    def fullJustify(self, words, maxWidth):
        ans = [] # To store the final justified text
        while len(words) > 0:
            # Create a line and get remaining words
            run, words = self.lineCreate(words, maxWidth)
            # Justify the line and append to the result
            ans.append(self.spaceBulker(' '.join(run), maxWidth))

        # Handle the last line separately, justifying it to the left
        if ans:
            last = ans[-1]
            last = ' '.join(last.split())
            ans[-1] = last + ' ' * (maxWidth - len(last))

        return ans
