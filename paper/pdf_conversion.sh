#!/bin/sh
# https://learnbyexample.github.io/customizing-pandoc/
pandoc documentation.md \
-f gfm \
-H header.tex \
--include-before-body title.tex \
-V linkcolor:blue \
-V geometry:margin=2cm \
--pdf-engine=xelatex \
-o documentation.pdf \
#--verbose

# --toc \
#-V fontsize=12pt \

# Szükséges:
# sudo apt install librsvg2-bin texlive-xetex
