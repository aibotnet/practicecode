#import nltk

import nltk
#from nltk import word_tokenize
print "1"
sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
#tokens = word_tokenize(sentence)

#print tokens
tagged = nltk.pos_tag(tokens)
print tagged[0:6]
