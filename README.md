# Terminal App for T1A3 Assessment
## List of features in the application

1. Choose an opponent
   There are two characters as the opponent to the human player. The human player can choose which one to play against or choose to let the program pick a random character. If the player picks an unavailable character, the program will display a message which shows available characters and let them choose again. 

2. Play a word  
   When it is their turn, the player can play a word onto the board. The word must be made from the letters on their rack, the input will be checked against a dictionary (.txt file). There are three scenarios: 

   * If the word contains characters that are not in the player's rack, the program will rejects the word with an explanation, and prompts the user to try again.
   * If the word is not a valid English word, the program will reject the word with a response, and prompts the user to try again.
   * If the word only uses valid characters and is an English word, the program excepts it and prints it onto the terminal.

    The computer opponent will say a response that is appropriate for the scenario. 

3. Skip a turn  
   The player can skip a turn if they cannot form a valid word by typing `\skip` within their turn, with each skip, the player will be given a new set of characters. Their input will bypass the verification mechanism and they score 0 in that turn. Computer will play its turn then the game continues.

4. Access HELP for rules  
   The player can type `\help` to see valid keyboard inputs such as `\skip`, `\help` and `\quit`. After that, they can return to where they were in the game. 

5. Quit anytime  
   The player can type `\quit` to quit at anytime. The program will display a farewell message and terminate.
  

## Implementation Plan  

In order of priority: 
1. Game Logic 
2. Classes, attributes and methods
3. Game features
4. Testing
5. Error Handling
6. Nice-to-haves 

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
            <td>[ ]</th>
            <td>Creating combinations of characters</th>
            <td>****</th>
            <td>Timeline</th>
        </tr>
        <tr>
            <td>[ ]</th>
            <td>Logic of word verification</th>
            <td>*****</th>
            <td>Timeline</th>
        </tr>
        <tr>
            <td>[ ]</th>
            <td>Score keeping</th>
            <td>****</th>
            <td>Timeline</th>
        </tr>
        <tr>
            <td>[ ]</th>
            <td>Weighted randomization</th>
            <td>****</th>
            <td>Timeline</th>
        </tr>
    </tbody>
</table>

### Classes, attributes and methods
`Character` class is the superclass, its attributes are: name, points and rack. Default points is 0, and rack is empty. This class has the `__repr__` and `__str__` methods both return the player's name. The human player is an instance of `Character` class with the name `'Human'`

`Computer` is a subclass of the `Character` class, it inherits all attributes and methods from `Character`. It has three additional methods that are `.shuffle_letters()`, `.play()` and `.response()` to make a comment on the player's words.

`Word` class has a 'word' attribute and a `verify()` method.

`Game` class has an `__init__` method and methods such as `get_input()`, `announce_players()`, `announce_turn()`, `calculate_points()`, `deal_characters()`

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
            <td>[ ]</th>
            <td>Create Character class, its attributes and methods</th>
            <td>**</th>
            <td>Timeline</th>
        </tr>
        <tr>
            <td>[ ]</th>
            <td>Create Computer class</th>
            <td>**</th>
            <td>Timeline</th>
        </tr>
        <tr>
            <td>[ ]</th>
            <td>Create Word class, its attributes and methods</th>
            <td>**</th>
            <td>Timeline</th>
        </tr>
        <tr>
            <td>[ ]</th>
            <td>Create Game class, its attributes and methods</th>
            <td>**</th>
            <td>Timeline</th>
        </tr>
    </tbody>
</table>


### Game features

1. Choose opponent
   * Get user input
   * Check it against available opponent characters 
     - if valid: return user input
     - if invalid: loop back to the prompt  
2. Play a word: 
   * get user input 
   * check it using the `.verify()` method 
        - if valid: return the valid result
        - if invalid: loop back to the input prompt
3. Skip a turn
   * Check user input for `\skip`
   * Print a response on the terminal
   * Player's word will be '####', which equals 0 points, bypass the verification step. 
   * Computer plays its turn 
4. Access help
   * Check user input for `\skip`
   * If true: print a response on the terminal
   * Loop back to the get input prompt
5. Quit anytime
   * Check user input for `\quit`
   * If true: print a farewell response on the terminal
   * Terminate the program


