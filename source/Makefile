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
	@ make shared.py
	@ for file in $(TARGETS); do make .$${file}; done;
	@ make veryclean
#-------------------------------------------------------------------------------
.adm: adm.tex shared.py
	@ make adm
.prd62: prd62.tex shared.py
	@ make prd62
.prd67: prd67.tex shared.py
	@ make prd67
.eqtn09: eqtn09.tex shared.py adm.tex eqtn10.tex prd62.tex
	@ make eqtn09
.eqtn10: eqtn10.tex shared.py adm.tex prd62.tex
	@ make eqtn10
.eqtn11: eqtn11.tex shared.py adm.tex prd62.tex
	@ make eqtn11
.eqtn12: eqtn12.tex shared.py adm.tex eqtn10.tex eqtn11.tex prd62.tex
	@ make eqtn12
.eqtn15: eqtn15.tex shared.py gamma.tex prd62.tex
	@ make eqtn15
.eqtn17: eqtn17.tex shared.py prd62.tex
	@ make eqtn17
.eqtn18: eqtn18.tex shared.py prd62.tex
	@ make eqtn18
.eqtn19: eqtn19.tex shared.py eqtn17.tex prd62.tex
	@ make eqtn19
.eqtn20: eqtn20.tex shared.py eqtn19.tex momentum.tex prd62.tex
	@ make eqtn20
.gamma: gamma.tex shared.py prd67.tex
	@ make gamma
.hamiltonian: hamiltonian.tex shared.py prd67.tex
	@ make hamiltonian
.momentum: momentum.tex shared.py gamma.tex prd67.tex
	@ make momentum
#-------------------------------------------------------------------------------
eqtns:
	@ echo "> cadabra eqtns ..."
	@ make .eqtns
.eqtns: eqtns.tex shared.py\
		  .eqtn09 .eqtn10 .eqtn11 .eqtn12 .eqtn15\
		  .eqtn17 .eqtn18 .eqtn19 .eqtn20\
		  .gamma .hamiltonian .momentum
	@ echo "> pdflatex eqtns ..."
	@ pdflatex -halt-on-error -interaction=batchmode eqtns &> /dev/null
	@ touch .eqtns
#-------------------------------------------------------------------------------
shared.py: shared.cdb
	@ echo "> cadabra2python shared ..."
	@ cadabra2python shared.cdb shared.py
#-------------------------------------------------------------------------------
%:
	@ echo "> cdblatex.sh $@ ..."
	@ cdblatex.sh -T -s -i $@ &> $@.cdblog
	@ # echo " -->"`cdbstats -i $@.cdblog`
	@ pdflatex -halt-on-error -interaction=batchmode $@ &> /dev/null
	@ touch .$@
#-------------------------------------------------------------------------------
rm-dot:
	@ for file in $(TARGETS); \
	  do \
	     rm -rf .$${file}; \
	  done
	@ rm -rf .[a-z]*.lb
	@ rm -rf .merged.tex .tmp.txt
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
	@ rm -rf shared.py
	@ rm -rf __pycache__
	@ if [[ -e eqtns.pdf ]]; then mv eqtns.pdf eqtns-save.pdf; fi
	@ for file in $(TARGETS); \
	  do \
	     rm -rf $${file}.pdf; \
		  rm -rf $${file}.json; \
		  rm -rf $${file}.cdbtex; \
	  done
	@ if [[ -e eqtns-save.pdf ]]; then mv eqtns-save.pdf eqtns.pdf; fi
#-------------------------------------------------------------------------------
# prepare files for github
github:
	@ make pristine
	@ make all
	@ make rm-dot
	@ make veryclean
