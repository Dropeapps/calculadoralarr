import streamlit as st
st.title('Calculadora de Peso')
n1=st.number_input('Peso: ')
n2=st.number_input('Qtd Solicitada: ')
n3=(n1*0.10+n1)*n2
st.write(f'O peso total é de {n3:.1f} ')

st.title('Calculadora de Horas')
n1 = st.number_input("Quantidade solicitada: ")
n2 = st.number_input("Peças por hora: ")
n3 = n1/n2
st.write(f'A máquina rodará durante {n3:.2f} horas')
