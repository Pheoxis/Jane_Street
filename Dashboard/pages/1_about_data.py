import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_extras.switch_page_button import switch_page
from io import BytesIO
import numpy as np

# Konfiguracja strony
st.set_page_config(
    page_title="Przegląd Danych",
    page_icon="📊",
    layout="wide",
)

# Niestandardowy CSS dla stylizacji
st.markdown("""
    <style>
        /* Ustawienia ogólne */
        body {
            background-color: #F5F5F5;
            color: #333333;
            font-family: 'sans serif';
        }
        /* Stylizacja tabeli danych */
        .dataframe {
            background-color: #FFFFFF;
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 20px;
        }
        /* Stylizacja przycisków */
        div.stButton > button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
        }
        div.stButton > button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# Tytuł i opis
st.title("📊 Przegląd Danych")
st.markdown("---")

# Funkcja do ładowania danych
@st.cache_data
def load_data(filepath):
    return pd.read_csv(filepath)

# Podgląd zbioru danych
st.subheader("Podgląd Zbioru Danych")
data = load_data(r'G:\JaneStreetReal\sampled_data_with_lags.csv')
st.dataframe(data, use_container_width=True)

st.markdown("""
**Kolumny w Zbiorze Danych:**
- **date_id** i **time_id**: Kolejne liczby całkowite zapewniające strukturę chronologiczną.
- **symbol_id**: Unikalny identyfikator instrumentów finansowych.
- **weight**: Waga używana w obliczeniach funkcji punktacji.
- **feature_{00...78}**: Zanonimizowane cechy danych rynkowych.
- **responder_{0...8}**: Zanonimizowane wartości odpowiedzi w zakresie od -5 do 5; **responder_6** jest zmienną docelową.
""")

# Metadane cech
st.subheader("Metadane Cech")
features_df = pd.read_csv(r'G:/JaneStreetReal/jane-street-real-time-market-data-forecasting/features.csv')
st.dataframe(features_df.head(), use_container_width=True)

tags_array_features = features_df.iloc[:, 1:].astype(int).values
features = features_df['feature'].values

# Compute the similarity matrix: number of matching tags between features
feature_matrix = np.dot(tags_array_features, tags_array_features.T)

# Streamlit app

shows_plot = st.checkbox("Pokaż macież dla features", value=False, key="feature_checkbox")
# Display the heatmap
if shows_plot:
    st.write("### Heatmap of Feature Similarities")
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(
        feature_matrix,
        annot=False,
        cmap="coolwarm",
        xticklabels=features,
        yticklabels=features,
        cbar=True,
        ax=ax,
    )
    ax.set_title("Feature Similarity Matrix")
    ax.set_xlabel("Features")
    ax.set_ylabel("Features")
    st.pyplot(fig)

st.markdown("Metadane dotyczące zanonimizowanych cech.")

# Metadane odpowiedzi
data = pd.read_csv(r'G:/JaneStreetReal/jane-street-real-time-market-data-forecasting/responders.csv')

# Display metadata
st.subheader("Metadane Odpowiedzi")
st.dataframe(data.head(), use_container_width=True)
st.markdown("Metadane dotyczące zanonimizowanych odpowiedzi.")

# Convert tag columns to a NumPy array for easy comparison
tags_array = data.iloc[:, 1:].astype(int).values
responders = data['responder'].values

# Compute a similarity matrix: number of matching tags between responders
responder_matrix = np.dot(tags_array, tags_array.T)
show_plot = st.checkbox("Pokaż macież dla responder", value=False, key="responder_checkbox")
# Display the heatmap
if show_plot:
    st.write("### Heatmap of Responder Similarities")
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.heatmap(responder_matrix, annot=True, cmap="viridis", xticklabels=responders, yticklabels=responders, cbar=True, ax=ax)
    ax.set_title("Responder Similarity Matrix")
    ax.set_xlabel("Responders")
    ax.set_ylabel("Responders")
    st.pyplot(fig)



# Przykładowy format zgłoszenia
st.subheader("Przykładowy Format Zgłoszenia")
sample_submission = load_data('G:/JaneStreetReal/jane-street-real-time-market-data-forecasting/sample_submission.csv')
st.dataframe(sample_submission.head(), use_container_width=True)

st.markdown("Ilustruje format, w jakim model powinien generować swoje przewidywania.")

# Przyciski nawigacyjne
col1, col2, col3 = st.columns([3, 7, 2])
with col1:
    if st.button("Przejdź do Wprowadzenia"):
        switch_page("introduction")
with col3:
    if st.button("Przejdź do Wykresu"):
        switch_page("charts")


