## Réseau de neurones convolutionnel (CNN)

Dans ce projet, un réseau de neurones convolutionnel (CNN) a été utilisé afin de réaliser une classification binaire d’images (chien / chat). Le choix du CNN s’explique par sa capacité à extraire automatiquement des caractéristiques discriminantes à partir des images, sans nécessiter de phase d’extraction manuelle de descripteurs.

---

## Architecture du réseau

L’architecture finale du réseau est volontairement compacte et se compose de :

- deux couches convolutionnelles, chacune suivie d’une couche de pooling ;
- une couche de *Flatten* permettant de transformer les cartes de caractéristiques en un vecteur ;
- une couche entièrement connectée pour la classification finale.

Les couches convolutionnelles utilisent la fonction d’activation **ReLU**, définie par la fonction `max(0, x)`. Cette fonction introduit de la non-linéarité dans le modèle tout en limitant les problèmes de gradient et en favorisant une convergence plus rapide.

La couche de sortie utilise la fonction **Sigmoid**, définie par la fonction : 1 / (1 + e⁻ˣ), particulièrement adaptée à une tâche de classification binaire.

---

## Choix de l’architecture et comparaison des modèles

Deux architectures ont été évaluées :

- un CNN à deux couches convolutionnelles ;
- un CNN à trois couches convolutionnelles.

Les expérimentations montrent que l’ajout d’une troisième couche convolutionnelle n’apporte pas d’amélioration significative de la précision sur l’ensemble de validation. En revanche, cette complexification augmente le temps d’entraînement et accentue le risque de sur-apprentissage, compte tenu de la taille du dataset.

Le choix final s’est donc porté sur une **architecture à deux couches convolutionnelles**, offrant un meilleur compromis entre performances, stabilité du modèle et coût de calcul.

---

## Ajustement du nombre de pas par epoch

Initialement, le nombre de pas par epoch avait été fixé au nombre total d’images, ce qui ne correspond pas au fonctionnement réel du réseau, qui traite les données par batch.

Ce paramètre a été corrigé afin qu’un epoch corresponde à un passage complet sur l’ensemble des données d’entraînement :

- **8000 images d’entraînement**
- **batch size = 32**
- **steps_per_epoch ≈ 250**

Cette correction permet une convergence plus stable du modèle et une interprétation plus fiable des métriques d’entraînement et de validation.

---

## Gestion du sur-apprentissage

Afin de limiter le sur-apprentissage, plusieurs mécanismes ont été mis en place :

- une sauvegarde automatique des poids du réseau à chaque epoch, permettant de reprendre l’entraînement en cas d’interruption ;
- l’utilisation d’un arrêt anticipé (*Early Stopping*), qui interrompt l’entraînement lorsque la performance sur l’ensemble de validation cesse de s’améliorer.

---

## Choix du nombre d’epochs

Plusieurs entraînements ont été réalisés afin d’analyser l’évolution de la perte et de la précision. Les résultats montrent que le modèle commence à sur-apprendre au-delà de **14 à 16 epochs**.

Le nombre maximal d’epochs a donc été fixé à **20**, l’arrêt anticipé permettant d’interrompre automatiquement l’entraînement dès que la performance sur l’ensemble de validation se dégrade.

---

## Résultats et justification du modèle retenu

Le modèle final retenu est un **CNN à deux couches convolutionnelles**, qui présente :

- une **val_accuracy stable autour de 80 à 82 %** ;
- un temps d’entraînement raisonnable ;
- un risque de sur-apprentissage plus faible qu’un modèle plus profond.

À l’inverse, le CNN à trois couches convolutionnelles n’apporte pas de gain significatif en précision, tout en augmentant la complexité du modèle et le temps de calcul. Il n’est donc pas optimal pour une base de taille intermédiaire (8000 images).