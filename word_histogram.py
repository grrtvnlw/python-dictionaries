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