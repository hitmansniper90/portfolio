# 🤖 MODULE_LINE_FOLLOWER_ROBOT.md  
**Robot suiveur de ligne — Arduino + Adafruit Motor Shield V1 (L293D)**

Ce document décrit le **matériel**, le **câblage** et la **mise en route** pour le code fourni (2 capteurs IR + 4 moteurs DC).

---

## ✨ Fonctionnement (résumé)
Le robot utilise **2 capteurs de ligne** :
- capteur **gauche** sur **A0**
- capteur **droit** sur **A1**

Selon l’état des capteurs :
- ✅ **00** → avance tout droit  
- ✅ **01** → tourne à droite  
- ✅ **10** → tourne à gauche  
- ✅ **11** → stop

*(0 = détecte la ligne / 1 = ne détecte pas, selon le type de capteur et le réglage du potentiomètre)*

---

## 🧰 Liste des composants

| Quantité | Composant | Détails |
|--------:|----------|---------|
| 1 | Arduino Uno (ou compatible) | Recommandé pour Motor Shield V1 |
| 1 | **Adafruit Motor Shield V1** | Basé sur **L293D** |
| 4 | Moteurs DC | 3–6V (ou adaptés à ton alimentation) |
| 1 | Châssis + roues | 4 roues (ou 2 roues + 2 roues folles) |
| 2 | Capteurs suiveur de ligne IR | Modules type TCRT5000 / KY-033 / LM393 |
| 1 | Batterie | 6–12V (selon moteurs + shield) |
| - | Fils Dupont / borniers | Connexions |
| - | Interrupteur (optionnel) | Pour couper l’alim moteur |

---

## 📚 Librairies Arduino IDE

### ✅ Installation
Dans Arduino IDE :
**Sketch → Include Library → Manage Libraries…**  
Cherche et installe :

| Librairie | Nom à rechercher |
|----------|------------------|
| Adafruit Motor Shield V1 | `Adafruit Motor Shield V1` |
| AFMotor | Souvent installée avec la précédente |

> Le code utilise : `#include <AFMotor.h>`

---

## 🔌 Câblage (tableaux clairs)

### 1) Capteurs de ligne (2 modules)

Chaque module de capteur a généralement : **VCC / GND / OUT**  
(OUT peut s’appeler **DO**)

#### Connexions (comme dans ton code)

| Capteur | Broche capteur | Arduino |
|--------|-----------------|---------|
| Gauche | VCC | 5V |
| Gauche | GND | GND |
| Gauche | OUT | **A0** |
| Droit  | VCC | 5V |
| Droit  | GND | GND |
| Droit  | OUT | **A1** |

✅ **Important :** les masses doivent être communes (GND capteurs = GND Arduino = GND alimentation moteur).

---

### 2) Moteurs DC via Motor Shield V1

Le shield a 4 sorties moteurs : **M1, M2, M3, M4**  
Ton code utilise :

| Moteur (code) | Port shield |
|--------------|-------------|
| motor1 | M1 |
| motor2 | M2 |
| motor3 | M3 |
| motor4 | M4 |

#### Connexions
- Branche **chaque moteur DC** sur les borniers **M1/M2/M3/M4**
- Si un moteur tourne “à l’envers”, inverse simplement ses deux fils sur le bornier.

---

### 3) Alimentation (très important)

| Élément | Recommandation |
|--------|----------------|
| Arduino (logique) | USB ou 7–12V sur Jack |
| Moteurs (puissance) | Batterie dédiée sur bornier **EXT_PWR** du shield |

✅ Conseillé : **séparer logique et moteurs** (moins de parasites).

⚠️ Ne pas alimenter les moteurs depuis le 5V Arduino (ça reset souvent l’Arduino).

---

## ⚙️ Réglage des capteurs
La plupart des capteurs IR ont un petit **potentiomètre** :
- place le robot sur la ligne
- ajuste jusqu’à obtenir un changement net entre **0** et **1** sur le Moniteur Série

---

## 🧪 Test rapide (Moniteur Série)
Le code affiche :
- `digitalRead(A0)` (gauche)
- `digitalRead(A1)` (droit)

Ouvre le **Moniteur Série à 9600 bauds** et vérifie que :
- sur la ligne : 0 (ou 1 selon capteur)
- hors ligne : l’autre état

---

## 🛠️ Notes sur le code fourni (petites corrections utiles)
Dans ton code, il y a des comparaisons qui peuvent prêter à confusion :

- `!analogRead(right)==0`  
- `!digitalRead(left)==0`

👉 Plus clair et plus sûr :
- `digitalRead(right) != 0`
- `digitalRead(left) != 0`

Et comme tes broches sont **A0/A1**, reste cohérent en **digitalRead** si tu utilises la sortie digitale du module.

---

## ✅ Conseils pour un robot plus stable
- Ajoute un **condensateur** près des moteurs (ex: 100nF sur chaque moteur)
- Utilise une **batterie moteurs** séparée
- Réduis `setSpeed()` si le robot dépasse la ligne
- Place les capteurs **proches du sol** (3–8 mm typiquement)

---

## 📁 Fichiers
- `line_follower.ino` → code Arduino
- `MODULE_LINE_FOLLOWER_ROBOT.md` → ce document

---

## 🧩 Évolutions possibles

| Amélioration | Pourquoi |
|------------|----------|
| 3 capteurs (gauche/centre/droit) | Meilleur suivi de ligne |
| PID | Suivi beaucoup plus fluide |
| Calibration automatique | Marche sur plus de surfaces |
| Lecture analogique | Détection plus fine |
