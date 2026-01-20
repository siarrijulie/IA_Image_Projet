# Projet IA – Classification d’Images

Projet de **classification d’images** utilisant des méthodes de **vision par ordinateur** et d’**apprentissage automatique**.

Le code de base est fourni par le professeur.

---

## Prérequis

- **Python 3.10 (64 bits)**
- **pip**
- **Jupyter Notebook**

---

## Création de l’environnement virtuel

### Windows
```bash
py -3.10 -m venv venv
venv\Scripts\activate
```

### macOS / Linux
```bash
python3.10 -m venv venv
source venv/bin/activate
```

---

## Installation des dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Datasets

**Les datasets ne sont pas inclus dans le dépôt GitHub.**

### Datasets utilisés

- **MNIST (chiffres manuscrits)**  
  https://keras.io/api/datasets/mnist/

- **Dogs & Cats (Kaggle)**  
  https://www.kaggle.com/chetankv/dogs-cats-images

- **Intel Image Classification (Kaggle)**  
  https://www.kaggle.com/datasets/puneet6060/intel-image-classification

---

## Structure du projet attendue

```text
Projet_IA_Image/
│
├── cnn.py
├── RK_Image_Classification_Bag_of_Visual_Words.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── dataset/                 # Non inclus sur GitHub
│   ├── training_set/
│   │   ├── class1/
│   │   └── class2/
│   └── test_set/
│       ├── class1/
│       └── class2/
│
├── notebooks/
│   ├── CNN_DogsCats.ipynb
│   ├── CNN_IntelImageClassification.ipynb
│   ├── checkpoints_cnn_2/
│   └── checkpoints_cnn_3/
│
├── single_prediction/       # À créer manuellement
│   └── cat_or_dog1.jpg
│
├── documents/
│   └── consignes.pdf
│
└── venv/                    # Non inclus sur GitHub
```

---

## Exécution des notebooks (CNN)

Les expérimentations CNN (notamment pour **Dogs & Cats**) sont réalisées via des **notebooks Jupyter**.

### Étapes à suivre

1. Se placer à la racine du projet  
2. Activer l’environnement virtuel  
3. Lancer Jupyter Notebook :

```bash
jupyter notebook
```

4. Ouvrir le dossier `notebooks/`  
5. Exécuter les notebooks :
   - `CNN_DogsCats.ipynb`
   - `CNN_IntelImageClassification.ipynb`

---

## Checkpoints

Les poids des modèles sont automatiquement sauvegardés pendant l’entraînement.

### CNN à 2 convolutions
```text
notebooks/checkpoints_cnn_2/
```

### CNN à 3 convolutions
```text
notebooks/checkpoints_cnn_3/
```

Ces checkpoints correspondent aux expériences de classification **Dogs & Cats** et permettent de restaurer le **meilleur modèle** grâce à l’**early stopping**.

---

## ▶Exécution du script classique (optionnel)

Pour exécuter la version script du modèle CNN :

```bash
python cnn.py
```
