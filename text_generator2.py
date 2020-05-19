import numpy as np
import sys

class Posts:


  def make_pairs(self, corpus):
      for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])
  

  def fillDict(self, f):
    tmp = open(f, encoding='utf8').read()
    corpus = tmp.split() 
    pairs = self.make_pairs(corpus)
    word_dict = {}
    for word_1, word_2 in pairs:
      word_1 = word_1.replace('"', '')
      word_1 = word_1.replace('(', '')
      word_1 = word_1.replace(')', '')
      word_1 = word_1.replace('"', '')
      word_2 = word_2.replace('"', '')
      word_2 = word_2.replace('(', '')
      word_2 = word_2.replace(')', '')
      word_2 = word_2.replace('"', '')
      if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
      else:
        word_dict[word_1] = [word_2]
    return word_dict, corpus

    

  def generateText(self, corpus, w_dict):
    chain = []
    first_word = np.random.choice(corpus)
    while first_word.islower() or not first_word.isalpha():
      first_word = np.random.choice(corpus)
      chain = [first_word]
      n_words = 100
      for i in range(n_words):
        try:
          chain.append(np.random.choice(w_dict[chain[-1]]))
        except:
          continue
    ' '.join(chain)
    #f = open("ai_week3.txt", "a")
    #f.write("AI POST: \n")
    text = []
    for word in chain:
      text.append(word)
    text.reverse()
    return text

  def printWords(self, text, x):
    words = []
    response = "Number exceeds length of text"
    if x > len(text):
      return response
    else:
      for i in range(x):
        #print(text.pop())
        tmp = text.pop()
        words.append(tmp)
      return " ".join(words)


  def printSentence(self, text, week):
    end = ['.', '!', '?']
    words = []
    write = True
    while write and len(text) > 1:
      tmp = text.pop()
      words.append(tmp)
      if tmp[len(tmp)-1] in end:
        write = False
    output = " ".join(words)
    if output.isspace() or output == '':
      generate(str(week))
    else:
      # print(output)
      return output


  def makePost(self, text):
    end = ['.', '!', '?']
    post = []
    for i in range(8):
      s = self.printSentence(text)
      post.append(s) 
    output = " ".join(post)
    if output.isspace():
      print("Regenerate text")
    else:
      return output

