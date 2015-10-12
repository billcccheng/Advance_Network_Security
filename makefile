FILE = CSCE665_Final_Project.tex

PDFFILE = $(addsuffix .pdf, $(basename $(FILE)))

$(PDFFILE): ${FILE}
	pdflatex -interaction=nonstopmode $(FILE)

run: $(PDFFILE)
	open $(PDFFILE)
