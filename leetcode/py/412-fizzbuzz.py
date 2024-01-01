class Solution:
    def fizzBuzz(self, n: int):
        answer = ['1']
        i = 1
        while i < n:
            c = i + 1
            fizz = True if (c // 3 == c / 3) else False
            buzz = True if (c // 5 == c / 5) else False
            if fizz and buzz:
                answer.append('FizzBuzz')
            elif fizz:
                answer.append('Fizz')
            elif buzz:
                answer.append('Buzz')
            else:
                answer.append(str(c))
            i += 1
        return answer