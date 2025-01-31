# Jane_Street  
Fighting for high rank in the competition  

Temat: Prognozowanie w czasie rzeczywistym danych rynkowych przy użyciu algorytmów uczenia maszynowego  
Dziedzina: Finanse  
Opis: Projekt opiera się na konkursie Kaggle "Jane Street Real-Time Market Data Forecasting", gdzie celem jest opracowanie modelu przewidującego odpowiedź rynku na podstawie historycznych danych finansowych. Analizowane dane obejmują zmienne czasowe, takie jak symbol, czas i zmienne finansowe z dużą liczbą braków danych i niestacjonarności.  
________________________________________
Metoda Pozyskiwania Danych  
Dane do projektu zostały pozyskane z oficjalnego zestawu udostępnionego przez organizatorów konkursu Kaggle, zawierającego pliki w formacie .parquet. Dane te obejmują historyczne zmienne finansowe, odpowiedzi rynkowe oraz zmienne pomocnicze, takie jak wagi i identyfikatory symboli.[ Link do Strony z której można pobrać ](https://www.kaggle.com/competitions/jane-street-real-time-market-data-forecasting/data?select=responders.csv)  
W projekcie wykorzystano również biblioteki Polars oraz Pandas do wstępnej analizy i przetwarzania danych.  
Etapy pozyskiwania danych:  
1.	Pobranie danych z platformy Kaggle.  
2.	Wczytanie danych do analizy przy użyciu narzędzi Python 3.10+ (Polars, Pandas).  
3.	Przygotowanie danych do modelowania poprzez stworzenie lagów czasowych oraz imputację braków danych.  
________________________________________
Cel Badania  
Główny cel: Stworzenie modelu uczenia maszynowego zdolnego do przewidywania odpowiedzi rynkowej (responder_6) w czasie rzeczywistym na podstawie zmiennych finansowych.  
Cele szczegółowe:  
•	Analiza struktury danych i identyfikacja kluczowych cech.  
•	Stworzenie zaawansowanego modelu predykcyjnego (XGBoost, LightGBM, Neural Networks).  
•	Zastosowanie metody ensemble w celu poprawy wyników modelu.  
•	Ocena wydajności modelu przy użyciu metryk takich jak Zero-Mean R² i analiza wyników.  
________________________________________
Analiza Danych i Tworzenie Dashboardu  
Złożoność Zbioru Danych  
Dane są wielowymiarowe i niestacjonarne, co wymaga zastosowania zaawansowanych technik analizy szeregów czasowych. Szczególnym wyzwaniem są:  
•	Braki danych w wielu zmiennych.  
•	Niestabilne zmienne czasowe i symboliczne.  
•	Dynamika wprowadzania nowych symboli i cech w czasie trwania danych.  
Dostosowanie Metod Analizy  
Metody analizy zostały dostosowane do specyficznych wymagań projektu:  
1.	Przetwarzanie Danych:   
o	Stworzenie lagów czasowych w celu wykorzystania informacji historycznych.  
o	Normalizacja/transformacja zmiennych w oparciu o cechy symboliczne i czasowe.  
2.	Modelowanie:  
o	Użycie architektur takich jak Neural Networks z mechanizmami uwagi (attention mechanisms), Denoising Autoencoder.  
o	Testowanie modeli LightGBM i XGBoost dla porównania wyników.  
3.	Walidacja:   
o	Zastosowanie Cross-Validation z uwzględnieniem porządku czasowego danych.  
Wizualizacja  
Projekt zakłada stworzenie interaktywnego dashboardu przedstawiającego:  
•	Rozkład zmiennych finansowych w czasie.  
•	Wyniki predykcji dla wybranych modeli.  
•	Wizualizacje znaczenia cech (SHAP).  
________________________________________
Opis struktury projektu: 

1.	EDA :  
o	EDA.ipynb -> skrypt zawierający cały przebieg analizy EDA  
o	README.md -> zawiera opis EDA  
o	sampled_output.parquet -> zawiera zsamplowane dane na których zostało przeprowadzone eda  
2.	Dashboard:  
o		imiges -> zawiera pomniejsze foldery i zdjęcia które sa wykorzystywane w dashboardzie, posegregowane do poszczególnych problemów  
o	  pages -> zawiera plik 1_about_data.py i 2_charts.py opisane są w folderze README.md   
o	  introduction.py -> główna strona dashboardu, bardziej opisana w README.md  
o	  features.csv -> zawiera przykładowe featuery z projektu  
o	  sample_submission.csv -> zawiera wstępną odpowiedź modelu  
o	  sampled_data_with_lags.csv -> przykładowe cechy z projektu  
o	  responders.csv -> przykadowe odpowiedzi z projektu  
o	  README.md -> zawiera krótki opis najważniejszych plików
3.	Modeling :  
o   
