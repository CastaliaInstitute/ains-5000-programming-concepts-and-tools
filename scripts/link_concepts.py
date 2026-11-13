#!/usr/bin/env python3
"""Link first-use concepts in a Jupyter Book's readings and notebook slides.

Run from the course root: python scripts/link_concepts.py .
Definitions and graduate lesson destinations come from references/concepts.json.
Existing links, code, math, headings, and executable notebook cells are preserved.
"""
import argparse,json,os,re
from pathlib import Path

def glossary(root,concepts):
 text='# Cross-course glossary\n\nPlain-language definitions with links to programming readiness and related graduate lessons. Read the linked lesson for the discipline-specific context.\n\n[Programming readiness and tool help](https://aurnova.github.io/ains5000-course/book/reference.html)\n\n'
 for c in concepts:
  text+=f'({c["slug"]})=\n## {c["label"]}\n\n{c["definition"]}\n\n'
  links=[]
  if c['lesson']:links.append(f'[AINS5000 · Module {c["lesson"]}](https://aurnova.github.io/ains5000-course/book/lessons/module-{c["lesson"]}.html)')
  links += [f'[{x["course"]} · {x["title"]}]({x["url"]})' for x in c['learn']]
  if links:text+='Learn more: '+' · '.join(links)+'\n\n'
 (root/'glossary.md').write_text(text.rstrip()+'\n')

# Protect authored Markdown structures. This is deliberately conservative:
# annotations belong in narrative text, not code examples or existing links.
protected=re.compile(r'(```[\s\S]*?```|~~~[\s\S]*?~~~|`[^`\n]+`|!?\[[^\]\n]*\]\([^\n)]*\)|\{[^}\n]+\}`[^`]+`|https?://\S+|\$\$[\s\S]*?\$\$|\$[^$\n]+\$|^#{1,6}[^\n]*|<[^>\n]+>)',re.M)
def annotate(text,link,concepts,seen):
 aliases={name.lower():c for c in concepts for name in [c['label'],*c.get('aliases',[])]}
 # Normalize our own links so repeat runs do not link the next occurrence.
 text=re.sub(r'\[([^\]\n]+)\]\('+re.escape(link)+r'#([^)]*)\)', lambda m: m[1] if m[1].lower() in aliases and aliases[m[1].lower()]['slug']==m[2] else m[0], text)
 pattern=re.compile(r'(?<![\w/-])('+ '|'.join(re.escape(a) for a in sorted(aliases,key=len,reverse=True))+r')(?![\w/-])',re.I)
 chunks=protected.split(text)
 for i in range(0,len(chunks),2):
  def replace(match):
   c=aliases[match[0].lower()]
   if c['slug'] in seen:return match[0]
   seen.add(c['slug']);return f'[{match[0]}]({link}#{c["slug"]})'
  chunks[i]=pattern.sub(replace,chunks[i])
 return ''.join(chunks)

def apply(root):
 concepts=json.loads((root/'references/concepts.json').read_text())
 glossary(root,concepts)
 readings=list((root/'modules').glob('module-*/book-prose.md'))+list((root/'modules').glob('module-*/overview.md'))+list((root/'lessons').glob('module-*.md'))
 readings += [root/n for n in ['intro.md','student-guide.md','technical-requirements.md','resources.md'] if (root/n).exists()]
 count=0
 for p in readings:
  before=p.read_text();link=Path(os.path.relpath(root/'glossary.md',p.parent)).as_posix();seen=set()
  after=annotate(before,link,concepts,seen)
  if after!=before:p.write_text(after);count+=1
 decks=list((root/'modules').glob('module-*/slides.ipynb'))+list((root/'slides').glob('module-*.ipynb'))
 for p in decks:
  book=json.loads(p.read_text());link=Path(os.path.relpath(root/'glossary.md',p.parent)).as_posix();seen=set()
  for cell in book['cells']:
   if cell['cell_type']!='markdown':continue
   source=''.join(cell['source'])
   cell['source']=annotate(source,link,concepts,seen).splitlines(True)
  if not any('<!-- AINS CONCEPT HELP -->' in ''.join(c['source']) for c in book['cells']):
   book['cells'].append({'cell_type':'markdown','id':'ains-concept-help','metadata':{'slideshow':{'slide_type':'slide'}},'source':['<!-- AINS CONCEPT HELP -->\n','# Concept reference and programming help\n\n',f'[Cross-course glossary]({link}) · [AINS5000 programming readiness](https://aurnova.github.io/ains5000-course/book/reference.html)\n\n','Follow a glossary entry to its definition and the related graduate lessons. Review the beginner lesson when a tool or programming step is unfamiliar.']})
  p.write_text(json.dumps(book,indent=1,ensure_ascii=False)+'\n')
 toc=root/'_toc.yml'
 if toc.exists() and not re.search(r'file:\s*[\'"]?glossary\b',toc.read_text()):toc.write_text(toc.read_text().rstrip()+'\n  - file: glossary\n')
 marker='<!-- AINS5000 READINESS -->'
 block='''\n<!-- AINS5000 READINESS -->
## Programming readiness and concept help

New to programming or the course tools? [AINS5000: Programming Concepts and Tools for AI](https://aurnova.github.io/ains5000-course/book/intro.html) provides short lessons on GitHub accounts, Colab, Codespaces, Python concepts, saving work, and asking for help. Use its [quick reference](https://aurnova.github.io/ains5000-course/book/reference.html) to jump directly to the skill an activity requires.

The [cross-course glossary](glossary.md) links definitions to foundational explanations and related AINS graduate lessons. It supports the published book and slide references. Your instructor's access, assessment, and submission instructions remain authoritative.
<!-- END AINS5000 READINESS -->
'''
 for name in ['intro.md','student-guide.md','README.md']:
  p=root/name
  if p.exists() and marker not in p.read_text():p.write_text(p.read_text().rstrip()+'\n'+block)
 return {'repo':root.name,'readings':count,'decks':len(decks),'concepts':len(concepts)}
if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('root',type=Path,nargs='?',default=Path('.'));args=parser.parse_args();print(json.dumps(apply(args.root.resolve())))
