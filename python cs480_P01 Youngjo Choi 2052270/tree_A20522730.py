class Tree:
  def __init__(self):
      self.minus_infinity = float('-inf')
      self.plus_infinity = float('inf')
      self.nodes_generated = 0

  def minimax_search(self, game, state):
    player = game.to_move(state)  # X is our min player
    if player == 'X':
      value, move = self.min_value(game, state)
    else:
      value, move = self.max_value(game, state) # O is our max player
    return move # an action, which is a position number


  def max_value(self, game, state):
    #print("Checking state in max_value:", state.board)
    self.nodes_generated += 1
    player = game.to_move(state)
    if game.is_terminal(state):
      return game.utility(state, player), None
    v = self.minus_infinity
    for a in game.actions(state):
      v2, a2 = self.min_value(game, game.result(state, a))
      if v2 > v:
        v = v2
        move = a
    return v, move  # v: utility, move: position number / action

  def min_value(self, game, state):
    #print("Checking state in min_value:", state.board)
    self.nodes_generated += 1
    player = game.to_move(state) 
    if game.is_terminal(state):
      return game.utility(state, player), None
    v = self.plus_infinity
    for a in game.actions(state):
      v2, a2 = self.max_value(game, game.result(state, a))
      if v2 < v:
        v = v2
        move = a
    return v, move

  
  def alpha_beta_search(self, game, state):
    player = game.to_move(state)
    if player == 'O':
      value, move = self.alpha_beta_max_value(game, state, self.minus_infinity, self.plus_infinity)
    else:
      value, move = self.alpha_beta_min_value(game, state, self.minus_infinity, self.plus_infinity)
    return move # an action
  
  def alpha_beta_max_value(self, game, state, alpha, beta):
    self.nodes_generated += 1
    player = game.to_move(state)
    if game.is_terminal(state):
      return game.utility(state, player), None
    v = self.minus_infinity
    for a in game.actions(state):
      v2, a2 = self.alpha_beta_min_value(game, game.result(state,a), alpha, beta)
      if v2 > v:
        v = v2
        move = a
        alpha = max(alpha, v)
      if v >= beta:
        return v, move
    return v, move
  
  def alpha_beta_min_value(self, game, state, alpha, beta):
    self.nodes_generated += 1
    player = game.to_move(state)
    if game.is_terminal(state):
      return game.utility(state, player), None
    v = self.plus_infinity
    for a in game.actions(state):
      v2, a2 = self.alpha_beta_max_value(game, game.result(state, a), alpha, beta)
      if v2 < v:
        v = v2
        move = a
        beta = min(beta, v)
      if v <= alpha:
        return v, move
    return v, move
  