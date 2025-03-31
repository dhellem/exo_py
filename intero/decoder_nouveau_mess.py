from pathlib import Path
import re

mot_cle = {
    'abbey': 'a', 'amber': 'b', 'bliss': 'c', 'breeze': 'd', 'cactus': 'e', 
    'cloud': 'f', 'daisy': 'g', 'dawn': 'h', 'eagle': 'i', 'echo': 'j', 
    'falcon': 'k', 'feast': 'l', 'garden': 'm', 'glow': 'n', 'harmony': 'o', 
    'haven': 'p', 'ice': 'q', 'ivory': 'r', 'jade': 's', 'jazz': 't', 
    'koala': 'u', 'lagoon': 'v', 'luna': 'w', 'marvel': 'x', 'meadow': 'y', 
    'nebula': 'z', 'nest': '0', 'oasis': '1', 'ocean': '2', 'palm': '3', 
    'pearl': '4', 'quartz': '5', 'quest': '6', 'rain': '7', 'river': '8', 
    'serene': '9'
}

# Obtenir le dossier où se trouve le script
dossier_script = Path(__file__).parent

# Définir le chemin du fichier
path = dossier_script / "text/nouveau_message.txt"
contenu = ""
# Vérifier si le fichier existe
if path.exists():
    print(f"Le fichier existe : {path.resolve()}")
    with path.open(mode='r', encoding='utf-8') as file:
        contenu = file.read().lower() 
else:
    print("Le fichier n'existe pas. Vérifie le chemin.")

# Nettoyer le contenu du fichier
contenu_nettoye = re.sub(r"[^\w\s]", "", contenu)

words = contenu_nettoye.split()
decoded_message = ''.join([mot_cle[word] for word in words if word in mot_cle])

# Afficher le message décodé
print("Message décodé :", decoded_message)
