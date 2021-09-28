
num_x = int(input())
x = input()
num_y = int(input())
y = input()

words_x = set(x.split())
words_y = set(y.split())

final = words_x.symmetric_difference(words_y)

print(len(final))