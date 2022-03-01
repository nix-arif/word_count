import re
from functools import reduce
file = open('file_handling.txt', 'r')
text = file.read()

def count_text(input_text, pattern):
  regex_result = re.findall(pattern, input_text)
  result_count = len(regex_result)
  return 'Total Occurances for {} : {}'.format(pattern, result_count)

print(count_text(text, 'Python'))
print(count_text(text, 'Read'))
print(count_text(text, 'and'))
print(count_text(text, 'between'))
print(count_text(text, 'choosing'))

freqtable = dict()

for word in text.split():
  if word in freqtable:
    freqtable[word] += 1
  else:
    freqtable[word] = 1

sorted_tuples = sorted(freqtable.items(), key=lambda item: item[1], reverse=True)
print(sorted_tuples)



