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