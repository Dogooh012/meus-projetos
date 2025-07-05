import streamlit as st

st.title('cadastro de clientes')

nome = st.text_input("digite o nome do cliente")
endereco = st.text_input('digite o seu endereço')
dt_nasc = st.date_input('escolha a data de seu nascimento')
tipo_cliente = st.selectbox('tipo de cliente',
                             ["pessoa física", "pessoa jurídica"])

cadastrar = st.button('cadastre-se')

if cadastrar:
    with open('clientes.csv', "a", encoding="utf8") as arquivo:
        arquivo.write(f"{nome},{endereco},{dt_nasc},{tipo_cliente}\n")
        st.success('cliente cadastrado com sucesso !')

    # streamlit run .\app.py
