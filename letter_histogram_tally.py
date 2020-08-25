from collections import Counter

inp = input('Please enter a word: ')

def letter_histogram(str):

  result = {}

  for letter in str:
    if letter in result.keys():
      result[letter] += 1
    else:
      result[letter] = 1

  return result

print(letter_histogram(inp))


def letter_histogram_tally(dict):

  k = Counter(dict)

  high = k.most_common(3)

  for i in high:
    print(f'{i[0]} : {i[1]}')

letter_histogram_tally(letter_histogram_tally(inp))
