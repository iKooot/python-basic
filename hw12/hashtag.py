import string

user_string = input("Enter some string.\n")

transformed_string = ''.join([char for char in user_string.title() if char not in string.punctuation and not char.isspace()])[0:139]

hashtag = f'#{transformed_string}'
print(hashtag)
