# 🎮 Insta Grid Architect - Wii Edition ⚪

**Insta Grid Architect** est un outil de création de grilles Instagram (3xN) automatisé. Il transforme une image unique en une mosaïque esthétique, tout en adoptant un style inspiré de l'interface de la **Nintendo Wii**.

L'application garantit que **100% de votre image** est visible (pas de rognage involontaire sur le profil) et optimise le rendu pour le fil d'actualité au format **4:5**.

---

## ✨ Fonctionnalités clés

* **Mode Wii Automatique** : Intègre le fond texturé officiel et applique un cadre gris arrondi (`#DCDCDC`) pour un look "Menu Wii" authentique.
* **Adaptation Intégrale** : L'image source est redimensionnée pour tenir entièrement dans la grille, peu importe son ratio (Portrait, Paysage ou Carré).
* **Optimisation Instagram** :
    * **Sur le profil** : Une grille 3xN parfaitement alignée.
    * **Dans le fil d'actualité** : Des posts au format **4:5 (Portrait)** avec des marges blanches pour un aspect épuré.
* **Export ZIP** : Génère toutes les tuiles numérotées et prêtes à l'emploi.

---

## 🛠️ Installation et Prérequis

### 1. Logiciels nécessaires
Vous devez avoir **Python 3.8+** installé sur votre système.

### 2. Bibliothèques Python
Ouvrez un terminal et installez les dépendances :
```bash
pip install streamlit Pillow
```

### 3. Structure du dossier
Pour que l'application fonctionne, assurez-vous d'avoir ces fichiers dans le même dossier :
* `app.py` : Le code source de l'application.
* `Wii_bg.png` : L'image de fond texturée fournie.
* `README.md` : Ce guide.

---

## 🚀 Guide de Lancement (Multi-plateforme)

### 🪟 Sur Windows (Lancement rapide)
Pour lancer l'application sans ouvrir de logiciel de code :
1.  Créez un fichier texte nommé `lancer_app.bat` dans votre dossier.
2.  Éditez-le et collez la ligne suivante :
```batch
@echo off
streamlit run app.py
pause
```
3.  Double-cliquez sur `lancer_app.bat`.

### 🦎 Sur Pyzo
1.  Ouvrez le fichier `app.py` dans Pyzo.
2.  Allez dans l'onglet **Shell** en bas de l'écran.
3.  Tapez la commande suivante et appuyez sur **Entrée** :
```bash
streamlit run app.py
```

### 💻 Sur Bash (Linux, macOS, Git Bash)
1.  Ouvrez votre terminal et déplacez-vous dans le dossier du projet :
```bash
cd /chemin/vers/votre/dossier
```
2.  Lancez l'application :
```bash
streamlit run app.py
```

### 🏆 Dans PyCharm
1.  Ouvrez le **Terminal** intégré (en bas de la fenêtre).
2.  Tapez : 
```bash
streamlit run app.py
```

---

## 📖 Mode d'emploi

1.  **Nombre de lignes** : Choisissez sur combien de rangées verticales votre image doit s'étendre (3 images par rangée).
2.  **Style Wii** : Laissez la case cochée pour activer le contour gris et utiliser le fond `Wii_bg.png` automatiquement.
3.  **Image principale** : Chargez la photo que vous souhaitez transformer.
4.  **Générer** : Cliquez sur le bouton "🚀 Générer la grille".
5.  **Télécharger** : Récupérez le fichier `.zip` contenant vos images découpées.

> [!CAUTION]
> ### 📤 Ordre de Publication (Crucial)
> Instagram affiche les photos de la plus récente à la plus ancienne. Pour que votre grille ne soit pas mélangée, vous devez uploader les fichiers dans l'ordre de leur numéro :
> 1. Postez **`grid_1.jpg`** en premier (elle apparaîtra en bas à droite de votre profil).
> 2. Postez **`grid_2.jpg`**, puis la 3, et ainsi de suite.
> 3. Le dernier numéro sera l'image située en haut à gauche de votre grille.

---

## 📐 Spécifications Techniques

* **Format de sortie** : JPEG (.jpg) haute qualité.
* **Dimensions par tuile** : 1080 x 1350 pixels (Format Portrait Instagram).
* **Design** : Contour Gris Wii (`RGB 220, 220, 220`), coins arrondis (Rayon 60px), marges blanches de sécurité.

---
*Développé pour transformer votre profil Instagram en une interface de légende.*
