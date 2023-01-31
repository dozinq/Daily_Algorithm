def check_palindrome(a) :
    print (a)
    if a == a[::-1]:
        print('입력하신 단어는 회문(Palindrome)입니다.')
    else:
        print('입력하신 단어는 회문(Palindrome)이 아닙니다.')

b = input()
check_palindrome(b)