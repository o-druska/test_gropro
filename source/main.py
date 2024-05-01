from problem_solver import ProblemSolver
import argparse


def main() -> None:
    """
    main
    :return: None
    """
    """
    parser = argparse.ArgumentParser(description=
                                     "find optimal city configuration")
    parser.add_argument('-f', '--file', type=str, required=True)
    args = parser.parse_args()
    """

    solver = ProblemSolver('Matsehausen.txt')
    solver.solve()
    print("problem solved")


if __name__ == '__main__':
    main()