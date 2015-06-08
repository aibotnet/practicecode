'''
Created on 05-Dec-2013

@author: aknauhwar
'''

import nltk
 
class Splitter(object):
    def __init__(self):
        
        self.nltk_splitter = nltk.data.load('tokenizers/punkt/english.pickle')
        self.nltk_tokenizer = nltk.TreebankWordTokenizer()
 
    def split(self, text):
        """
        input format: a paragraph of text
        output format: a list of lists of words.
        e.g.: [['this', 'is', 'a', 'sentence'], ['this', 'is', 'another', 'one']]
        """
        sentences = self.nltk_splitter.tokenize(text)
        tokenized_sentences = [self.nltk_tokenizer.tokenize(sent) for sent in sentences]
        return tokenized_sentences
 
 
class POSTagger(object):
    def __init__(self):
        pass
    def pos_tag(self, sentences):
        """
        input format: list of lists of words
        e.g.: [['this', 'is', 'a', 'sentence'], ['this', 'is', 'another', 'one']]
        output format: list of lists of tagged tokens. Each tagged tokens has a
        form, a lemma, and a list of tags
        e.g: [[('this', 'this', ['DT']), ('is', 'be', ['VB']), ('a', 'a', ['DT']), ('sentence', 'sentence', ['NN'])],
        [('this', 'this', ['DT']), ('is', 'be', ['VB']), ('another', 'another', ['DT']), ('one', 'one', ['CARD'])]]
        """
 
        pos = [nltk.pos_tag(sentence) for sentence in sentences]
        #adapt format
        pos = [[(word, word, [postag]) for (word, postag) in sentence] for sentence in pos]
        return pos
    
    
    
    
text = """What can I say about this place. The staff of the restaurant is nice and the eggplant is not bad. Apart from that, very uninspired food, lack of atmosphere and too expensive. I am a staunch vegetarian and was sorely dissapointed with the veggie options on the menu. Will be the last time I visit, I recommend others to avoid."""
 
splitter = Splitter()
postagger = POSTagger()
 
splitted_sentences = splitter.split(text)
 
print splitted_sentences
#[['What', 'can', 'I', 'say', 'about', 'this', 'place', '.'], ['The', 'staff', 'of', 'the', 'restaurant', 'is', 'nice', 'and', 'eggplant', 'is', 'not', 'bad', '.'], ['apart', 'from', 'that', ',', 'very', 'uninspired', 'food', ',', 'lack', 'of', 'atmosphere', 'and', 'too', 'expensive', '.'], ['I', 'am', 'a', 'staunch', 'vegetarian', 'and', 'was', 'sorely', 'dissapointed', 'with', 'the', 'veggie', 'options', 'on', 'the', 'menu', '.'], ['Will', 'be', 'the', 'last', 'time', 'I', 'visit', ',', 'I', 'recommend', 'others', 'to', 'avoid', '.']]
 
pos_tagged_sentences = postagger.pos_tag(splitted_sentences)
 
print pos_tagged_sentences
#[[('What', 'What', ['WP']), ('can', 'can', ['MD']), ('I', 'I', ['PRP']), ('say', 'say', ['VB']), ('about', 'about', ['IN']), ('this', 'this', ['DT']), ('place', 'place', ['NN']), ('.', '.', ['.'])], [('The', 'The', ['DT']), ('staff', 'staff', ['NN']), ('of', 'of', ['IN']), ('the', 'the', ['DT']), ('restaurant', 'restaurant', ['NN']), ('is', 'is', ['VBZ']), ('nice', 'nice', ['JJ']), ('and', 'and', ['CC']), ('eggplant', 'eggplant', ['NN']), ('is', 'is', ['VBZ']), ('not', 'not', ['RB']), ('bad', 'bad', ['JJ']), ('.', '.', ['.'])], [('apart', 'apart', ['NN']), ('from', 'from', ['IN']), ('that', 'that', ['DT']), (',', ',', [',']), ('very', 'very', ['RB']), ('uninspired', 'uninspired', ['VBN']), ('food', 'food', ['NN']), (',', ',', [',']), ('lack', 'lack', ['NN']), ('of', 'of', ['IN']), ('atmosphere', 'atmosphere', ['NN']), ('and', 'and', ['CC']), ('too', 'too', ['RB']), ('expensive', 'expensive', ['JJ']), ('.', '.', ['.'])], [('I', 'I', ['PRP']), ('am', 'am', ['VBP']), ('a', 'a', ['DT']), ('staunch', 'staunch', ['NN']), ('vegetarian', 'vegetarian', ['NN']), ('and', 'and', ['CC']), ('was', 'was', ['VBD']), ('sorely', 'sorely', ['RB']), ('dissapointed', 'dissapointed', ['VBN']), ('with', 'with', ['IN']), ('the', 'the', ['DT']), ('veggie', 'veggie', ['NN']), ('options', 'options', ['NNS']), ('on', 'on', ['IN']), ('the', 'the', ['DT']), ('menu', 'menu', ['NN']), ('.', '.', ['.'])], [('Will', 'Will', ['NNP']), ('be', 'be', ['VB']), ('the', 'the', ['DT']), ('last', 'last', ['JJ']), ('time', 'time', ['NN']), ('I', 'I', ['PRP']), ('visit', 'visit', ['VBP']), (',', ',', [',']), ('I', 'I', ['PRP']), ('recommend', 'recommend', ['VBP']), ('others', 'others', ['NNS']), ('to', 'to', ['TO']), ('avoid', 'avoid', ['VB']), ('.', '.', ['.'])]]    

    
    
    
    
    
    
    
    

