# Day 2: Anagram Check - With and Without Sorting

def is_anagram_sorted(s1: str, s2: str) -> bool:
    """
    Check if two strings are anagrams using sorting.
    Ignores spaces and is case-insensitive.
    """
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)


def is_anagram_counter(s1: str, s2: str) -> bool:
    """
    Check if two strings are anagrams using frequency counter.
    Ignores spaces and is case-insensitive.
    """
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    count = {}
    for char in s1:
        count[char] = count.get(char, 0) + 1

    for char in s2:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True


# Run test cases
if __name__ == "__main__":
    print("Using sort:")
    print(is_anagram_sorted("Listen", "Silent"))   # True
    print(is_anagram_sorted("Hello", "Olelh"))     # True
    print(is_anagram_sorted("Dog", "Gods"))        # False

    print("\nUsing counter:")
    print(is_anagram_counter("Listen", "Silent"))  # True
    print(is_anagram_counter("Hello", "Olelh"))    # True
    print(is_anagram_counter("Dog", "Gods"))       # False
