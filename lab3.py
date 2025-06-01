import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='sepal length (cm)', y='sepal width (cm)', hue='species', palette='Set1', s=80, alpha=0.8)

plt.title('Зависимость длины и ширины чашелистика у разных видов ирисов', pad=20)
plt.xlabel('Длина чашелистика (см)', fontsize=12)
plt.ylabel('Ширина чашелистика (см)', fontsize=12)
plt.legend(title='Вид ириса', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()
