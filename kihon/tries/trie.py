_end = '_end_'

class Trie:

  def __init__(self):
    self.root = {}

  def addText(self, text):
    self.addWords(text.split(' '))

  def addWords(self, *words):
    for word in words:
      self.addWord(word)

  def addWord(self, word):
      v = self.root
      for letter in word:
      	  v = v.setdefault(letter, {})
      v = v.setdefault(_end, _end)

  def contains(self, word):
    v = self.root
    for letter in word:
      if letter in v:
        v = v[letter]
      else:
      	return False
    else:
        return _end in v

  def prefix(self, word):
    v = self.root
    for letter in word:
      if letter in v:
        v = v[letter]
      else:
      	return False
    return True
