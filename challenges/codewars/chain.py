class ChainAbleAdd(int):
    def __call__(self, value):
        return ChainAbleAdd(self + value)


def add(number: int) -> ChainAbleAdd:
    return ChainAbleAdd(number)
