See [`prepare.py`](prepare.py).

The following interactive session shows the commands issued and the resulting outputs, with `$` indicating the command-line prompt.

    $ ./prepare.py en.tok
    $ ngramsymbols en.tok en.sym
    $ farcompilestrings \
        --fst_type=compact \
        --symbols=en.sym \
        --keep_symbols \
        en.tok \
        en.far
    $ ngramcount --order=3 en.far en.cnt
    $ ngrammake --method=kneser_ney en.cnt en.lm
    $ ngraminfo en.lm
    # of states                                       9818101
    # of ngram arcs                                   41220846
    # of backoff arcs                                 9818100
    initial state                                     1
    unigram state                                     0
    # of final states                                 365727
    ngram order                                       3
    # of 1-grams                                      624743
    # of 2-grams                                      9243419
    # of 3-grams                                      31718411
    well-formed                                       y
    normalized                                        y
    $ ngramrandgen --max_sents=1 en.lm | farprintstrings
    the birth of his group was <epsilon> $ 4,000 <epsilon> works , and alon mualem cfo <epsilon> <epsilon> goalwards by <epsilon> exposure to the present-day <epsilon> india <epsilon> weighs opening the <epsilon> manual <epsilon> ) <epsilon> includes <epsilon> hundreds of architectural barriers to international , <epsilon> 69 , then <epsilon> <epsilon> nationwide in the third period . -- prosecutors have used modern <epsilon> <epsilon> 26-31 <epsilon> 1995 the <epsilon> importance of <epsilon> sales , surpassing the 0.9 percent <epsilon> favored the <epsilon> economy and the willingness and <epsilon> always <epsilon> attracted to the washington post staff writer thursday , <epsilon> thor <epsilon> <epsilon> britain ’ s lawsuit <epsilon> <epsilon> wachtel <epsilon> suspect the president considers bloated .
