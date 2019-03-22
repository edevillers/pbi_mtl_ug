# Prolog - Auto Generated #
import os, matplotlib.pyplot, uuid, pandas
os.chdir(u'C:/Users/etien/PythonEditorWrapper_456bdbde-f275-401c-9872-6923c11096d0')
dataset = pandas.read_csv('input_df_00dd0cd9-85bc-4769-bcfa-a00f9df2b73f.csv')

matplotlib.pyplot.figure(figsize=(5.55555555555556,4.16666666666667))
matplotlib.pyplot.show = lambda args=None,kw=None: matplotlib.pyplot.savefig(str(uuid.uuid1()))
# Original Script. Please update your script content here and once completed copy below section back to the original editing window #
# Le code suivant, qui crée un dataframe et supprime les lignes dupliquées, est toujours exécuté et sert de préambule à votre script : 

# dataset = pandas.DataFrame(Acceleration, Aggression)
# dataset = dataset.drop_duplicates()

# Collez ou tapez votre code de script ici :
import seaborn as sns
sns.set(style="ticks")

sns.pairplot(dataset)
matplotlib.pyplot.show()

dataset.info()

# Epilog - Auto Generated #
os.chdir(u'C:/Users/etien/PythonEditorWrapper_456bdbde-f275-401c-9872-6923c11096d0')
