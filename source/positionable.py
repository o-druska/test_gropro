import math
from no_movement_exception import NoMovementException
from collision_exception import CollisionException


class Positionable:
    """
    Coordinate object to track positions.
    Can only have integer coordinates.
    Also tracks all Positionables with collision.
    """
    positionables_with_collision = []

    def __init__(self, x: int, y: int, collision=False):
        """
        create Positionable object to track coordinates of entitites
        :param x: x-coordiante
        :param y: y-coordiante
        :param collision: wether or not two Positionable objects collide
        """

        self._x = int(x)
        self._y = int(y)
        self._collision = collision

        if self._collision:
            self.positionables_with_collision.append(self)

    def __eq__(self, other: 'Positionable') -> bool:
        """
        True, if all coordinates of Positionable are equal element-wise
        :param other: Positionable object to compare
        :return: bool
        """
        return self._x == other.x() and self._y == other.y()

    def __str__(self) -> str:
        """
        String representation of Positionable object.
        Shows current coordinates.
        :return: str
        """
        return f"({self._x},{self._y})"

    def get_distance(self, p: 'Positionable') -> float:
        """
        Calculates distance between two Positionable object
        :param p: Positionable object
        :return: float
        """
        return math.sqrt(
            (self._x - p.x()) ** 2
            + (self._y - p.y()) ** 2
        )

    def get_position(self) -> 'Positionable':
        """
        returns self
        :return: self: Positionable
        """
        return self

    def has_collision(self) -> bool:
        """
        returns True, if Positionable has collision
        :return:
        """
        return self._collision

    def x(self) -> int:
        """
        return x-coordinate of Positionable object
        :return: int
        """
        return self._x

    def y(self) -> int:
        """
        return y-coordinate of Positionable object
        :return: int
        """
        return self._y

    def move(self, p: 'Positionable') -> None:
        """
        Move self to the given Positionable p.
        :throws: NoMovementException if self == p
        :throws: CollisionException if p is occupied by Positionable with collision
        :param: p - target Positionable
        :return: None
        """
        print("Move " + str(self) + " to " + str(p))

        if self == p:
            raise NoMovementException("Self and p are on the same spot")

        if self.has_collision():
            # new position matches any of the positionables with collision
            # ergo p is a position with collision
            if any([p == collisionable for collisionable in self.positionables_with_collision]):
                raise CollisionException('COLLISION occured - cannot move')

        self._x = p.x()
        self._y = p.y()
