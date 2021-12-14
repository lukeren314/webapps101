
class PalindromeCounter:
    def __init__(self, filename: str) -> None:
        self.file = open(filename)
    
    def count_palindromes(self) -> int:
        count = 0
        for line in self.file:
            line = line.strip()
            if self._is_palindrome(line):
                count += 1
        return count
    
    def _is_palindrome(self, word: str) -> bool:
        return word == word[::-1]


if __name__ == "__main__":
    palindrome_counter = PalindromeCounter("palindromes.txt")
    print(palindrome_counter.count_palindromes())