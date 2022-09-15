# Terminal App for T1A3 Assessment
## List of features in the application
1. Play a word onto the board  
   When it is their turn, player can play a word onto the board. The word must be made from the tiles on their rack and use one tile from the board, it must be a valid English word.    

2. Shuffle the tiles on the rack  
   Within their turn, the player can shuffle the tiles on their rack to help them visualising a word to play. The player can shuffle as many time as they wish.  

3. Skip a turn  
   The player can skip a turn if they cannot form a valid word, with each skip, they are given a random tile.   

4. Access HELP for rules  
   The player can type `\help\` to access the rules at any time. How many times they access `\help\` is unlimited.  

5. Quit anytime  
   The player can type `\quit\` to quit at anytime.  
  
6. Get a hint  
    Within their turn, the player can type `\hint\` to get a hint, each hint will cost 10 points.  

## Implementation Plan
Features in order of priority: 
1. Play a word onto the board
2. Shuffle the tiles on the rack  
3. Skip a turn
4. Access HELP for rules
5. Quit anytime
6. Get a hint  
   
### Play a word onto the board
To decide first play, both the player and computer are given one random tile each. Whose tile is closest to A goes first.

At the start of the game, both the player and computer player will be provided with 5 random tiles, 2 words are randomly generated to be on the board as starters.

To play a word, the players must use the tiles on their rack and one letter from the board. The word is checked against a dictionary to determine if it is a valid word. 

<table>
    <thead>
        <tr>
            <th>Checkbox</th>
            <th>Task</th>
            <th>Timeline</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>[ ]</th>
            <td>Create classes and their attributes</th>
            <td>Timeline</th>
        </tr>
        <tr>
            <td>[ ]</th>
            <td>Create instances of classes</th>
            <td>Timeline</th>
        </tr>
        <tr>
            <td>[ ]</th>
            <td>Function to randomly draw tiles</th>
            <td>Timeline</th>
        </tr>
        <tr>
            <td>[ ]</th>
            <td>Function to determine how close a character is to A</th>
            <td>Timeline</th>
        </tr>
        <tr>
            <td>[ ]</th>
            <td>Function to check if a word is valid</th>
            <td>Timeline</th>
        </tr>
        <tr>
            <td>[ ]</th>
            <td>Function to remove drawn tiles from bag</th>
            <td>Timeline</th>
        </tr>
    </tbody>
</table>
