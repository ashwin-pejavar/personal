class Levenshtein:
    subCost, insCost, delCost = (1, 1, 1)

    def __init__(self, word1: str, word2: str):
        self.word1 = word1
        self.word2 = word2
        self.distances = list[list[int]]
        self.distances = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            self.distances[i][0] = i * Levenshtein.insCost

        for i in range(len(word2) + 1):
            self.distances[0][i] = i * Levenshtein.insCost

    def print(self):
        for row in self.distances:
            print(row)

    def distance(self) -> int:
        for i in range(1, len(self.word1) + 1):
            for j in range(1, len(self.word2) + 1):
                s_cost = 0 if self.word1[i-1] == self.word2[j-1] else Levenshtein.subCost
                self.distances[i][j] = min(
                    self.distances[i-1][j] + Levenshtein.insCost,
                    self.distances[i][j-1] + Levenshtein.delCost,
                    self.distances[i-1][j-1] + s_cost
                )
        return self.distances[len(self.word1)][len(self.word2)]


ll = Levenshtein("surplate", "plate")
print(ll.distance())