# BoundingBox

## Presentation 

Bouding box est un projet scolaire dont le sujet détaillé ce trouve dans le fichier sujet.pdf.

Le but du projet est d'implémenté les algorithmes de Ritter et de Toussaint, calculant respectivement le cercle minimum et le rectangle minimum contenant un ensemble de points. 

A partir de ces algorithmes, un rapport 'disponible dans rapport.pdf) de recherche doit être fait pour les présenter, et en présenter les résultat, notament la qualité des conteneurs et le temps d'execution des algorithmes. 

## Execution du projet

Pour lancer le projet, vous devez avoir python 3.6 ou supérieur d'installer, et python doit être lancable via la commande bash `python3`

Il vous faudra vous placer dans le dossier racine du projet :

`cd BoundingBox`

donner les droits d'execution au script de lancement si celui-ci ne les possède pas :

`chmod 700 run.sh`

Vous pouvez ensuite lancer le projet de plusieurs manières, selon les arguments passés au script : 

`./run.sh` : lancera l'execution des algorithmes sur le premier test de la base de test et vous affichera le résultat (cercle et rectangle minimum) graphiquement, depuis cette fenêtre graphique, vous pouvez télécharger l'image du résultat via le bouton associé, ou **passer au résultat suivant en appuyant sur la touche 'd' de votre clavier.**

`./run.sh quality` : lancera l'execution des tets de qualitée des conteneurs et vous affichera les courbes résultats, vous pouvez télécharger les résultats via le bouton associer. Dans le terminal s'afficheront également les moyennes et écarts type.

`./run.sh time` : lancera l'execution des tests de vitesse et affichera les courbes résultats que vous pouvez télécharger via le bouton associer. Par défaut, les tests de vitesses ce font sur des listes de points de la base de test allant de 256 à 425 728 points, néanmoins, le projet étant développer en python et le résultats etant long à calculer de ce fait, on applique par défaut un gap de 1000 : on testera donc sur 256, 1256, 2256 ... etc. 
Vous pouvez modifier ce gap en passant un deuxieme argument, par exemple si je veux appliquer un gap de 10 000, je lancerais : `./run.sh time 10000`

**Si vous avez un problème avec le script de lancement** : Vous pouvez lancer manuelement le projet depuis la racine de celui-ci, via votre commande python, par exemple :

`python3 src/graphics.py time 10000` : pour lancer les tests de vitesse avec un gap de 10 000.

## Fichiers du projet

Le projet contient les fichier et dossiers suivant : 

**results :** Contient les images résultats pour les test de qualité et vitesse.

**samples :** Contient la base de test.

**src :** Contient le code source.

**run.sh :** Script de lancement du projet.

**src/algorithms.py :** Contient l'implémentation des algorithmes de Ritter, Graham, et Toussaint.

**src/graphics.py :** 
Contient les fonctions nécéssaire pour l'affichage ainsi que le main.

**src/tests.py :**
Contient les fonctions nécéssaire pour lancer les tests.

**src/utils.py :** Contient des fonctions et structures utilisés par les algorithmes, notament les structures : *Point*, *Circle*, *Rectangle*, et *Line*