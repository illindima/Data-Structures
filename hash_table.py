class HashTable:
  def __init__(self):
    self.table = [None] * 12500
  def add(self, string, value):
    hv = self.calculate_hash_value(string)

    if hv != -1:
      if self.table[hv] != None:
        self.table[hv].append(value)
      else:
        self.table[hv] = [value]

  def lookup(self, string):
    hv = self.calculate_hash_value(string)

    if hv != -1:
      return self.table[hv]
    else:
      return -1

  def calculate_hash_value(self, string):
    return ord(string[0]) * 100 + ord(string[1])

# Test cases


ht = HashTable()

ht.add('key', 10)
ht.add('key', 'hi')

print(ht.lookup('key'))