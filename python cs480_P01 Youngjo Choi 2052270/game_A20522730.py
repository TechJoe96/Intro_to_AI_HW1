import state_A20522730

class Game:
  def __init__(self, first):  # These inputs are strings
    self.algo = None 
    self.first = first
    self.mode = None 
    self.winner = None

  # returns whose turn is next
  def to_move(self, state):
    x_count = sum(row.count('X') for row in state.board)
    o_count = sum(row.count('O') for row in state.board)
    
    if self.first == 'X': # human did it first
      if x_count == 0:
        return 'X'
      elif x_count > o_count:
        return 'O'
      else:
        return 'X'
    elif self.first == 'O': # "O" played first
      if o_count == 0:
        return 'O'
      elif x_count < o_count:
        return 'X'
      else:
        return 'O'

  # return True when the game ends
  def is_terminal(self, state):
    for i in range(3):
      # row bingo
      if state.board[i][0] == state.board[i][1] == state.board[i][2] and state.board[i][0] != ' ':
        self.winner = state.board[i][0]
        #print("ROW BINGO")
        return True
      # column bingo
      if state.board[0][i] == state.board[1][i] == state.board[2][i] and state.board[0][i] != ' ':
        self.winner = state.board[1][i]
        #print("COL BINGO")
        return True

    # diagonal bingo
    if state.board[0][0] == state.board[1][1] == state.board[2][2] and state.board[0][0] != ' ':
      self.winner = state.board[1][1]
      #print("DIAG1 BINGO")
      return True
    
    if state.board[0][2] == state.board[1][1] and state.board[1][1] == state.board[2][0] and state.board[0][2] != ' ':
      self.winner = state.board[1][1]
      #print("DIAG2 BINGO")
      return True
    
    # Draw
    if all(cell not in list(map(str, range(1, 10))) for row in state.board for cell in row):
      self.winner = "draw"
      #print("DRAW")
      return True

    return False

      
  # return utility value: either 1,0,-1. Return None when it's not terminal.
  def utility(self, state, player):
      for i in range(3):
          # row win
          if state.board[i][0] == state.board[i][1] == state.board[i][2]:
              if state.board[i][0] == 'O':  # 'O' is the maximizing player
                  return 1
              else:
                  return -1
          # column win
          if state.board[0][i] == state.board[1][i] == state.board[2][i]:
              if state.board[0][i] == 'O':
                  return 1
              else:
                  return -1
      # diagonal wins
      if state.board[0][0] == state.board[1][1] == state.board[2][2]:
          if state.board[0][0] == 'O':
              return 1
          else:
              return -1
      if state.board[0][2] == state.board[1][1] == state.board[2][0]:
          if state.board[0][2] == 'O':
              return 1
          else:
              return -1
      # draw
      if all(cell not in list(map(str, range(1, 10))) for row in state.board for cell in row):
          return 0
      # if not terminal
      return None

  # returns available places to move
  def actions(self, state):
    moves = []
    for i in range(3):
      for j in range(3):
        if state.board[i][j] not in ['X', 'O']:
          moves.append(state.board[i][j])
    return moves

  # returns an updated state
  def result(self, state1, action):  
      new_board = [row.copy() for row in state1.board]  # Create a deep copy of the board
      action = int(action)
        
      row = (action - 1) // 3
      col = (action - 1) % 3  

      # initiate a new object, otherwise the object will reach to a terminal state.
      # Because minimax/alpha-beta algorithms traverse through all states
      new_board[row][col] = self.to_move(state1)
        
      new_state = state_A20522730.State()  
      new_state.board = new_board
      return new_state

  # returns visualized board
  def print_board(self, state):
    for i in range(3):
        for j in range(3):
            # Check the value and print accordingly
            if state.board[i][j] in ['X', 'O'] and j!=2:
              print(f' {state.board[i][j]}' , end=' |')
            if state.board[i][j] in ['X', 'O'] and j==2:
              print(f' {state.board[i][j]}' , end=' ')
            if state.board[i][j] not in ['X', 'O'] and j!=2:
              print('   ', end='|')  # prints empty spaces
            if state.board[i][j] not in ['X', 'O'] and j==2:
              print('   ', end=' ')  # prints empty spaces

        print()  # Ends the line after each row
        if i != 2:
            print('---+---+---')
