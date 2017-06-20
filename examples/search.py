from pattern.en import parsetree
from pattern.search import search

s = 'The mobile web is more important than mobile apps.'
s = parsetree(s, relations=True, lemmata=True)

for match in search('NP be RB?+ important than NP', s):
    print match.constituents()[-1], '=>', \
          match.constituents()[0]