# Jane Street Real-Time Market Data Forecasting 

## Temat: Prognozowanie w czasie rzeczywistym danych rynkowych przy użyciu algorytmów uczenia maszynowego  
**Dziedzina:** Finanse  
**Opis:** Projekt opiera się na konkursie Kaggle "Jane Street Real-Time Market Data Forecasting", gdzie celem jest opracowanie modelu przewidującego odpowiedź rynku na podstawie historycznych danych finansowych. Analizowane dane obejmują zmienne czasowe, takie jak symbol, czas i zmienne finansowe z dużą liczbą braków danych i niestacjonarności.  

## Metoda Pozyskiwania Danych  
Dane do projektu zostały pozyskane z oficjalnego zestawu udostępnionego przez organizatorów konkursu Kaggle, zawierającego pliki w formacie .parquet. Dane te obejmują historyczne zmienne finansowe, odpowiedzi rynkowe oraz zmienne pomocnicze, takie jak wagi i identyfikatory symboli. [Link do Strony z której można pobrać](https://www.kaggle.com/competitions/jane-street-real-time-market-data-forecasting/data?select=responders.csv)  

W projekcie wykorzystano również biblioteki **Polars** oraz **Pandas** do wstępnej analizy i przetwarzania danych.  

### Etapy pozyskiwania danych:  
1. Pobranie danych z platformy Kaggle.  
2. Wczytanie danych do analizy przy użyciu narzędzi Python 3.10+ (Polars, Pandas).  
3. Przygotowanie danych do modelowania poprzez stworzenie lagów czasowych oraz imputację braków danych.  

## Cel Badania  
**Główny cel:** Stworzenie modelu uczenia maszynowego zdolnego do przewidywania odpowiedzi rynkowej (*responder_6*) w czasie rzeczywistym na podstawie zmiennych finansowych.  

### Cele szczegółowe:  
- Analiza struktury danych i identyfikacja kluczowych cech.  
- Stworzenie zaawansowanego modelu predykcyjnego (**XGBoost**, **LightGBM**, **Neural Networks**).  
- Zastosowanie metody **ensemble** w celu poprawy wyników modelu.  
- Optymalizacja hiperparametrów przy użyciu **Ray Tune** i **ASHAScheduler**.  
- Ocena wydajności modelu przy użyciu metryk takich jak **Zero-Mean R²** i analiza wyników.  

## Analiza Danych i Tworzenie Dashboardu  

### Złożoność Zbioru Danych  
Dane są wielowymiarowe i niestacjonarne, co wymaga zastosowania zaawansowanych technik analizy szeregów czasowych. Szczególnym wyzwaniem są:  
- Braki danych w wielu zmiennych.  
- Niestabilne zmienne czasowe i symboliczne.  
- Dynamika wprowadzania nowych symboli i cech w czasie trwania danych.  

### Dostosowanie Metod Analizy  
#### Przetwarzanie Danych:  
- Stworzenie lagów czasowych w celu wykorzystania informacji historycznych.  
- Normalizacja/transformacja zmiennych w oparciu o cechy symboliczne i czasowe.  

#### Modelowanie:  
- Użycie architektur takich jak **Neural Networks** z mechanizmami uwagi (*attention mechanisms*), **Denoising Autoencoder**.  
- Testowanie modeli **LightGBM** i **XGBoost** dla porównania wyników.  

#### Walidacja:  
- Zastosowanie **Cross-Validation** z uwzględnieniem porządku czasowego danych.  

### Wizualizacja  
Projekt zakłada stworzenie interaktywnego **dashboardu** przedstawiającego:  
- Rozkład zmiennych finansowych w czasie.  
- Wyniki predykcji dla wybranych modeli.  
- Wizualizacje znaczenia cech (**SHAP**).  

## Opis Struktury Projektu  

### 1. EDA :  
- **EDA.ipynb** -> skrypt zawierający cały przebieg analizy EDA.  
- **README.md** -> zawiera opis EDA.  
- **sampled_output.parquet** -> zawiera zsamplowane dane, na których zostało przeprowadzone EDA.  

### 2. [Dashboard](https://janedashboard.streamlit.app/about_data):  
- **images/** -> zawiera pomniejsze foldery i zdjęcia wykorzystywane w dashboardzie.  
- **pages/** -> zawiera pliki *1_about_data.py* i *2_charts.py*, opisane w README.md.  
- **introduction.py** -> główna strona dashboardu, bardziej opisana w README.md.  
- **features.csv** -> przykładowe cechy z projektu.  
- **sample_submission.csv** -> przykładowa odpowiedź modelu.  
- **sampled_data_with_lags.csv** -> przykładowe cechy z projektu.  
- **responders.csv** -> przykładowe odpowiedzi z projektu.  
- **README.md** -> zawiera krótki opis najważniejszych plików.  

### 3. Modelowanie:  
- **RayTuneHPO.ipynb** -> Skrypt do optymalizacji hiperparametrów z użyciem **Ray Tune** oraz **OptunaSearch**.  
- **AutoGluon.ipynb** -> Implementacja modelowania przy użyciu **AutoGluon** oraz preprocessing danych.  
- **DatasetConversion.ipynb** -> Konwersja zbioru danych z **Parquet** na **CSV**, w tym dodawanie lagów i podział na zbiór treningowy, walidacyjny i testowy.  
- **README.md** (Modeling) -> Szczegółowy opis procesu modelowania, pipeline'u oraz używanych technik.
