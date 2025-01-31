import streamlit as st 
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

st.set_page_config(
    page_title="Przegląd Wykresów",
    page_icon="📊",
    layout="wide",
)

path = r'G:\JaneStreetReal\Dashboard\imiges'

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

st.title("📊 Przegląd Wykresów")
st.markdown("---")
st.subheader("Responders")
st.markdown("Heatmap")

image = Image.open(f'{path}\Responders\heatmap.png')
st.image(image, width=500, use_container_width=False)

txt0 ="""
### Podsumowanie Macierzy Korelacji

---

#### Analiza:
1. **Ogólna struktura**:
   - Macierz przedstawia współczynniki korelacji pomiędzy zmiennymi `responder_0` do `responder_8`.
   - Wartości współczynników korelacji mieszczą się w przedziale od -1 (pełna korelacja negatywna) do 1 (pełna korelacja pozytywna).

2. **Najsilniejsze korelacje pozytywne**:
   - **`responder_4` i `responder_7`**: Współczynnik korelacji wynosi 0.84, co wskazuje na bardzo silny dodatni związek między tymi zmiennymi.
   - **`responder_5` i `responder_8`**: Korelacja wynosi 0.7, co oznacza również silny dodatni związek.

3. **Najsilniejsze korelacje negatywne**:
   - **`responder_6` i `responder_0`**: Korelacja wynosi -0.11, co wskazuje na słaby ujemny związek.
   - Większość ujemnych korelacji w macierzy jest bardzo słaba (blisko 0).

4. **Słabe korelacje**:
   - Większość korelacji pomiędzy zmiennymi wynosi od -0.1 do 0.4, co sugeruje słabe lub umiarkowane związki.

5. **Brak silnych korelacji ogólnych**:
   - Większość zmiennych jest ze sobą tylko umiarkowanie skorelowana, co może świadczyć o ich niezależności lub różnej strukturze danych.

---

#### Interpretacja:
- Silne korelacje, takie jak między `responder_4` a `responder_7`, mogą sugerować, że te zmienne mogą być powiązane lub zawierać podobne informacje.
- Słabe korelacje (bliskie 0) mogą wskazywać na brak bezpośredniego związku między zmiennymi.
"""
st.markdown(txt0)

st.markdown("Histogramy rozkładu wartości zmiennych responder_X")
images = [Image.open(rf'{path}\Responders\res0.png'), Image.open(rf'{path}\Responders\res1.png'), Image.open(rf'{path}\Responders\res2.png'),Image.open(rf'{path}\Responders\res3.png')
          ,Image.open(rf'{path}\Responders\res4.png'),Image.open(rf'{path}\Responders\res5.png'),Image.open(rf'{path}\Responders\res6.png'),Image.open(rf'{path}\Responders\res7.png'),Image.open(rf'{path}\Responders\res8.png')]
st.image(images, width=500, use_container_width=False)
txt="""
### Podsumowanie Histogramów

#### Nazwa:
**Histogramy rozkładu wartości zmiennych `responder_X`**, gdzie `X` oznacza numer zmiennej (np. `responder_0`, `responder_1`, itd.).

---

#### Analiza:
1. **Rozkład normalny**:
   - Wszystkie histogramy mają kształt zbliżony do rozkładu normalnego, z wyraźnym skupieniem wartości wokół zera.

2. **Symetria**:
   - Histogramy są w większości symetryczne, z niewielkimi odchyleniami po obu stronach średniej.

3. **Odchylenia standardowe**:
   - Dane mają wąskie zakresy skupienia wokół wartości centralnej, co sugeruje niskie odchylenie standardowe.
   - Występują pojedyncze wartości ekstremalne (tzw. długie ogony rozkładu).

4. **Gęstość danych**:
   - Najwięcej obserwacji znajduje się w przedziale \(-1\) do \(1\).
   - Liczba rekordów gwałtownie spada poza tym zakresem.

5. **Dane odstające**:
   - Na końcach rozkładu (np. \(<-4\) i \(>4\)) występuje bardzo niewiele obserwacji, co może sugerować obecność potencjalnych wartości odstających.
"""

st.markdown(txt)

st.subheader("ACF and PACF for responder_6")

images1 = [Image.open(rf'{path}\ACF.png'), Image.open(rf'{path}\PACF.png')]
captions = ['ACF', 'PACF']
st.image(images1, width=500, use_container_width=False)

txt1 ="""
### Podsumowanie Analizy ACF i PACF dla `responder_6`

---

#### Autocorrelation Function (ACF):
1. **Opis**:
   - ACF mierzy zależność pomiędzy bieżącymi wartościami a ich przesunięciami w czasie (lagami).
   - Wartość na lag 0 wynosi 1, co oznacza doskonałą korelację z samą sobą.

2. **Wnioski**:
   - Korelacja dla dalszych lagów spada blisko zera, co wskazuje na brak silnych długookresowych zależności w danych.
   - Na wyższych lagach (np. 35-40) występują lekkie odchylenia, które mogą sugerować pewne okresowe struktury.

---

#### Partial Autocorrelation Function (PACF):
1. **Opis**:
   - PACF mierzy korelację pomiędzy wartościami zmiennej a jej przesunięciami, eliminując wpływ wartości pośrednich.
   - Pomaga w określeniu liczby lagów, które należy uwzględnić w modelu autoregresyjnym (AR).

2. **Wnioski**:
   - Znacząca korelacja występuje dla lagu 1, co sugeruje, że występuje krótkookresowa zależność w danych.
   - Korelacje na dalszych lagach są znikome i bliskie zera, co wskazuje na brak silnych związków dla większych opóźnień.

---

#### Interpretacja:
- Wartości ACF i PACF sugerują, że dane `responder_6` mogą być opisane przez prosty model autoregresyjny z małą liczbą lagów (np. AR(1)).
- Brak długoterminowych zależności sugeruje, że dane są w dużej mierze stacjonarne lub zawierają tylko lokalne zależności czasowe.
"""
st.markdown(txt1)
st.subheader("Features")

images2 = [Image.open(rf'{path}\Features\feat.png'), Image.open(rf'{path}\Features\feat1.png'), Image.open(rf'{path}\Features\feat2.png'),Image.open(rf'{path}\Features\feat3.png')
          ,Image.open(rf'{path}\Features\feat4.png'),Image.open(rf'{path}\Features\feat5.png'),Image.open(rf'{path}\Features\feat6.png'),Image.open(rf'{path}\Features\feat7.png'),Image.open(rf'{path}\Features\feat8.png'),
          Image.open(rf'{path}\Features\feat9.png')]

st.image(images2, width=500, use_container_width=False)

txt11 ="""
### Wnioski:

### Ogólny Opis i Wnioski dla Wykresów

---

#### **Ogólny opis:**
- Wykresy przedstawiają **rozkład liczby rekordów dla różnych wartości `symbol_id`** w danych, z uwzględnieniem różnych warunków filtrowania lub segmentacji.
- Dla pełnego zbioru danych (`symbol_id` dla wszystkich warunków) widoczny jest **równomierny rozkład** liczby rekordów w większości kategorii, z minimalnymi brakami danych.
- W miarę zastosowania warunków lub filtrów, rozkład liczby rekordów zaczyna ujawniać **nierównomierności**:
  - W niektórych przypadkach liczba rekordów znacząco spada dla wybranych `symbol_id`.
  - Część `symbol_id` staje się niedoreprezentowana, a w skrajnych przypadkach całkowicie brakuje danych.

---

#### **Wnioski:**

1. **Nierównomierność w danych:**
   - Zastosowanie filtrów lub segmentacji powoduje, że dane stają się mniej zrównoważone.
   - Niektóre wartości `symbol_id` mają znacznie mniej rekordów, co może wpłynąć na wyniki analizy lub modelowania (np. bias w predykcji).

2. **Luki w danych:**
   - Wraz z zaostrzeniem warunków rośnie liczba brakujących danych w wybranych `symbol_id`.
   - W skrajnych przypadkach pewne `symbol_id` całkowicie znikają z danych, co sugeruje potencjalne problemy w procesie zbierania lub filtrowania danych.

3. **Zależność od warunków:**
   - Dane są wrażliwe na zastosowane kryteria filtrowania, co wskazuje na potrzebę dokładnego rozważenia tych kryteriów przed analizą.
   - Segmentacja danych wprowadza różnorodność w rozkładach `symbol_id`, co może być zarówno zaletą (większa szczegółowość analizy), jak i wyzwaniem (potrzeba większego czyszczenia danych).

4. **Wpływ na analizy i modele:**
   - Nierównomierność liczby rekordów może prowadzić do błędów w analizie, takich jak **nadreprezentacja** niektórych `symbol_id` w modelach predykcyjnych.
   - Warto rozważyć zastosowanie metod takich jak oversampling, undersampling lub wagi w modelach, aby zrównoważyć dane.
---

#### **Podsumowanie:**
Wykresy pokazują, że dane `symbol_id` są stosunkowo kompletne w pełnym zbiorze danych, ale ich rozkład staje się nierównomierny po zastosowaniu kolejnych warunków filtrowania. Nierównomierność i luki w danych mogą mieć istotny wpływ na wyniki analiz i modeli, dlatego niezbędne jest odpowiednie przetwarzanie tych danych przed ich wykorzystaniem. 
"""

st.markdown(txt11)

st.subheader("Weights")

image2 = Image.open(f'{path}\Weights\weight.png')
st.image(image2, width=500, use_container_width=False)

txt2="""
#### 1. **Histogram wartości niezerowych wag**

**Opis:**
- Histogram przedstawia rozkład wag, pomijając wartości zerowe.
- Wartości wag mają lewoskośny rozkład, z największą liczbą obserwacji w zakresie od 1 do 2.
- Widoczne są długie ogony po prawej stronie rozkładu, co wskazuje na rzadkie, ale wyższe wartości wag.

---
"""
st.markdown(txt2)

image3 = Image.open(f'{path}\Weights\weight2.png')
st.image(image3, width=500, use_container_width=False)

txt3="""
#### 2. **Histogram logarytmu wartości niezerowych wag**

**Opis:**
- Wykres przedstawia histogram wartości logarytmów wag.
- Rozkład logarytmów jest symetryczny i skoncentrowany wokół wartości bliskiej zera, co sugeruje normalność po zastosowaniu logarytmowania.
- Transformacja logarytmiczna wygładziła dane, redukując wpływ wartości odstających.

---
"""
st.markdown(txt3)

image4 = Image.open(f'{path}\Weights\weight3.png')
st.image(image4, width=500, use_container_width=False)

txt4="""
#### 3. **Log-transformed: Zależność wag od `responders_6`**

**Opis:**
- Scatter plot przedstawia zależność logarytmu wag (y) od logarytmu wartości `responders_6` (x).
- Widać rozproszenie danych, ale z wyraźnym trendem wzrostowym – wyższe wartości `responders_6` odpowiadają wyższym logarytmowanym wagom.
- Pojedyncze punkty odstające na krańcach wykresu mogą wymagać dalszej analizy.

---
"""
st.markdown(txt4)

image5 = Image.open(f'{path}\Weights\weight4.png')
st.image(image5, width=500, use_container_width=False)

txt5="""
#### 4. **Zależność wag od `responders_6` (Trend)**

**Opis:**
- Scatter plot ukazuje zależność średnich wag (y) od wartości `responders_6` (x).
- Trend wzrostowy jest wyraźny – wyższe wartości `responders_6` wiążą się z wyższymi wagami.
- Występuje większe zagęszczenie danych w centralnej części wykresu, co może odpowiadać typowym przypadkom.

---
"""
st.markdown(txt5)


image6 = Image.open(f'{path}\Weights\weight5.png')
st.image(image6, width=500, use_container_width=False)

txt6="""
#### 5. **Średnia waga dla różnych wartości `responders_6` (Binned)**

**Opis:**
- Ten wykres przedstawia średnią wagę (y) dla danych przedziałów wartości `responders_6` (x), które zostały podzielone na zakresy (biny).
- Widać, że średnia waga wzrasta w miarę przesuwania się w kierunku wyższych wartości `responders_6`.
- Przedziały binów są równomiernie rozdzielone, co umożliwia łatwą interpretację zależności.

---
"""
st.markdown(txt6)

text7 = """

### Wnioski:
- Wartości wag są skorelowane z wartościami `responders_6`.
- Histogramy wskazują na potrzebę transformacji danych, aby lepiej uchwycić zależności (co potwierdza logarytmowanie).
- Scatter ploty sugerują pozytywną zależność między zmiennymi, która może być wykorzystana w modelach predykcyjnych. 

"""
st.markdown(text7)

st.subheader("NaN")

image7 = Image.open(rf'{path}\nan.png')
st.image(image7, width=500, use_container_width=False)

txt7="""
#### 1. **Średnia liczba brakujących wartości dla cech na transakcję, dla każdego dnia**

**Opis:**
- Wykres liniowy przedstawia średnią liczbę brakujących wartości na transakcję w zależności od dnia.
- Średnia liczba braków początkowo jest wysoka (ponad 10), ale z czasem zmniejsza się i oscyluje wokół wartości 2 (przedstawionej linią przerywaną).
- Wykres ujawnia nieregularności w danych, szczególnie na początku, co może wskazywać na problemy z jakością danych w tych okresach.

---
"""
st.markdown(txt7)

image8 = Image.open(rf'{path}\nan1.png')
st.image(image8, width=500, use_container_width=False)

txt8="""
#### 2. **Całkowita liczba brakujących wartości we wszystkich cechach dla każdego dnia**

**Opis:**
- Wykres liniowy przedstawia sumę brakujących wartości we wszystkich cechach dla każdego dnia.
- Początkowe dni mają bardzo dużą liczbę braków (ponad 80 000), która systematycznie maleje w kolejnych dniach.
- Czerwony przerywany wskaźnik na początku wykresu podkreśla kluczowy punkt lub próg dla analizy braków.
- Dane wykazują dużą zmienność na początkowych etapach, co może wymagać szczegółowego czyszczenia.

---
"""
st.markdown(txt8)

image9 = Image.open(rf'{path}\nan2.png')
st.image(image9, width=500, use_container_width=False)

txt9="""
#### 3. **Całkowita liczba brakujących wartości dla każdej kolumny**

**Opis:**
- Wykres słupkowy z gradientem kolorów przedstawia całkowitą liczbę brakujących wartości dla każdej kolumny.
- Najbardziej problematyczne kolumny to te o najwyższych słupkach (np. `feature_23`, `feature_24`), które mają ponad 150 000 braków.
- Większość kolumn ma stosunkowo małą liczbę braków (poniżej 50 000).
- Gradient kolorów pomaga wizualnie zidentyfikować najbardziej brakujące cechy.

---
"""
st.markdown(txt9)

txt10="""
### Wnioski:
1. **Jakość danych**:
   - Duża liczba brakujących wartości w początkowych dniach i w niektórych kolumnach sugeruje problemy z jakością danych, które wymagają czyszczenia lub imputacji.

2. **Potencjalne działania**:
   - Imputacja braków lub usunięcie najbardziej problematycznych kolumn (np. `feature_23`, `feature_24`).
   - Dogłębna analiza danych w pierwszych dniach (duże braki) w celu zidentyfikowania ich przyczyn.

3. **Kolumny do priorytetyzacji**:
   - Skupić się na kolumnach o najmniejszej liczbie braków, aby zachować ich informacyjność w modelach predykcyjnych.

"""
st.markdown(txt10)


col1, col2, col3 = st.columns([3, 7, 3])
with col1:
    if st.button("Przejdz do opisu danych"):
        switch_page("about data")
with col3:
    if st.button("Przejdź do Modelowania"):
        switch_page("model")