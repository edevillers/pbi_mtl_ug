## Récupérer des données d'un Google Spreadsheet via authentification

Cette méthode vous permet de récupérer des données d'un Google Spreadsheet et des les importer dans un rapport Power Bi, **sans devoir rendre votre Google Spreadsheet public**. 

1. Il faut d'abord faire une petite installation pour utiliser gspread, une librairie pour parler à Google Spreadsheets à partir de Python. [Suivre les instructions ici](https://gspread.readthedocs.io/en/latest/oauth2.html). 

2. Puis après ce petit bout de code dans votre vous permettra de récupérer le data : 

```
# le texte sur une ligne après un dièse (#) est un commentaire, et l'interpréteur n'en tient pas compte


import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name("METTRE LE PATH VERS VOTRE FICHIER JSON ICI", scope)
# par exemple : 
# credentials = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\etien\\MeetUp Bi\\Power PyBi_\\pympPowerBi-72417e0c908e.json", scope)

gc = gspread.authorize(credentials)

# on va aller chercher la première feuille de notre spreadsheet
sheet1 = gc.open_by_key("METTRE LA CLÉ DE VOTRE SPREADSHEET ICI").sheet1
# par exemple : 
# sheet1 = gc.open_by_key("1JzfY2XkCGlMD9ot7HGLQz81adgnME8XWOo3GmLcfK2Y").sheet1

# get_all_values retourne la liste de rangées.
rows = sheet1.get_all_values()
# print(rows)

# Convertir en DataFrame de Pandas et stocker dans la variable df
df = pd.DataFrame.from_records(rows)
```

Préférablement aller chercher le code directement dans le fichier import_df.py
