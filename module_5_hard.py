import time



class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other


class UrTube:
    def __init__(self):
        self.users = list()
        self.videos = list()
        self.current_user = None

    def log_in(self, nickname, password):
        """
        nickname, password и пытается найти пользователя в users с такими же логином и паролем.
        Если такой пользователь существует, то current_user меняется на найденного.
        :return:
        """

        if nickname in self.users:
            if nickname.password == hash(password):
                self.current_user = nickname.nickname
            else:
                print('Неверный пароль!')
        else:
            print('Пользователя с таким логином и паролем не зарегистрировано.')

    def register(self, nickname, password, age):
        """
         Tри аргумента: nickname, password, age, и добавляет пользователя в список,
         если пользователя не существует (с таким же nickname).
         Если существует, выводит на экран: "Пользователь {nickname} уже существует".
         После регистрации, вход выполняется автоматически.
        :return:
        """
        not_in_users = True

        for i_user in self.users:
            if i_user.nickname == nickname:
                not_in_users = False

        if not_in_users:
            digit_in_pass = any(character.isdigit() for character in password)
            upper_in_pass = any(character.isupper() for character in password)

            if digit_in_pass and upper_in_pass and len(password) > 8:
                nickname = User(nickname, hash(password), age)
                self.users.append(nickname)
                self.log_in(nickname, password)

            else:
                print('Пароль не прошел проверку на надежность: \n'
                      'Длинна 8+ символов, 1 заглавная буква, 1 цифра\n'
                      'Повторите попытку регистрации.')

        else:
            print(f'Пользователь {nickname} уже существует')


    def log_out(self):
        """
        сброс текущего пользователя на None
        """
        self.current_user = None
        pass

    def add(self, *args):
        """
        Принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
        если с таким же названием видео ещё не существует.
        В противном случае ничего не происходит
        :return:
        """
        for i_video in args:

            if i_video.title not in self.videos:
                tittle = Video(i_video.title, i_video.duration)
                self.videos.append(tittle)
            else:
                print('Такое видео уже есть в списке.')

    def get_videos(self, searing_str):
        """
        Принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово.
        Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
        :param searing_str:
        :return:
        """
        result_video_list = list()

        for i_video in self.videos:
            if searing_str.lower() in i_video.title.lower():
                result_video_list.append(i_video.title)

        return result_video_list



    def watch_video(self, film_name):
        """
        Принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится,
        если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
        После текущее время просмотра данного видео сбрасывается.

        1) Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
        2) Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
        В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
        3) Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+.
         Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
        4) После воспроизведения нужно выводить: "Конец видео"
        :param film_name:
        :return:
        """
        age_user = 0
        if self.current_user != None:
            for i_user in self.users:
                if i_user.nickname == self.current_user:
                    age_user = i_user.age


            for i_video in self.videos:
                if i_video.title == film_name:

                    if not i_video.adult_mode and age_user < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')

                    else:
                        for i in range(1, i_video.duration+1):
                            print(i_video.time_now, end=' ')
                            time.sleep(1)
                            i_video.time_now += 1
                        print('Конец видео')
                        i_video.time_now = 0

        else:
            print("Не выполнен вход на сайте, пожалуйста авторизуйтесь")






if __name__ == "__main__":
    pass
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 3)
    v2 = Video('Для чего девушкам парень программист?', 4, adult_mode=True)


    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'l1olkekcGburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')