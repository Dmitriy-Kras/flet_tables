from abc import ABC, abstractmethod
from itertools import count, product


class BaseMatrix(ABC):
    def __init__(self, rows, columns=None, start=1, reflex=False) -> None:
        self.rows = rows
        self.columns = columns or rows
        self.start = start
        self.reflex = reflex

    def empty_mtrx(self):
        return [[None for _ in range(self.columns)] for _ in range(self.rows)]

    @abstractmethod
    def _prepare(self):
        pass

    def raw(self):
        return self._prepare()

    @property
    def filled(self):
        mtrx = self.empty_mtrx()
        for i, j, val in self.raw():
            mtrx[i][j] = val
        return mtrx

    def rotate_left(self):
        return [
            [self.filled[i][~j] for i in range(self.rows)] for j in range(self.columns)
        ]

    def rotate_right(self):
        return [
            [self.filled[~i][j] for i in range(self.rows)] for j in range(self.columns)
        ]

    def rotate_double(self):
        return [
            [self.filled[~i][~j] for j in range(self.columns)] for i in range(self.rows)
        ]


class Snake(BaseMatrix):
    def _prepare(self):
        nums = count(self.start)
        for i, j in product(range(self.rows), range(self.columns)):
            x = [j, ~j][(i + self.reflex) % 2]
            yield i, x % self.columns, next(nums)


class Spiral(BaseMatrix):
    def _prepare(self):
        cnt, i, j, di, dj = 0, 0, 0, 0, 1
        match self.__class__.__name__:
            case "Spiral":
                drt = False
            case "Darts":
                drt = True
                self.columns = self.rows
        r, c = self.rows, self.columns
        turn = c - 1
        for k in range(r * c):
            x = (j, ~j)[self.reflex]
            val = [k + self.start, self.start + cnt // 4][drt]
            yield i, x % c, val
            if k == turn:
                di, dj = dj, -di
                cnt += 1
                turn += [c, r][cnt % 2] - (cnt + (cnt % 2 != 0)) // 2
            i, j = i + di, j + dj


class Darts(Spiral):
    pass


class Diagonal(BaseMatrix):
    def _prepare(self):
        nums = count(self.start)
        for j in range(self.rows + self.columns - 1):
            for i in range(max(0, j - self.columns + 1), min(j, self.rows - 1) + 1):
                x = (j - i, ~(j - i))[self.reflex]
                yield i, x % self.columns, next(nums)


def print_matrix(mtrx):
    print("\n".join("".join(f"{elem:<5}" for elem in row) for row in mtrx))


if __name__ == "__main__":
    tbl = Snake(6, 4, 1)
    print_matrix(tbl.filled)
    print()
    print_matrix(tbl.rotate_double())
    print()
    print(*tbl.raw())
