# finds all coordinates of a specific color of pawn 
def get_color_locations (board, color):
  color_locs = []
  # look through each character on the board
  if board == None:
    return None
  for i in range(len(board)):
    for j in range(len(board[i])):
      # if character is color, record its location
      if board[i][j] == color:
        color_locs.append([i, j])
  return color_locs

# copy the board into a list of lists rather than a list of strings
# this allows for easy altering of specific characters 
def board_copy(board):
  new_board = []
  for row in board:
    r = []
    for char in row:
      r.append(char)
    new_board.append(r)
  return(new_board)

# turns the board formated as a list of lists back to a list of strings 
def formatter(board_as_lists):
  new_board = []
  for row in board_as_lists:
    string = ""
    for char in row:
      string = string + char
    new_board.append(string)
  return new_board

def white_move_generater(board):
  # if the current board is a winning board dont generate more
  if is_win(board, "b", "b") != "n":
    return board
  boards = []
  # find placement of all pieces 
  white_locs = get_color_locations(board, "w")
  black_locs = get_color_locations(board, "b")
  # find all possible moves
  for white in white_locs:
    # if no black in front, white can move forward
    if ([white[0] + 1, white[1]] not in black_locs) and ([white[0] + 1, white[1]] not in white_locs):
      next_move = board_copy(board)
      next_move[white[0]][white[1]] = '-'
      next_move[white[0] + 1][white[1]] = 'w'
      boards.append(formatter(next_move))
    # if black to the right diagnol, white can move diagnol
    if [white[0] + 1, white[1] + 1] in black_locs:
      next_move = board_copy(board)
      next_move[white[0]][white[1]] = '-'
      next_move[white[0] + 1][white[1] + 1] = 'w'
      boards.append(formatter(next_move))
    # if black to the left diagnol, white can move diagnol
    if [white[0] + 1, white[1] - 1] in black_locs:
      next_move = board_copy(board)
      next_move[white[0]][white[1]] = '-'
      next_move[white[0] + 1][white[1] - 1] = 'w'
      boards.append(formatter(next_move))
  # if no boards can be made return current board
  if len(boards) == 0:
    return board
  return boards

def black_move_generater(board):
  # if the current board is a winning board dont generate more
  if is_win(board, "b", "b") != "n":
    return board
  boards = []
  # find placement of all pieces 
  white_locs = get_color_locations(board, "w")
  black_locs = get_color_locations(board, "b")
  # find all possible moves
  for black in black_locs:
    # if no black in front, white can move forward
    if ([black[0] - 1, black[1]] not in white_locs) and ([black[0] - 1, black[1]] not in black_locs):
      next_move = board_copy(board)
      next_move[black[0]][black[1]] = '-'
      next_move[black[0] - 1][black[1]] = 'b'
      boards.append(formatter(next_move))
    # if black to the right diagnol, white can move diagnol
    if [black[0] - 1, black[1] + 1] in white_locs:
      next_move = board_copy(board)
      next_move[black[0]][black[1]] = '-'
      next_move[black[0] - 1][black[1] + 1] = 'b'
      boards.append(formatter(next_move))
    # if black to the left diagnol, white can move diagnol
    if [black[0] - 1, black[1] - 1] in white_locs:
      next_move = board_copy(board)
      next_move[black[0]][black[1]] = '-'
      next_move[black[0] - 1][black[1] - 1] = 'b'
      boards.append(formatter(next_move))
  # if no boards can be made return current board
  if len(boards) == 0:
    return board
  return boards

# calls the correct next state generater depending on whose turn it is
def next_state_generater(board, turn):
  next_states = []
  if turn == "w":
    next_states = white_move_generater(board)
  else:
    next_states = black_move_generater(board)
  return next_states

# determines if the column infront of each white pawn is empty
def num_white_clear_path(board):
  clear = 0
  white_locs = get_color_locations(board, "w")
  for white in white_locs:
    non_empty = 0
    for i in range(white[0] + 1, len(board)):
      # if a non dash is found, the column is not empty
      if board[i][white[1]] != "-":
        non_empty += 1
    if non_empty == 0:
      clear += 1
  return clear 

# determines if the column infront of each black pawn is empty
def num_black_clear_path(board):
  clear = 0
  black_locs = get_color_locations(board, "b")
  for black in black_locs:
    non_empty = 0
    for i in range(0, black[0]):
      # if a non dash is found, the column is not empty
      if board[i][black[1]] != "-":
        non_empty += 1
    if non_empty == 0:
      clear += 1
  return clear 

# determines if the column infront of each black pawn is empty
# b if finding black clear, w if finding white clear
def num_player_clear_path(board, player):
  clear = 0
  if player == "b":
    clear = num_black_clear_path(board)
  else:
    clear = num_white_clear_path(board)
  return clear 

# finds the number of opponent pieces diaganol to the player
# b if finding black clear, w if finding white clear
def num_diags(board, player):
  white_diags = 0
  black_diags = 0
  white_locs = get_color_locations(board, "w")
  black_locs = get_color_locations(board, "b")
  for white in white_locs:
    if [white[0] + 1, white[1] + 1] in black_locs:
      white_diags += 1
    if [white[0] + 1, white[1] - 1] in black_locs:
      white_diags += 1
  for black in black_locs:
    if [black[0] - 1, black[1] + 1] in white_locs:
      black_diags += 1
    if [black[0] - 1, black[1] - 1] in white_locs:
      black_diags += 1
  if player == "w":
    return white_diags
  else:
    return black_diags


def is_win(board, player, turn):
  white_locs = get_color_locations(board, "w")
  black_locs = get_color_locations(board, "b")
  # no black left white wins
  if black_locs == None:
    return "w"
  # no white left black wins
  if white_locs == None:
    return "b"
  # white at end (white wins)
  for white in white_locs:
    if white[0] == len(board) - 1:
      return "w"
  # black at the other end, return -10
  for black in black_locs:
    if black[0] == 0:
      return "b"
  # for next player, if no clear count = 0, and diag count = 0 
  if turn == "w":
    if num_diags(board, "b") == 0 and num_player_clear_path(board, "b") == 0:
      return "w"
  else:
    if num_diags(board, "w") == 0 and num_player_clear_path(board, "w") == 0:
      return "b"
  # if none of these are true return "n" for no win
  return "n"



# if player = w, positive points for white doing better, negatice for black doing better
# if player = b, positive points for black doing better, negative for white doing better
# this point calculator was borrowed from the midterm:
# +10 for a win for player, -10 for a win for the opponent
# otherwise the points are calculated by:
# adding the number of the players pawns plus the number of player pawns with a clear path
# subtracting the number of opponent pawns plus the number of opponent pawns with a clear path 
def get_board_points(board, player, turn):
  white_locs = get_color_locations(board, "w")
  black_locs = get_color_locations(board, "b")
  # See if anyone wins
  winner = is_win(board, player, turn)
  # if player wins, return +10
  if winner == player:
    return 10
  # if someone wins and its not the player, return -10
  if winner != "n":
    return -10
  # calculate points if no win 
  white_clear = num_player_clear_path(board, "w")
  black_clear = num_player_clear_path(board, "b")
  white_count = len(white_locs)
  black_count = len(black_locs)
  # calculate if player is white
  if player == "w":
    return (white_clear - black_clear + white_count - black_count)
  else:
    return (black_clear - white_clear + black_count - white_count)

# returns the index at which the maximum value in a list is located
def get_max_index(lst):
  max_num = max(lst)
  for i in range(len(lst)):
    if lst[i] == max_num:
      return i

# returns the index at which the minimum value in a list is located
def get_min_index(lst):
  min_num = min(lst)
  for i in range(len(lst)):
    if lst[i] == min_num:
      return i

# this function deals with winning based on the next player not being able to move
def block_move_win(current_states, turn):
  for i in range(len(current_states)):
      # generate the next moves, just to see if someone won by preventing
      # opponent from being able to move
      next_moves = []
      if turn == "w":
        next_moves = white_move_generater(current_states[i])
        # if no next moves possible, propogate a board where white clearly wins
        if next_moves == None:
          board = current_states[i] 
          board[len(board) - 1][0] = "w"
          current_states[i] = board
      else:
        next_moves = black_move_generater(current_states[i])
        # if no next moves possible, propogate a board where black clearly wins
        if next_moves == None:
          board = current_states[i] 
          board[0][0] = "b"
          current_states[i] = board
  return current_states


def make_tree(current_states, tree_depth, max_depth, player, turn):
  # first generate a next state for each state:
  # base case: reached the end of the tree
  if tree_depth == max_depth:
    points = []
    # find the points associated with each board generated
    for state in current_states:
      t = ''
      if turn == 'w':
        t = 'b'
      else:
        t = 'w'
      point = get_board_points(state, player, t)
      points.append(point)
      # if its the players turn return the board associated with the max points
    best_points = 0
    best_board = []
    if turn != player:
      best_points = max(points)
      best_board = get_max_index(points)
    # if its not the players turn return the min
    else:
      best_points = min(points)
      best_board = get_min_index(points)
    return [best_points, best_board]

  # evaluate the states from the previous recursion 
  else:
    propogated_points = []
    best_board = []
    # get result from calling make tree on each state from current state
    for state in current_states:
      # recurse current states; switching whos turn it is 
      if turn == "w":
        result = make_tree(white_move_generater(state), tree_depth + 1, max_depth, player, "b")
        propogated_points.append(result[0])
        best_board = result[1]
      else:
        result = make_tree(black_move_generater(state), tree_depth + 1, max_depth, player, "w")
        propogated_points.append(result[0])
        best_board = result[1]
    # if depth is 0, return the board as an answer 
    if tree_depth == 0:
      return(next_state_generater(current_states[0], turn)[best_board])

    # if player == turn; return the board associated with the max value from the next moves
    if player != turn:
      best_points = max(propogated_points)
      best_board = get_max_index(propogated_points)

    # if player != turn; return the board associated with the min value from the next moves 
    else:
      best_points = min(propogated_points)
      best_board = get_min_index(propogated_points)
    return [best_points, best_board]

# This one just calls the tree function so that it can pass in whose turn it is
def hexapawn(board,board_size,player,max_depth):
  # ensure that all inputs are valid

  # check that the board dimensions are correct 
  if len(board) != board_size:
    print("Invalid board dimensions!")
    print("Check that the size of the board provided matches the provided dimension.")
    return
  for row in board:
    if len(row) != board_size:
      print("Invalid board dimensions!")
      print("Check that the size of the board provided matches the provided dimension.")
      return

  # check that max depth is 1 or more
  if max_depth < 0:
    print("Search depth must be a positive number!")
    return 
  if max_depth == 0:
    return board

  # if the board is already in a winning state dont do anything
  board_points = get_board_points(board, player, player)
  if board_points == 10 or board_points == -10:
    print("The board you provided is already a winning state")
    print("Please provide a board that is not already a winning state")
    return

  # if the player cannot move, do not do anything
  next_moves = []
  if player == "b":
    next_moves = black_move_generater(board)
  else:
    next_moves = white_move_generater(board)
  if len(next_moves) == 0:
    print("Player", player, "cannot make a move")
    print("Please provide a board that is not already a winning state")
    return

  # if all input is valid; find the best next move 
  best_move = make_tree([board], 0, max_depth, player, player)
  return best_move