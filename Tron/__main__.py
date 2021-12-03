import constants

from game.casting.cast import Cast
from game.casting.lightcycle import LightCycle
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("cycle_1", LightCycle())
    cycle_1 = cast.get_first_actor("cycle_1")
    cycle_1.prepare_body(Point(50, 50), Point(constants.CELL_SIZE, 0), constants.YELLOW)
    cast.add_actor("cycle_2", LightCycle())
    cycle_2 = cast.get_first_actor("cycle_2")
    cycle_2.prepare_body(Point(845, 545), Point(constants.CELL_SIZE, 0), constants.RED)

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()