import codecs
from pathlib import Path
import sys

import frontmatter
import textdistance

home = Path(__file__).parent.parent

failure = False

possible_authors = [a.name for a in (home / "content/authors").iterdir() if a.is_dir()]

for publication_folder in (home / "content/publication").iterdir():
    if publication_folder.name == "_index.md":
        continue
    if not publication_folder.is_dir():
        print(f"Unexpected file {publication_folder.name} in publications folder : {home / 'content/publication'}", file=sys.stderr)
        print(f"", file=sys.stderr)
        failure = True
    for file in publication_folder.iterdir():
        if file.name == "cite.bib":
            continue
        elif file.name == "index.md":
            with open(file, 'r') as f:
                text = f.read()
            lines = [l.strip('\\') for l in text.split('\n')]
            lines = [codecs.decode(codecs.encode(l, 'latin-1', 'backslashreplace'), 'unicode-escape') for l in lines]
            publication_info = frontmatter.loads(text)
            authors = publication_info['authors']
            for a in authors:
                names = a.split()
                probable_names = [pa for pa in possible_authors if textdistance.levenshtein(names[-1].lower(), pa.split('-')[-1]) < 2]
                probable_names = [pa for pa in probable_names if pa[0] == a[0].lower()]
                if len(names[0]) == 1 or (len(names[0]) == 2 and names[0][1] == '.'):
                    print("Full names should be used to facilitate linking to staff member pages", file=sys.stderr)
                    print(f"Found : {a} in {file}", file=sys.stderr)
                    print(f"", file=sys.stderr)
                    line = next(i for i,l in enumerate(lines) if a in l)
                    endLine = line
                    title = f"Full names"
                    message = "Full names should be used to facilitate linking to staff member pages"
                    print(f"::warning file={file.relative_to(home)},line={line},endLine={endLine},title={title}::{message}")
                    failure = True
                if probable_names:
                    print("Author should probably link to permanent staff member", file=sys.stderr)
                    print(f"{a} -> {probable_names}", file=sys.stderr)
                    print(f"", file=sys.stderr)
                    line = next(i for i,l in enumerate(lines) if a in l)
                    endLine = line
                    title = f"{a} -> {probable_names}"
                    message = "Author should probably link to permanent staff member"
                    print(f"::warning file={file.relative_to(home)},line={line},endLine={endLine},title={title}::{message}")
        else:
            print(f"Unexpected file {file.name} in publications folder : {publication_folder}", file=sys.stderr)
            print(f"", file=sys.stderr)
            failure = True

if failure:
    sys.exit(1)
