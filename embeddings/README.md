# Pre-trained embeddings
## SWEBOK
Pre-trained [GloVe](https://nlp.stanford.edu/projects/glove/)-based embedding trained on [SWEBOK](https://www.computer.org/education/bodies-of-knowledge/software-engineering/v3) text corpus resides in `swebok.txt.glove.074.txt.wv`. Based on our test cases, the best epoch is 74.

## Reseach papers
Pre-trained GloVe-based embedding trained on research papers reside in `*one-year*.wv` files. The file names adhere to the following template
```
one-year-increments-five-year-window/X_to_Y_one-year.txt.glove.Z.txt.wv
```
where `X` is the starting year of the 5-year interval, `Y` is the ending year of the 5-year interval, and `Z` is the best train epoch (based on our test cases).

These embeddings are trained on titles and abstracts of 15233 research papers collected from "Transactions in Software Engineering" (TSE), and proceedings of "International Conference on Software Engineering" (ICSE), "Mining Software Repositories" (MSR), "Software Analysis, Maintenance, Evolution and Reengineering" (SANER), "Working Conference of Reverse Engineering" (WCRE), "Conference on Software Maintenance and Reengineering" (CSMR), "International Conference on Software Maintenance and Evolution" (ICSME), "International Conference on Software Maintenance" (ICSM), "International Symposium on Requirements Engineering (ISRE), "International Conference on Requirements Engineering" (ICRE), and "International Requirements Engineering Conference" (RE). Thus, conceptually, we have six "meta-venues": TSE, ICSE, MSR, RE (and its predecessors ICRE and ISRE), ICSME (and its predecessor ICSM), and SANER (and its ancestors CSMR and WCRE).

Note that the IEEE Xplore API does not capture some papers from the venues. For example, the IEEE library does not have ICSE proceedings for years before 1988, and the years of 2006 and 2014. However, while comparing the yearly paper count harvest with the one on the [DBLP](https://dblp.org), on average, we are able to capture more than 75% of papers for all the venues and years.
