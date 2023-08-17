**Objective**: Develop a RESTful API for a Tic Tac Toe game using Python.

**Minimum Requirements**:

1. **Endpoints**:
   
   **a.** `POST /move`
   - **Payload**:
     ```json
     {
         "player": "X|O",
         "location": [x, y]
     }
     ```
   - **Response**:
     ```json
     {
         "board": [
             [], [], []
         ],
         "winner": "X|O|None"
     }
     ```

   **b.** `GET /board`
   - **Response**:
     ```json
     {
         "board": [
             [], [], []
         ],
         "winner": "X|O|None"
     }
     ```

2. **Functionality**: 
   - Allow players 'X' and 'O' to make moves.
   - Return the updated game board after each move.
   - Indicate the winner if the game has concluded.
