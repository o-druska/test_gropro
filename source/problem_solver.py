from input_parser import InputParser
from output_writer import OutputWriter
from positionable import Positionable
from no_movement_exception import NoMovementException
from collision_exception import CollisionException
import random


class ProblemSolver:
    def __init__(self, input_file: str):
        self.input_parser = InputParser(input_file)
        self.stadt = self.input_parser.create_stadt()
        self.output_writer = OutputWriter(self.stadt.get_name())

    def _init_problem(self, seed=13):
        """
        Initialize the problem by choosing random
        starting Positionables for movable rescue stations
        :return:
        """

        print(f"initializing problem")

        if seed:
            random.seed(seed)

        # find random starting points for movable _rettungsstationen
        rs = [r for r in self.stadt.get_rettungsstationen() if r.is_movable()]
        for r in rs:
            while True:
                x = random.randint(0, self.stadt.get_length())*1000
                y = random.randint(0, self.stadt.get_width())*1000
                try:
                    # if moving passes -> place next Rettungsstation
                    r.move(Positionable(x, y))
                    break
                except ValueError as e:
                    print(e)
                    pass

    def solve(self):
        """
        Solve Stadt problem using the following algorithm:
        1. Initialize the problem by choosing random starting positions for movable rescue stations
        2. Compute distances from each borrow to each resuce station
        3. assign each rescue station all their nearest borrows
        4. Compute pseudo center-of-mass for each rescue station weighed by the accident counts of their assigend RS
        5. Move each movable RS to the crossing nearest to that pseudo center-of-mass
        6. loop through 2.
        7. once no RS moves anymore, compute collective distances and print output files of curent Stadt config
        :return:
        """
        self._init_problem()
        print(f"solving problem")

        positions_changed = True

        while positions_changed:
            positions_changed = False

            # Stadtteile ihren nächsten Rettungsstationen zuordnen
            for s in self.stadt.get_borrows():
                dist_r = []
                for r in self.stadt.get_rettungsstationen():
                    dist_r.append((s.get_distance(r), r))
                min(dist_r, key=lambda p: p[0])[1].add_responsibility(s)

            # Schwerpunkte berechnen und bewegliche Rettungsstationen verschieben
            for r in [r for r in self.stadt.get_rettungsstationen() if r.is_movable()]:
                borrows = r.get_responsibilities()  # alle Stadtteile einer Rettungsstation
                pseudo_x = sum([b.x() * b.get_unfallquote() for b in borrows])/len(borrows)
                pseudo_y = sum([b.y() * b.get_unfallquote() for b in borrows])/len(borrows)


                # make sure, RS dont get positioned outside of stadt boundaries
                if pseudo_x > self.stadt.get_length()*1000:
                    pseudo_x = self.stadt.get_length()*1000

                if pseudo_x > self.stadt.get_length()*1000:
                    pseudo_x = self.stadt.get_length()*1000

                pseudo = Positionable(round(pseudo_x), round(pseudo_y))

                try:
                    r.move(pseudo)
                    positions_changed = True
                except CollisionException as c:
                    print(c)
                    continue
                except NoMovementException as n:
                    print(n)
                    continue

        # Positionen nicht geändert
        # lokales Minimum der aktuellen startkonfiguration gefunden
        self.output_writer.write_txt(self.stadt)
        self.output_writer.write_csv(self.stadt)
