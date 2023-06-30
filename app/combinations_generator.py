class CombinationsGenerator:
    @staticmethod
    def combinations_with_replacement(lst, k):
        if k == 0:
            yield []
        else:
            for i, item in enumerate(lst):
                for combo in CombinationsGenerator.combinations_with_replacement(
                    lst[i:], k - 1
                ):
                    yield [item] + combo

    @staticmethod
    def permutations_with_replacement(lst, k):
        if k == 0:
            yield []
        else:
            for i in range(len(lst)):
                for combo in CombinationsGenerator.permutations_with_replacement(
                    lst, k - 1
                ):
                    yield [lst[i]] + combo
