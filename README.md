# CeneoScraper11S
# Etap 1 - pobranie pojedynczeej opinii 
- opinia    : li.review-box
- identyfikator : li.review-box[data-entry-id]
- autor     : div.reviewer-name-line
- rekomendacja      : div.product-review-summary > em
- liczba gwiazdek       :  span.review-score-count
- czy potwierdzona zakupem  :  div.product-review-pz
- data wystawienia      : span.review-time > time  (pierwsze wystapienie)
- data zakupu       :  span.review-time > time  (drugie wystapienie)
- przydatna     : button.votes-yes[data-total-vote]
- nieprzydatna      : button.votes-no[data-total-vote]
- treść     : p.product-review-body
- wady      : div.pros-cell > ul
- zalety    : div.cons-cell > ul

04.03.2020

## Etap 2 - pobiarnie wszystkich opinii z pojedynczej strony
- zapis składowych opinii do złożonej struktury danych
## Etap 3 - Pobranie wszystkich opinii o pojedynczym produkcie
- sposób przechodzenia po poszczegolnych stronach z opiniami
- Eksport opinii do pliku .js
## Etap 4 - analiza pobranych danych
- zapisanie pobranych danych do obiektu dataframe
- wykonanie prostych obliczen na danych
- wykonanie prostych wykresow
## Etap 5 - analiza pobranych danych
- zapis pobranych danych do obiektu dataframe (ramka danych)
- wykonanie prostych obliczeń na danych
- wykonanie prostych wykresów
## Etap 6 - interfejs webowy aplikacji (framework flask)
- zainstalowanie i uruchamianie Flask'a
- struktura aplikacji
    /CeneoScrapper
        /run.py
        /config.py
        /app
            /__init__.py
            /routes.py
            /models.py
            /forms.py
            /scrapper.py
            /analyzer.py
            /static/
                /main.css
                /figures/
                    /fig.png
            /templates/
                /base.html
            /opinions
        /requirements.txt
        /.venv
- routing (nawigowanie po stronach serwisu)
- widoki (Jinja)
