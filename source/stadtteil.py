from positionable import Positionable


class Stadtteil(Positionable):
    def __init__(self, x: int, y: int, unfallquote: int):
        Positionable.__init__(self, x, y, collision=False)
        self._unfallquote = unfallquote

    # Override move methode, because _borrows shall not be movable
    def move(self, p: Positionable):
        print("Stadtteil immovable")
        pass

    def get_unfallquote(self):
        return self._unfallquote
