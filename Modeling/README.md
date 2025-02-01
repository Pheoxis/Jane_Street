# README

## 1. Wprowadzenie
Projekt dotyczy modelowania szeregów czasowych i optymalizacji hiperparametrów dla konkursu Jane Street. Implementacja wykorzystuje podejście **Weighted Ensemble** oraz **Time Series Cross Validation (TSCV)**, a optymalizacja odbywa się za pomocą **Ray Tune** oraz **ASHAScheduler**.

## 2. Struktura plików

### Pliki:

- **README.md** – Opis projektu, jego struktury oraz wykorzystywanych bibliotek.
- **RayTuneHPO.ipynb** – Skrypt do optymalizacji hiperparametrów z użyciem **Ray Tune** oraz **OptunaSearch**.
- **AutoGluon.ipynb** – Implementacja modelowania przy użyciu **AutoGluon** oraz preprocessing danych.
- **DatasetConversion.ipynb** – Konwersja zbioru danych z **Parquet** na **CSV**, w tym dodawanie lagów.

## 3. Biblioteki i narzędzia
W projekcie używane są następujące biblioteki:

- **numpy** 2.1.3 – obliczenia numeryczne
- **dask** 2025.1.0 – obsługa dużych zbiorów danych
- **lightgbm** 4.5.0 – boosting drzew decyzyjnych
- **xgboost** 2.1.3 – alternatywny model boostingu
- **scikit-learn** 1.6.1 – metryki i preprocessing
- **ray[tune]** 2.41.0 – optymalizacja hiperparametrów
- **shap** 0.46.0 – analiza ważności cech
- **wandb** 0.19.5 – monitorowanie eksperymentów
- **polars** – szybka manipulacja danymi

## 4. Pipeline modelowania

### a) Time Series Cross Validation (TSCV)
Podział danych na **n-folds** z podziałem na zbiór treningowy i walidacyjny, tak aby uniknąć **data leakage**.

### b) Trening modeli
Dwa główne modele:
- **LightGBM** – optymalny na CPU
- **XGBoost** – zoptymalizowany pod kątem GPU

### c) Optymalizacja hiperparametrów
Optymalizacja przeprowadzana jest za pomocą **Ray Tune** oraz **ASHAScheduler**, który dynamicznie alokuje zasoby, zatrzymując nieobiecujące próby.

### d) Weighted Ensemble
Predykcje modeli są łączone w sposób ważony, bazując na metodach zastosowanych w **AutoGluon**.

### e) Ewaluacja wyników
Metryka oceny to **zero-mean R²**, dostosowana do wymagań konkursu Jane Street.

## 5. Konwersja i preprocessing danych
Skrypt **DatasetConversion.ipynb** konwertuje dane do formatu **CSV**, tworzy lags oraz dzieli dane na zbiór treningowy, walidacyjny i testowy.

## 6. Uruchomienie optymalizacji hiperparametrów
W celu uruchomienia Ray Tune HPO, ustaw `RUN_HPO = True` w **RayTuneHPO.ipynb** i uruchom kod. Wyniki zapisywane są w katalogu `ray_optuna_results`.

