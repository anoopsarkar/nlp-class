# make handout=no TARGET
# make handout=yes TARGET

.PHONY: all clean
TARGETS=prob.pdf lm.pdf hmm.pdf linearmodels.pdf mtintro.pdf ibm123.pdf
handout=yes

all: $(TARGETS)

ifeq ($(handout),yes)
%.pdf: %.tex
		pdflatex "\PassOptionsToClass{handout}{beamer}\input{$<}"
		pdflatex "\PassOptionsToClass{handout}{beamer}\input{$<}"
else
%.pdf: %.tex
		pdflatex $<
		pdflatex $<
endif

clean:
	for i in `cat .gitignore`; do \
		echo "removing" $$i ; \
		/bin/rm -f $$i ; \
	done;
	/bin/rm -f $(TARGETS)
