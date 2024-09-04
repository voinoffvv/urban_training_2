from time import sleep
import sys

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'Пользователь: {self.nickname}'

    def __eq__(self, other):
        if isinstance(other, User):
            return other.nickname == self.nickname and self.password == hash(other.password)
        return False

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode = False):
        self.title = title
        self.duration = duration # продолжительность, секунды
        self.time_now = time_now # секунда остановки (изначально 0)
        self.adult_mode = adult_mode # ограничение по возрасту, bool (False по умолчанию)

    def __str__(self):
        return f'{self.title} (duration={self.duration}, time_now={self.time_now}, adult_mode={self.adult_mode}).'

class UrTube:
    Users = []
    Videos = []
    current_user = None

    # Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с такими же логином и паролем.
    # Если такой пользователь существует, то current_user меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.
    def log_in(self, nickname, password):
        for user in self.Users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                break

    # Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname).
    # Если существует, выводит на экран: "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
    def register(self, nickname, password, age):
        # self.current_user = None
        for u in self.Users:
            if u.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return False

        user = User(nickname, password, age)
        self.Users.append(user)
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    # Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же названием видео ещё не существует.
    # В противном случае ничего не происходит.
    def add(self, *videos):
        for v in videos:
            if v not in self.Videos:
                self.Videos.append(v)


    #Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово.
    # Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
    def get_videos(self, video_name):
        res = []
        for v in self.Videos:
            if video_name.upper() in v.title.upper():
                res.append(v.title)
        return res

    # Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится,
    # если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
    # Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
    # Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+.
    # Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
    # После воспроизведения нужно выводить: "Конец видео"
    def watch_video(self, video_name):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео.')
        else:
            for v in self.Videos:
                if video_name == v.title:
                    if v.adult_mode == True:
                        if self.current_user.age < 18:
                            print('Вам нет 18 лет, пожалуйста покиньте страницу.')
                            break
                    for c in ' '.join(str(i) for i in range(v.duration)):
                        print(c, end='')
                        sys.stdout.flush()
                        sleep(1)
                    print(' Конец видео.')
                    break

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2, v1)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
