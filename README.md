

> Status do projeto: Em desenvolvimento



```
Data Science

```

a74 = df_gols.drop_duplicates('partida_id', keep='first')
a74.to_csv('camp-bras-gols-a-74.csv', index=False)
#a74.sort_values(by='minuto', ascending=False, inplace=True) código não rodou