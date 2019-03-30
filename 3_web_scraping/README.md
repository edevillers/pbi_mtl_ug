## Utiliser des librairies python pour automatiser des actions dans le navigateur web

Power Bi dispose déjà d'une très bonne intégration pour récupérer des données sur le web, dans des tables html, et avec de la détection automatique de sélecteurs. Avec Python on peut aller à la coche supérieure, en envoyant également des keystrokes et même des mouvements de souris à un navigateurs. **Si vous êtes capables de le faire avec votre clavier/souris, c'est automatisable !**

1. Installation préalable de selenium webdriver `pip install -U selenium`, qui nous permettra de contrôler le navigateur. 

2. Faut aussi avoir un petit truc qui s'appelle geckodriver. Suivre la réponse à cette [question](https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path). Assurez-vous de prendre l'exécutable qui correspond à votre architecture (32 vs 64 bits). 

3. Puis mettre le script dans vingt48.py dans la query python. 

### Petite roche sur le chargement pour prévisualisation

Lorsqu'on procède de la sorte, PowerBi va effectuer l'automatisation à chaque fois qu'il tente de donner un aperçu du data... Ça peut rapidement devenir embêtant. 

Pour certaines applications plus complexes, une meilleure solution serait de découpler l'automatisation de Power Bi en produisant une source aisément comestible pour PowerBi (csv, json, SQL server)
