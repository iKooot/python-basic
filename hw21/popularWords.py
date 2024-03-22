from string import punctuation


def popular_words(text: str, words: list) -> dict:
    transformed_text_gen = (char for char in text.lower() if char not in punctuation)
    transformed_text = ''.join(transformed_text_gen).split()

    words_count = {word.lower(): 0 for word in words}

    for word in transformed_text:
        if word in words_count:
            words_count[word] += 1

    return words_count


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
