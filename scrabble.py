letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Assign each letter a point value
letter_to_points = {key: value for key, value in zip(letters, points)}
letter_to_points[" "] = 0

#Score a word
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points[letter]
  return point_total
#Test Function
#brownie_points = score_word("BROWNIE")
#print (brownie_points)

#List of players and their words... so far ;)
player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"],
  "wordNerd": ["EARTH", "EYES", "MACHINE"],
  "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
  "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

#Convert players words to points and assing to dict player_to_points
def convert_to_points():
    player_to_points = {}
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points
    return player_to_points

#Add a word to a players list and return the point totals for each player
def play_word(player, word):
    word_upper = word.upper()
    player_to_words[player].append(word_upper)
    print (player + " played " + word_upper + " for " + str(score_word(word_upper)) + " points!")
    return convert_to_points()

print (play_word("player1", "Hello World"))
print (play_word("wordNerd", "HUMpdAY"))
print (play_word("Lexi Con", "Indupitably"))
print (play_word("Prof Reader", "YELLOW"))
