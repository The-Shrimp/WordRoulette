from my_module.classes import WordRoulette

# Create an instance of WordRoulette
lyrics = "light and dark"
key = "and"
game = WordRoulette(lyrics, key)

# Test Initialization
assert game.lyrics == "light and dark"
assert game.key == "and", "Key not initialized correctly"
assert isinstance(game.lyric_list, list), "Lyric list not created correctly"
assert len(game.lyric_list) == 3, "Lyric list length incorrect"

# Test Str to List Conversion
assert game.str_to_list() == ["light", "and,", "dark"], "Lyrics not converted to list correctly"

# Test Count Total Occurrences
assert game.total_occurrences == 1, "Total occurrences counted incorrectly"

# Test Chance Counter - assuming starting chance based on setup
assert game.chance_counter() in ["1 in 3"], "Initial chance calculation incorrect"

# Test Take Turn

# Invalid turn - Out of range
game.take_turn(10)
assert 10 not in game.used_indexes, "Out of range index incorrectly added to used_indexes"

# Valid turn - Correct guess
game.take_turn(1)
assert 1 in game.correct_indexes, "Correct index not added to correct_indexes"
assert game.available_occurrences == 0, "Available occurrences not updated correctly after correct guess"

# Repeat valid turn - Repeat guess
game.take_turn(0) # Repeat guess at index 0
assert game.used_indexes.count(0) == 1, "Repeat index incorrectly handled"

# Valid turn - Incorrect guess
game.take_turn(2) # Incorrect guess at index 1
assert 2 not in game.correct_indexes, "Incorrect index incorrectly added to correct_indexes"

print("All tests passed successfully!")
