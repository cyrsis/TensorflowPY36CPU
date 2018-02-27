class ChessCoordinate:

    def __init__(self, file, rank):

        if len(file) != 1:
            raise ValueError("{} component file {!r} does not have a length of one."
                             .format(self.__class__.__name__, file))

        if file not in 'abcdefgh':
            raise ValueError("{} component file {!r} is out of range."
                             .format(self.__class__.__name__, file))

        if rank not in range(1, 9):
            raise ValueError("{} component rank {!r} is out of range."
                             .format(self.__class__.__name__, rank))

        self._file = file
        self._rank = rank

    @property
    def file(self):
        return self._file

    @property
    def rank(self):
        return self._rank

    def __repr__(self):
        return "{}(file={}, rank={})".format(self.__class__.__name__, self.file, self.rank)

    def __str__(self):
        return '{}{}'.format(self.file, self.rank)


def main():
    white_queen = ChessCoordinate('d', 4)
    print(white_queen)


if __name__ == '__main__':
    main()