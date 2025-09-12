import requests
import os
import re
import datetime
import yaml
from pathlib import Path
import unidecode

# === Config ===
PROJECT_NAME = "gysela"     # change to your project keyword
AUTHOR_DIR = Path(__file__).parent.parent / "content" / "authors"
PUBLICATION_DIR = Path(__file__).parent.parent / "content" / "publication"
last_run=os.environ['LAST_RUN']
#LAST_RUN_FILE = Path("last_run.txt")
VENUE_ABBREVIATIONS_FILE = Path("venue_abbreviations.yml")

existing_slugs = {p.stem for p in PUBLICATION_DIR.iterdir() if p.is_dir()}

# === Helpers ===
def load_abbrev_map():
    if VENUE_ABBREVIATIONS_FILE.exists():
        with open(VENUE_ABBREVIATIONS_FILE) as f:
            return yaml.safe_load(f)
    return {}

def load_key_authors():
    key_authors = []
    for md_file in Path(AUTHOR_DIR).rglob("*.md"):
        with open(md_file, encoding="utf-8") as f:
            content = f.read()
        if content.startswith("---"):
            front_matter = content.split("---", 2)[1]
            data = yaml.safe_load(front_matter)
            if "name" in data and "organizations" in data:
                orgs = [o["name"] for o in data.get("organizations", []) if "name" in o]
                key_authors.append({
                    "name": " ".join(data["name"].split(" ")[1:]),
                    "organizations": orgs
                })
    return key_authors

def get_first_author_surname(authorships):
    if authorships:
        first_author = authorships[0]["author"]["display_name"]
        surname = first_author.split()[-1]
        return unidecode.unidecode(surname).lower()
    return "unknown"

def get_all_authors(authorships):
    return " and ".join(a["author"]["display_name"] for a in authorships) if authorships else "Unknown"

def author_matches(work_authorships, key_authors):
    for a in work_authorships:
        author_name = a["raw_author_name"]
        institutions = [i["raw_affiliation_string"] for i in a["affiliations"]]
        for ka in key_authors:
            if (ka["name"].lower() in author_name.lower()) and \
                    any(org.lower() in instit.lower() for org in ka["organizations"] for instit in institutions):
                return True
    return False

def make_slug(meta, abbrev_map):
    surname = get_first_author_surname(meta["authorships"])
    if meta["venue_full"] in abbrev_map:
        venue = abbrev_map[meta["venue_full"]]['slug']
    else:
        venue = meta["venue_full"]
    year = str(meta["year"])
    slug_base = f"{surname}-{venue}-{year}"
    slug = slug_base
    i = 2
    while slug in existing_slugs:
        slug = f'{slug_base}_{i}'
        i+=1
    existing_slugs.add(slug)
    return slug

def extract_metadata(work, abbrev_map):
    """Extract shared metadata for front_matter and bibtex."""
    title = work.get("title", "")
    authorships = work.get("authorships", [])
    authors_list = [a["author"]["display_name"] for a in authorships]
    authors_bibtex = get_all_authors(authorships)
    surname = get_first_author_surname(authorships)
    venue_host = work.get("host_venue", {}).get("display_name")
    venue_primary = work.get("primary_location", {})
    if venue_primary:
        venue_primary = venue_primary.get("source", {})
        if venue_primary:
            venue_primary = venue_primary.get("display_name")
    venue_full = venue_primary or venue_host or ""
    year = work.get("publication_year", "")
    doi = work.get("doi")
    url = f"https://doi.org/{doi}" if doi else None
    pub_date = work.get("publication_date", "1900-01-01")
    biblio = work.get("biblio", {})
    volume = biblio.get("volume")
    issue = biblio.get("issue")
    first_page = biblio.get("first_page")
    last_page = biblio.get("last_page")
    pages = f"{first_page}--{last_page}" if first_page and last_page else None
    abstract = work.get("abstract_inverted_index") and " ".join(work["abstract_inverted_index"].keys()) or ""
    return {
        "title": title,
        "authors_list": authors_list,
        "authors_bibtex": authors_bibtex,
        "authorships": authorships,
        "venue_full": venue_full,
        "year": year,
        "doi": doi,
        "url": url,
        "pub_date": pub_date,
        "volume": volume,
        "issue": issue,
        "pages": pages,
        "surname": surname,
        "abstract": abstract
    }

def to_bibtex(meta, slug, abbrev_map):
    if meta["venue_full"] in abbrev_map:
        venue = abbrev_map[meta["venue_full"]]['bibtex']
    else:
        venue = meta["venue_full"]
    fields = {
        "title": meta["title"],
        "author": meta["authors_bibtex"],
        "journal": venue, 
        "year": meta["year"],
        "volume": meta["volume"],
        "number": meta["issue"],
        "pages": meta["pages"],
        "doi": meta["doi"],
        "url": meta["url"]
    }
    lines = [f"@article{{{slug},"]
    lines.extend(f"  {k} = {{{v}}}," for k, v in fields.items() if v)
    lines[-1] = lines[-1].rstrip(",")  # drop trailing comma
    lines.append("}")
    return "\n".join(lines)

def write_index_md(folder, meta):
    front_matter = {
        "title": meta["title"],
        "subtitle": "",
        "summary": "",
        "authors": meta["authors_list"],
        "tags": [],
        "categories": [],
        "date": meta["pub_date"],
        "lastmod": datetime.datetime.now().isoformat(),
        "featured": False,
        "draft": False,
        "image": {"caption": "", "focal_point": "", "preview_only": False},
        "projects": [],
        "publishDate": datetime.datetime.now().isoformat(),
        "publication_types": ["1"],
        "abstract": meta["abstract"],
        "publication": meta["venue_full"],
        "doi": meta["doi"] or ""
    }
    index_md = "---\n" + yaml.dump(front_matter, sort_keys=False) + "---\n"
    (folder / "_index.md").write_text(index_md, encoding="utf-8")

# === Main ===
def main():
    #last_run = load_last_run()
    abbrev_map = load_abbrev_map()
    key_authors = load_key_authors()

    found_doi = set()

    for PROJECT_NAME in ('gysela', 'gyselax', 'gyselalib'):
        url = "https://api.openalex.org/works"
        params = {
            "search": PROJECT_NAME,
            "filter": f"from_publication_date:{last_run}",
            "per-page": 50
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        results = data.get("results", [])
        print(f"Found {len(results)} results for {PROJECT_NAME} since {last_run}")

        for work in results:
            if work.get("type") == "preprint":
                continue
            meta = extract_metadata(work, abbrev_map)
            if "arxiv" in meta["venue_full"].lower():
                print("Discarding preprint : ", meta["title"])
                continue
            gysela_in_title = PROJECT_NAME in meta["title"].lower()
            gysela_in_abstract = PROJECT_NAME in meta["abstract"].lower()
            written_by_key_author = author_matches(meta["authorships"], key_authors)
            if not (gysela_in_title or gysela_in_abstract) and \
                    not written_by_key_author:
                print("Discarding citation : ", meta["title"], meta["authors_list"])
                continue

            if meta["doi"] in found_doi:
                continue
            found_doi.add(meta["doi"])

            print("Saving :")
            print("    ", meta["title"])
            print("    ", meta["authors_list"])
            if gysela_in_title or gysela_in_abstract:
                print("Mentioning Gysela prominently")
            if written_by_key_author:
                print("Written by permanent contributor")
            print()

            slug = make_slug(meta, abbrev_map)
            folder = PUBLICATION_DIR / slug
            folder.mkdir(parents=True, exist_ok=True)

            # Write index.md
            write_index_md(folder, meta)

            # Write cite.bib
            bibtex = to_bibtex(meta, slug, abbrev_map)
            (folder / "cite.bib").write_text(bibtex, encoding="utf-8")

    #today = datetime.date.today().isoformat()
    #save_last_run(today)
    #print(f"Updated last run date to {today}")

if __name__ == "__main__":
    main()

