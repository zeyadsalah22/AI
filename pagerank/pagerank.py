import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    pd = {}
    if len(corpus[page])==0:
        for j in corpus:
            pd[j] = 1/len(corpus)
    else:
        p = damping_factor/len(corpus[page])
        s = (1-damping_factor)/len(corpus)
        for i in corpus:
            if i in corpus[page]:
                pd[i] = p+s
            else:
                pd[i] = s
    return pd


    #raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    spr = {}
    for page in corpus:
        spr[page]=0
    s = None
    for i in range(n):
        if s==None:
            c = list(corpus.keys())
            s = random.choice(c)
            spr[s]+=1
        else:
            ns = transition_model(corpus,s,damping_factor)
            c = list(ns.keys())
            w = [ns[k] for k in c]
            s = random.choices(c,w).pop()
            spr[s]+=1
    spr = {key: value/n for key, value in spr.items()}
    return spr

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    ''
    pr = {}
    for page in corpus:
        pr[page] = 1/len(corpus)
    c = 1
    while c>=0.001:
        c = 0
        prc = pr.copy()
        for page in pr:
            i = [p for p in corpus if page in corpus[p]]
            r = (1-damping_factor)/len(corpus)
            if len(i)!=0:
                summ = 0
                for j in i:
                    summ+=pr[j]/len(corpus[j])
            pr[page] = r+(damping_factor*summ)
            nc = abs(pr[page]-prc[page])
            if c<nc:
                c = nc
    return pr



if __name__ == "__main__":
    main()
