import pytest

from lib.palindrome import longest_palindromic_substring


def is_palindrome(x: str) -> bool:
    return x == x[::-1]


@pytest.mark.parametrize(
    "s, expected_set",
    [
        ("babad", {"bab", "aba"}),          # either is valid
        ("cbbd", {"bb"}),
        ("a", {"a"}),
        ("ac", {"a", "c"}),                 # either is valid
        ("racecar", {"racecar"}),
        ("aaaa", {"aaaa"}),                 # whole string palindrome
        ("abba", {"abba"}),                 # even-length palindrome
        ("abcde", {"a", "b", "c", "d", "e"}),  # no longer palindrome than 1
    ],
)
def test_known_cases_allow_multiple_valid_answers(s, expected_set):
    result = longest_palindromic_substring(s)
    assert result in expected_set


@pytest.mark.parametrize(
    "s",
    [
        "forgeeksskeegfor",   # known classic: "geeksskeeg"
        "bananas",            # "anana"
        "abcdedcbaXYZ",       # "abcdedcba"
        "XYZabcdedcba",       # "abcdedcba"
    ],
)
def test_result_is_a_palindrome_and_is_substring(s):
    result = longest_palindromic_substring(s)

    # must return a string
    assert isinstance(result, str)

    # must be a substring of input
    assert result in s

    # must be palindrome
    assert is_palindrome(result)

    # must be at least length 1 for non-empty input
    assert len(result) >= 1


def test_empty_string_returns_empty_string():
    # even if constraints say length >= 1, robust solutions handle empty input
    assert longest_palindromic_substring("") == ""


def test_long_input_does_not_crash():
    s = "a" * 1000
    result = longest_palindromic_substring(s)
    assert result == s


def test_multiple_max_palindromes_same_length():
    # Two max palindromes length 3: "aba" and "cdc"
    s = "abacdc"
    result = longest_palindromic_substring(s)
    assert result in {"aba", "cdc"}


def test_invalid_type_raises_typeerror():
    with pytest.raises(TypeError):
        longest_palindromic_substring(None)
