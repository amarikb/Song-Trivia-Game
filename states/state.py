"""
"Pygame Game States Tutorial: Creating an In-game Menu using States", ChristianD37
source: https://www.youtube.com/watch?v=b_DkQrJxpck
Ideas for the implementation of the pygame game states design (State Abstract Class)
Retrieved 10-19-2021  
"""
class State():
    def __init__(self, game):
        self.game = game
        self.prev_state = None

    def update(self, actions):
        pass

    def render(self, surface):
        pass

    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)

    def exit_state(self):
        self.game.state_stack.pop()