# Terminal App for T1A3 Assessment

## Links
1. GitHub repository: https://github.com/Thi-Tracey-Nguyen/word_game
2. Youtube presentation:  

## Code guide and styling conventions  
1. Goodger, D., Rossum, G. (2001) PEP 257 - Docstring Conventions [Styling Convention]. https://peps.python.org/pep-0257/  
2. Rossum, G., Warsaw, B., Coghlan, N. (2001) PEP8 - Style Guide for Python Code [Styling Convention]. https://peps.python.org/pep-0008/

## List of features in the application

1. Choose an opponent
   There are two characters as the opponent to the human player. The human player can choose which one to play against or choose to let the program pick a random character. If the player picks an unavailable character, the program will display a message which shows available characters and let them choose again.

2. Play a word  
   When it is their turn, the player can play a word. The word must be made from the letters on their rack, the input will be checked against a dictionary (.txt file). There are three scenarios:

   * If the word contains characters that are not in the player's rack, the program will rejects the word with an explanation, and prompts the user to try again.
   * If the word is not a valid English word, the program will reject the word with a response, and prompts the user to try again.
   * If the word only uses valid characters and is an English word, the program excepts it and prints it onto the terminal.

    The computer opponent will say a response that is appropriate for the scenario.

3. Skip a turn  
   The player can skip a turn if they cannot form a valid word by typing `%skip` within their turn. With each skip, the player will be given a new set of letters. Their input will bypass the verification mechanism and they score 0 in that turn. Computer will play its turn then the game continues.

4. Access HELP for rules  
   The player can type `%help` to see valid keyboard inputs such as `%skip`, `%help` and `%quit`. After that, they can return to where they were in the game.

5. Quit anytime  
   The player can type `%quit` or `Ctrl+C` to quit at anytime. The program will display a farewell message and terminate.
  
### Feature logics  

1. Choose opponent
   * Get user input
   * Check it against available opponent characters
     * if valid: return user input
     * if invalid: loop back to the prompt  
2. Play a word:
   * get user input
   * check it using the `.verify()` method
        * if valid: return the valid result
        * if invalid: loop back to the input prompt
3. Skip a turn
   * Check user input for `%skip`
   * Print a response on the terminal
   * Player's word will be '####', which equals 0 points, bypass the verification step.
   * Computer plays its turn
4. Access help
   * Check user input for `%help`
   * If true: print a response on the terminal
   * Loop back to the get input prompt
5. Quit anytime
   * Check user input for `%quit`
   * If true: print a farewell response on the terminal
   * Terminate the program

## Implementation Plan  

In order of priority:

1. Game Logic
2. Modules,classes, attributes and methods
3. Game features
4. Testing
5. Exception Handling

### Game Logic  

* Weighted randomization of word characters.
* Create permutations of characters with randomized permutation length to keep the game fair.
* Word verification requires two steps:  1/Checking if all the characters is from the player's rack and 2/Checking if the word is a valid English word.
* Score keeping: points for each character in the valid word are stored in a dictionary, use itertation to calculate points for each word and carry the points through the whole game.

<table>
    <thead>
        <tr>
            <th>Checkbox</th>
            <th>Task</th>
            <th>Priority</th>
            <th>Timeline</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>[x]</th>
            <td>Research on applicable modules (random, numpy, etc.)</th>
            <td>*****</th>
            <td>16-17 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Function to create combinations of characters</th>
            <td>*****</th>
            <td>16-17 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Logic of word verification</th>
            <td>******</th>
            <td>16-17 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Score keeping</th>
            <td>****</th>
            <td>16-17 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Weighted randomization</th>
            <td>****</th>
            <td>16-17 Sept</th>
        </tr>
    </tbody>
</table>

### Modules, classes, attributes and methods

1. ```character``` module  
   `Character` class is the superclass, its attributes are: name, points and rack. Default points is 0, and rack is empty. This class has the `__repr__` and `__str__` methods both return the player's name. The human player is an instance of `Character` class with the name `'Human'`  
   `Computer` is a subclass of the `Character` class, it inherits all attributes and methods from `Character`. It has three additional methods that are `.shuffle_letters()`, `.play()` and `.response()` to make a comment on the player's words.  
2. ```word``` module  
   `Word` class has a 'word' attribute and a `verify()` method.
3. ```game``` module  
   `Game` class has an `__init__` method and methods such as `get_input()`, `announce_players()`, `announce_turn()`, `calculate_points()`, `deal_characters()`
4. ```data``` module:  
   It contains constants such as `letter_values` which stores point values of each letter. `letter_collection` stores all the alphabet letters and its frequencies of occurance.  
   It also has constants which are lists of responses the computer uses to responde to the player's moves such as ```positive```, ```negative``` and ```skip``` to use when the computer cannot produce a valid word within 'try limits'.  
   This module has one method: ```typewriter()``` to print words to the console with typewriter effect, which helps with readability.

<table>
    <thead>
        <tr>
            <th>Checkbox</th>
            <th>Task</th>
            <th>Priority</th>
            <th>Timeline</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>[x]</th>
            <td>Create Character class, its attributes and methods</th>
            <td>***</th>
            <td>18-20 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Create Computer class</th>
            <td>***</th>
            <td>18-20 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Create Word class, its attributes and methods</th>
            <td>***</th>
            <td>18-20 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Create Game class, its attributes and methods</th>
            <td>***</th>
            <td>18-20 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Logic for difficulty control</th>
            <td>***</th>
            <td>20 Sept</th>
        </tr>
    </tbody>
</table>

![Trello Board](./docs/Screen%20Shot%202022-09-24%20at%208.25.06%20am.png)  

### Game features  

1. Choose an opponent  

* Requires a ```.get_input()``` method to compare users input to available characters
  * Instantiates a computer player according to the valid input
  * Loops back to input prompt if input was invalid

<table>
    <thead>
        <tr>
            <th>Checkbox</th>
            <th>Task</th>
            <th>Priority</th>
            <th>Timeline</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>[x]</th>
            <td>Create .get_input() in Game class </th>
            <td>***</th>
            <td>20-21 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Write methods to compare get_input to valid inputs</th>
            <td>***</th>
            <td>20-21 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Create a loop to go back if input is invalid</th>
            <td>***</th>
            <td>20-21 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Instantiate a computer_player as an object of Character class</th>
            <td>***</th>
            <td>20-21 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Raise exceptions if input meets conditions</th>
            <td>***</th>
            <td>20-21 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Write test case</th>
            <td>***</th>
            <td>20-21 Sept</th>
        </tr>
    </tbody>
</table>

2. Play a word  

* Uses `.get_input()` method to get user input  
* Uses `.verify()` method to verify the word on 2 aspects:
  * Checks if the word only uses letters in the player's rack, the number of occurence of each letter is also considered. If this test fails, the game loops back to get input prompt.
  * Once the word passes the previous check, it is checked against a dictionary.txt file. If valid, the method returns the valid word. If it fails this test, the game loops back to get input prompt.  

<table>
    <thead>
        <tr>
            <th>Checkbox</th>
            <th>Task</th>
            <th>Priority</th>
            <th>Timeline</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>[x]</th>
            <td>Create .get_word() in Game class, which uses .get_input()</th>
            <td>21-22 Sept</th>
            <td>Timeline</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Write methods to parse letters in the player's word and compare each letter to the rack</th>
            <td>***</th>
            <td>21-22 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Once the word passes the first step, check it in the dictionary</th>
            <td>***</th>
            <td>21-22 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>If the player's word is valid, returns it</th>
            <td>***</th>
            <td>21-22 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>If the player's word is invalid, loops back to the get_word() prompt</th>
            <td>***</th>
            <td>21-22 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Write test case</th>
            <td>***</th>
            <td>21-22 Sept</th>
        </tr>
    </tbody>
</table>

3. Skip a turn  

* Uses `.get_input()` method to get user input
* Checks user input if it is `%skip`, if True, a SkipTurn exception is raised
* Computer plays its turn
* Human player point is 0 for that turn  

<table>
    <thead>
        <tr>
            <th>Checkbox</th>
            <th>Task</th>
            <th>Priority</th>
            <th>Timeline</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>[x]</th>
            <td>Create a SkipTurn exception as a subclass of the built-in Exception class</th>
            <td>***</th>
            <td>22 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Function to check input receives from get_input() against %skip, raises SkipTurn exception if True</th>
            <td>***</th>
            <td>22 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Manage the control flow: computer plays its turn</th>
            <td>***</th>
            <td>22 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Player's word point is 0 for this round</th>
            <td>***</th>
            <td>22 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Write test case</th>
            <td>***</th>
            <td>22 Sept</th>
        </tr>
    </tbody>
</table>

4. Access Help

* Uses ```.get_input()``` method to get user input
* Checks user input if it is ```%help```, if True, a HelpRequired exception is raised
* 'Help' message is printed on the terminal. It shows valid inputs and reminds the player of high-scoring letters (J, X, Q, Z )
* Loops back to where the player was before typing ```%help```

<table>
    <thead>
        <tr>
            <th>Checkbox</th>
            <th>Task</th>
            <th>Priority</th>
            <th>Timeline</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>[x]</th>
            <td>Create a HelpRequired exception as a subclass of the built-in Exception class</th>
            <td>***</th>
            <td>22 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Function to check input receives from get_input() against %help, raises HelpRequired exception if True</th>
            <td>***</th>
            <td>22 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Manage the control flow: loops back to where the player was</th>
            <td>***</th>
            <td>22 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>The game must continue afterward</th>
            <td>***</th>
            <td>22 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Write test case</th>
            <td>***</th>
            <td>22 Sept</th>
        </tr>
    </tbody>
</table>

5. Quit anytime  

* Checks user input if it is `%quit`, if True, a Quit exception is raised
* This feature also handles built-in KeyboardInterrupt error and terminates gracefully
* Print a farewell message to the terminal and the program terminates.

<table>
    <thead>
        <tr>
            <th>Checkbox</th>
            <th>Task</th>
            <th>Priority</th>
            <th>Timeline</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>[x]</th>
            <td>Create a Quit exception as a subclass of the built-in Exception class</th>
            <td>***</th>
            <td>Timeline</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Function to check input receives from get_input() against %quit, raises Quit exception if True</th>
            <td>***</th>
            <td>Timeline</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Manage the control flow: print a farewell message</th>
            <td>***</th>
            <td>23 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Terminate the program</th>
            <td>***</th>
            <td>23 Sept</th>
        </tr>
        <tr>
            <td>[x]</th>
            <td>Write test case</th>
            <td>***</th>
            <td>23 Sept</th>
        </tr>
    </tbody>
</table>

![Trello board](./docs/Screen%20Shot%202022-09-24%20at%208.29.59%20am.png)

## Installation
### System requirements
- The application requires python 3.10 to run. If you do not have python in your machine, go [here](https://www.python.org/downloads/) and install the appropriate program for your operating system.

### Steps to install
1. Open terminal by: 
- On Mac: pressing Command + space, type 'Terminal', hit enter
- On window: pressing Windows key + X then click Command prompt, at the command prompt, type: 'bash' then hit Enter
2. In the terminal, input the followings:  
* Clone this repository to your computer  
```git clone https://github.com/Thi-Tracey-Nguyen/word_game```
* Change the working directory to where you downloaded the folder:   
```cd <filepath>```  
* Open the downloaded file:  
```open src```  
* Allow the execution of the bash script:  
```chmod +x word_game.sh```  
* Run the program:  
```./word_game.sh```

### Dependencies
These dependencies will be automatically installed in your virtual environment:  
```attrs==22.1.0
clearing==1.0.0
iniconfig==1.1.1
numpy==1.23.3
packaging==21.3
pluggy==1.0.0
py==1.11.0
pyparsing==3.0.9
pytest==7.1.3
tomli==2.0.1
```

### Valid inputs for the application
1. `%Help` to see Help menu
2. `%Quit` or `Ctrl+C` to quit anytime
3. `%Skip` to skip when it's your turn.  
