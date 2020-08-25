inp = input('Please enter a sentence: ')

def word_histogram(sentence):

  sentence = sentence.lower().split(' ')
  
  result = {}

  for word in sentence:
    if word in result.keys():
      result[word] += 1
    else:
      result[word] = 1

  return result

print(word_histogram(inp))

def word_histogram_tally(dict):

  dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)

  print(dict)

  for i in dict:
    print(f'{i[0]}: {i[1]}')

word_histogram_tally(word_histogram(inp))