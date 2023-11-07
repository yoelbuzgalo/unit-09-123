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

def test_hash_sum_abc():
    # Setup
    x = "abc"
    expected = 294 # 97+98+99 (from ASCII table)

    # Invoke
    result = hash_race.hash_sum(x)

    # Analysis
    assert result == expected

def test_hash_sum_empty():
    # Setup
    x = ""
    expected = 0

    # Invoke
    result = hash_race.hash_sum(x)

    # Analysis
    assert result == expected

def test_hash_positional_empty():
    # Setup
    x = ""
    expected = 0

    # Invoke
    result = hash_race.hash_positional_sum(x)

    # Analysis
    assert result == expected

def test_hash_positional_sum_abcd():
    # Setup
    x = "abcd"
    expected = 2987074

    # Invoke
    result = hash_race.hash_positional_sum(x)

    # Analysis
    assert result == expected

def test_hash_positional_sum_bdca():
    # Setup
    x = "bdca"
    expected = 3018784

    # Invoke
    result = hash_race.hash_positional_sum(x)

    # Analysis
    assert result == expected