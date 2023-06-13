from sys import stdin
import pymorphy2

s = stdin.read().lower()
prepositions = ('.', ',', ':', ';', '!', '?', '-', '—', '«', '»', '(', ')')
text = ''.join([i if i not in prepositions else ' ' for i in s]).split()
morphology = pymorphy2.MorphAnalyzer()
nouns_with_counts = {}
for i in text:
   word = morphology.parse(i)[0]
   if word.tag.POS == 'NOUN' and word.score > 0.5:
       nouns_with_counts[word.normal_form] = nouns_with_counts.get(word.normal_form, 0) + 1
nouns_with_counts = [x[0] for x in sorted(nouns_with_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)]
print(*nouns_with_counts[:10])
