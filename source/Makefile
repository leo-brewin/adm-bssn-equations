#-------------------------------------------------------------------------------
SHELL = /bin/bash
#-------------------------------------------------------------------------------
.PHONY: all
#-------------------------------------------------------------------------------
TARGETS = \
		prd62 prd67\
		adm gamma hamiltonian momentum\
		eqtn10 eqtn09 eqtn11 eqtn12\
		eqtn15 eqtn17 eqtn18\
		eqtn19 eqtn20\
		eqtns
#-------------------------------------------------------------------------------
all:
	@ mkdir -p lib
	@ mkdir -p ../pdf
	@ make version
	@ touch shared.cdb # forces old versions of Cadabra < 2.5.12 to update its cache
	@ for file in $(TARGETS); do make .$${file}; done;
	@ make veryclean
#-------------------------------------------------------------------------------
.adm: adm.tex shared.cdb
	@ make adm
.prd62: prd62.tex shared.cdb
	@ make prd62
.prd67: prd67.tex shared.cdb
	@ make prd67
.eqtn09: eqtn09.tex shared.cdb adm.tex eqtn10.tex prd62.tex
	@ make eqtn09
.eqtn10: eqtn10.tex shared.cdb adm.tex prd62.tex
	@ make eqtn10
.eqtn11: eqtn11.tex shared.cdb adm.tex prd62.tex
	@ make eqtn11
.eqtn12: eqtn12.tex shared.cdb adm.tex eqtn10.tex eqtn11.tex prd62.tex
	@ make eqtn12
.eqtn15: eqtn15.tex shared.cdb gamma.tex prd62.tex
	@ make eqtn15
.eqtn17: eqtn17.tex shared.cdb prd62.tex
	@ make eqtn17
.eqtn18: eqtn18.tex shared.cdb prd62.tex
	@ make eqtn18
.eqtn19: eqtn19.tex shared.cdb eqtn17.tex prd62.tex
	@ make eqtn19
.eqtn20: eqtn20.tex shared.cdb eqtn19.tex momentum.tex prd62.tex
	@ make eqtn20
.gamma: gamma.tex shared.cdb prd67.tex
	@ make gamma
.hamiltonian: hamiltonian.tex shared.cdb prd67.tex
	@ make hamiltonian
.momentum: momentum.tex shared.cdb gamma.tex prd67.tex
	@ make momentum
#-------------------------------------------------------------------------------
eqtns:
	@ echo "cadabra eqtns ..."
	@ make .eqtns
.eqtns: eqtns.tex shared.cdb\
		  .eqtn09 .eqtn10 .eqtn11 .eqtn12 .eqtn15\
		  .eqtn17 .eqtn18 .eqtn19 .eqtn20\
		  .gamma .hamiltonian .momentum
	@ echo "pdflatex eqtns ..."
	@ pdflatex -halt-on-error -interaction=batchmode eqtns &> /dev/null
	@ cp -f eqtns.pdf ../pdf/.
	@ touch .eqtns
#-------------------------------------------------------------------------------
%:
	@ echo "cdblatex.sh $@ ..."
	@ ${CDBLATEX} -T -s -i $@ &> $@.cdblog
	@ # echo " -->"`cputime -i $@.cdblog`
	@ cp -f $@.cdbtex lib/.
	@ pdflatex -halt-on-error -interaction=batchmode $@ &> /dev/null
	@ cp -f $@.pdf ../pdf/.
	@ touch .$@
#-------------------------------------------------------------------------------
version:
	@ version.sh
#-------------------------------------------------------------------------------
rm-dot:
	@ for file in $(TARGETS); \
	  do \
	     rm -rf .$${file}; \
	  done
	@ rm -rf .[a-z]*.lb
	@ rm -rf .merged.tex .tmp.txt
#-------------------------------------------------------------------------------
pdf:
	@ mkdir -p ../pdf
	@ for file in $(TARGETS); \
	  do \
	     mv $${file}.pdf ../pdf/.; \
	  done
#-------------------------------------------------------------------------------
clean:
	@ for file in $(TARGETS); \
	  do \
	     rm -rf $${file}.aux $${file}.log $${file}.out $${file}.synctex.gz; \
	  done
#-------------------------------------------------------------------------------
veryclean:
	@ make clean
	@ for file in $(TARGETS); \
	  do \
	     rm -rf $${file}.cdb $${file}_.cdb; \
		  rm -rf $${file}.cdbidx $${file}.cdbtxt $${file}.cdblog; \
		  rm -rf $${file}.py; \
	  done
	@ rm -rf .merged.tex .tmp.txt
#-------------------------------------------------------------------------------
pristine:
	@ make rm-dot
	@ make veryclean
	@ rm -rf lib/*
	@ rm -rf __pycache__
	@ for file in $(TARGETS); \
	  do \
	     rm -rf $${file}.pdf; \
		  rm -rf $${file}.json; \
		  rm -rf $${file}.cdbtex; \
	  done
#-------------------------------------------------------------------------------
github-clean:
	@ make rm-dot
	@ make veryclean
	@ rm -rf __pycache__
	@ for file in $(TARGETS); \
	  do \
	     rm -rf $${file}.pdf; \
		  rm -rf $${file}.json; \
		  rm -rf $${file}.cdbtex; \
	  done
#-------------------------------------------------------------------------------
# prepare files for github
github:
	@ make pristine
	@ make all
	@ make pdf
	@ make github-clean
	@ rm -rf expected
	@ mv ../pdf/* ../expected/.
