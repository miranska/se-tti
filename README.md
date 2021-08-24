# Term Interrelations and Trends in Software Engineering 

This repository contains the word embeddings, test cases, and a tool testing embeddings' quality. It also shows sample code to generate and investigate interrelated terms in Software Engineering. See the [paper](https://doi.org/10.1145/3468264.3473132) for details. 

## Pre-trained Embeddings

To download pre-trained word embedding models, which are trained on 15233 research papers, please see the `./embeddings` folder. 

## Tests of Emedding's Quality

To test the quality of embeddings, please see `./test_embeddings` folder, which contains test cases and the test harness.

## Exploring Related Terms

To find interrelated terms which showcase the similarity of software engineering concepts across a temporal regime, please see `./find_keywords` folder.

## Publication

For details on the tools and data, see the [paper](https://dl.acm.org/doi/10.1145/3468264.3473132) (or its [pre-print](https://arxiv.org/abs/2108.09529)) published in the proceedings of ESEC/FSE 2021. Please cite the tool and data as

```bibtex
@INPROCEEDINGS{baskararajah2021term,
  author = {Baskararajah, Janusan and Zhang, Lei and Miranskyy, Andriy},
  title = {Term Interrelations and Trends in Software Engineering},
  year = {2021},
  isbn = {9781450385626},
  publisher = {Association for Computing Machinery},
  address = {New York, NY, USA},
  url = {https://doi.org/10.1145/3468264.3473132},
  doi = {10.1145/3468264.3473132},
  booktitle = {Proceedings of the 29th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering},
  pages = {1471--1474},
  numpages = {4},
  location = {Athens, Greece},
  series = {ESEC/FSE 2021},
  keywords = {software engineering trends, term interrelations, word embeddings},
  abstract = {The Software Engineering (SE) community is prolific, making it challenging for experts
  to keep up with the flood of new papers and for neophytes to enter the field. Therefore,
  we posit that the community may benefit from a tool extracting terms and their interrelations
  from the SE community's text corpus and showing terms' trends. In this paper, we build
  a prototyping tool using the word embedding technique. We train the embeddings on
  the SE Body of Knowledge handbook and 15,233 research papers' titles and abstracts.
  We also create test cases necessary for validation of the training of the embeddings.
  We provide representative examples showing that the embeddings may aid in summarizing
  terms and uncovering trends in the knowledge base.}
}
```

## License

This project is licensed under the MIT License.

## Contact Us

If you have found a bug or came up with a new feature -- please open an [issue](https://github.com/miranska/se-tti/issues) or [pull request](https://github.com/miranska/se-tti/pulls).

## Acknowledgments

We thank Ryerson University and Natural Sciences and Engineering Research Council of Canada for supporting and funding this work. We thank IEEE for providing us access to IEEE Xplore API.
