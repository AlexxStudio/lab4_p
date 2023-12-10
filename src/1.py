from collections import Counter
class Film:
    def __init__(self, film_id, title):
        self.film_id = film_id
        self.title = title

class Recommendation:
    def __init__(self, list_of_films, history_file):
        self.films = self.load_films(list_of_films)
        self.history = self.load_history(history_file)

    def load_films(self, list_of_films):
        films = {}
        with open(list_of_films) as f:
            for line in f:
                film_id, title = line.strip().split(',')
                films[int(film_id)] = Film(int(film_id), title)
        return films

    def load_history(self, history_file):
        history = []
        with open(history_file) as f:
            for line in f:
                viewed_films = list(map(int, line.strip().split(',')))
                history.append(viewed_films)
        return history

    def recommended_film(self, user_history):
        matching_users = [history for history in self.history if len(set(user_history) & set(history)) >= len(user_history) / 2]

        viewed_films = set(user_history)
        remaining_films = [film for history in matching_users for film in history if film not in viewed_films]

        if remaining_films:
            film_views_count = Counter(remaining_films)
            recommended_film_id = max(film_views_count, key=film_views_count.get)
            recommended_film_title = self.films[recommended_film_id].title
            return recommended_film_title
        else:
            return "Нет рекомендаций"

if __name__ == "__main__":
    list_of_films = "films.txt"
    history_file = "history.txt"

    recommendation_system = Recommendation(list_of_films, history_file)

    user_input = input("Введите историю просмотров через запятую: ")
    user_history = list(map(int, user_input.split(',')))

    recommended_film = recommendation_system.recommended_film(user_history)

    print(f"Рекомендуемый фильм: {recommended_film}")