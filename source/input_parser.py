from stadt import Stadt
from rettungsstation import RettungsStation


class InputParser:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.name = file_path.split("/")[-1].split(".")[0]
        # self._parse_input()

    def _parse_input(self):
        """
        parse given file path and read out the values
        neded to create Stadt object

        DOESNT WORK
        :return:
        """
        _unfallquote = []
        _r_old = []
        _r_new = []
        _city_shape = ()
        _oldnew_keyword = {"neu": True, "alt": False}

        # return tuple containing count and wether old or new
        read_rescue_station = lambda l: int(l.split(" ")[2])
        read_city_shape = lambda l: ( int(l.split(" ")[1].split(",")[0]),
                                      int(l.split(" ")[1].split(",")[1])
                                      )
        read_position = lambda l: (int(l.split(",")[0]), int(l.split(",")[1]))


        print('parsing input file')
        with open(self.file_path, "r") as f:
            lines = f.readlines()
            # Throw out all comment lines
            lines = [l for l in lines if not l.startswith("//")]

            for line in lines:
                try:
                    _city_shape = read_city_shape(line)
                    continue
                except Exception as e:
                    try:
                        r_count = read_rescue_station(line)
                        for i in range(r_count):
                            _r_old.append(read_position(line+i))
                    except Exception as e:
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
