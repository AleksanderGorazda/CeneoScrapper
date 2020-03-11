#import bibliotek
import requests
from bs4 import BeautifulSoup
#adres URl strony z opiniami
url = "https://www.ceneo.pl/81643787#tab=reviews"

#pobranie kodu HTML strony z adresu URL
page_response = requests.get(url)
page_tree = BeautifulSoup(page_response.text, 'html.parser')

#wybranie z kodu strony fragmentów odpowiadających poszczególnym opiniom
opinions = page_tree.select("li.review-box")
opinion = opinions[0]
opinion_id = opinion["data-entry-id"]
author = opinion.select('div.reviewer-name-line').pop().string
recomendation = opinion.select('div.product-review-summary > em').pop().string
stars = opinion.select('span.review-score-count').pop().string
purchased = opinion.select('div.product-review-pz').pop().string
useful = opinion.select('button.vote-yes').pop()["data-total-vote"]
useless = opinion.select('button.vote-no').pop()["data-total-vote"]
content = opinion.select('p.product-review-body').pop().get_text()
print(opinion_id)
print(useful)
print(useless)
# - opinia: li.review-box
# - identyfikator: li.review-box["data-entry-id"]
# - autor: div.reviewer-name-line
# - rekomendacja: div.product-review-summary > em
# - liczba gwiazdek: span.review-score-count
# - czy potwierdzona zakupem: div.product-review-pz
# - data wystawienia: span.review-time > time["datetime"][0]
# - data zakupu: span.review-time > time["datetime"][1]
# - przydatna: button.votes-yes["data-total-vote"]
# - nieprzydatna: button.votes-no["data-total-vote"]
# - treść: p.product-review-body
# - wady: div.cons-cell > ul
# - zalety: div.pros-cell > ul
#ekstrakcja składowyh dla pierwszej opinii z listy