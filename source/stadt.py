from stadtteil import Stadtteil
from rettungsstation import RettungsStation


class Stadt:
    def __init__(self, name: str, unfallquoten: list[list[int]], rettungsstationen: list[RettungsStation]):
        """
        Create Stadt object holding rescue stations, borrows and their accident rates.
        Is assigned a name which is used to create the output files
        :param name:
        :param unfallquoten: used to create borrows
        :param rettungsstationen: List of RettungsStation objects
        """
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
        """
        :return: Stadt name
        """
        return self._name

    def get_width(self):
        """
        :return: Stadt width
        """
        return self.__width

    def get_length(self):
        """
        :return: Stadt length
        """
        return self.__length

    def get_borrows(self):
        """
        :return: Stadt borrows as 2d-array
        """
        return self._borrows

    def get_rettungsstationen(self):
        """
        :return: Stadt rettungsstationen as list
        """
        return self._rettungsstationen

    def get_total_distance(self) -> float:
        """
        Compute the total distance based on the weighed distances
        of each rescue station
        :return:
        """
        print("compute total distance")
        sum_ = 0.0
        for r in self._rettungsstationen:
            sum_ += r.cum_dist()
        return sum_
