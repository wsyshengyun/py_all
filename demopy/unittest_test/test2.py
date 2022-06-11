# coding:utf8


class Pet:
    def __init__(self):
        """ """


class Handler:
    _next_handler = None

    def __init__(self, shiwu):
        """ """
        self.name = shiwu

    def set_next(self, handler):
        """

        """
        self._next_handler = handler
d:\QMDownload\Hotfix\其它\Y 视频\130809_689_01-HD.rmvb        return handler

    def handler(self, shiwu):
        if self._next_handler:
            return self._next_handler.handler(shiwu)
        else:
            print(f"no body is eat {shiwu}")

    def __str__(self):
        return '<Handler>'


class DogHandler(Handler):

    def handler(self, shiwu):
        if shiwu == self.name:
            print(f"dog is eating {shiwu}")
            return
        else:
            super(DogHandler, self).handler(shiwu)

    def __str__(self):
        return '<DogHandler>'


class MonkeyHandler(Handler):
    def handler(self, shiwu):
        if shiwu == self.name:
            print(f"monkey is eating {shiwu}")
            return
        else:
            super(MonkeyHandler, self).handler(shiwu)

    def __str__(self):
        return '<MonkeyHandler>'


class SongShuHandler(Handler):
    def handler(self, shiwu):
        if shiwu == self.name:
            print(f"songshu is eating {shiwu}")
            return
        else:
            super(SongShuHandler, self).handler(shiwu)

    def __str__(self):
        return '<SongShuHandler>'


def main():
    """

    """
    dog = DogHandler('rou')
    songshu = SongShuHandler('jianguo')
    monkey = MonkeyHandler('bananer')
    foods = ['rou', 'jianguo', 'bananer', 'yu']
    dog.set_next(songshu).set_next(monkey)

    for shiwu in foods:
        print(f"____now food is {shiwu}")
        dog.handler(shiwu)


if __name__ == '__main__':
    main()
