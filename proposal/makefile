FILE = proposal.tex

PDFFILE = $(addsuffix .pdf, $(basename $(FILE)))

$(PDFFILE): ${FILE}
	pdflatex -interaction=nonstopmode $(FILE)

.PHONY: run
run: $(PDFFILE)
	open $(PDFFILE)
