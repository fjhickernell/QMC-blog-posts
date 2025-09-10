SHELL := /bin/bash

MAIN = QMC_Blog_Posts.tex
BASENAME = QMC_Blog_Posts
PDF = QMC_Blog_Posts.pdf
TEXS := $(shell find . -type f -name '*.tex' -not -path './.git/*')

.PHONY: all clean view force rebuild

pdf: $(TEXS) clean
	pdflatex $(MAIN)
	biber $(BASENAME)
	pdflatex -interaction=nonstopmode -halt-on-error $(MAIN)
	pdflatex -interaction=nonstopmode -halt-on-error $(MAIN)

force:
	rm -f $(PDF)
	$(MAKE) all

rebuild: clean all

clean:
	find . -type f \( -name '*.aux' -o -name '*.log' -o -name '*.out' -o -name '*.fls' -o -name '*.toc' -o -name '*.bbl*' -o -name '*.bcf*' -o -name '*.blg' -o -name '*.run.xml' -o -name '*.fdb_latexmk' -o -name '*.fls' -o -name '*.synctex*' \) -delete

view: $(PDF)
	open $(PDF)