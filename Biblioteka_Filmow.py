#System obsługujący bibliotekę filmów i seriali:

import random
from secrets import choice
import datetime
date = datetime.date.today().strftime('%d-%m-%Y') #Data w formacie DD.MM.RRR

#Biblioteka Filmów, Klasa podstawowa Movie:
class Movie:
    def __init__(self, title, release_year, species, number_of_playes):
        self.title = title
        self.release_year = release_year
        self.species = species
        self.number_of_playes = number_of_playes

#Po wyświetleniu filmu jako string widoczne są tytuł i rok wydania np. “Pulp Fiction (1994)”   
    def __str__(self):
        return f"{self.title} ({self.release_year})"
        
    def __repr__(self):
        return self.__str__()

#Metoda play zwiększająca liczbę odtworzeń danego tytułu o 1:
    def play(self, step=1):
        self.number_of_playes += step
    

#Klasa Series, dziedzicząca z Klasy Movie:  
class Series(Movie):
    def __init__(self, season_number, episode_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

#Po wyświetleniu serialu jako string pokazują się informacje o konkretnym odcinku, np.: “The Simpsons S01E05”
    def __str__(self):
        return f"{self.title} S{0}{self.season_number}E{0}{self.episode_number}" 


M_1 = Movie("Narodziny Gwiazdy", 2018, "Dramat/Muzyczny", 100)
M_2 = Movie("Nomadland", 2020, "Dramat", 85)
M_3 = Movie("CODA", 2021, "Dramat", 45)
M_4 = Movie("Diuna", 2021, "Sci-Fi", 97)
M_5 = Movie("Furioza", 2022, "Dramat/Akcja", 55)
S_1 = Series(2, 8, "Wiedźmin", 2019, "Fantasy", 98,)
S_2 = Series(1, 6,"Peaky Blinders", 2013, "Kryminał, Dramat historyczny", 60)
S_3 = Series(1, 15, "Stranger Things", 2016, "Dramat, Horror, Sci-Fi", 150)
S_4 = Series(2, 10, "Gra o Tron", 2011, "Dramat, Fantasy, Przygodowy", 333)
S_5 = Series(1, 6, "Król", 2010, "Gangsterski", 101)

movies = [M_1, M_2, M_3, M_4, M_5]
series = [S_1, S_2, S_3, S_4, S_5]

#Wspólna lista Filmów i Seriali:
my_list = [movies + series]

#Funkcje get_movies, get_series, filtrują listę i zwracają odpowiednio tylko filmy oraz tylko seriale. Sortują listę wynikową alfabetycznie.
def get_movies():
    for i in my_list:
        return sorted(movies, key = lambda movies: movies.title)

def get_series():
    for i in my_list:
        return sorted(series, key = lambda series: series.title)

#Funkcja search wyszukująca filmy po jego tytule:
def search():
    my_list_dict = {
    M_1: "Narodziny Gwiazdy",
    M_2: "Nomadland",
    M_3: "CODA",
    M_4: "Diuna",
    M_5: "Furioza",
    S_1: "Wiedźmin",
    S_2: "Peaky Blinders",
    S_3: "Stranger Things",
    S_4: "Gra o Tron",
    S_5: "Król"
    }
    
    search_title = input(f"Jakiego filmu lub serialu szukasz? Podaj tytuł: ")

    if search_title in my_list_dict.values():
        return f"Szukany tytuł: {search_title} znajduje się w naszej Bibliotece"
    else:
        return f"Szukany tytuł {search_title} nie znajduje się w naszej Bibliotece"

#Funkcja generate_views: losowo wybiera element z biblioteki, a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń:
def generate_views():
    for i in my_list:
        return f"Wylosowany tytuł to: {random.choice(i)}, który ma {random.randint(0,100)} odtworzeń."

#Funkcja uruchamiająca funkcję generate_views 10 razy:
def ten_times():
    for i in range(10):
        print(generate_views())  

#Funkcja top_titles zwracająca najpopularniejsze seriale lub filmy:
def top_titles(how_many_items, content_type):
    sorted_movies_playes = sorted(movies, key = lambda movies: movies.number_of_playes, reverse = True)
    sorted_series_playes = sorted(series, key = lambda series: series.number_of_playes, reverse = True)

    for i in my_list:
        if content_type == movies:
            return sorted_movies_playes[0:how_many_items]
        if content_type == series:
            return sorted_series_playes[0:how_many_items]

if __name__ == "__main__":
    print(f"""Biblioteka Filmów:\n{my_list}""")
    print()
    print(generate_views())
    print()
    print(f"Najpopularniejsze filmy i seriale dnia {date} to: {(top_titles(3, movies))}, {(top_titles(3, series))}")



