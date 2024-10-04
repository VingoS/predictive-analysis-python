import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados de emplacamento de cada mês
df_jul = pd.read_csv('data/emplacamentos_jul_2024.csv')
df_ago = pd.read_csv('data/emplacamentos_ago_2024.csv')
df_set = pd.read_csv('data/emplacamentos_set_2024.csv')

# Identificar a coluna de emplacamentos (segunda coluna em cada arquivo)
jul_column = df_jul.columns[1]  # Pega a segunda coluna que representa emplacamentos de julho
ago_column = df_ago.columns[1]  # Pega a segunda coluna que representa emplacamentos de agosto
set_column = df_set.columns[1]  # Pega a segunda coluna que representa emplacamentos de setembro

# Função para normalizar os dados (renomear a coluna do mês e adicionar a coluna de Mês)
def normalize_data(df, month_column, month_name):
    df = df.rename(columns={month_column: 'Emplacamentos'})  # Renomear a coluna do mês para 'Emplacamentos'
    df['Mês'] = month_name  # Adicionar a coluna do mês
    return df[['Modelo', 'Emplacamentos', 'Mês']]  # Usar 'Modelo', já que sabemos que é o nome correto

# Normalizar os dados para cada mês
df_jul = normalize_data(df_jul, jul_column, 'Julho')
df_ago = normalize_data(df_ago, ago_column, 'Agosto')
df_set = normalize_data(df_set, set_column, 'Setembro')

# Concatenar os três DataFrames em um único
df_total = pd.concat([df_jul, df_ago, df_set])

# Verificar os cinco veículos mais emplacados de cada mês
top5_jul = df_jul.nlargest(5, 'Emplacamentos')
top5_ago = df_ago.nlargest(5, 'Emplacamentos')
top5_set = df_set.nlargest(5, 'Emplacamentos')

print("Top 5 veículos emplacados em Julho:")
print(top5_jul)
print("\nTop 5 veículos emplacados em Agosto:")
print(top5_ago)
print("\nTop 5 veículos emplacados em Setembro:")
print(top5_set)

# Comparar os veículos mais vendidos entre os três meses
# Criar um gráfico para visualizar os dados
plt.figure(figsize=(10, 6))
sns.barplot(x='Modelo', y='Emplacamentos', hue='Mês', data=df_total[df_total['Modelo'].isin(top5_jul['Modelo']) | df_total['Modelo'].isin(top5_ago['Modelo']) | df_total['Modelo'].isin(top5_set['Modelo'])])
plt.title('Comparação dos Top 5 Veículos Mais Emplacados (Julho, Agosto e Setembro)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()