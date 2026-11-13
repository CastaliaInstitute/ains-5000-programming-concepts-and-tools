from pathlib import Path
import shutil
root = Path(__file__).resolve().parents[1]
site = root / 'site'
if site.exists(): shutil.rmtree(site)
(site / 'book').mkdir(parents=True)
shutil.copytree(root / '_build/html', site / 'book', dirs_exist_ok=True)
(site / 'downloads').mkdir()
pdfs = list((root / '_build/latex').glob('*.pdf'))
if not pdfs: raise SystemExit('Build the PDF before staging the site')
shutil.copyfile(pdfs[0], site / 'downloads/ains5000.pdf')
(site / 'index.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>AINS5000</title></head><body><h1>AINS5000: Programming Concepts and Tools for AI</h1><p><a href="book/intro.html">Read the course</a> · <a href="downloads/ains5000.pdf">Download the linked PDF</a> · <a href="book/glossary.html">Cross-course glossary</a></p></body></html>')
(site / '.nojekyll').touch()
