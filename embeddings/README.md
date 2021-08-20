# Pre-trained embeddings
## SWEBOK
Pre-trained [GloVe](https://nlp.stanford.edu/projects/glove/)-based embedding trained on [SWEBOK](https://www.computer.org/education/bodies-of-knowledge/software-engineering/v3) text corpus resides in `swebok.txt.glove.074.txt.wv`. Based on our test cases, the best epoch is 74.

## Reseach papers
Pre-trained GloVe-based embedding trained on research papers reside in `*one-year*.wv` files. The file names adhere to the following template
```
one-year-increments-five-year-window/X_to_Y_one-year.txt.glove.Z.txt.wv
```
where `X` is the starting year of the 5-year interval, `Y` is the ending year of the 5-year interval, and `Z` is the best train epoch (based on our test cases).
