import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._dead_player = None

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_self_collision(cast)
            self._handle_other_collisions(cast)
            # self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    
    # def _handle_segment_collision(self, cast):
    #     """Sets the game over flag if the snake collides with one of its segments.
        
    #     Args:
    #         cast (Cast): The cast of Actors in the game.
    #     """
    #     cycle_1 = cast.get_first_actor("cycle_1")
    #     head = cycle_1.get_segments()[0]
    #     cycle_1_segments = cycle_1.get_segments()[1:]

    #     cycle_2 = cast.get_first_actor("cycle_2")
    #     cycle_2_segments = cycle_2.get_segments()[1:]
        
    #     # check to see if player 1 run into self
    #     for segment in cycle_1_segments:
    #         if head.get_position().equals(segment.get_position()):
    #             self._is_game_over = True
    #             self._dead_player = "cycle_1"
                
    #     # Run into other player   
    #     for segment_2 in cycle_2_segments:
    #         if head.get_position().equals(segment_2.get_position()):
    #             self._is_game_over = True
    #             self._dead_player = "cycle_1"
        
    #     cycle_2 = cast.get_first_actor("cycle_2")
    #     head = cycle_2.get_segments()[0]
    #     cycle_2_segments = cycle_2.get_segments()[1:]

    #     cycle_1 = cast.get_first_actor("cycle_1")
    #     cycle_1_segments = cycle_1.get_segments()[1:]

    #     for segment in cycle_2_segments:
    #         if head.get_position().equals(segment.get_position()):
    #             self._is_game_over = True
    #             self._dead_player = "cycle_2"

    #     for segment_1 in cycle_1_segments:
    #         if head.get_position().equals(segment_1.get_position()):
    #             self._is_game_over = True
    #             self._dead_player = "cycle_2"

    def _handle_self_collision(self,cast):
        cycle_1 = cast.get_first_actor("cycle_1")
        cycle_1_head = cycle_1.get_segments()[0]
        cycle_1_segments = cycle_1.get_segments()[1:]

        cycle_2 = cast.get_first_actor("cycle_2")
        cycle_2_head = cycle_2.get_segments()[0]
        cycle_2_segments = cycle_2.get_segments()[1:]

        for segment in cycle_1_segments:
            if cycle_1_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._dead_player = "cycle_1"
        
        for segment in cycle_2_segments:
            if cycle_2_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._dead_player = "cycle_2"

    def _handle_other_collisions(self,cast):
        cycle_1 = cast.get_first_actor("cycle_1")
        cycle_1_head = cycle_1.get_segments()[0]
        cycle_1_segments = cycle_1.get_segments()[1:]

        cycle_2 = cast.get_first_actor("cycle_2")
        cycle_2_head = cycle_2.get_segments()[0]
        cycle_2_segments = cycle_2.get_segments()[1:]

        # check if cycle_2 hit cycle_1
        for segment in cycle_1_segments:
            if cycle_2_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._dead_player = "cycle_2"

        # check if cycle_1 hit cycle_2
        for segment in cycle_2_segments:
            if cycle_1_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._dead_player = "cycle_1"

    def _handle_game_over(self, cast):
        """Shows the 'game over' message if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            if self._dead_player == "cycle_1":
                color_winner = "Red"
            elif self._dead_player == "cycle_2":
                color_winner = "Yellow"
            message.set_text(f"Game Over! {color_winner} Wins!")
            message.set_position(position)
            cast.add_actor("messages", message)
