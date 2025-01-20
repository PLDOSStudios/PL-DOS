import random

words = ['apple', 'banana', 'cherry', 'orange', 'pear']
word = random.choice(words)
letters = set(word)
correct_guesses = set()
incorrect_guesses = set()
tries = 6

while tries > 0 and letters != correct_guesses:
    print('可用次数：', tries)
    print('已猜对的字母：', ' '.join(correct_guesses))
    print('已猜错的字母：', ' '.join(incorrect_guesses))
    guess = input('请猜一个字母或整个单词：')
    if len(guess) == 1:
        if guess in letters:
            correct_guesses.add(guess)
        else:
            incorrect_guesses.add(guess)
            tries -= 1
    else:
        if guess == word:
            correct_guesses = letters
        else:
            incorrect_guesses.add(guess)
            tries -= 1

if letters == correct_guesses:
    print('恭喜你，猜对了！单词是', word)
else:
    print('很遗憾，你没有猜对。正确答案是', word)