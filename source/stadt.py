from stadtteil import Stadtteil
from rettungsstation import RettungsStation
import numpy as np


class Stadt:
    def __init__(self, name: str, unfallquoten: list[list[int]], rettungsstationen: list[RettungsStation]):
        print(f"creating Stadt object")
        self._name = name
        self._rettungsstationen = rettungsstationen

        self.__length = len(unfallquoten[0])
        self.__width = len(unfallquoten)

        # TODO: fix assigning coordinates so that
        #  bottom left input is 0,0 in coordinate system
        self._borrows = [Stadtteil(x=i * 1000 + 500, y=k * 1000 + 500, unfallquote=unfallquoten[k][i])
                         for i in range(self.__length)
                         for k in range(self.__width)]
        pass

    def get_name(self):
        return self._name

    def get_width(self):
        return self.__width

    def get_length(self):
        return self.__length

    def get_borrows(self):
        return self._borrows

    def get_rettungsstationen(self):
        return self._rettungsstationen

    def get_total_distance(self) -> float:
        print("computing total distance")
        sum_ = 0.0
        for r in self._rettungsstationen:
            sum_ += r.cum_dist()
        return sum_
