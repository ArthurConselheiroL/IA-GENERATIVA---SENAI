import streamlit as st 

import pandas as pd 

st.title("Calculadora")

n1 = st.number_input("Número 1:",value = 0)
n2 = st.number_input("Número 2:", value = 0)

soma, sub, div, mult = st.columns(4)

if soma.button("Soma"):
    soma = n1 + n2 
    st.title(soma)
elif sub.button("Subtração"):
    sub = n1 - n2
    st.title(sub)
elif div.button("Divisão"):
    divisao = n1/n2
    st.title(divisao)    
elif mult.button("Multiplicação"):
    multiplicacao = n1 * n2 
    st.title(multiplicacao)



st.title("Desafio 1: O Cartão de Visitas Digital (Exibição de Texto)")

st.header("Cartão Visa")

st.text("Texto")

st.markdown("Isso é um parágrafo de comentário")

#----------------------------------------------------------------------

st.title(" Desafio 2: Formulário de Cadastro de Usuário (Entrada de Dados)")

nome =  st.text_input("Digite um nome: ")
idade = st.number_input("Digite sua idade", value = 0)
aceitou = st.checkbox("Aceitar os termos")

if st.button("Enviar"):
    if  aceitou == True:
        st.success(f"Nome: {nome}, Idade: {idade}")
    else: 
        st.header("Aceite os termos")

#---------------------------------------------------------------------

st.title(" Desafio 3: O Seletor de Cursos (Componentes de Escolha)")

curso = st.selectbox("Escolha um curso!",("Selecione", "Python", "Web", "Gravity", "Gestão"))
tecnologias = st.multiselect("Escolha as tecnologias",("HTML", "CSS", "SQL", "GIT"))
if curso:
    if tecnologias:
        st.success(f"{curso},  {tecnologias}")
    else: 
        st.write("Escolha")

#----------------------------------------------------------------------

st.title(" Desafio 4: Visualizador de Planilhas Interativo (Exibição de Dados)")


dados = {}