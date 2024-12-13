from collections import deque, defaultdict

class AhoCorasick:
    def __init__(self):
        self.trie = defaultdict(dict)
        self.output = defaultdict(list)
        self.fail = {}

    def add_pattern(self, pattern):
        """Dodaje wzorzec do drzewa trie."""
        node = 0
        for char in pattern:
            if char not in self.trie[node]:
                self.trie[node][char] = len(self.trie)
            node = self.trie[node][char]
        self.output[node].append(pattern)

    def build(self):
        """Buduje funkcje fail dla automatu Aho-Corasick."""
        self.fail = {0: 0}
        queue = deque()

        # Inicjalizujemy fail-linki dla dzieci korzenia
        for char, node in self.trie[0].items():
            self.fail[node] = 0
            queue.append(node)

        # Przetwarzanie reszty drzewa
        while queue:
            current_node = queue.popleft()

            for char, next_node in self.trie[current_node].items():
                queue.append(next_node)
                fail_state = self.fail[current_node]

                while fail_state and char not in self.trie[fail_state]:
                    fail_state = self.fail[fail_state]

                self.fail[next_node] = self.trie[fail_state].get(char, 0)
                self.output[next_node] += self.output[self.fail[next_node]]

    def search(self, text):
        """Przeszukuje tekst za pomocą zbudowanego automatu."""
        node = 0
        results = []

        for i, char in enumerate(text):
            while node and char not in self.trie[node]:
                node = self.fail[node]

            node = self.trie[node].get(char, 0)

            if self.output[node]:
                for pattern in self.output[node]:
                    results.append((i - len(pattern) + 1, pattern))

        return results

# Przykład użycia
ac = AhoCorasick()
patterns = ["he", "she", "his", "hers"]
for pattern in patterns:
    ac.add_pattern(pattern)
ac.build()

text = "ahishers"
matches = ac.search(text)
print(matches)
