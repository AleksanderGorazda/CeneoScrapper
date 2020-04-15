#import bibliotek
import os
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#wyswietlenie zawartosci katalogu
print(os.listdir("./opinions"))

#wczytanie id produktu
product_id = input("Podaj kod produktu: ")

opinions = pd.read_json("opinions/"+product_id+".json")
opinions = opinions.set_index("opinion_id")

#histogram częstości występowania poszczególnych ocen
opinions["stars"] = opinions["stars"].map(lambda x: float(x.split("/")[0].replace(",",".")))
stars = opinions["stars"].value_counts().sort_index().reindex(list(np.arange(0,5.5,0.5)), fill_value=0)
fig, ax = plt.subplots()
stars.plot.bar(color="lightskyblue")
ax.set_title("Gwiazdki")
ax.set_xlabel("liczba gwaizdek")
ax.set_ylabel("liczba opinii")
plt.savefig("figures/"+product_id+"_bar.png")
plt.close()

#udział poszczególnych rekomendacji w ogólnej liczbie opinni
recommendation = opinions["recommendation"].value_counts()
fig, ax = plt.subplots()
recommendation.plot.pie(label="", autopct="%1.1f%%", colors=["green", "red"])
ax.set_title("Rekomendacje")
plt.savefig("figures/"+product_id+"_pie.png")

average_score = opinions["stars"].mean()
pros = opinions["pros"].count()
cons = opinions["cons"].count()
purchased = opinions["purchased"].sum()

print(average_score, pros, cons, purchased)

stars_purchased = pd.crosstab(opinions["stars"], opinions["purchased"])

print(stars_purchased)