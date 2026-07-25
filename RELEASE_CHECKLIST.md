# Checklist de publication d’une release de données

## Scientifique

- [ ] Tous les candidats ont franchi les portes prévues.
- [ ] Aucun asset rejeté ou diagnostique n’est présent.
- [ ] Version FES, conventions, catalogue et méthode d’interpolation documentés.
- [ ] Comparaisons de référence jointes au rapport de la passe.

## Intégrité

- [ ] `manifest.json` valide contre le schéma.
- [ ] SHA-256 et taille de chaque asset contrôlés localement.
- [ ] Aucun `.nc`, `.nc.xz`, `.xz`, `.pyc` ou `__pycache__`.
- [ ] Aucun secret, token, chemin personnel ou donnée d’accès.

## Juridique

- [ ] Conditions AVISO+/FES revues pour la redistribution du format dérivé.
- [ ] Attribution CNES/LEGOS/NOVELTIS/CLS/AVISO+ présente.
- [ ] Aucun courant FES2022 ni autre produit à accès restreint.

## GitHub

- [ ] Release créée en brouillon.
- [ ] Tag cohérent avec `dataVersion`.
- [ ] Assets téléversés sans modification de nom.
- [ ] URL de chaque asset vérifiée.
- [ ] Test de téléchargement anonyme réussi.
- [ ] Release publiée seulement après test Android.
