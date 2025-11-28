import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(layout='centered')

st.markdown("""
    <style>
    div.stButton > button {
        height: 80px;  /* Tall buttons for fat fingers */
        font-weight: bold;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

st.title('Contar chegadas')

if 'df' not in st.session_state:
    df = pd.DataFrame({
        'Tempo_chegada': []
    })
    st.session_state.df = df

with st.container(border=True):
    for i in range(1, 11):
        st.button(
            label=f'+{i}',
            width='stretch',
            type='primary',
            key=f'b{i}'
        )

for i in range(1, 11):
    if st.session_state[f'b{i}']:
        new_row = pd.DataFrame({'Tempo_chegada': i*[(datetime.now() - timedelta(hours=3)).strftime("%H:%M:%S")]})
        st.session_state.df = pd.concat([st.session_state.df, new_row])
        st.toast(
            body='salvo!',
            duration=1,
            icon='✅'
        )

csv = st.session_state.df.to_csv(index=False).encode('utf-8')
st.download_button(
    "📥Baixar",
    csv,
    f"contagem.csv",
    "text/csv",
    use_container_width=True
)

        
        

    