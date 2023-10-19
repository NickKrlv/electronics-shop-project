from src.item import Item


class MixinLog:
    language = "EN"

    def __init__(self) -> None:
        self.language = "EN"

    def change_lang(self) -> None:
        if self.language == 'EN':
            self.language = 'RU'
        elif self.language == 'RU':
            self.language = 'EN'


class Keyboard(Item, MixinLog):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self.language = "EN"
