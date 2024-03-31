class MemoryRepository:
    def __init__(self):
        self.__clients = []
        self.__movies = []
        self.__rentals = []

    def get_clients(self):
        return self.__clients

    def get_movies(self):
        return self.__movies

    def get_rentals(self):
        return self.__rentals

    def add_client(self, client):
        self.__clients.append(client)

    def add_movie(self, movie):
        self.__movies.append(movie)

    def add_rental(self, rental):
        self.__rentals.append(rental)

    def remove_client(self, client):
        self.__clients.remove(client)

    def remove_movie(self, movie):
        self.__movies.remove(movie)

    def remove_rental(self, rental):
        self.__rentals.remove(rental)
