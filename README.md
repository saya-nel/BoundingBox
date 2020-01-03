# BoundingBox

## Presentation 

Bouding box est un projet scolaire dont le sujet détaillé se trouve dans le fichier : *sujet.pdf*.

Le but du projet est d'implémenter les algorithmes de Ritter et de Toussaint. Ils calculent respectivement le cercle minimum et le rectangle minimum, contenant un ensemble de points. 

A partir de ces algorithmes, un rapport (disponible dans rapport.pdf) de recherche les présente et présente les résultats obtenus, tels que la qualité des conteneurs et le temps d'exécution des algorithmes. 

## Exécution du projet

Afin de lancer le projet, il est nécéssaire d'avoir la version de python 3.6 ou supérieur. Le programme python doit être lancé via la commande bash `python3`

Il faudra ensuite, vous placez dans le dossier racine du projet :

`cd BoundingBox`

Donnez les droits d'exécution au script de lancement si celui-ci ne les possède pas :

`chmod 700 run.sh`

Vous pouvez maintenant lancer le projet de plusieurs manières, selon les arguments passés au script : 

`./run.sh` : lance l'exécution des algorithmes sur le premier test de la base de test et affiche le résultat (cercle et rectangle minimum) graphiquement. Depuis cette fenêtre graphique, vous pouvez télécharger l'image du résultat via le bouton associé, ou **passer au résultat suivant en appuyant sur la touche 'd' de votre clavier.**

`./run.sh quality` : lance l'exécution des tests de qualité des conteneurs et affiche les courbes résultats. Vous pouvez télécharger les résultats via le bouton associer. Dans le terminal s'afficheront également les moyennes et les écarts type.

`./run.sh time` : lance l'exécution des tests de vitesse et affiche les courbes résultats que vous pouvez télécharger via le bouton associer. Par défaut, les tests de vitesses se font sur des listes de points de la base de test allant de 256 à 425 728 points. Néanmoins, le projet étant développé en python et le résultats  long à calculer, on applique par défaut un gap de 1000 : on testera donc sur des tailles 256, 1256, 2256 ..., etc. 
Il est possible de modifier ce gap en passant un deuxième argument, par exemple : si je veux appliquer un gap de 10 000, je lance : `./run.sh time 10000`

**Si vous rencontrez un problème avec le script de lancement** : Vous pouvez lancer manuellement le projet depuis la racine de celui-ci, via votre commande python, par exemple :

`python3 src/graphics.py time 10000` : pour lancer les tests de vitesse avec un gap de 10 000.

## Fichiers du projet

Le projet contient les fichiers et dossiers suivant : 

**results :** Contient les images résultats pour les tests de qualité et vitesse.

**samples :** Contient la base de tests.

**src :** Contient le code source.

**run.sh :** Script de lancement du projet.

**src/algorithms.py :** Contient l'implémentation des algorithmes de Ritter, Graham, et Toussaint.

**src/graphics.py :** 
Contient les fonctions nécessaires pour l'affichage, ainsi que le main.

**src/tests.py :**
Contient les fonctions nécessaires pour lancer les tests.

**src/utils.py :** Contient des fonctions et structures utilisées par les algorithmes, notamment les structures : *Point*, *Circle*, *Rectangle*, et *Line*