from stadt import Stadt
from rettungsstation import RettungsStation


class InputParser:
    def __init__(self, file_path: str):
        print(f"init InputParser")
        self.file_path = file_path
        self.name = file_path.split("/")[-1].split(".")[0]
        # self._parse_input()

    def _parse_input(self):
        """
        parse given file path and read out the values
        neded to create Stadt object
        :return:
        """
        pass

    def create_stadt(self):
        """
        create Stadt object based on input file
        :return:
        """
        print(f"creating stadt")

        # currently hardcoded bc parsing doesnt work yet
        u = [[3, 2, 1, 0, 0, 2, 1, 2, 3, 0, 0, 4],
             [3, 1, 0, 2, 1, 0, 0, 0, 1, 2, 1, 0],
             [0, 0, 0, 2, 0, 0, 1, 2, 0, 1, 0, 0],
             [0, 0, 0, 1, 3, 1, 0, 0, 0, 2, 3, 1],
             [0, 1, 2, 1, 2, 0, 0, 2, 2, 1, 2, 1],
             [2, 0, 1, 1, 2, 0, 0, 0, 0, 4, 3, 2]]

        name = self.name

        r1 = RettungsStation(immovable=True, x=2000, y=1000)
        r2 = RettungsStation(immovable=False)
        r3 = RettungsStation(immovable=False)

        r = [r1, r2, r3]

        return Stadt(name, u, r)
