# Politique de publication des données

## Principe

Le dépôt ne stocke que les métadonnées et la documentation. Les fichiers binaires destinés à l’application sont publiés comme assets GitHub Releases.

## Règles obligatoires

- aucun NetCDF ou XZ AVISO+/FES original ;
- aucun identifiant d’accès ;
- un SHA-256 pour chaque asset ;
- format, version scientifique, emprise géographique et qualité documentés ;
- publication atomique : manifest et assets d’une même version sont immuables ;
- une nouvelle correction produit une nouvelle release, jamais un remplacement silencieux ;
- les assets rejetés ou diagnostiques ne sont jamais publiés ;
- la release doit rester en brouillon tant que la checklist n’est pas validée.
