import math
import nltk
import sys
import os
import string
FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    t = {}
    pathtd = os.path.join('.',f'{directory}')
    for file in os.listdir(pathtd):
        pathtf = os.path.join(pathtd,file)
        with open(pathtf,'r',encoding='utf8') as f:
            word = f.read()
        t[file[:-4]] = word
    return t



def tokenize(document):
    wt = nltk.word_tokenize(document.lower())
    s = nltk.corpus.stopwords.words("english")
    l = []
    for word in wt:
        i = ''.join(c for c in word if c not in string.punctuation)
        if i and i not in s:
            l.append(i)
    return l


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    n = len(documents)
    term = {}
    idfs = {}
    for doc in documents:
        for word in set(documents[doc]):
           if word in term:
              term[word]+=1
           else:
               term[word] = 1
    for w in term:
        idfs[w] = math.log(n/term[w])
    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    nfile = {}
    for file in files:
        nfile[file] = 0
        for i in query:
            if i in idfs:
                idf = idfs[i]
                tf = files[file].count(i)
            nfile[file] += tf*idf
    sfiles = sorted(files, key= lambda k: nfile[k],reverse=True)
    return sfiles[:n]

def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    nsentence = {}
    for sentence in sentences:
        nsentence[sentence] = {}
        nsentence[sentence]['idf'] = 0
        nsentence[sentence]['word'] = 0
        for i in query:
            if i in sentences[sentence]:
                nsentence[sentence]['word'] +=sentences[sentence].count(i)
                nsentence[sentence]['idf']+=idfs[i]
        nsentence[sentence]['qtd'] = nsentence[sentence]['word']/len(sentences[sentence])
    tsentence = sorted(sentences, key=lambda sentence : (nsentence[sentence]['idf'] , nsentence[sentence]['qtd']),reverse=True)
    return tsentence[:n]


if __name__ == "__main__":
    main()
