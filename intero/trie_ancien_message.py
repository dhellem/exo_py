from pathlib import Path

# Obtenir le dossier où se trouve le script
dossier_script = Path(__file__).parent

# Définir le chemin du fichier
path = dossier_script / "text/ancien_message.txt"
contenu = ""
# Vérifier si le fichier existe
if path.exists():
    print(f" Le fichier existe : {path.resolve()}")
    with path.open(mode='r', encoding='utf-8') as file:
    
        contenu = file.read()
else:
    print(" Le fichier n'existe pas. Vérifie le chemin.")

mot_a_supprimer ={'rhubarb', 'quince', 'watermelon', 'ximenia', 'nut', 'zucchini',
'blackberry', 'vine', 'cranberry',
 'durian', 'papaya', 'huckleberry', 'jujube', 'xerophyte', 'elderberry',
'tangerine', 'satsuma','kiwi', 'victoria', 'lime', 'saffron', 'ugni', 'rasp', 'kale', 'avocado',
'xigua', 'ugly','waxberry', 'eggplant', 'honeydew', 'lychee', 'dragonfruit', 'zinfandel',
'raspberry', 'guava','indian', 'fig', 'orange', 'yuzu', 'date', 'tamarind', 'yam', 'strawberry',
'hawthorn', 'apple','nectarine', 'cherry', 'fennel', 'elderflower', 'quandary', 'blueberry',
'quandong', 'zest','wildberry', 'yellow', 'apricot', 'onion', 'cantaloupe', 'nutmeg',
'persimmon', 'mandarin', 'olive','lemon', 'tamarillo', 'ugli', 'mango', 'grape', 'banana', 'jackfruit',
'gooseberry', 'vanilla','mulberry', 'kumquat', 'peach', 'feijoa'}
contenu = contenu.lower()
tableau = contenu.split()
tableau = [mot for mot in tableau if mot not in mot_a_supprimer]
contenu = ' '.join(tableau)

print(contenu)