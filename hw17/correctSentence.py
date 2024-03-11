def correct_sentence(text):
    sentences = [sentence.strip().capitalize() for sentence in text.split('.')]
    result = '. '.join(sentences).strip()

    if not text.endswith('.'):
        result += '.'

    return result

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')