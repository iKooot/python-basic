from string import punctuation, whitespace
def is_palindrome(text):
    cleaned_text = ''.join(char for char in text.lower() if char not in punctuation and char not in whitespace)

    if cleaned_text == cleaned_text[::-1]:
        return True

    return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")