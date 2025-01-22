%-handout.pdf: %.md
	pandoc $< -H header.tex -o $@

%.pdf: %.md
	pandoc -t beamer $< -V theme:boxes -H header-beamer.tex -o $@
