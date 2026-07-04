# NOTAS DE ESTUDOS 

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.header('ANALISE DE NOTAS - PREVENDO')

estudos = pd.DataFrame({
'notas':[1,2,4,6,8,10,2,8],
'horas':[2,4,5,7,9,10,1,6]
})

st.line_chart(estudos, x = 'horas', y= 'notas')
modelo_escola = LinearRegression() 
modelo_escola.fit(estudos[['horas']], estudos['notas'])

h_estudo = st.slider('horas de estudos', 0,12,5)
# h_estudo2 = st.text_input('horas de estudos', 0,12,5)
nota_final = modelo_escola.predict([[h_estudo]])
print(nota_final)

st.metric(f'sua nota seria' ,f'{min(nota_final[0], 10.0):.1f}')


#---------------------------------------------------------------------
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

st.header("Previsão de Vendas")

# Dados: [Investimento em Marketing] -> Faturamento
dados_vendas = pd.DataFrame({
    'investimento': [100, 200, 300, 400, 500, 600],
    'faturamento': [1200, 2500, 3200, 4800, 5100, 6300]
})


st.bar_chart(dados_vendas, x = 'investimento', y = 'faturamento')
modelo_investimento = LinearRegression()
modelo_investimento.fit(dados_vendas[['investimento']], dados_vendas[['faturamento']])

t_investido = st.slider('Total investido' ,0,600,500)
faturamento_final = modelo_investimento.predict([[t_investido]])
print(faturamento_final)
st.metric(f'Seu faturamento seria de', f' {min(faturamento_final[0], 6300.0)}')

# objetivo: previsão de FATURAMENTO baseado nos investimentos

#------------------------------------------------------------------------------

import streamlit as st

import pandas as pd

from sklearn.linear_model import LinearRegression

import numpy as np



st.header('ANALISE DE NOTAS - PREVENDO')




d = pd.read_csv('teste.csv')



# print(d)



estudos = pd.DataFrame({

'vendas': d['vendas'],

'temperatura':d['temperatura']

})



print(estudos)



st.bar_chart(estudos, x = 'temperatura', y= 'vendas')

modelo_escola = LinearRegression() 

modelo_escola.fit(estudos[['temperatura']], estudos['vendas'])



# h_estudo = st.slider('horas de estudos', 0,12,5)

temperatura = st.number_input('Temperarura', value = 0)

# n  =  np.array(temperatura)

nota_final = modelo_escola.predict([[temperatura]])

st.write(nota_final)



st.metric(f'sua Venda' ,f'{min(nota_final[0], 1000.0):.1f}')