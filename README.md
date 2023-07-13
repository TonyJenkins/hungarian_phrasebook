# Welcome

This, the [Hungarian Phrasebook](https://youtu.be/G6D1YI-41ao), is yet another Python Book

## Requirements

The book is written using [Sphinx, The Python Documentation Generator (https://www.sphinx-doc.org/)]. Building it requires:

* Python 3.10 or later.
* Pip.
* Sphinx, at least version 6.
* Sphinx Packages:
  * sphinx-book-theme
  * sphinx-copybutton

In addition, for PDF output, the easiest way is to also have installed:

* LaTeX (specifically `pdflatex`).
* Sundry fonts (see below).

## Runes

Install the following, ideally in a `venv`. See also the `requirements.txt` in the repo.

``$ pip install -U sphinx`` \
``$ pip install sphinx-book-theme`` \
``$ pip install sphinx-copybutton``

The following packages are needed for PDf output on Ubuntu/Mint/Debian. The list could probably be trimmed if different fonts were used.

``$ apt install texlive-latex-base`` \
``$ apt install texlive-latex-extra`` \
``$ apt install texlive-fonts-extra`` \
``$ apt install latexmk``

## Building

In the ``source`` folder:

``$ make html`` \
``$ make latexpdf``

## Windows

You're on your own. You might also want to consider your poor operating system choices.
