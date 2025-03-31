from pathlib import Path

# Obtenir le dossier où se trouve le script
dossier_script = Path(__file__).parent

# Définir le chemin du fichier
path = dossier_script / "text/ancien_message_ordre_alphab.txt"
contenu = ""
# Vérifier si le fichier existe
if path.exists():
    print(f" Le fichier existe ")
    with path.open(mode='r', encoding='utf-8') as file:
        
        contenu = file.read()
else:
    print(" Le fichier n'existe pas. Vérifie le chemin.")

cle = 'a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9'
tab_cle = cle.split()
print(len(tab_cle))
tableau = contenu.split()
print(len(tableau))

mots_et_cle = {}

for i, mot in enumerate(tableau):
    if i < len(tab_cle):
        mots_et_cle[mot] = tab_cle[i]
    else:
        mots_et_cle[mot] = tab_cle[i % len(tab_cle)]

# Afficher les mots et leurs clés attribuées
for mot, cle_attribuee in mots_et_cle.items():
    print(f"{mot + cle_attribuee}")

