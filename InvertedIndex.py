## Class for Information Retrieval
## author: Saina Lajevardi
## date: February 21, 2017
#
#
## A class called InverseIndex is designed to create a data structure to hold the indices (words) of documents!
## Note that the document which is passed to this class is assumed to have already processed (i.e. the document  
## has been tokenized; stopword are removed; and token are normalized by stemming)

## This class contains four methods:
#			1) wordInDoc: receives the documents and the page ID and construct a dictionary to hold the indexes as the key  
#              of the dictionary and the pageID, along with the positions of the words are the values of this dictionary
#			2) termFreqInDoc: constructs the dictionary based on wordInDoc; uses the length of the position vector 
#              as the number of occurrence of the term to find the frquency (0-1) of the term in the doc. It replaces  
#              the vector of position with the term frequency.
#			3) wordFreqInDoc: merge the two dictionaries of vector positions and term frequency as the inverted index.
#			4) createCorpus: creates the corpus by merging inverted index from documents of interest.

### a simple, quick example at the end of this document shows the use of this class..

class InverseIndex:

	def __init__(self):
		self.index_corpus = {}

	def wordInDoc(self,doc,pageID):

		M = len(doc)
		self.index_doc = {}

		for pos,token in enumerate(doc): 
			if token in self.index_doc:
				self.index_doc[token][1].append(pos)
			else:
				self.index_doc[token] = [pageID,[pos]]  
   															
		return self.index_doc


	def termFreqInDoc(self):
		import copy
		self.index_freq = copy.deepcopy(self.index_doc)
		M = len(self.index_doc)
		
		for token in self.index_doc: 
			self.index_freq[token][1] = round(len(self.index_doc[token][1])/M,4)

		return self.index_freq


	def wordFreqInDoc(self):
		import copy
		self.index_docFreq = copy.deepcopy(self.index_doc)

		for token in self.index_doc:
			self.index_docFreq[token].append(self.index_freq[token][1])

		return self.index_docFreq


	def createCorpus(self):

		for token in self.index_docFreq:
			if token not in self.index_corpus:
				self.index_corpus[token] = [self.index_docFreq[token]]
			else:
				self.index_corpus[token].append(self.index_docFreq[token])

		return self.index_corpus		
	

#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
doc1 = "I gave you one dollar and you accept my dollar and then you call me stupid you are stupid"
doc2 = "You asked me if I gave you one dollar and then you called me stupid"
documents = [doc1,doc2]

s = InverseIndex()

for i,doc in enumerate(documents):
	s.wordInDoc(doc.split(),i+1)
	s.termFreqInDoc()
	s.wordFreqInDoc()
	print(s.createCorpus())


	{'I': [[1, [0], 0.0769], [2, [4], 0.0769]], 'gave': [[1, [1], 0.0769], [2, [5], 0.0769]], 
	'you': [[1, [2, 6, 12, 16], 0.3077], [2, [6, 11], 0.1538]], 'one': [[1, [3], 0.0769], [2, [7], 0.0769]], 
	'dollar': [[1, [4, 9], 0.1538], [2, [8], 0.0769]], 'and': [[1, [5, 10], 0.1538], [2, [9], 0.0769]], 
	'accept': [[1, [7], 0.0769]], 'my': [[1, [8], 0.0769]], 'then': [[1, [11], 0.0769], [2, [10], 0.0769]], 
	'call': [[1, [13], 0.0769]], 'me': [[1, [14], 0.0769], [2, [2, 13], 0.1538]], 'stupid': [[1, [15, 18], 0.1538], [2, [14], 0.0769]], 
	'are': [[1, [17], 0.0769]], 'You': [[2, [0], 0.0769]], 'asked': [[2, [1], 0.0769]], 'if': [[2, [3], 0.0769]], 
	'called': [[2, [12], 0.0769]]}
