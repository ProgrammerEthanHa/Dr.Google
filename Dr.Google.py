import streamlit as st
import pandas as pd
import altair as alt

st.header("Doktor Google, wie schlimm ist es?")
st.subheader("Anteil der Befragten (16 bis 74 Jahre), die sich im Internet über ihre Gesundheit informiert haben (in%)")

source = pd.DataFrame({
        'Anteil(%)': [80, 75, 69, 66, 60, 56, 53, 54],
        'Länder': ['Finnland', 'Dänemark', 'Spanien', 'Irland', 'Österreich', 'Frankreich', 'Italien', 'Deutschland']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Länder:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    EU-Länder; 2021
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle:  Eurostat")