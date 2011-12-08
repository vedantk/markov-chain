#!/usr/bin/pypy

from markov import MarkovChain

def walk_corpus(fname):
        with open(fname, 'r') as f:
                words = f.read().split()
        chain = MarkovChain(5)
        chain.add_sequence(words)
        return chain.walk()

if __name__ == '__main__':
        nr = 5000
        gen = walk_corpus("the_tempest.txt")
        print(' '.join([next(gen) for k in xrange(nr)]))
