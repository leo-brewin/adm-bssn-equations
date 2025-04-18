#!/bin/bash

export CADABRA_NO_UNICODE=1
export PYTHONWARNINGS="ignore"

file="<none>"
silent="no"
keep="no"
skiplatex="no"
Timer=""
CDB=/usr/local/bin/
sty=""
nowarn=""

# -----------------------------------------------------------------------------------------
# Parse the command-line options

OPTIND=1

while getopts 'i:I:P:sktTxhN' option
do
   case "$option" in
   "i")  file="$OPTARG"           ;;
   "I")  sty="-I$OPTARG"          ;;
   "P")  CDB="$OPTARG"            ;;
   "s")  silent="yes"             ;;
   "k")  keep="yes"               ;;
   "t")  Timer="/usr/bin/time"    ;;
   "T")  Timer="/usr/bin/time -l" ;;
   "x")  skiplatex="yes"          ;;
   "N")  nowarn="-N"              ;;
   "h")  echo "usage : cdblatex.sh -i file [-P<path to Cadabra bin dir>]"
         echo "                            [-I<path to cdbmacros.sty>] [-s] [-k] [-x] [-N] [-h]"
         echo "options :  -i file : source file (with or without .tex extension)"
         echo "           -I file : full path to cdbmacros.sty file"
         echo "           -P file : path to Cadabra bin directory"
         echo "           -s : silent, don't open the pdf file"
         echo "           -k : keep all temporary files"
         echo "           -t : report brief cpu time"
         echo "           -T : report detailed cpu time plus memory usage"
         echo "           -x : don't call latex"
         echo "           -N : don't warn if errors found in the output for some tags"
         echo "           -h : this help message"
         echo "example : cdblatex.sh -i file"
         exit                ;;
   ?)    echo "cdblatex.sh : Unknown option specified."
         exit                ;;
   esac
done

# strip .tex if given
file=$(basename -s ".tex" "$file")
name=$file

if [[ $file = "<none>" ]]; then
   echo "> no source file given, use cdblatex.sh -i file"
   exit 1;
fi;

if [[ ! -e $file.tex ]]; then
   echo "> file ""$file.tex"" not found, exit"
   exit 1;
fi

# does the source contain \Input?
num=$(egrep -c -e'^\s*(\\|\@|\$)Input\{' "$file".tex)

# yes, now merge source files
if ! [[ $num = 0 ]]; then
   ${MRGSRC} -i $file.tex -o $file"_.tex"
   name=$file"_"
fi

touch $file.cdbtxt

${CDBPREP} -i $file -m $name            || exit 1

$Timer $CDB/cadabra2 $file"_.cdb" > $file"_.txt"   || exit 3

iconv -c -f UTF-8 -t ASCII//translit $file"_.txt" > $file.cdbtxt

${CDBPOSTP} $nowarn -i $file $sty       || exit 5

if [[ $skiplatex = "no" ]]; then
   pdflatex -halt-on-error -interaction=batchmode -synctex=1 $file || exit 7
   echo " " # for some silly reason pdfsync forgets a trailing \n
else
   silent="yes"
fi

if [[ $silent = "no" ]]; then
   open $file.pdf       # macOS
   # xdg-open $file.pdf   # Linux
   # evince $file.pdf     # Linux
fi

if [[ $keep = "no" ]]; then
   rm -rf $file"_.tex" $file"_.txt" $file"_.cdb"
   rm -rf $file.log $file.out $file.py $file.cdbidx $file.cdbtxt
fi
