class CombinationsGenerator:
    @staticmethod
    def generate_combinations(list1, list2, max_list2):
        combinations = []
        for i in range(2, min(5, len(list1) + len(list2)) + 1):
            for comb2_len in range(min(i, len(list2)) + 1):
                for comb2 in CombinationsGenerator.combinations_with_replacement(
                    list2, comb2_len
                ):
                    comb1_len = i - comb2_len
                    for comb1 in CombinationsGenerator.permutations_with_replacement(
                        list1, comb1_len
                    ):
                        num_list2 = sum(1 for x in comb1 + comb2 if x in list2)
                        if num_list2 <= max_list2:
                            combination = "".join(comb1 + comb2)
                            combinations.append(combination)
        return combinations

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
