class Robot:
    """
    a
    """

    def __init__(self, width: int, height: int):
        # y, x
        self.pos = (0, 0)
        self.dir = (0, 1)  # East (0 in y, 1 in x)
        self.width = width - 1
        self.height = height - 1

    def isValid(self, point: tuple[int, int]):
        return 0 <= point[1] <= self.width and 0 <= point[0] <= self.height

    def sum(self, p1, p2):
        return tuple(x + y for x, y in zip(p1, p2))

    def step(self, num: int) -> None:
        for _ in range(num):
            nextPoint = self.sum(self.pos, self.dir)
            if self.isValid(nextPoint):
                self.pos = nextPoint
            else:
                # Try rotating *clockwise* until valid dirn found
                while not self.isValid(nextPoint):
                    sgn = 1 if self.dir[1] == 1 else -1
                    newDirn = (sgn * self.dir[1], sgn * self.dir[0])
                    nextPoint = self.sum(self.pos, newDirn)
                self.pos = nextPoint
                self.dir = newDirn

    def getPos(self) -> list[int]:
        return list(self.pos)

    def getDir(self) -> str:
        return {
            (1, 0): "North",
            (0, 1): "East",
            (-1, 0): "South",
            (0, -1): "West",
        }[self.dir]


robot = Robot(6, 3)
robot.step(2)
robot.step(2)
robot.getPos()
robot.getDir()
robot.step(2)


robot.step(1)
robot.step(4)

robot.getPos()
robot.getDir()
