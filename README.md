

> Status do projeto: Em desenvolvimento



```
Data Science

```

a74 = df_gols.drop_duplicates('partida_id', keep='first')
a74.to_csv('camp-bras-gols-a-74.csv', index=False)
#a74.sort_values(by='minuto', ascending=False, inplace=True) código não rodou
# Ajustar a conversão para lidar com valores decimais e outros possíveis erros
def converter_minuto_corrigido(valor):
    valor = str(valor).strip()  # Remover espaços extras
    if "+" in valor:
        base, extra = valor.split("+")
        return int(base) + int(extra)
    try:
        return int(float(valor))  # Converter corretamente valores como '59.0' para inteiros
    except ValueError:
        return None  # Retorna None se não for possível converter

# Aplicar a conversão corrigida
df_clean["minuto"] = df_clean["minuto"].apply(converter_minuto_corrigido)

# Remover valores inválidos (caso tenham ficado como None)
df_clean = df_clean.dropna(subset=["minuto"])

# Filtrar os gols marcados a partir do minuto 75
df_gols_corrigidos = df_clean[df_clean["minuto"] >= 75]

# Contagem de gols por minuto
gols_por_minuto = df_gols_corrigidos["minuto"].value_counts().sort_index()

# Criar o gráfico corrigido
plt.figure(figsize=(10,5))
plt.bar(gols_por_minuto.index, gols_por_minuto.values, color='blue', alpha=0.7)
plt.xlabel("Minuto do Jogo")
plt.ylabel("Quantidade de Gols")
plt.title("Distribuição dos Gols Marcados do Minuto 75 até o Último Minuto")
plt.xticks(range(75, max(gols_por_minuto.index) + 1, 2))  # Eixo X a cada 2 minutos
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.show()
