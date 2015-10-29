FILE = progress.tex
BIBFILE = references.bib

BASENAME = $(basename $(FILE))
BBLFILE = $(addsuffix .bbl, $(basename $(FILE)))
AUXFILE = $(addsuffix .aux, $(basename $(FILE)))
PDFFILE = $(addsuffix .pdf, $(basename $(FILE)))

$(PDFFILE): $(FILE) $(BBLFILE)
	pdflatex -interaction=nonstopmode $(FILE)

$(BBLFILE): $(BIBFILE)
	latex -interaction=nonstopmode $(FILE)
	bibtex $(AUXFILE)
	latex -interaction=nonstopmode $(FILE)
	latex -interaction=nonstopmode $(FILE)
	@#pdflatex -interaction=nonstopmode $(FILE)
	@#latex -interaction=nonstopmode $(BASENAME)
	@#bibtex $(BASENAME)
	@#latex -interaction=nonstopmode $(BASENAME)
	@#latex -interaction=nonstopmode $(BASENAME)

.PHONY: run
run: $(PDFFILE)
	open $(PDFFILE)
