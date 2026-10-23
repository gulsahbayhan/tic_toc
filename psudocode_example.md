1- WELCOME MESSAGE
   print welcome message + rules + board
   OUTPUT welcome message
   OUTPUT rules
   OUTPUT initial empty board (positions 1 to 9)

2- CHOOSE SYMBOLS
   PROMPT Player 1 to choose "X" or "O"
   IF Player 1 chooses "X" THEN
       SET Player 2 = "O"
   ELSE
       SET Player 2 = "X"
   ENDIF

3- initialize variables
   SET move_count = 0
   SET game_over = FALSE

4- main game loop
   WHILE game_over IS FALSE DO
       
       # Determine player's turn
       IF move_count MOD 2 == 0 THEN
           SET current_player = Player 1
       ELSE
           SET current_player = Player 2
       ENDIF

       # Get player input
       OUTPUT current board
       PROMPT current_player to enter a position (1-9)
       INPUT chosen_position

       # Validate and place move
       IF chosen_position is already taken OR not between 1 and 9 THEN
           OUTPUT "Invalid move, try again."
       ELSE
           PLACE current_player symbol on chosen_position
           INCREMENT move_count by 1

           # Check for winner (rows, columns, diagonals)
           IF current_player has 3 symbols in a row THEN
               OUTPUT final board
               OUTPUT current_player + " wins the game!"
               SET game_over = TRUE
           
           # Check for draw
           ELSE IF move_count == 9 THEN
               OUTPUT final board
               OUTPUT "It's a draw!"
               SET game_over = TRUE
           ENDIF
       ENDIF

   ENDWHILE