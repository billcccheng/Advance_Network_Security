FILE = proposal.tex
BIBFILE = references.bib

BBLFILE = $(addsuffix .bbl, $(basename $(FILE)))
AUXFILE = $(addsuffix .aux, $(basename $(FILE)))
PDFFILE = $(addsuffix .pdf, $(basename $(FILE)))

$(PDFFILE): ${FILE} ${BBLFILE}
	pdflatex -interaction=nonstopmode $(FILE)

${BBLFILE}: ${BIBFILE}
	pdflatex -interaction=nonstopmode $(FILE)
	bibtex $(AUXFILE)

.PHONY: run
run: $(PDFFILE)
	open $(PDFFILE)
