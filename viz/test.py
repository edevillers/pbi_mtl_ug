# Prolog - Auto Generated #
import os, matplotlib.pyplot, uuid, pandas
os.chdir(u'C:/Users/etien/PythonEditorWrapper_59f4ffa4-39cf-4104-b466-651b62890487')
dataset = pandas.read_csv('input_df_2cb88e38-69e1-4039-a5de-22c1250b663c.csv')

matplotlib.pyplot.figure(figsize=(5.55555555555556,4.16666666666667))
matplotlib.pyplot.show = lambda args=None,kw=None: matplotlib.pyplot.savefig(str(uuid.uuid1()))
# Original Script. Please update your script content here and once completed copy below section back to the original editing window #
# Le code suivant, qui crée un dataframe et supprime les lignes dupliquées, est toujours exécuté et sert de préambule à votre script : 

# dataset = pandas.DataFrame(Acceleration, Age)
# dataset = dataset.drop_duplicates()

# Collez ou tapez votre code de script ici :
import seaborn as sns

print(dataset)

def plot_density_hist(dataset, cols, bins = 10, hist = False):
    for col in cols:
        sns.set_style("whitegrid")
        sns.distplot(dataset[col], bins = bins, rug=True, hist = hist)
        plt.title('Histogram of ' + col) # Give the plot a main title
        plt.xlabel(col) # Set text for the x axis
        plt.ylabel('Number of autos')# Set text for y axis
        plt.show()
        
plot_density_hist(dataset, ['Age', 'Acceleration'])        

# Epilog - Auto Generated #
os.chdir(u'C:/Users/etien/PythonEditorWrapper_59f4ffa4-39cf-4104-b466-651b62890487')
