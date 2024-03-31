import random
import datetime
from datetime import date

from src.repository.memory_repository import MemoryRepository
from src.domain.client import Client
from src.domain.movie import Movie
from src.domain.rental import Rental


class Services():
    def __init__(self, can_generate):
        self.__repo = MemoryRepository()
        if can_generate == True:
            self.generate_clients()
            self.generate_movies()
            self.generate_rentals()

    def validate_and_add_client(self, client):
        """
        This function validates and adds a client to the current list of clients
        :param client:an object of type client
        :return: -, if no exceptions are raised
        """
        self.validate_client(client)
        self.__repo.add_client(client)

    def validate_and_add_movie(self, movie):
        """
        This function validates and adds a movie to the current list of movies
        :param movie: an object of type movie
        :return: -, if no exceptions are raised
        """
        self.validate_movie(movie)
        self.__repo.add_movie(movie)

    def validate_and_add_rental(self, rental):
        """
        This function validates and adds a rental to the current list of rentals
        :param rental: an object of type rental
        :return: -, if no exceptions are raised
        """
        self.validate_rental(rental)
        self.__repo.add_rental(rental)

    def return_movie(self, movie_id, returned_date):
        cpy = returned_date
        returned_date = returned_date.split("-")
        for i in range(len(returned_date)):
            returned_date[i] = int(returned_date[i])
        if len(returned_date) != 3:
            raise Exception("The return date is invalid")
        else:
            returned_date = datetime.datetime(returned_date[2], returned_date[1], returned_date[0])

        found = False
        rentals = self.get_rentals()
        for rental in rentals:
            if rental.get_movie_id() == movie_id:
                found = True
                if rental.get_returned_date() == "0":

                    rented_date = rental.get_rented_date().split("-")
                    for i in range(len(rented_date)):
                        rented_date[i] = int(rented_date[i])
                    rented_date = datetime.datetime(rented_date[2], rented_date[1], rented_date[0])
                    if rented_date > returned_date:
                        raise Exception("The returned date cannot be lower that the rented date")

                    rental.set_returned_date(cpy)
                    return
        if found == False:
            raise Exception("There is no movie with the id you provided")
        raise Exception("The movie has already been returned")

    def validate_rental(self, rental):
        errors = ""

        rentals = self.get_rentals()
        for elem in rentals:
            if elem.get_rental_id() == rental.get_rental_id():
                errors += "There already is rental with the id you provided\n"
                break

        movies = self.get_movies()
        found = False
        for movie in movies:
            if movie.get_movie_id() == rental.get_movie_id():
                found = True
                break
        if found == False:
            errors += "There is no movie with the id you provided\n"

        clients = self.get_clients()
        found = False
        for client in clients:
            if client.get_client_id() == rental.get_client_id():
                found = True
                break
        if found == False:
            errors += "There is no client with the id you provided\n"

        rentals = self.get_rentals()
        for elem in rentals:
            if elem.get_movie_id() == rental.get_movie_id() and elem.get_returned_date() == "0":
                errors += "The movie with the id you provided is already rented\n"

        for elem in rentals:
            if elem.get_client_id() == rental.get_client_id():
                if self.is_late_return(elem) == True:
                    errors += "The client has had late returns in the past\n"
                    break

        rented_date = rental.get_rented_date().split("-")
        for i in range(len(rented_date)):
            rented_date[i] = int(rented_date[i])
        if len(rented_date) != 3:
            errors += "The returned date is invalid\n"
        else:
            rented_date = datetime.datetime(rented_date[2], rented_date[1], rented_date[0])

        due_date = rental.get_due_date().split("-")
        for i in range(len(due_date)):
            due_date[i] = int(due_date[i])
        if len(due_date) != 3:
            errors += "The due date is invalid\n"
        else:
            due_date = datetime.datetime(due_date[2], due_date[1], due_date[0])

        if due_date < rented_date:
            errors += "The due date cannot be less than the rented date"

        if len(errors) > 0:
            raise Exception(errors)

    @staticmethod
    def is_late_return(rental):
        if rental.get_returned_date() == "0":
            return False

        due_date = rental.get_due_date().split("-")
        returned_date = rental.get_returned_date().split("-")
        for i in range(len(due_date)):
            due_date[i] = int(due_date[i])
        for i in range(len(returned_date)):
            returned_date[i] = int(returned_date[i])

        due_time = datetime.datetime(due_date[2], due_date[1], due_date[0])
        returned_time = datetime.datetime(returned_date[2], returned_date[1], returned_date[0])
        if due_time < returned_time:
            return True
        return False

    def remove_client_based_rentals(self, client_id):
        """
        This function removes a rental based on a client id
        :param client_id: an integer representing the id of a client
        :return: -
        """
        rentals = self.get_rentals()
        for rental in rentals:
            if rental.get_client_id() == client_id:
                self.__repo.remove_rental(rental)

    def remove_client(self, client_id):
        """
        This function removes a client from the list of clients
        :param client_id: an integer representing the id of a client
        :return: -
        """
        self.remove_client_based_rentals(client_id)

        clients = self.get_clients()
        for client in clients:
            if client.get_client_id() == client_id:
                self.__repo.remove_client(client)
                return

        raise Exception("No client with the id you provided was found")

    def remove_movie_based_rentals(self, movie_id):
        """
        This function removes a rental based on a movie_id
        :param movie_id: an integer representing the id of a movie
        :return: -
        """
        rentals = self.get_rentals()
        for rental in rentals:
            if rental.get_movie_id() == movie_id:
                self.__repo.remove_rental(rental)

    def remove_movie(self, movie_id):
        """
        This function removes a movies from the current list of movies
        :param movie_id: an integer representing the is of a movie
        :return: -
        """
        self.remove_movie_based_rentals(movie_id)

        movies = self.get_movies()
        for movie in movies:
            if movie.get_movie_id() == movie_id:
                self.__repo.remove_movie(movie)
                return

        raise Exception("No movie with the id you provided was found")

    def modify_client(self, old_id, new_id, new_name):
        """
        This function modifies a client
        :param old_id: an integer representing the old id of a client
        :param new_id:an integer representing the new id of a client
        :param new_name: a string representing the new name of a client
        :return: -
        """
        new_client = Client(new_id, new_name)
        clients = self.get_clients()

        if old_id == new_id:
            self.validate_client_name(new_client)
            for client in clients:
                if client.get_client_id() == old_id:
                    client.set_name(new_name)
                    return
            raise Exception("No client with the id you provided was found")

        self.validate_client(new_client)
        for client in clients:
            if client.get_client_id() == old_id:
                client.set_client_id(new_id)
                client.set_name(new_name)
                return
        raise Exception("No client with the id you provided was found")

    def modify_movie(self, old_id, new_id, new_title, new_description, new_genre):
        """
        This function modifies a movie
        :param old_id: an integer representing the old id of a movie
        :param new_id: an integer representing the new id of a movie
        :param new_title: a string representing the title of a movie
        :param new_description: a string representing the description of a movie
        :param new_genre: a string representing the genre of a movie
        :return: -
        """
        new_movie = Movie(new_id, new_title, new_description, new_genre)
        movies = self.get_movies()

        if old_id == new_id:
            self.validate_movie_title_description_genre(new_movie)
            for movie in movies:
                if movie.get_movie_id() == old_id:
                    movie.set_title(new_title)
                    movie.set_description(new_description)
                    movie.set_genre(new_genre)
                    return
            raise Exception("No movie with the id you provided was found")

        self.validate_movie(new_movie)
        for movie in movies:
            if movie.get_movie_id() == old_id:
                movie.set_movie_id(new_id)
                movie.set_title(new_title)
                movie.set_description(new_description)
                movie.set_genre(new_genre)
                return
        raise Exception("No movie with the id you provided was found")

    def get_clients(self):
        return self.__repo.get_clients()

    def get_movies(self):
        return self.__repo.get_movies()

    def get_rentals(self):
        return self.__repo.get_rentals()

    def get_next_rental_id(self):
        rental_id = 0
        rentals = self.get_rentals()
        for rental in rentals:
            if rental.get_rental_id() > rental_id:
                rental_id = rental.get_rental_id()
        return rental_id + 1

    def get_next_client_id(self):
        client_id = 0
        clients = self.get_clients()
        for client in clients:
            if client.get_client_id() > client_id:
                client_id = client.get_client_id()
        return client_id + 1

    def get_next_movie_id(self):
        movie_id = 0
        movies = self.get_movies()
        for movie in movies:
            if movie.get_movie_id() > movie_id:
                movie_id = movie.get_movie_id()
        return movie_id + 1

    def get_clients_by_id(self, client_id):
        arr = []
        clients = self.get_clients()
        for client in clients:
            if client.get_client_id() == client_id:
                arr.append(client)
        return arr

    def get_clients_by_name(self, client_name):
        arr = []
        clients = self.get_clients()
        for client in clients:
            temp = client.get_name()
            temp = temp.lower()
            if client_name in temp:
                arr.append(client)
        return arr

    def get_movies_by_id(self, movie_id):
        arr = []
        movies = self.get_movies()
        for movie in movies:
            if movie.get_movie_id() == movie_id:
                arr.append(movie)
        return arr

    def get_movies_by_title(self, movie_title):
        arr = []
        movies = self.get_movies()
        for movie in movies:
            temp = movie.get_title()
            temp = temp.lower()
            if movie_title in temp:
                arr.append(movie)
        return arr

    def get_movies_by_description(self, movie_description):
        arr = []
        movies = self.get_movies()
        for movie in movies:
            temp = movie.get_description()
            temp = temp.lower()
            if movie_description in temp:
                arr.append(movie)
        return arr

    def get_movies_by_genre(self, movie_genre):
        arr = []
        movies = self.get_movies()
        for movie in movies:
            temp = movie.get_genre()
            temp = temp.lower()
            if movie_genre in temp:
                arr.append(movie)
        return arr

    def get_client_name_by_id(self, client_id):
        clients = self.get_clients()
        for client in clients:
            if client.get_client_id() == client_id:
                return client.get_name()
        raise Exception("No client with the id you provided was found")

    def get_most_rented_movies(self):
        dict = {}

        rentals = self.get_rentals()
        for rental in rentals:
            if rental.get_returned_date() == "0":
                continue

            rented_time = rental.get_rented_date().split("-")
            for i in range(len(rented_time)):
                rented_time[i] = int(rented_time[i])
            rented_time = date(rented_time[2], rented_time[1], rented_time[0])
            returned_time = rental.get_returned_date().split("-")
            for i in range(len(returned_time)):
                returned_time[i] = int(returned_time[i])
            returned_time = date(returned_time[2], returned_time[1], returned_time[0])

            days = (returned_time - rented_time).days + 1
            movie = self.get_movies_by_id(rental.get_movie_id())[0]

            if movie.get_title() in dict:
                dict[movie.get_title()] += days
            else:
                dict[movie.get_title()] = days

        arr1 = list(dict)
        arr2 = list(dict.values())
        for i in range(len(arr2)):
            for j in range(i, len(arr2)):
                if arr2[i] < arr2[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                    arr2[i], arr2[j] = arr2[j], arr2[i]

        arr = []
        for i in range(len(arr1)):
            arr.append((arr1[i], arr2[i]))
        return arr

    def get_most_active_clients(self):
        dict = {}

        rentals = self.get_rentals()
        for rental in rentals:
            if rental.get_returned_date() == "0":
                continue

            rented_time = rental.get_rented_date().split("-")
            for i in range(len(rented_time)):
                rented_time[i] = int(rented_time[i])
            rented_time = date(rented_time[2], rented_time[1], rented_time[0])
            returned_time = rental.get_returned_date().split("-")
            for i in range(len(returned_time)):
                returned_time[i] = int(returned_time[i])
            returned_time = date(returned_time[2], returned_time[1], returned_time[0])

            days = (returned_time - rented_time).days + 1
            client_id = rental.get_client_id()

            if client_id in dict:
                dict[client_id] += days
            else:
                dict[client_id] = days

        arr1 = list(dict)
        arr2 = list(dict.values())
        for i in range(len(arr2)):
            for j in range(i, len(arr2)):
                if arr2[i] < arr2[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                    arr2[i], arr2[j] = arr2[j], arr2[i]

        arr = []
        for i in range(len(arr1)):
            arr.append((arr1[i], arr2[i]))
        return arr

    def get_late_rentals(self, current_date):
        arr1, arr2 = [], []

        date_time = current_date.split("-")
        for i in range(len(date_time)):
            date_time[i] = int(date_time[i])
        date_time = date(date_time[2], date_time[1], date_time[0])

        rentals = self.get_rentals()
        for rental in rentals:
            if rental.get_returned_date() == "0":
                due_time = rental.get_due_date().split("-")
                for i in range(len(due_time)):
                    due_time[i] = int(due_time[i])
                due_time = date(due_time[2], due_time[1], due_time[0])

                if date_time > due_time:
                    arr1.append(rental.get_movie_id())
                    arr2.append((date_time - due_time).days)

        for i in range(len(arr2)):
            for j in range(i, len(arr2)):
                if arr2[i] < arr2[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                    arr2[i], arr2[j] = arr2[j], arr2[i]

        arr = []
        for i in range(len(arr1)):
            arr.append((arr1[i], arr2[i]))
        return arr

    @staticmethod
    def validate_date(date):
        date = date.split("-")
        for i in range(len(date)):
            date[i] = int(date[i])
        if len(date) != 3:
            raise Exception("The returned date is invalid")
        else:
            datetime.datetime(date[2], date[1], date[0])

    def validate_client(self, client):
        """
        This function validates an object of type client
        :param client: an object of type client
        :return: -, if no exceptions are raised
        """
        errors = ""

        # Validating the id
        clients = self.get_clients()
        for elem in clients:
            if elem.get_client_id() == client.get_client_id():
                errors += "A client with this id already exists\n"

        # Validating the name
        client_name = client.get_name()
        client_name = client_name.strip()
        if client_name == "":
            errors += "The client name cannot be empty\n"
        if not client_name.isalpha():
            errors += "The client name cannot contain any special characters\n"

        if len(errors) > 0:
            raise Exception(errors)

    def validate_movie(self, movie):
        """
        This function validates an object of type movie
        :param movie: an object of type movie
        :return: -, if no exception are raised
        """
        errors = ""

        # Validating the id
        movies = self.get_movies()
        for elem in movies:
            if elem.get_movie_id() == movie.get_movie_id():
                errors += "A movie with this id already exists\n"

        # Validating the title
        movie_title = movie.get_title()
        movie_title = movie_title.strip()
        if movie_title == "":
            errors += "The movie title cannot be empty\n"
        if not movie_title.isalpha():
            errors += "The movie title cannot contain any special characters\n"

        # Validating the description
        movie_description = movie.get_description()
        movie_description = movie_description.strip()
        if movie_description == "":
            errors += "The movie description cannot be empty\n"
        if not movie_description.isalpha():
            errors += "The movie description cannot contain any special characters\n"

        # Validating the genre
        movie_genre = movie.get_genre()
        movie_genre = movie_genre.strip()
        if movie_genre == "":
            errors += "The movie genre cannot be empty\n"
        if not movie_genre.isalpha():
            errors += "The movie genre cannot contain any special characters\n"

        if len(errors) > 0:
            raise Exception(errors)

    def validate_movie_title_description_genre(self, movie):
        errors = ""

        # Validating the title
        movie_title = movie.get_title()
        movie_title = movie_title.strip()
        if movie_title == "":
            errors += "The movie title cannot be empty\n"
        if not movie_title.isalpha():
            errors += "The movie title cannot contain any special characters\n"

        # Validating the description
        movie_description = movie.get_description()
        movie_description = movie_description.strip()
        if movie_description == "":
            errors += "The movie description cannot be empty\n"
        if not movie_description.isalpha():
            errors += "The movie description cannot contain any special characters\n"

        # Validating the genre
        movie_genre = movie.get_genre()
        movie_genre = movie_genre.strip()
        if movie_genre == "":
            errors += "The movie genre cannot be empty\n"
        if not movie_genre.isalpha():
            errors += "The movie genre cannot contain any special characters\n"

        if len(errors) > 0:
            raise Exception(errors)

    @staticmethod
    def validate_client_name(client):
        """
        This function validates the name of a client
        :param client: an object of type client
        :return: -, if no exception are raised
        """
        errors = ""

        client_name = client.get_name()
        client_name = client_name.strip()
        if client_name == "":
            errors += "The client name cannot be empty\n"
        if not client_name.isalpha():
            errors += "The client name cannot contain any special characters\n"

        if len(errors) > 0:
            raise Exception(errors)

    def generate_clients(self):
        names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry", "Ivy", "Jack",
                 "Kate", "Leo", "Mia", "Nathan", "Olivia", "Peter", "Quinn", "Rachel", "Sam", "Tina",
                 "Ulysses", "Victoria", "Walter", "Xena", "Yasmine", "Zach"]
        for i in range(20):
            client = Client(i, random.choice(names))
            self.__repo.add_client(client)

    def generate_movies(self):
        arr1 = ["Adventurous", "Mysterious", "Enchanting", "Thrilling", "Epic", "Whimsical",
                "Daring", "Spectacular", "Intriguing", "Fantastic"]
        arr2 = ["Journey", "Quest", "Mystery", "Adventure", "Discovery", "Enigma", "Legacy",
                "Odyssey", "Legend", "Miracle"]
        for i in range(20):
            movie_id = i
            movie_title = random.choice(arr1) + " " + random.choice(arr2)
            movie_description = random.choice(arr1)
            movie_genre = random.choice(arr2)
            movie = Movie(movie_id, movie_title, movie_description, movie_genre)
            self.__repo.add_movie(movie)

    def generate_rentals(self):
        for i in range(20):
            rental_id = i
            movie_id = i
            client_id = i
            lower_bound = random.randint(1, 15)
            upper_bound = random.randint(15, 30)
            rented_date = str(lower_bound) + "-11-2023"
            returned_date = str(random.randint(lower_bound, upper_bound)) + "-11-2023"
            due_date = str(upper_bound) + "-11-2023"
            rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
            self.__repo.add_rental(rental)
