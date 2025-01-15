import hashlib
import time

# Класс пользователя
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self._hash_password(password)   # Хэшируем пароль
        self.age = age

    def _hash_password(self, password):
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)   # Хэш пароля

    def __eq__(self, other):
        return self.nickname == other.nickname  # Сравнение пользователей по никнейму

    def __str__(self):
        return self.nickname    # Представление пользователя в виду строки

# Класс видео
class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title  # Заголовок видео
        self.duration = duration    # длительность видео в сек.
        self.time_now = 0   # Текущее время просмотра
        self.adult_mode = adult_mode    # Ограничение видео 18+

    def __eq__(self, other):
        return self.title == other.title    # Сравнение видео по заголовку

    def __str__(self):
        return self.title   # Представление видео в виду строки

# Основной класс платформы УрТуб
class UrTube:
    def __init__(self):
        self.users = [] # Список пользователей
        self.videos = []    # Список видео
        self.current_user = None    # Текущий пользователь

    # Метод для входа в аккаунт
    def log_in(self, nickname, password):
        hashed_password = int(hashlib.sha256(password.encode()).hexdigest(), 16)    # Хэшируем пароль
        user = next((u for u in self.users if u.nickname == nickname and u.password == hashed_password), None)
        if user:
            self.current_user = user    # Устанавливаем текущего пользователя
        else:
            print("Неверный логин или пароль")

    # Метод для регистрации нового пользователя
    def register(self, nickname, password, age):
        if any(u.nickname == nickname for u in self.users):
            print(f"Пользователь {nickname} уже существует")    # Проверка на уникальность никнейма
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user) # Добавляем нового пользователя
            self.current_user = new_user    # Выполняем автоматический вход

    # Метод для выхода из аккаунта
    def log_out(self):
        self.current_user = None    # Сбрасываем тек. пользователя

    # Метод для добавления видео на платформу
    def add(self, *videos):
        for video in videos:
            if video not in self.videos:    # Проверяем, что видео еще нет в списке
                self.videos.append(video)

    # Метод для поиска видео по ключевому слову
    def get_videos(self, search_term):
        search_term = search_term.lower()   # Приводим ключевое слово к ниж. регистру
        return [video.title for video in self.videos if search_term in video.title.lower()]

    # Метод для просмотра видео
    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")    # Проверка авторизации
            return

        video = next((v for v in self.videos if v.title == title), None)
        if not video:
            return  # Если видео не найдено

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")   # Проверка возрастного ограничения
            return

        # Вывод текущего времени просмотра видео
        for second in range(video.time_now + 1, video.duration + 1):
            print(second, end=" ", flush=True)
            time.sleep(1)  # Пауза между секундами воспроизведения
        print("\nКонец видео")
        video.time_now = 0  # Срабатываем текущее время просмотра


# Тест
if __name__ == "__main__":
    ur = UrTube()

    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    ur.add(v1, v2)

    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    ur.watch_video('Для чего девушкам парень программист?')

    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')

    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    ur.watch_video('Лучший язык программирования 2024 года!')
