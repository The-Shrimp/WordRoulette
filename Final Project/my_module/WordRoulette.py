class WordRoulette(): 
    '''
    A game that calculates the chances of guessing a keyword within lyrics.
    
    Attributes:
    
        User input atributes:
            lyrics (str): The lyrics of a song
            key (str): The keyword to guess within the lyric
        
        Attributes derrivative of game state and user inputs:
            lyric_list (list): List of words from the lyrics
            wordcount (int): The total number of words in the lyrics
            used_indexes (list): List of indexes already guessed
            correct_indexes (list): List of indexes correctly guessed
            
        Chance Attributes
            total_occurrences (int): Total occurrences of the keyword in the lyrics
            available_occurrences (int): Remaining occurrences of the keyword
            your_chances (str): Current chances of guessing the keyword correctly
    '''
    # instance variables
    def __init__(self, lyrics, key):
        '''
        Initialize WordRoulette with user input for lyrics and key
        
        Inputs:
            lyrics (str) - lyrics that will be searched for the key
            key (str) - key string that will be searched for in lyrics
        '''
        #homogenize to lowercase to avoid case sensitivity issues
        self.lyrics = lyrics.lower()
        self.key = key.lower()
        
        self.lyric_list = self.str_to_list()
        self.wordcount = len(self.lyric_list)
        
        # index guesses from user
        self.used_indexes = []
        self.correct_indexes = []
        
        # chances
        self.total_occurrences = self.count_total_occurrences()
        self.available_occurrences = self.total_occurrences
        self.your_chances = self.chance_counter()
   
    def str_to_list(self):
        '''
        Converts lyrics from string to a list of words 
        '''
        return self.lyrics.split()
    
    def count_total_occurrences(self):
        '''
        count total occurrences of key in the lyrics
        
        returns: 
           occurences - how many times the key exists within the lyrics
        '''
        # initialize
        occurrences = 0
        
        # determine numberator by: iterate over each word
        for lyric in self.lyric_list:
            
            # then check if key in word, incrementing numerator for each instance
            if self.key in lyric:
                occurrences += 1
            else:
                continue
                
        return occurrences
    
    def chance_counter(self):
        '''
        Calculates the chances (rounded) of the user finding the key
        
        Returns:
            string - current chances '1 in 4' or 'No more chances'
        '''
        
        # calculate total words that haven't been correctly guessed.
        remaining_words = self.wordcount - len(self.used_indexes)
        
        # check there are remaining occurrences
        if self.available_occurrences > 0:
            remaining_words = self.wordcount - len(self.used_indexes)
            
            # use max so at least 1 chance is shown if occurrences are available
            chance_ratio = max(1, remaining_words // self.available_occurrences)
            return f'1 in {chance_ratio}'
        else:
            return 'No more chances'

    def take_turn(self, index_choice):
        '''
        Checks is the user's input is valid, determining if the game procedes or requires another (valid) input
        
        Inputs:
            index_choice (int): The index input by the user
        
        Returns:
            bool: True if the guess was valid, False if invalid
        '''
       
        # practice using try --> my code here is original, I used the guide below, but I wrote the code inside :)
        # https://www.w3schools.com/python/python_try_except.asp
        # check's if user input a valid input, then tells them the rules (parameters) of the correct input
        try:
            # define index choice
            index_choice = int(index_choice)
            
            # check if index is within available bounds (0 to wordcount)
            if index_choice < 0 or index_choice >= self.wordcount:
                print("That index is out of range. Try again.")
                return False
            
            #check if choice is not already used
            if index_choice in self.used_indexes:
                print("You have already guessed this index. Try a different one.")
                return False
            
            # if neither above conditions are met, append valid choice to used_index list
            self.used_indexes.append(index_choice)
            
            #if key (substring included) exists within the indexed lyric
            if self.key in self.lyric_list[index_choice]:
                
                # and index choice has not already been correctly guessed
                if index_choice not in self.correct_indexes:
                    
                    # append correct guess to correct guess list
                    self.correct_indexes.append(index_choice)
                    
                    # Decrease available occurrences
                    self.available_occurrences -= 1
                    
                    # this was based off a drinking game that my friends and I do with common phrases in anime
                    print("TAKE A SHOT!")
                else:
                    print("You've already found this one!")
            else:
                print("Not this time. Try again.")
            
            # Update chances after every guess
            self.your_chances = self.chance_counter()
            return True
        
        # identifies and lets user know if they input an invalid number i.e 3.2213123
        except ValueError:
            print("Please enter a valid number.")
            return False