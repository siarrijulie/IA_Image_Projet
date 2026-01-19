# Projet IA - Classification d’Images

Projet de classification d’images utilisant des méthodes de vision par ordinateur
et d’apprentissage automatique.

Le code de base est fourni par le professeur.

---

## Prérequis

- Python 3.10 (64 bits)
- pip

---

## Création de l’environnement virtuel

### Windows
py -3.10 -m venv venv  
venv\Scripts\activate  

### macOS / Linux
python3.10 -m venv venv  
source venv/bin/activate  

---

## Installation des dépendances

pip install --upgrade pip  
pip install -r requirements.txt  

---

## Datasets

Les datasets ne sont **pas inclus** dans le dépôt GitHub.

### Datasets utilisés

- **MNIST (chiffres manuscrits)**  
  https://keras.io/api/datasets/mnist/

- **Dogs & Cats (Kaggle)**  
  https://www.kaggle.com/chetankv/dogs-cats-images

- **Intel Image Classification (Kaggle)**  
  https://www.kaggle.com/datasets/puneet6060/intel-image-classification

### Structure attendue

dataset/
├─ training_set/
│  ├─ class1/
│  └─ class2/
└─ test_set/
   ├─ class1/
   └─ class2/


---

## Exécution

Lancer le script principal :

python cnn.py

---

## Remarques

- TensorFlow s’exécute en mode CPU
- Les poids peuvent être sauvegardés pour reprendre l’entraînement
- Les fonctions d’activation utilisées sont ReLU et Sigmoid
