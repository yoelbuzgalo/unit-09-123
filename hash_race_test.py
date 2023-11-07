import hash_race

def test_hash_first_char_a():
    # Setup
    x = "abc"
    expected = 97 # From ASCII table

    # Invoke
    result = hash_race.hash_first_char(x)

    # Analysis
    assert result == expected

def test_hash_first_char_empty():
    # Setup
    x = ""
    expected = 0

    # Invoke
    result = hash_race.hash_first_char(x)

    # Analysis
    assert result == expected