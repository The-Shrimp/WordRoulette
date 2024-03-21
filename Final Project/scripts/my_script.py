from my_module.classes import WordRoulette

class Game():
    '''
    Manages the execution and gameplay loop of WordRoulette
    
    Attributes:
        running: (bool) determines if the game is running
    '''
    
    def __init__(self):
        '''
        Initializes the game state as running
        '''
        self.running = True
    
    # Method that starts the game
    def start_game(self):
        
        '''
        - Starts the game
        - displays rules and prompts to user
        
        User inputs initialize WordRoulette: 
            - lyrics
            - key
            
        Then starts gameplay loop
        
            - display's probability
            - user input (guess)
            
            - provides feedback on user's guess
            
            repeat until user enters "exit"
        '''
        
        #player assigns lyrics
        print("Welcome to Word Roulette!")
        print("Please insert some lyrics:")
        lyrics = input().strip()
        
        # player assigns key
        print("Please insert your keyword:")
        key = input().strip()
        
        # create instance of WordRoulette
        running_game = WordRoulette(lyrics, key)

        # Game loop
        while self.running:
            
            # print rules
            print("\nGuess an index where you think the keyword is (or type 'exit' to quit):")
            print("\nYour chances of guessing the keyword correctly are: ", running_game.your_chances)
            
            # take user input & strip to avoid errors
            user_input = input().strip()
            
            # check for exit conditions (user types: exit)
            if user_input.lower() == 'exit':
                self.running = False
                print("The owner of each of these guesses should take a shot: ", running_game.correct_indexes)
                
            # if no exit message, take another turn
            else:
                running_game.take_turn(user_input)

if __name__ == '__main__':
    unittest.main()