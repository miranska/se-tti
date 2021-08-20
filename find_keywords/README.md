# Finding Closest Keywords

This folder contains the files required to find interrelated terms which showcase the similarity of software engineering concepts across a temporal regime. Please see the `./finding_keywords` folder.

The file `./showcase_intererelations.ipynb` contains sample script to find keywords/concepts that are related to the target.

For example, to find top 5 closest words to the following target of `defect + classification` run
```python
testcases(['defect', 'classification'], top_n=5)
```

For a target of `Requirements - Elicitation + Defects` and top 20 closest words run
```python
testcases(positive=['requirements','defect'], negative=['elicitations'], top_n = 20)
```
