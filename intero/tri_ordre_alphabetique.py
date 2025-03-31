from pathlib import Path

# Obtenir le dossier où se trouve le script
dossier_script = Path(__file__).parent

# Définir le chemin du fichier
path = dossier_script / "text/ancien_message_trier.txt"
contenu = ""
# Vérifier si le fichier existe
if path.exists():
    print(f" Le fichier existe ")
    with path.open(mode='r', encoding='utf-8') as file:
        # Lire le contenu du fichier
        contenu = file.read()
else:
    print(" Le fichier n'existe pas. Vérifie le chemin.")

tableau = contenu.split()

tableau = sorted(tableau, key=lambda x: x.lower())  # Trier le tableau par ordre alphabétique

print(tableau)