## Anonymiser de l'information confidentielle en conservant l'unicité à travers une fonction de hachage

On pourrait imaginer un cas où le champ de votre modèle sur lequel vous effectuez une jointure entre une table de dimension et une table de faits est une information sensible (email, NAS, NAM, etc.)

Avec Python et la librairie standard *hashlib* on peut encrypter le champ sensible, et continuer de l'utiliser dans  notre modèle qui serait publié dans le service.  

Dans cet exemple, on bâtit sur ce qui a été fait précédemment dans l'exemple 1, en transformant la colonne email en unique_id à travers la fonction md5 de la librairie hlib. 

Voici le snippet à insérer dans une étape de votre PowerQuery : 
```
# 'dataset' contient les données d'entrée pour ce script
import hashlib

def encrypt(colonne):
    colonne_utf8 = colonne.encode('utf-8')
    colonne_hash = hashlib.md5(colonne_utf8).hexdigest()
    return colonne_hash

dataset['unique_id'] = dataset['Email'].apply(encrypt)
```

L'exemple est également visible si vous ouvrez le .pbix