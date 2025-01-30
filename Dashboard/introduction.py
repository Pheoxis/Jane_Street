import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Set page configuration
st.set_page_config(
    page_title="Wprowadzenie i opis projektu",
    page_icon="📘",
    layout="wide",
)

# Custom CSS for styling
st.markdown("""
    <style>
        /* General settings */
        body {
            background-color: #F5F5F5;
            color: #333333;
            font-family: 'sans serif';
        }
        /* Title styling */
        .stApp > header {
            background-color: #4CAF50;
            padding: 10px;
            border-radius: 10px;
        }
        .stApp > header h1 {
            color: white;
        }
        /* Button styling */
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

# Title and subtitle
st.title("📘Wprowadzenie i opis projektu")
st.subheader("Nasze założenia i przebieg projektu")

# Project description
st.markdown("""
**Jane Street Real-Time Market Data Forecasting**

**Temat**: Prognozowanie w czasie rzeczywistym danych rynkowych przy użyciu algorytmów uczenia maszynowego  
**Dziedzina**: Finanse  
**Opis**: Projekt opiera się na konkursie Kaggle "Jane Street Real-Time Market Data Forecasting", gdzie celem jest opracowanie modelu przewidującego odpowiedź rynku na podstawie historycznych danych finansowych. Analizowane dane obejmują zmienne czasowe, takie jak symbol, czas i zmienne finansowe z dużą liczbą braków danych i niestacjonarności.
""")

st.markdown("---")

# Data acquisition method
st.subheader("Metoda Pozyskiwania Danych")
st.markdown("""
Dane do projektu zostały pozyskane z oficjalnego zestawu udostępnionego przez organizatorów konkursu Kaggle, zawierającego pliki w formacie .parquet. Dane te obejmują historyczne zmienne finansowe, odpowiedzi rynkowe oraz zmienne pomocnicze, takie jak wagi i identyfikatory symboli.

W projekcie wykorzystano również biblioteki Polars oraz Pandas do wstępnej analizy i przetwarzania danych.

**Etapy pozyskiwania danych:**
1. Pobranie danych z platformy Kaggle.
2. Wczytanie danych do analizy przy użyciu narzędzi Python (Polars, Pandas).
3. Przygotowanie danych do modelowania poprzez stworzenie lagów czasowych oraz imputację braków danych.
""")

st.markdown("---")

# Research objectives
st.subheader("Cel Badania")
st.markdown("""
**Główny cel**: Stworzenie modelu uczenia maszynowego zdolnego do przewidywania odpowiedzi rynkowej (**responder_6**) w czasie rzeczywistym na podstawie zmiennych finansowych.

**Cele szczegółowe:**
- Analiza struktury danych i identyfikacja kluczowych cech.
- Stworzenie zaawansowanego modelu predykcyjnego (XGBoost, LightGBM, Neural Networks).
- Zastosowanie metody ensemble w celu poprawy wyników modelu.
- Ocena wydajności modelu przy użyciu metryk takich jak Zero-Mean R² i analiza wyników.
""")

st.markdown("---")

# Data analysis and dashboard creation
st.subheader("Analiza Danych i Tworzenie Dashboardu")
st.markdown("""
**Złożoność Zbioru Danych**

Dane są wielowymiarowe i niestacjonarne, co wymaga zastosowania zaawansowanych technik analizy szeregów czasowych. Szczególnym wyzwaniem są:
- Braki danych w wielu zmiennych.
- Niestabilne zmienne czasowe i symboliczne.
- Dynamika wprowadzania nowych symboli i cech w czasie trwania danych.

**Dostosowanie Metod Analizy**

Metody analizy zostały dostosowane do specyficznych wymagań projektu:
1. **Przetwarzanie Danych**: 
   - Stworzenie lagów czasowych w celu wykorzystania informacji historycznych.
   - Normalizacja/transformacja zmiennych w oparciu o cechy symboliczne i czasowe.
2. **Modelowanie**: 
   - Użycie architektur takich jak Neural Networks z mechanizmami uwagi (attention mechanisms), Denoising Autoencoder.
   - Testowanie modeli LightGBM i XGBoost dla porównania wyników.
3. **Walidacja**: 
   - Zastosowanie Cross-Validation z uwzględnieniem porządku czasowego danych.

**Wizualizacja**

Projekt zakłada stworzenie interaktywnego dashboardu przedstawiającego:
- Rozkład zmiennych finansowych w czasie.
- Wyniki predykcji dla wybranych modeli.
- Wizualizacje znaczenia cech (SHAP).
""")

st.markdown("---")

# Results and next steps
st.subheader("Rezultaty i Następne Kroki")
st.markdown("""
Na obecnym etapie projektu przygotowano dane i przetestowano wstępne modele predykcyjne. Kolejne kroki obejmują:
- Optymalizację hiperparametrów przy użyciu bibliotek takich jak Optuna.
- Zastosowanie metod ensemble (stacking, blending).
- Integrację wyników z dashboardem i przygotowanie finalnej prezentacji.
""")

st.markdown("---")

# Navigation button
col1, col2, col3 = st.columns([2, 7, 3])
with col3:
    if st.button("Przejdź do opisu danych"):
        switch_page("about data")
