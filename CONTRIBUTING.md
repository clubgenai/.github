# Contribuer

## Nomenclature des repos

Format : `[domaine]-[nom]` en kebab-case

| Préfixe | Usage | Visibilité |
|---|---|---|
| `infra-` | Config serveur, NixOS, ops | private |
| `app-` | Apps web internes | private |
| `mcp-` | Serveurs MCP | private |
| `workshop-` | Sessions communautaires | public |
| `tool-` | Outils internes | private |

- Description obligatoire à la création
- kebab-case strict, pas de majuscules

## Branches

- `main` — branche par défaut
- Features sur branches courtes, PR pour merger

## Commits

Format : `type: message court`
Types : `feat`, `fix`, `infra`, `docs`, `chore`
