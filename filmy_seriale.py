class Movies:
    def __init__(self, tytul, rok, gatunek, odtworzenia):
        self.tytul = tytul
        self.rok = rok
        self.gatunek = gatunek
        self.odtworzenia = odtworzenia

    def play(self, step=1):
        self.odtworzenia += step

    def __str__(self):
        return f"{self.tytul} ({self.rok})"


class Series(Movies):
    def __init__(self, numer_odcinka, numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu

    def play(self, step=1):
        self.odtworzenia += step

    def __str__(self):
        return f"{self.tytul} S%.2iE%.2i" % (
            int(self.numer_sezonu),
            int(self.numer_odcinka),
        )


def get_movies(movies_and_series_list):
    movies_list = []
    for i in range(len(movies_and_series_list)):
        if isinstance(movies_and_series_list[i], Series) == True:
            pass
        else:
            movies_list.append(movies_and_series_list[i])
    sorted(movies_list, key=lambda movies: movies.tytul)
    return movies_list


def get_series(movies_and_series_list):
    series_list = []
    for i in range(len(movies_and_series_list)):
        if isinstance(movies_and_series_list[i], Series) == True:
            series_list.append(movies_and_series_list[i])
        else:
            pass
    sorted(series_list, key=lambda series: series.tytul)
    return series_list


def search(title, lista_filmow_i_seriali):
    for i in range(len(lista_filmow_i_seriali)):
        if title == lista_filmow_i_seriali[i].tytul:
            print("Mamy tę pozycję w bibliotece")
            break
        else:
            if i == len(lista_filmow_i_seriali) - 1:
                print("Nie ma takiego tytułu w bibliotece")


import random


def generate_views(lista_filmow_i_seriali):
    n = random.randint(0, len(lista_filmow_i_seriali) - 1)
    m = random.randint(0, 100)
    lista_filmow_i_seriali[n].odtworzenia += m
    print(
        f"Odtworzenia pozycji {lista_filmow_i_seriali[n].tytul}: {lista_filmow_i_seriali[n].odtworzenia}"
    )


def generate_views_x10(lista_filmow_i_seriali):
    for i in range(10):
        generate_views(lista_filmow_i_seriali)


def top_titles(lista_filmow_i_seriali, n, type):
    if n >= len(lista_filmow_i_seriali):
        n = len(lista_filmow_i_seriali) - 1
    if type == 1:
        top_movies_list = []
        sorted(
            get_movies(lista_filmow_i_seriali), key=lambda movies: movies.odtworzenia
        )
        for i in range(n):
            top_movies_list.append(get_movies(lista_filmow_i_seriali)[i].tytul)
        return top_movies_list
    elif type == 2:
        top_series_list = []
        sorted(
            get_series(lista_filmow_i_seriali), key=lambda series: series.odtworzenia
        )
        for i in range(n):
            top_series_list.append(get_series(lista_filmow_i_seriali)[i].tytul)
        return top_series_list


if __name__ == "__main__":

    filmy_i_seriale = [
        Movies(tytul="Harold and Maude", rok=1984, gatunek="horror", odtworzenia=0),
        Series(
            tytul="Allo allo",
            rok=1984,
            gatunek="horror",
            odtworzenia=0,
            numer_odcinka=3,
            numer_sezonu=4,
        ),
    ]

    print(filmy_i_seriale[0], filmy_i_seriale[1])

    for i in range(len(get_movies(filmy_i_seriale))):
        print(get_movies(filmy_i_seriale)[i])

    for i in range(len(get_series(filmy_i_seriale))):
        print(get_series(filmy_i_seriale)[i])

    search("Allo allo", filmy_i_seriale)

    generate_views(filmy_i_seriale)

    generate_views_x10(filmy_i_seriale)

    print(top_titles(filmy_i_seriale, 3, 2))
