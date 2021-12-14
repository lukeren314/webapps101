
def is_palindrome(word):
    return word == word[::-1]

def count_palindromes(filename):
    with open(filename, 'r') as f:
        count = 0
        for line in f:
            if is_palindrome(line):
                count += 1
    return count

if __name__ == '__main__':
    print(count_palindromes('palindromes.txt'))