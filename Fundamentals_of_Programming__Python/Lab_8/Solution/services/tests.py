import unittest


from Fundamentals_of_Programming__Python.Lab_8.Solution.domain.client import Client
from Fundamentals_of_Programming__Python.Lab_8.Solution.domain.movie import Movie
from Fundamentals_of_Programming__Python.Lab_8.Solution.domain.rental import Rental
from Fundamentals_of_Programming__Python.Lab_8.Solution.services.services import Services


class Tests(unittest.TestCase):
    def test_client_str(self):
        self.__services = Services(False)

        client_id = 4312
        client_name = "John"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)

        self.assertEqual(self.__services.get_clients()[0].__str__(), "id: 4312, name: John")

    def test_movie_str(self):
        self.__services = Services(False)

        movie_id = 1
        movie_title = "Terminator"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)

        self.assertEqual(self.__services.get_movies()[0].__str__(), "id: 1, title: Terminator, "
                                                                            "description: Fantasy, genre: Horror")

    def test_rental_str(self):
        self.__services = Services(False)

        movie_id = 1
        movie_title = "Terminator"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)

        client_id = 1
        client_name = "John"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)

        rental_id = 1
        movie_id = 1
        client_id = 1
        rented_date = "10-10-2023"
        due_date = "10-10-2023"
        returned_date = "0"
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self.__services.validate_and_add_rental(rental)

        self.assertEqual(self.__services.get_rentals()[0].__str__(), "rental id: 1, movie id: 1, client id: 1, "
                                                                             "rented date: 10-10-2023, due date: "
                                                                             "10-10-2023, returned date: 0")

    def test_validate_and_add_client(self):
        self.__services = Services(False)

        client_id = 4312
        client_name = "John"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)

        self.assertEqual(self.__services.get_clients()[0].get_client_id(), 4312)
        self.assertEqual(self.__services.get_clients()[0].get_name(), "John")

    def test_get_clients_by_id(self):
        self.__services = Services(False)

        client_id = 4312
        client_name = "John"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)

        self.assertEqual(self.__services.get_clients_by_id(client_id)[0].get_name(), "John")

    def test_modify_client(self):
        self.__services = Services(False)

        client_id = 1
        client_name = "John"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)

        try:
            self.assertRaises(self.__services.modify_client(4, 2, "John"))
        except Exception:
            pass
        try:
            self.assertRaises(self.__services.modify_client(4, 4, "John"))
        except Exception:
            pass
        self.__services.modify_client(1, 2, "John")
        self.__services.modify_client(2, 2, "John")

        self.assertEqual(self.__services.get_clients()[0].get_name(), "John")

    def test_validate_client(self):
        self.__services = Services(False)

        client_id = 4312
        client_name = ""
        client = Client(client_id, client_name)
        try:
            self.assertRaises(self.__services.validate_client(client))
        except Exception:
            pass

        client_id = 4312
        client_name = "John"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)
        try:
            self.assertRaises(self.__services.validate_client(client))
        except Exception:
            pass

    def test_get_clients_by_name(self):
        self.__services = Services(False)

        client_id = 4312
        client_name = "John"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)

        self.assertEqual(self.__services.get_clients_by_name("j")[0].get_name(), "John")

    def test_get_movies_by_title(self):
        self.__services = Services(False)

        movie_id = 1
        movie_title = "Terminator"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)

        self.assertEqual(self.__services.get_movies_by_title("t")[0].get_title(), "Terminator")

    def test_modify_movie(self):
        self.__services = Services(False)

        movie_id = 1
        movie_title = "Terminator"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)

        try:
            self.assertRaises(self.__services.modify_movie(4, 2, "Terminator", "Fantasy", "Horror"))
        except Exception:
            pass
        try:
            self.assertRaises(self.__services.modify_movie(4, 4, "Terminator", "Fantasy", "Horror"))
        except Exception:
            pass
        self.__services.modify_movie(1, 2, "Terminator", "Fantasy", "Horror")
        self.__services.modify_movie(2, 2, "Terminator", "Fantasy", "Horror")

        self.assertEqual(self.__services.get_movies()[0].get_movie_id(), 2)

    def test_get_movies_by_description(self):
        self.__services = Services(False)

        movie_id = 1
        movie_title = "Terminator"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)

        self.assertEqual(self.__services.get_movies_by_description("f")[0].get_description(), "Fantasy")

    def test_remove_movie(self):
        self.__services = Services(False)

        movie_id = 1
        movie_title = "Terminator"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)

        try:
            self.assertRaises(self.__services.remove_movie(3))
        except Exception:
            pass
        self.__services.remove_movie(1)
        self.assertEqual(self.__services.get_movies(), [])

    def test_get_movies_by_genre(self):
        self.__services = Services(False)

        movie_id = 1
        movie_title = "Terminator"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)

        self.assertEqual(self.__services.get_movies_by_genre("h")[0].get_genre(), "Horror")

    def test_validate_and_add_movie(self):
        self.__services = Services(False)

        movie_id = 1
        movie_title = "Terminator"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)

        self.assertEqual(self.__services.get_movies()[0].get_movie_id(), 1)
        self.assertEqual(self.__services.get_movies()[0].get_title(), "Terminator")
        self.assertEqual(self.__services.get_movies()[0].get_description(), "Fantasy")
        self.assertEqual(self.__services.get_movies()[0].get_genre(), "Horror")

    def test_validate_movie(self):
        self.__services = Services(False)

        movie_id = 1
        movie_title = ""
        movie_description = ""
        movie_genre = ""
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        try:
            self.assertRaises(self.__services.validate_movie(movie))
        except Exception:
            pass

        movie_id = 1
        movie_title = "Terminator"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)
        try:
            self.assertRaises(self.__services.validate_movie(movie))
        except Exception:
            pass

    def test_validate_and_add_rental(self):
        self.__services = Services(False)

        movie_id = 1
        movie_title = "Terminator"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)

        client_id = 1
        client_name = "John"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)

        rental_id = 1
        movie_id = 1
        client_id = 1
        rented_date = "10-10-2023"
        due_date = "10-10-2023"
        returned_date = "0"
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self.__services.validate_and_add_rental(rental)

        self.assertEqual(self.__services.get_rentals()[0].get_rental_id(), 1)
        self.assertEqual(self.__services.get_rentals()[0].get_movie_id(), 1)
        self.assertEqual(self.__services.get_rentals()[0].get_client_id(), 1)
        self.assertEqual(self.__services.get_rentals()[0].get_rented_date(), "10-10-2023")
        self.assertEqual(self.__services.get_rentals()[0].get_due_date(), "10-10-2023")
        self.assertEqual(self.__services.get_rentals()[0].get_returned_date(), "0")

    def test_remove_movie_based_rentals(self):
        self.__services = Services(False)

        movie_id = 1
        movie_title = "Terminator"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)

        client_id = 1
        client_name = "John"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)

        rental_id = 1
        movie_id = 1
        client_id = 1
        rented_date = "10-10-2023"
        due_date = "10-10-2023"
        returned_date = "0"
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self.__services.validate_and_add_rental(rental)

        self.__services.remove_movie_based_rentals(1)
        self.assertEqual(self.__services.get_rentals(), [])

    def test_remove_client_based_rentals(self):
        self.__services = Services(False)

        movie_id = 1
        movie_title = "Terminator"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)

        client_id = 1
        client_name = "John"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)

        rental_id = 1
        movie_id = 1
        client_id = 1
        rented_date = "10-10-2023"
        due_date = "10-10-2023"
        returned_date = "0"
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self.__services.validate_and_add_rental(rental)

        self.__services.remove_client_based_rentals(1)
        self.assertEqual(self.__services.get_rentals(), [])

    def test_return_movie(self):
        self.__services = Services(False)

        movie_id = 1
        movie_title = "Terminator"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)

        client_id = 1
        client_name = "John"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)

        rental_id = 1
        movie_id = 1
        client_id = 1
        rented_date = "10-10-2023"
        due_date = "10-10-2023"
        returned_date = "0"
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self.__services.validate_and_add_rental(rental)

        self.__services.return_movie(1, "10-10-2023")
        self.assertEqual(self.__services.get_rentals()[0].get_returned_date(), "10-10-2023")

    def test_generate_clients(self):
        self.__services = Services(False)

        self.__services.generate_clients()
        self.assertNotEqual(self.__services.get_clients(), [])

    def test_generate_movies(self):
        self.__services = Services(False)

        self.__services.generate_movies()
        self.assertNotEqual(self.__services.get_movies, [])

    def test_generate_rentals(self):
        self.__services = Services(False)

        self.__services.generate_rentals()
        self.assertNotEqual(self.__services.get_rentals, [])

    def test_validate_validate_movie_title_description_genre(self):
        self.__services = Services(False)

        movie_id = 1
        movie_title = ""
        movie_description = ""
        movie_genre = ""
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        try:
            self.assertRaises(self.__services.validate_movie_title_description_genre(movie))
        except Exception:
            pass

    def test_validate_client_name(self):
        self.__services = Services(False)

        client_id = 4312
        client_name = ""
        client = Client(client_id, client_name)
        try:
            self.assertRaises(self.__services.validate_client_name(client))
        except Exception:
            pass

    def test_random(self):
        self.__services = Services(True)

        self.assertNotEqual(self.__services.get_rentals(), [])

    def test_validate_date(self):
        self.__services = Services(False)

        date = "10-10-2023"
        try:
            self.assertRaises(self.__services.validate_date(date))
        except Exception:
            pass
        date = "10-10"
        try:
            self.assertRaises(self.__services.validate_date(date))
        except Exception:
            pass

    def test_get_next_rental_id(self):
        self.__services = Services(False)

        movie_id = 1
        movie_title = "Terminator"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)

        client_id = 1
        client_name = "John"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)

        rental_id = 1
        movie_id = 1
        client_id = 1
        rented_date = "10-10-2023"
        due_date = "10-10-2023"
        returned_date = "0"
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self.__services.validate_and_add_rental(rental)

        next_rental_id = self.__services.get_next_rental_id()
        self.assertEqual(next_rental_id, 2)

    def test_get_next_client_id(self):
        self.__services = Services(False)

        client_id = 1
        client_name = "John"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)

        next_client_id = self.__services.get_next_client_id()
        self.assertEqual(next_client_id, 2)

    def test_get_next_movie_id(self):
        self.__services = Services(False)

        movie_id = 1
        movie_title = "Terminator"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)

        next_movie_id = self.__services.get_next_movie_id()
        self.assertEqual(next_movie_id, 2)

    def test_get_client_name_by_id(self):
        self.__services = Services(False)

        client_id = 1
        client_name = "John"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)

        name = self.__services.get_client_name_by_id(client_id)
        self.assertEqual(name, "John")

        try:
            self.__services.get_client_name_by_id(0)
        except Exception:
            pass

    def test_get_most_rented_movies(self):
        self.__services = Services(False)

        movie_id = 1
        movie_title = "Terminator"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)
        movie_id = 2
        movie_title = "Fantasy"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)
        movie_id = 3
        movie_title = "Fantasy"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)
        movie_id = 4
        movie_title = "Fantasy"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)

        client_id = 1
        client_name = "John"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)
        client_id = 2
        client_name = "Mike"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)
        client_id = 3
        client_name = "Tim"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)
        client_id = 4
        client_name = "Sam"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)


        rental_id = 1
        movie_id = 1
        client_id = 1
        rented_date = "10-10-2023"
        due_date = "10-10-2023"
        returned_date = "10-10-2023"
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self.__services.validate_and_add_rental(rental)
        rental_id = 2
        movie_id = 2
        client_id = 2
        rented_date = "10-10-2023"
        due_date = "10-10-2023"
        returned_date = "0"
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self.__services.validate_and_add_rental(rental)
        rental_id = 3
        movie_id = 3
        client_id = 3
        rented_date = "10-10-2023"
        due_date = "17-10-2023"
        returned_date = "15-10-2023"
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self.__services.validate_and_add_rental(rental)
        rental_id = 4
        movie_id = 4
        client_id = 4
        rented_date = "10-10-2023"
        due_date = "17-10-2023"
        returned_date = "15-10-2023"
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self.__services.validate_and_add_rental(rental)

        self.assertEqual(self.__services.get_most_rented_movies()[0][1], 12)

    def test_remove_client(self):
        self.__services = Services(False)

        client_id = 1
        client_name = "John"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)

        self.__services.remove_client(client_id)
        self.assertEqual(self.__services.get_clients(), [])

        try:
            self.__services.remove_client(client_id)
        except Exception:
            pass

    def test_get_late_rentals(self):
        self.__services = Services(False)

        movie_id = 1
        movie_title = "Terminator"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)
        movie_id = 2
        movie_title = "Fantasy"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)
        movie_id = 3
        movie_title = "Fantasy"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)
        movie_id = 4
        movie_title = "Fantasy"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)

        client_id = 1
        client_name = "John"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)
        client_id = 2
        client_name = "Mike"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)
        client_id = 3
        client_name = "Tim"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)
        client_id = 4
        client_name = "Sam"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)


        rental_id = 1
        movie_id = 1
        client_id = 1
        rented_date = "10-10-2023"
        due_date = "19-10-2023"
        returned_date = "0"
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self.__services.validate_and_add_rental(rental)
        rental_id = 2
        movie_id = 2
        client_id = 2
        rented_date = "10-10-2023"
        due_date = "20-10-2023"
        returned_date = "0"
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self.__services.validate_and_add_rental(rental)
        rental_id = 3
        movie_id = 3
        client_id = 3
        rented_date = "10-10-2023"
        due_date = "17-10-2023"
        returned_date = "0"
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self.__services.validate_and_add_rental(rental)
        rental_id = 4
        movie_id = 4
        client_id = 4
        rented_date = "10-10-2023"
        due_date = "17-10-2023"
        returned_date = "0"
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self.__services.validate_and_add_rental(rental)

        self.assertEqual(self.__services.get_late_rentals("12-12-2300")[0][1], 101228)

    def test_get_most_active_clients(self):
        self.__services = Services(False)

        movie_id = 1
        movie_title = "Terminator"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)
        movie_id = 2
        movie_title = "Fantasy"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)
        movie_id = 3
        movie_title = "Fantasy"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)
        movie_id = 4
        movie_title = "Fantasy"
        movie_description = "Fantasy"
        movie_genre = "Horror"
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__services.validate_and_add_movie(movie)

        client_id = 1
        client_name = "John"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)
        client_id = 2
        client_name = "Mike"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)
        client_id = 3
        client_name = "Tim"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)
        client_id = 4
        client_name = "Sam"
        client = Client(client_id, client_name)
        self.__services.validate_and_add_client(client)


        rental_id = 1
        movie_id = 1
        client_id = 1
        rented_date = "10-10-2023"
        due_date = "19-10-2023"
        returned_date = "19-10-2023"
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self.__services.validate_and_add_rental(rental)
        rental_id = 2
        movie_id = 2
        client_id = 2
        rented_date = "10-10-2023"
        due_date = "20-10-2023"
        returned_date = "20-10-2023"
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self.__services.validate_and_add_rental(rental)
        rental_id = 3
        movie_id = 2
        client_id = 2
        rented_date = "10-10-2023"
        due_date = "17-10-2023"
        returned_date = "17-10-2023"
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self.__services.validate_and_add_rental(rental)
        rental_id = 4
        movie_id = 4
        client_id = 4
        rented_date = "10-10-2023"
        due_date = "17-10-2023"
        returned_date = "0"
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self.__services.validate_and_add_rental(rental)

        self.assertEqual(self.__services.get_most_active_clients()[0][0], 2)
