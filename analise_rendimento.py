import matplotlib.pyplot as plt

# Dados extraídos da Tabela 2 do Relatório
grupos = ['A1 (1:1)', 'A2 (1:1)', 'B1 (2:1)', 'B2 (2:1)']
rendimentos = [92.34, 94.16, 94.10, 94.50]
cores = ['#1f77b4', '#1f77b4', '#ff7f0e', '#ff7f0e'] # Azul para A (Rígida), Laranja para B (Flexível)

# Criando o gráfico de barras
plt.figure(figsize=(8, 5))
barras = plt.bar(grupos, rendimentos, color=cores)

# Adicionando linha de meta (100%)
plt.axhline(y=100, color='r', linestyle='--', label='Rendimento Teórico (100%)')

# Ajustes do gráfico
plt.ylim(80, 105) # Focando a escala para ver a diferença
plt.ylabel('Rendimento (%)')
plt.title('Eficiência da Reação de Polimerização do PU por Grupo')
plt.legend(['Teórico', 'Real obtido'])

# Adicionando os valores em cima das barras
for barra in barras:
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2., altura,
             f'{altura}%',
             ha='center', va='bottom')

# Salvando o gráfico
plt.savefig('grafico_rendimentos.png')
print("Gráfico gerado com sucesso!")
