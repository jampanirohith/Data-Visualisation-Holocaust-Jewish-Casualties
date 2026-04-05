import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
data = {
    'Source': ['Arolsen Document', 'Raul Hilberg', 'USHMM Consensus', 'Wolfgang Benz'],
    'Deaths': [271301, 5100000, 6000000, 5750000],
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 7))
ax = sns.barplot(x='Source', y='Deaths', data=df, palette=['red', 'blue', 'blue', 'blue'])

plt.title('Holocaust Jewish Death Toll:\nEvidence-Based Studies vs Common Misconceptions', fontsize=13, pad=20)

plt.ylabel('Estimated Number of Jewish Victims', fontsize=12)
plt.xlabel('Source', fontsize=12)

plt.yticks([0, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000],
           ['0', '1000000', '2000000', '3000000', '4000000', '5000000', '6000000', '7000000'])

for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width()/2., height + 180000, 
            f'{int(height):,}', 
            ha='center', va='bottom', fontsize=11, fontweight='bold') 

plt.savefig('holocaust_death_toll_simple.png', dpi=300, bbox_inches='tight')
plt.show()

print("Graph saved as 'holocaust_death_toll_simple.png'")