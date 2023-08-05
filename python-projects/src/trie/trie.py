class Trie:

    def __init__(self):
        self.root = [None]*27

    @staticmethod
    def __get_idx(c: chr) -> int:
        return ord(c) - ord("a")

    def add(self, word: str):
        word = word.lower()
        cur = self.root
        for c in word:
            idx = self.__get_idx(c)
            if not cur[idx]:
                cur[idx] = [None]*27
            cur = cur[idx]
        cur[26] = word

    def __traverse(self, node: list) -> list:
        result = []
        if not node:
            return result
        if node[26]:
            result.append(node[26])
        for i in range(26):
            if node[i]:
                result.extend(self.__traverse(node[i]))
        return result

    def find(self, prefix: str) -> [str]:
        cur = self.root
        for c in prefix:
            idx = self.__get_idx(c)
            cur = cur[idx]
            if not cur:
                break
        return self.__traverse(cur)


t = Trie()
t.add("ashwin")
t.add("ass")
t.add("ash")
t.add("bunch")
t.add("brunch")
print(t.find("as"))
