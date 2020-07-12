def palindrome(word):
    i=1
    rev=[]
    while i <= len(word):
        rev.append(list(word)[-i])
        i+=1
    if list(word)!=rev:
        raise NorPalindromeError
    print(word)

class NorPalindromeError(Exception):
    def __init__(self):
        super().__init__('회문이 아닙니다.')

try:
    word = input()
    palindrome(word)
except NorPalindromeError as e:
    print(e)
