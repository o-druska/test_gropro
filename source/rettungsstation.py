from positionable import Positionable
from stadtteil import Stadtteil


class RettungsStation(Positionable):
    count = 0

    def __init__(self, immovable: bool, x=-1, y=-1):
        print("create RettungsStation")

        Positionable.__init__(self, x, y, collision=True)

        # Private, bc solidity does not change
        self.__immovable = immovable

        # Private, bc IDs should not be changed by user just-like-that
        RettungsStation.count += 1
        self.__id = RettungsStation.count

        self._responsibilities = []

    def move(self, p: Positionable) -> bool:
        print("trying to move RS")
        if self.is_movable():
            # snap target coordinates to nearest crossing
            # round to thousand
            nearest_crossing = Positionable(x=1000 * round(p.x()/1000),
                                            y=1000 * round(p.y()/1000))

            print(f"nearest_crossing is {nearest_crossing}")

            Positionable.move(self, nearest_crossing)
        else:
            print("Rettungsstation nicht bewegbar -- noop")
            return False

    def add_responsibility(self, responsibility: Stadtteil):
        print(f"adding responsibility: {responsibility}")
        self._responsibilities.append(responsibility)

    def remove_responsibility(self, responsibility: Stadtteil):
        print(f"removing responsibility: {responsibility}")
        self._responsibilities.remove(responsibility)

    def get_responsibilities(self):
        return self._responsibilities

    def get_id(self):
        return self.__id

    def is_movable(self) -> bool:
        return not self.__immovable

    def cum_dist(self) -> float:
        """
        Compute the cumulative distance between self and all assigned
        responsibilities, weighed by number of Unfaelle per responsibility.
        :return:
        cumulative distance
        """
        print("compute cumulative distance")

        sum_ = 0.0
        for responsibility in self._responsibilities:
            sum_ += (self.get_distance(responsibility.get_position())
                     * responsibility.get_unfallquote())
        return sum_
