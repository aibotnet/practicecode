
import nltk

def main():
    sentence = "My name is  vikas"
    tokens = nltk.word_tokenize(sentence)

    tagged = nltk.pos_tag(tokens)

    entities = nltk.chunk.ne_chunk(tagged)

    length = len(tokens)

    for i in range(0, length):
        print 'For token  ---', tokens[i], '----tag is : ', tagged[i], ' and entities is ', entities[i]


main()