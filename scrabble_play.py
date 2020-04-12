#Play Scrabble against a computer
#Modules
import random

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

computer_words = ["MILK", "PIZZA", "HUNGRY", "LIST", "NUKE", "FUNNY", "QUIZ", "BIG BLACK BALLS OF MARBLES"]

#Assign each letter a point value
letter_to_points = {key: value for key, value in zip(letters, points)}
letter_to_points[" "] = 0

#Store users and their played words
player_to_words = {}

#Player Introduction
username = input("Pick a username: ")
print ("Hi, " + username)
#Add to player dictionary
player_to_words[username] = []
player_to_words["Computer"] = []

print (player_to_words)

#Score a word
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points[letter]
  return point_total

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
    player_to_words[player].append(word)
    print (player + " played " + word + " for " + str(score_word(word)) + " points!")
    return convert_to_points()

turn = 0

#Computer plays a random words from his list of words, word is then removed from list
def computer_play():
    choices = len(computer_words)
    computer_choice = random.randint(0, choices - 1)
    computer_word = computer_words[computer_choice]
    play_word("Computer", computer_word)
    computer_words.pop(computer_choice)

#Play a word
def play():
    print ("TURN: " + str(turn))
    word_temp = input("Type a word: ")
    word_temp_upper = word_temp.upper()
    print (play_word(username, word_temp_upper))
    print (player_to_words)
    computer_play()
    print (player_to_words)

#Iterate through a number of turns
while turn <= 4:
    play()
    turn += 1