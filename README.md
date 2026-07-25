# PêcheScore Tide Data

Dépôt public destiné à distribuer des **fichiers dérivés et versionnés** nécessaires au moteur de marée de PêcheScore.

## Contenu autorisé

- manifests JSON ;
- schémas JSON ;
- documentation de provenance et d’attribution ;
- scripts légers de contrôle ;
- assets binaires dérivés publiés dans **GitHub Releases** après validation scientifique et juridique.

## Contenu interdit

- fichiers FES/AVISO+ originaux (`.nc`, `.nc.xz`) ;
- identifiants AVISO+, mots de passe, jetons ou clés ;
- données d’accès Google Play ;
- caches Python (`__pycache__`, `.pyc`) ;
- builds Android, APK, AAB ou données personnelles ;
- code source privé de l’application PêcheScore.

## Distribution

Les applications consomment un manifest de release, vérifient le SHA-256 de chaque asset, puis mettent localement en cache les données nécessaires au spot.

Aucune release de données ne doit être publiée avant :

1. validation du format final ;
2. validation scientifique des données dérivées ;
3. confirmation des obligations de licence et d’attribution ;
4. contrôle qu’aucune donnée source originale n’est redistribuée.
