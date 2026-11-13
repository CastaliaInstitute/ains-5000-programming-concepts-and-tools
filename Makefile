html:
	jupyter-book build .

pdf:
	jupyter-book build . --builder pdflatex

site: html pdf
	python scripts/stage_site.py
