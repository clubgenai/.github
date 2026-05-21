import json, sys

HEADER = """# Club GenAI Bordeaux

Communauté IA générative — meetups, workshops, projets.

## Workshops disponibles

| Workshop | Description | Slides |
|----------|-------------|--------|"""

FOOTER = """
---

[Contribuer](CONTRIBUTING.md) · [clubgenai.github.io](https://clubgenai.github.io)"""

def main(path):
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            repo = json.loads(line)
            name = repo['name']
            label = name.replace('workshop-', '').replace('-', ' ').title()
            desc = repo.get('description') or ''
            url = repo.get('homepageUrl') or f"https://clubgenai.github.io/{name}/"
            rows.append(f"| [{label}]({url}) | {desc} | [Voir]({url}) |")

    if rows:
        print(HEADER)
        print('\n'.join(rows))
    else:
        print(HEADER.replace(
            '| Workshop | Description | Slides |\n|----------|-------------|--------|',
            '*Aucun workshop publié pour le moment.*'
        ))
    print(FOOTER)

if __name__ == '__main__':
    main(sys.argv[1])
