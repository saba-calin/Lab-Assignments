import tkinter as tk

from src.services.services import Services
from src.domain.client import Client
from src.domain.movie import Movie
from src.domain.rental import Rental


class TkinterUI:
    def __init__(self):
        self.__services = Services(True)

        self.__window = tk.Tk()
        self.__window.geometry("1920x1080")

    def start_program(self):
        self.__print_menu()

    def __print_menu(self):
        self.__clear_window()
        button1 = tk.Button(self.__window, text="Manage clients.", command=self.__print_manage_clients_menu)
        button2 = tk.Button(self.__window, text="Manage movies.", command=self.__print_manage_movies_menu)
        button3 = tk.Button(self.__window, text="Manage rentals.", command=self.__print_manage_rentals_menu)
        button4 = tk.Button(self.__window, text="Search for clients.", command=self.__print_search_for_clients_menu)
        button5 = tk.Button(self.__window, text="Search for movies.", command=self.__print_search_for_movies_menu)
        button6 = tk.Button(self.__window, text="Create statistics.", command=self.__print_statistics_menu)
        button7 = tk.Button(self.__window, text="Exit the application.", command=exit)
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()
        button7.pack()
        self.__window.mainloop()

    def __print_manage_clients_menu(self):
        self.__clear_window()
        button1 = tk.Button(self.__window, text="Add a client.", command=self.__add_client)
        button2 = tk.Button(self.__window, text="Delete a client.", command=self.__remove_client)
        button3 = tk.Button(self.__window, text="Modify the list of clients..", command=self.__modify_client)
        button4 = tk.Button(self.__window, text="Display the list of clients.", command=self.__print_clients)
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        self.__window.mainloop()

    def __print_manage_movies_menu(self):
        self.__clear_window()
        button1 = tk.Button(self.__window, text="Add a movie.", command=self.__add_movie)
        button2 = tk.Button(self.__window, text="Delete a movie.", command=self.__remove_movie)
        button3 = tk.Button(self.__window, text="Modify the list of movies.", command=self.__modify_movie)
        button4 = tk.Button(self.__window, text="Display the list of movies.", command=self.__print_movies)
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        self.__window.mainloop()

    def __print_manage_rentals_menu(self):
        self.__clear_window()
        button1 = tk.Button(self.__window, text="Rent a movie.", command=self.__rent_movie)
        button2 = tk.Button(self.__window, text="Return a movie.", command=self.__return_movie)
        button3 = tk.Button(self.__window, text="Display the list of rentals.", command=self.__print_rentals)
        button1.pack()
        button2.pack()
        button3.pack()
        self.__window.mainloop()

    def __print_search_for_clients_menu(self):
        self.__clear_window()
        button1 = tk.Button(self.__window, text="Search for clients by id.", command=self.__search_for_clients_by_id)
        button2 = tk.Button(self.__window, text="Search for clients by name.", command=self.__search_for_clients_by_name)
        button1.pack()
        button2.pack()
        self.__window.mainloop()

    def __print_search_for_movies_menu(self):
        self.__clear_window()
        button1 = tk.Button(self.__window, text="Search for movies by id.", command=self.__search_for_movies_by_id)
        button2 = tk.Button(self.__window, text="Search for movies by title.", command=self.__search_for_movies_by_title)
        button3 = tk.Button(self.__window, text="Search for movies by description.", command=self.__search_for_movies_by_description)
        button4 = tk.Button(self.__window, text="Search for movies by genre.", command=self.__search_for_movies_by_genre)
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        self.__window.mainloop()

    def __print_statistics_menu(self):
        self.__clear_window()
        button1 = tk.Button(self.__window, text="Display the most rented movies.", command=self.__print_most_rented_movies)
        button2 = tk.Button(self.__window, text="Display the most active clients.", command=self.__print_most_active_clients)
        button3 = tk.Button(self.__window, text="Display the late rentals.", command=self.__print_late_rentals)
        button1.pack()
        button2.pack()
        button3.pack()
        self.__window.mainloop()

    def __clear_window(self):
        widgets = self.__window.winfo_children()
        for widget in widgets:
            widget.destroy()

    def __search_for_clients_by_id(self):
        self.__clear_window()
        id_label = tk.Label(self.__window, text="client id = ")
        id_label.pack()
        id_entry = tk.Entry(self.__window)
        id_entry.pack()
        id_button = tk.Button(self.__window, text="Search", command=lambda: self.
                              __search_for_clients_by_id_lambda(int(id_entry.get())))
        id_button.pack()
        self.__window.mainloop()

    def __search_for_clients_by_id_lambda(self, client_id):
        self.__clear_window()
        clients = self.__services.get_clients_by_id(client_id)

        if len(clients) == 0:
            text_label = tk.Label(self.__window, text="There are no clients in the list")
            text_label.pack()
        else:
            for client in clients:
                client_label = tk.Label(self.__window, text="id: " + str(client.get_client_id()) +
                                                            ", name: " + client.get_name())
                client_label.pack()

        menu_button = tk.Button(self.__window, text="Back to menu", command=self.__print_menu)
        menu_button.pack()
        self.__window.mainloop()

    def __search_for_clients_by_name(self):
        self.__clear_window()
        name_label = tk.Label(self.__window, text="name = ")
        name_label.pack()
        name_entry = tk.Entry(self.__window)
        name_entry.pack()
        id_button = tk.Button(self.__window, text="Search", command=lambda: self.
                              __search_for_clients_by_name_lambda(name_entry.get()))
        id_button.pack()
        self.__window.mainloop()

    def __search_for_clients_by_name_lambda(self, client_name):
        self.__clear_window()
        clients = self.__services.get_clients_by_name(client_name)

        if len(clients) == 0:
            text_label = tk.Label(self.__window, text="There are no clients in the list")
            text_label.pack()
        else:
            for client in clients:
                client_label = tk.Label(self.__window, text="id: " + str(client.get_client_id()) +
                                                            ", name: " + client.get_name())
                client_label.pack()

        menu_button = tk.Button(self.__window, text="Back to menu", command=self.__print_menu)
        menu_button.pack()
        self.__window.mainloop()

    def __search_for_movies_by_id(self):
        self.__clear_window()
        id_label = tk.Label(self.__window, text="id = ")
        id_label.pack()
        id_entry = tk.Entry(self.__window)
        id_entry.pack()
        id_button = tk.Button(self.__window, text="Search", command=lambda: self.
                              __search_for_movies_by_id_lambda(int(id_entry.get())))
        id_button.pack()

    def __search_for_movies_by_id_lambda(self, movie_id):
        self.__clear_window()
        movies = self.__services.get_movies_by_id(movie_id)

        if len(movies) == 0:
            text_label = tk.Label(self.__window, text="There are no movies in the list")
            text_label.pack()
        else:
            for movie in movies:
                movie_label = tk.Label(self.__window, text="id: " + str(movie.get_movie_id()) +
                                                           ", title: " + movie.get_title() +
                                                           ", description: " + movie.get_description() +
                                                           ", genre: " + movie.get_genre())
                movie_label.pack()

        menu_button = tk.Button(self.__window, text="Back to menu", command=self.__print_menu)
        menu_button.pack()
        self.__window.mainloop()

    def __search_for_movies_by_title(self):
        self.__clear_window()
        title_label = tk.Label(self.__window, text="title = ")
        title_label.pack()
        title_entry = tk.Entry(self.__window)
        title_entry.pack()
        id_button = tk.Button(self.__window, text="Search", command=lambda: self.
                              __search_for_movies_by_title_lambda(title_entry.get()))
        id_button.pack()
        self.__window.mainloop()

    def __search_for_movies_by_title_lambda(self, movie_title):
        self.__clear_window()
        movies = self.__services.get_movies_by_title(movie_title)

        if len(movies) == 0:
            text_label = tk.Label(self.__window, text="There are no movies in the list")
            text_label.pack()
        else:
            for movie in movies:
                movie_label = tk.Label(self.__window, text="id: " + str(movie.get_movie_id()) +
                                                           ", title: " + movie.get_title() +
                                                           ", description: " + movie.get_description() +
                                                           ", genre: " + movie.get_genre())
                movie_label.pack()

        menu_button = tk.Button(self.__window, text="Back to menu", command=self.__print_menu)
        menu_button.pack()
        self.__window.mainloop()

    def __search_for_movies_by_description(self):
        self.__clear_window()
        description_label = tk.Label(self.__window, text="description = ")
        description_label.pack()
        description_entry = tk.Entry(self.__window)
        description_entry.pack()
        id_button = tk.Button(self.__window, text="Search", command=lambda: self.
                              __search_for_movies_by_description_lambda(description_entry.get()))
        id_button.pack()
        self.__window.mainloop()

    def __search_for_movies_by_description_lambda(self, movie_description):
        self.__clear_window()
        movies = self.__services.get_movies_by_description(movie_description)

        if len(movies) == 0:
            text_label = tk.Label(self.__window, text="There are no movies in the list")
            text_label.pack()
        else:
            for movie in movies:
                movie_label = tk.Label(self.__window, text="id: " + str(movie.get_movie_id()) +
                                                           ", title: " + movie.get_title() +
                                                           ", description: " + movie.get_description() +
                                                           ", genre: " + movie.get_genre())
                movie_label.pack()

        menu_button = tk.Button(self.__window, text="Back to menu", command=self.__print_menu)
        menu_button.pack()
        self.__window.mainloop()

    def __search_for_movies_by_genre(self):
        self.__clear_window()
        genre_label = tk.Label(self.__window, text="genre = ")
        genre_label.pack()
        genre_entry = tk.Entry(self.__window)
        genre_entry.pack()
        id_button = tk.Button(self.__window, text="Search", command=lambda: self.
                              __search_for_movies_by_genre_lambda(genre_entry.get()))
        id_button.pack()
        self.__window.mainloop()

    def __search_for_movies_by_genre_lambda(self, movie_genre):
        self.__clear_window()
        movies = self.__services.get_movies_by_genre(movie_genre)

        if len(movies) == 0:
            text_label = tk.Label(self.__window, text="There are no movies in the list")
            text_label.pack()
        else:
            for movie in movies:
                movie_label = tk.Label(self.__window, text="id: " + str(movie.get_movie_id()) +
                                                           ", title: " + movie.get_title() +
                                                           ", description: " + movie.get_description() +
                                                           ", genre: " + movie.get_genre())
                movie_label.pack()

        menu_button = tk.Button(self.__window, text="Back to menu", command=self.__print_menu)
        menu_button.pack()
        self.__window.mainloop()

    def __print_most_rented_movies(self):
        self.__clear_window()
        movies = self.__services.get_most_rented_movies()

        if len(movies) == 0:
            text_label = tk.Label(self.__window, text="There are no clients in the list")
            text_label.pack()
        else:
            for movie in movies:
                client_label = tk.Label(self.__window, text="title: " + movie[0] +
                                                            ", days: " + str(movie[1]))
                client_label.pack()

        menu_button = tk.Button(self.__window, text="Back to menu", command=self.__print_menu)
        menu_button.pack()
        self.__window.mainloop()

    def __print_most_active_clients(self):
        self.__clear_window()
        movies = clients = self.__services.get_most_active_clients()

        if len(clients) == 0:
            text_label = tk.Label(self.__window, text="There are no clients in the list")
            text_label.pack()
        else:
            for client in clients:
                client_label = tk.Label(self.__window, text="client: " + self.__services.get_client_name_by_id(client[0]) +
                                                            ", days: " + str(client[1]))
                client_label.pack()

        menu_button = tk.Button(self.__window, text="Back to menu", command=self.__print_menu)
        menu_button.pack()
        self.__window.mainloop()

    def __print_late_rentals(self):
        self.__clear_window()
        data_label = tk.Label(self.__window, text = "current date(dd/mm/yyyy) = ")
        data_label.pack()
        data_entry = tk.Entry(self.__window)
        data_entry.pack()
        search_button = tk.Button(self.__window, text = "Search", command=lambda:self.__print_late_rentals_lambda(data_entry.get()))
        search_button.pack()
        self.__window.mainloop()

        # current_date = input("current date(dd-mm-yyyy) = ")
        # rentals = self.__services.get_late_rentals(current_date)
        #
        # if len(rentals) == 0:
        #     print("There are no rentals in the list")
        #     return
        #
        # for rental in rentals:
        #     print("movie id: " + str(rental[0]) + ", days: " + str(rental[1]))

    def __print_late_rentals_lambda(self, current_date):
        self.__clear_window()
        rentals = self.__services.get_late_rentals(current_date)

        if len(rentals) == 0:
            text_label = tk.Label(self.__window, text="There are no late rentals")
            text_label.pack()
        else:
            for rental in rentals:
                client_label = tk.Label(self.__window, text="movie_id: " + str(rental[0]) +
                                                            ", days: " + str(rental[1]))
                client_label.pack()

        menu_button = tk.Button(self.__window, text="Back to menu", command=self.__print_menu)
        menu_button.pack()
        self.__window.mainloop()

    def __rent_movie(self):
        self.__clear_window()
        rental_id = self.__services.get_next_rental_id()
        movie_label = tk.Label(self.__window, text="movie id = ")
        movie_label.pack()
        movie_entry = tk.Entry(self.__window)
        movie_entry.pack()
        client_label = tk.Label(self.__window, text="client id = ")
        client_label.pack()
        client_entry = tk.Entry(self.__window)
        client_entry.pack()
        rented_label = tk.Label(self.__window, text="rented date(dd-mm-yyyy) = ")
        rented_label.pack()
        rented_entry = tk.Entry(self.__window)
        rented_entry.pack()
        due_label = tk.Label(self.__window, text="due date(dd-mm-yyyy) = ")
        due_label.pack()
        due_entry = tk.Entry(self.__window)
        due_entry.pack()
        returned_date = "0"
        add_button = tk.Button(self.__window, text="Rent movie", command=lambda: self.__rent_movie_lambda(rental_id,
                                                                                                          int(movie_entry.get()),
                                                                                                          int(client_entry.get()),
                                                                                                          rented_entry.get(),
                                                                                                          due_entry.get(),
                                                                                                          returned_date))
        add_button.pack()
        self.__window.mainloop()

    def __rent_movie_lambda(self, rental_id, movie_id, client_id, rented_date, due_date, returned_date):
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self.__services.validate_and_add_rental(rental)
        self.__print_menu()

    def __return_movie(self):
        self.__clear_window()
        id_label = tk.Label(self.__window, text="movie id = ")
        id_label.pack()
        id_entry = tk.Entry(self.__window)
        id_entry.pack()
        returned_label = tk.Label(self.__window, text="returned date(dd-mm-yyyy) = ")
        returned_label.pack()
        returned_entry = tk.Entry(self.__window)
        returned_entry.pack()
        return_button = tk.Button(self.__window, text="Return movie", command=lambda: self.
                                  __return_movie_lambda(int(id_entry.get()), returned_entry.get()))
        return_button.pack()
        self.__window.mainloop()

    def __return_movie_lambda(self, movie_id, returned_date):
        self.__services.return_movie(movie_id, returned_date)
        self.__print_menu()

    def __add_client(self):
        self.__clear_window()
        client_id = self.__services.get_next_client_id()
        name_label = tk.Label(self.__window, text="name = ")
        name_label.pack()
        name_entry = tk.Entry(self.__window)
        name_entry.pack()
        add_button = tk.Button(self.__window, text="Add client", command=lambda: self.__add_client_lambda(
            Client(client_id, name_entry.get())))
        add_button.pack()
        self.__window.mainloop()

    def __add_client_lambda(self, client):
        self.__services.validate_and_add_client(client)
        self.__print_menu()

    def __add_movie(self):
        self.__clear_window()
        movie_id = self.__services.get_next_movie_id()
        title_label = tk.Label(self.__window, text="title = ")
        title_label.pack()
        title_entry = tk.Entry(self.__window)
        title_entry.pack()
        description_label = tk.Label(self.__window, text="description = ")
        description_label.pack()
        description_entry = tk.Entry(self.__window)
        description_entry.pack()
        genre_label = tk.Label(self.__window, text="genre = ")
        genre_label.pack()
        genre_entry = tk.Entry(self.__window)
        genre_entry.pack()
        add_button = tk.Button(self.__window, text="Add movie", command=lambda: self.__add_movie_lambda(Movie(
            movie_id, title_entry.get(), description_entry.get(), genre_entry.get())))
        add_button.pack()
        self.__window.mainloop()

    def __add_movie_lambda(self, movie):
        self.__services.validate_and_add_movie(movie)
        self.__print_menu()

    def __remove_client(self):
        self.__clear_window()
        id_label = tk.Label(self.__window, text="id = ")
        id_label.pack()
        id_entry = tk.Entry(self.__window)
        id_entry.pack()
        delete_button = tk.Button(self.__window, text="Remove client", command=lambda: self.
                                  __remove_client_lambda(int(id_entry.get())))
        delete_button.pack()
        self.__window.mainloop()

    def __remove_client_lambda(self, client_id):
        self.__services.remove_client(client_id)
        self.__print_menu()

    def __remove_movie(self):
        self.__clear_window()
        id_label = tk.Label(self.__window, text="id = ")
        id_label.pack()
        id_entry = tk.Entry(self.__window)
        id_entry.pack()
        delete_button = tk.Button(self.__window, text="Remove movie", command=lambda: self.
                                  __remove_movie_lambda(int(id_entry.get())))
        delete_button.pack()
        self.__window.mainloop()

    def __remove_movie_lambda(self, movie_id):
        self.__services.remove_movie(movie_id)
        self.__print_menu()

    def __modify_client(self):
        self.__clear_window()
        old_id_label = tk.Label(self.__window, text="id of the client you want to modify = ")
        old_id_label.pack()
        old_id_entry = tk.Entry(self.__window)
        old_id_entry.pack()
        new_id_label = tk.Label(self.__window, text="new id = ")
        new_id_label.pack()
        new_id_entry = tk.Entry(self.__window)
        new_id_entry.pack()
        new_name_label = tk.Label(self.__window, text="new name = ")
        new_name_label.pack()
        new_name_entry = tk.Entry(self.__window)
        new_name_entry.pack()
        modify_client_button = tk.Button(self.__window, text="Modify client", command=lambda: self.
                                         __modify_client_lambda(int(old_id_entry.get()),
                                                                int(new_id_entry.get()),
                                                                new_name_entry.get()))
        modify_client_button.pack()
        self.__window.mainloop()

    def __modify_client_lambda(self, old_id, new_id, new_name):
        self.__services.modify_client(old_id, new_id, new_name)
        self.__print_menu()

    def __modify_movie(self):
        self.__clear_window()
        old_id_label = tk.Label(self.__window, text="id of the client you want to modify = ")
        old_id_label.pack()
        old_id_entry = tk.Entry(self.__window)
        old_id_entry.pack()
        new_id_label = tk.Label(self.__window, text="new id = ")
        new_id_label.pack()
        new_id_entry = tk.Entry(self.__window)
        new_id_entry.pack()
        new_title_label = tk.Label(self.__window, text="new title = ")
        new_title_label.pack()
        new_title_entry = tk.Entry(self.__window)
        new_title_entry.pack()
        new_description_label = tk.Label(self.__window, text="new description = ")
        new_description_label.pack()
        new_description_entry = tk.Entry(self.__window)
        new_description_entry.pack()
        new_genre_label = tk.Label(self.__window, text="new genre = ")
        new_genre_label.pack()
        new_genre_entry = tk.Entry(self.__window)
        new_genre_entry.pack()
        modify_movie_button = tk.Button(self.__window, text="modify movie = ", command=lambda: self.
                                        __modify_movie_lambda(int(old_id_entry.get()), int(new_id_entry.get()),
                                                              new_title_entry.get(), new_description_entry.get(),
                                                              new_genre_entry.get()))
        modify_movie_button.pack()
        self.__window.mainloop()

    def __modify_movie_lambda(self, old_id, new_id, new_title, new_description, new_genre):
        self.__services.modify_movie(old_id, new_id, new_title, new_description, new_genre)
        self.__print_menu()

    def __print_clients(self):
        self.__clear_window()
        clients = self.__services.get_clients()

        if len(clients) == 0:
            text_label = tk.Label(self.__window, text="There are no clients in the list")
            text_label.pack()
        else:
            for client in clients:
                client_label = tk.Label(self.__window, text="id: " + str(client.get_client_id()) +
                                                            ", name: " + client.get_name())
                client_label.pack()

        menu_button = tk.Button(self.__window, text="Back to menu", command=self.__print_menu)
        menu_button.pack()
        self.__window.mainloop()

    def __print_movies(self):
        self.__clear_window()
        movies = self.__services.get_movies()

        if len(movies) == 0:
            text_label = tk.Label(text="There are no movies in the list")
            text_label.pack()
        else:
            for movie in movies:
                movie_label = tk.Label(self.__window, text="id: " + str(movie.get_movie_id()) + ", title: " +
                                                           str(movie.get_title()) + ", description: " + str(
                    movie.get_description()) +
                                                           ", genre: " + str(movie.get_genre()))
                movie_label.pack()

        menu_button = tk.Button(text="Back to menu", command=self.__print_menu)
        menu_button.pack()
        self.__window.mainloop()

    def __print_rentals(self):
        self.__clear_window()
        rentals = self.__services.get_rentals()

        if len(rentals) == 0:
            text_label = tk.Label(text="There are no rentals in the list")
            text_label.pack()
        else:
            for rental in rentals:
                rental_label = tk.Label(self.__window, text="rental id: " + str(rental.get_rental_id()) +
                                                            ", movie id: " + str(
                    rental.get_movie_id()) + ", client id: " +
                                                            str(rental.get_client_id()) + ", rented date: " +
                                                            str(rental.get_rented_date()) + ", due date: " +
                                                            str(rental.get_due_date()) + ", returned date: " +
                                                            str(rental.get_returned_date()))
                rental_label.pack()
                print(rental)

        menu_button = tk.Button(text="Back to menu", command=self.__print_menu)
        menu_button.pack()
        self.__window.mainloop()
