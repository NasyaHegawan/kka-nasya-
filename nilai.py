import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('nilai_siswa.csv')
print(data.info())
print(data.head())
print(data.describe())

print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])

matematika = data[data['Matpel'] == 'Matematika']
print(matematika)
bahasaIndonesia = data[data['Matpel'] == 'Bahasa Indonesia']
print(bahasaIndonesia)
bahasaInggris = data[data['Matpel'] == 'Bahasa Inggris']
print(bahasaInggris)
produktif = data[data['Matpel'] == 'Produktif']
print(produktif)

data.groupby('Matpel')['Nilai'].agg(['max','min'])

rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar')
plt.title('Rata-Rata Nilai per Matpel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

sns.boxplot(x='Matpel', y='Nilai', data=data)
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.show()