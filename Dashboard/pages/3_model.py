
import streamlit as st 
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
from pathlib import Path

st.set_page_config(
    page_title="Modelowanie",
    page_icon="📊",
    layout="wide",
)

BASE_DIR = Path(__file__).resolve().parent
DASHBOARD_DIR = BASE_DIR.parent

st.markdown("""
    <style>
        /* General settings */
        body {
            background-color: #F5F5F5;
            color: #333333;
            font-family: 'sans serif';
        }
        /* Dataframe styling */
        .dataframe {
            background-color: #FFFFFF;
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 20px;
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

        /* Center image styling */
        .centered-image {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Modelowanie")
st.markdown("---")

st.subheader("Analiza modelu")

image = Image.open(DASHBOARD_DIR/'imiges/cechySHAP.png')
st.image(image, width=500, use_container_width=False)

st.markdown('''
            Wykres przedstawia 20 najważniejszych cech modelu według wartości SHAP, co oznacza ich wpływ na przewidywanie 'responder_6'. 

Oś Y – zawiera nazwy cech, w tym 79 standardowych funkcji (feature_00 do feature_78) oraz 9 historycznych (responder_0_lag_1 do responder_8_lag_1).
Oś X – reprezentuje wartości SHAP, które wskazują, jak mocno dana cecha wpływa na predykcję modelu. Im wyższa wartość, tym większy wpływ cechy na wynik.
            ''')

st.markdown("---")
image = Image.open(DASHBOARD_DIR/'imiges/Rozkład.png')
st.image(image, width=500, use_container_width=False)

st.markdown('''
            Wykres przedstawia rozkład wag w modelu zespołowym, składającym się z trzech modeli LightGBM (LGB) i dwóch modeli XGBoost (XGB). Oś pionowa pokazuje nazwy użytych modeli, a oś pozioma reprezentuje ich znormalizowany wkład wagowy w końcową predykcję.

Wagi te odzwierciedlają znaczenie poszczególnych modeli w ostatecznym wyniku ensemble – im wyższa wartość, tym większy wpływ danego modelu na wynik. Wszystkie wartości zostały znormalizowane tak, aby ich suma wynosiła 1, co pozwala lepiej porównać ich względne znaczenie.

Można zauważyć, że niektóre modele mają większy udział niż inne, co oznacza, że ich predykcje są bardziej istotne dla końcowego wyniku. Jeśli któryś z modeli miałby bardzo niską wagę, oznaczałoby to, że jego wpływ na finalną decyzję jest marginalny.
            ''')
st.markdown("---")

st.subheader('''
             Weighted Ensemble – Podsumowanie:

R² = 0.264 – najlepszy wynik.  
Bayesowska optymalizacja (Optuna):  
Indywidualne hiperparametry dla każdego modelu (LightGBM & XGBoost).  
Dynamiczny dobór wag:  
Modele lepiej dopasowane otrzymują wyższe wagi.  
Imputacja:  
Strategia "constant" z wartością 9999.  
Ray Tune:  
Wybrany ze względu na ograniczenia AutoGluon i PyCaret przy obsłudze Dask DataFrame.
             ''')

st.markdown("---")

st.markdown('''
    **Modele LightGBM**:
W trenowanych trzech modelach LightGBM dobrano między innymi następujące hiperparametry:

Learning rate: Wartości oscylowały wokół 0.012–0.059, co wpływa na tempo uczenia się modelu.
Liczba liści (num_leaves): Ustalono wartości od 36 do 90, co określa złożoność drzewa i pozwala na uchwycenie niuansów w danych.
Feature fraction: Parametr odpowiadający za losowe podpróbkowanie cech (zakres około 0.825–0.976) zapewnia element losowości, redukując ryzyko przeuczenia.
Extra trees: W jednym z modeli włączono dodatkową losowość (extra trees = True), co może zwiększyć różnorodność predykcji.
Współczynniki wagowe dla tych modeli (alpha_lgb) wynoszą odpowiednio około 2.26, 2.68 i 2.77, co oznacza, że ich predykcje mają dominujący wpływ przy łączeniu wyników.

**Modele XGBoost**:
Wśród dwóch trenowanych modeli XGBoost zastosowano m.in. następujące ustawienia:

Learning rate: Wartość około 0.020 dla pierwszego modelu i znacznie mniejsza (około 0.0012) dla drugiego, co sugeruje większą ostrożność w aktualizacji parametrów przy jednym z modeli.
Maksymalna głębokość drzewa (max_depth): Wybrano głębokość równą 6 dla pierwszego modelu i 14 dla drugiego, co wpływa na zdolność modelu do wychwytywania bardziej złożonych zależności.
Subsample oraz colsample_bytree: Parametry te (odpowiednio około 0.823–0.864 oraz wartość równomiernie ustawiona na 1.0) sterują losowym wyborem próbek i cech przy budowie drzew, co poprawia generalizację modelu.
Współczynniki wagowe dla modeli XGBoost (alpha_xgb) to około 1.55 oraz 0.35, wskazujące, że predykcje pierwszego modelu XGBoost są ważniejsze przy ostatecznym łączeniu wyników.
''')
# Przyciski nawigacyjne
col1, col2, col3 = st.columns([3, 7, 2])
with col1:
    if st.button("Wróć do Wykresu"):
        switch_page("charts")

