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
  
  result = []
  counter = 0
  dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)

  for i in dict:
    result.append((i[0], i[1]))
  
  print('The top three words are; ')
  while counter < 3:
    print(f'{result[counter][0]}: {result[counter][1]}')
    counter += 1

word_histogram_tally(word_histogram(inp))