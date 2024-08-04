import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dt
import mplfinance as mpl

# Lê a tabela e a salva no DataFrame df. A coluna Date é usada como o índice de cada linha.
df = pd.read_csv('IXIC.csv', parse_dates = ['Date'])
df.set_index('Date', inplace = True)

# Calcula as médias móveis e os resultados ao fim do DataFrame
df['media_movel3'] = df['Close'].rolling(3).mean()
df['media_movel6'] = df['Close'].rolling(6).mean()
df['media_movel9'] = df['Close'].rolling(9).mean()

# A função "sublots" retorna uma variável do tipo "Figure" e uma do tipo "Axes" do Matplotlib
# A variável figura não será utilizada para nada, mas eixo é a que efetivamente representa o gráfico com que vamos trabalhar
figura, eixo = plt.subplots()
for indice, linha in df.iterrows(): # iterrows() do Pandas evidentemente retorna os índices e as linhas do DataFrame
    if linha['Close'] >= linha['Open']:
        cor = 'green'
    else:
        cor = 'red'
    # Desenha uma linha vertical que vai de linha['Low'] até linha['High'], representando os pavios
    eixo.vlines(indice, linha['Low'], linha['High'], color = 'black', linewidth = 0.9, zorder = 2)
    # Desenha uma barra de altura "linha['Close'] - linha['Open']" deslocada do eixo X pelo valor de linha['Open'], representando as velas
    eixo.bar(indice, linha['Close'] - linha['Open'], bottom = linha['Open'], color = cor, zorder = 2)

# Insere os gráficos das três médias móveis
eixo.plot(df.index, df['media_movel3'], label = "Média móvel de 3 dias", color = 'blue', linewidth = 1.5, zorder = 3)
eixo.plot(df.index, df['media_movel6'], label = "Média móvel de 6 dias", color = 'orange', linewidth = 1.5, zorder = 3)
eixo.plot(df.index, df['media_movel9'], label = "Média móvel de 9 dias", color = 'lawngreen', linewidth = 1.5, zorder = 3)

# Configura os labels do eixo X, que representam os dias
eixo.xaxis.set_major_locator(dt.WeekdayLocator(dt.MONDAY))
eixo.xaxis.set_minor_locator(dt.DayLocator())
eixo.xaxis.set_major_formatter(dt.DateFormatter('%b %d'))
# Se essa configuração não é feita, os labels serão representados pelas strings tal qual estão no DataFrame, o que os torna ilegíveis

plt.title("Valores de fechamento do ativo IXIC para o mês de abril de 2024")
plt.xlabel("Dia")
plt.ylabel("Preço ($)")
plt.grid(zorder = 1)
plt.legend()
plt.savefig('grafico.png') # Salva o gráfico no diretório atual
plt.show()

# O valor "yahoo" do parâmetro style é usado para dar as cores verde e vermelho para o gráfico
mpl.plot(df, type = 'candle', ylabel = "Preço ($)", style = 'yahoo', mav = (3,6,9))
