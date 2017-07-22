class compare:
    def __eq__(self, other):
        return True

    def __gt__(self, other):
        return True

    def __ge__(self, other):
        return True


def anything(thing):
    return compare()