from src.item import Item


class MixinLog:

    def __init__(self) -> None:
        self.__language = "EN"

    def change_lang(self) -> None:
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'

    @property
    def language(self):
        return self.__language


class Keyboard(Item, MixinLog):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self.language = "EN"
