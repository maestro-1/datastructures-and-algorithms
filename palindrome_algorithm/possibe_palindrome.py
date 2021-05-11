import string


def canPermutePalindrome(string: str) -> bool:
    result = False

    charset = set()

    for char in string:
        if char in string.punctuation:
            continue

        if char in charset:
            charset.remove(char)
        else:
            charset.add(char)

    if len(charset) <= 1:
        result = True
    return result


if __name__ == '__main__':
    possible_palindrome = ['high', 'Wassamassaw', "A man, a plan, a canal--Panama!", "Hi I'm olaf"]

    for item in possible_palindrome:
        result = canPermutePalindrome(item)

        print(f'{item} is a palindrome') if result else print(f'{item} is not a palindrome')
