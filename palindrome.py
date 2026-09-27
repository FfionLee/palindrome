def palindrome(word):
    if len(word)==1 or len(word)==0:
        return(True)
    if word[0]!=word[-1]:
        return(False)
    return(palindrome(word[1:-1]))

p=palindrome('hello')
print(p)