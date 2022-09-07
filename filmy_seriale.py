import random


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

    def __repr__(self):
        return f"{self.tytul} ({self.rok})"


class Series(Movies):
    def __init__(self, numer_odcinka, numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu

    def __str__(self):
        return f"{self.tytul} S{self.numer_sezonu:02}E{self.numer_odcinka:02}"

    def __repr__(self):
        return f"{self.tytul} S{self.numer_sezonu:02}E{self.numer_odcinka:02}"


def get_kind(input_list, class_type):
    filtered_list = []
    for elem in input_list:
        if type(elem) == class_type:
            filtered_list.append(elem)
    filtered_list.sort(key=lambda x: x.tytul)
    return filtered_list


def get_movies(movies_and_series_list):
    return get_kind(movies_and_series_list, Movies)


def get_series(movies_and_series_list):
    return get_kind(movies_and_series_list, Series)


def lista_pozycji(lst_filmow_i_seriali, type):
    if type == 1:
        return get_movies(lst_filmow_i_seriali)
    elif type == 2:
        return get_series(lst_filmow_i_seriali)


def search(title, lista_filmow_i_seriali):
    is_found = False
    for elem in lista_filmow_i_seriali:
        if title == elem.tytul:
            print("Mamy tę pozycję w bibliotece")
            is_found = True
    if is_found == False:
        print("Nie ma takiego tytułu w bibliotece")


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
    top_list = []
    lst = []
    if type == 1:
        lst = get_movies(lista_filmow_i_seriali)
    elif type == 2:
        lst = get_series(lista_filmow_i_seriali)
    lst.sort(key=lambda list: list.odtworzenia, reverse=True)
    for i in range(n):
        top_list.append(lst[i])
    return top_list


if __name__ == "__main__":

    filmy_i_seriale = [
        Movies(tytul="Harold and Maude", rok=1984, gatunek="horror", odtworzenia=0),
        Movies(tytul="Odyseja kosmiczna", rok=1969, gatunek="sci-fi", odtworzenia=0),
        Movies(tytul="Abrakdabra", rok=2011, gatunek="sci-fi", odtworzenia=0),
        Series(
            tytul="Hallo allo",
            rok=1984,
            gatunek="horror",
            odtworzenia=0,
            numer_odcinka=3,
            numer_sezonu=4,
        ),
        Series(
            tytul="Breaking bad",
            rok=2000,
            gatunek="horror",
            odtworzenia=0,
            numer_odcinka=1,
            numer_sezonu=5,
        ),
        Series(
            tytul="True detective",
            rok=2001,
            gatunek="horror",
            odtworzenia=0,
            numer_odcinka=2,
            numer_sezonu=2,
        ),
    ]

    print(filmy_i_seriale)
    print()

    print(lista_pozycji(filmy_i_seriale, 1))
    print(lista_pozycji(filmy_i_seriale, 2))
    print()

    search("Hallo allo", filmy_i_seriale)
    print()

    generate_views(filmy_i_seriale)

    generate_views_x10(filmy_i_seriale)
    print()

    print(top_titles(filmy_i_seriale, 3, 2))
