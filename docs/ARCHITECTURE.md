# Architecture de distribution retenue

1. Les fichiers NetCDF FES restent sur le poste de génération, hors Git.
2. Un outil reproductible génère des assets spatiaux dérivés.
3. Les assets sont validés et hachés.
4. Le dépôt public conserve documentation, schémas et manifest de référence.
5. Les binaires sont publiés dans une GitHub Release.
6. PêcheScore télécharge le manifest puis seulement l’asset couvrant le spot.
7. L’application vérifie le SHA-256 avant lecture.
8. Les constantes calculées pour le spot sont mises en cache pour fonctionner hors ligne.

## URL stable possible

Pour un asset nommé `manifest.json` dans la dernière release :

`https://github.com/Philipppri/pechescore-tide-data/releases/latest/download/manifest.json`

Le code de production ne doit cependant accepter une nouvelle version que si son format et sa provenance sont compatibles.
