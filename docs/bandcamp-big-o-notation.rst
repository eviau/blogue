Bandcamp: big O notation for Fridays
====================================

.. post:: May 13, 2023
   :tags: art, bandcamp, informatique, computer science
   :author: me and a friend
   :language: fr
   
J'ai demandé la question suivante de façon anonyme:

```
ça prendrait quoi pour qu'un fichier audio soit turing complete et que bandcamp s'en rende pas compte ?
```

Et la brillante, excellente réponse anonyme:

RÉPONSE
-------

Le terme "Turing complete" s'applique à un ordinateur (qui traite une suite d'instructions) ou à un langage (dans le sens que c'est une suite d'instructions).
Typiquement ces langages peuvent être exprimés sous une grammaire du genre:

```
expression ::= atom | list
atom       ::= number | symbol
number     ::= [+-]?['0'-'9']+
symbol     ::= ['A'-'Z''a'-'z'].*
list       ::= '(' expression* ')'
```

Une telle grammaire est dite "Turing complete" si elle peut exprimer toutes les fonctions calculables. Les langages "Turing complete" sont tous équivalents en termes de capacité calculatoire.

Donc, pour ta question. Un fichier audio en soi n'est pas un langage. C'est une série de données ordonnées représentant des modulations sonores selon un standard spécifique. Les formats modernes sont souvent sous forme de conteneur: MP3, MP4, WAV, etc. 

A)
Est-ce possible de créer un standard audio qui contient à la fois une série de données sonores tout en étant un langage?

Oui. La solution triviale existe déjà, techniquement n'importe quel programme actuel l'est déjà. Tu peux faire le lire les données raw de n'importe quel programme à ta carte de son et elle produire quelque chose. Ça ne sera rien d'intéressant. La difficulté est de créer un langage qui produit des fichiers de programmes non triviaux qui encodent en même temps des sons non triviaux. (et de créer le décodeur approprié pour le nouveau format, et de rajouter ce décodeur à ton lecteur multimédia)

Comme solution un peu moins triviale: Le langage est simplement du C avec une entête qui dit la taille des instructions C. Le reste du programme est le data d'un WAV. Est-ce que ça remplit ton critère?

B)
Est-ce que ce nouveau fichier audio pourrait être téléversé dans Bandcamp s'en qu'il ne s'en rende compte?

1. Bandcamp ne supporte que certains types de fichiers. À moins de prétendre être un type différent (en fabriquant une fausse entête) le fichier sera probablement rejeté.
2. En supposant que le fichier ne soit pas rejeté, il sera simplement non lisible par le lecteur multimédia de la personne qui le lit. Une fois passé l'entête, le reste du fichier ne sera pas dans un format supporté. (à moins que tu arrives à rendre ton nouveau format mainstream, mais rendu là Bandcamp le supportera probablement de toute façon donc la condition "sans s'en rendre compte" sera fausse)

C)
Supposons qu'on a créé le langage/format audio parfait discuté en A et qu'il soit disponible sur Bandcamp (qui pense que c'est un autre format) et que ton lecteur multimédia le supporte. Lorsque traité comme fichier audio dans le lecteur multimédia, la musique pourra jouer normalement. Lorsque exécuté comme programme par ton système d'exploitation, le programme roulera.

Finalement, ce n'est pas impossible. Réaliser A est difficile et probablement inutile. Réaliser B est facile (à moins que Bandcamp ait beaucoup de mesures pour détecter les faux fichiers) mais le résultat ne sera utilisable que pour ceux qui ont un lecteur qui supporte le nouveau format.

- Edith, samedi 13 mai 2023, 14h28m00s
