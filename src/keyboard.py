from src.item import Item


class MixinLog:

    def __init__(self) -> None:
        self._language = "EN"  # Используйте _language для хранения значения

    def change_lang(self) -> None:
        if self._language == 'EN':
            self._language = 'RU'
        elif self._language == 'RU':
            self._language = 'EN'

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value


class Keyboard(Item, MixinLog):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self.language = "EN"
