class Anagram:
    """Detect anagrams for a given word."""

    def __init__(self, word: str):
        self.word = word
        # normalized lower-case form used for comparisons
        self._normalized = word.lower()
        # precompute the sorted letters for quick comparison
        self._sorted_letters = sorted(self._normalized)

    def match(self, candidates):
        """Return a list of candidates that are anagrams of the original word."""
        matches = []
        for candidate in candidates:
            cand_norm = candidate.lower()
            # identical words (case-insensitive) are not anagrams
            if cand_norm == self._normalized:
                continue
            if sorted(cand_norm) == self._sorted_letters:
                matches.append(candidate)
        return matches
