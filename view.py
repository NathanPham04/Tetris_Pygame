import pygame
import model
import game_logic
import time

BACKGROUND_COLOR = pygame.Color(192, 185, 185)
COLOR_LANDED = pygame.Color(245, 87, 39)

COLOR_WHITE = pygame.Color(255, 255, 255)
COLOR_BLACK = pygame.Color(0, 0, 0)
COLOR_RED = pygame.Color(255, 0, 0)
COLOR_ORANGE = pygame.Color(255, 128, 0)
COLOR_YELLOW = pygame.Color(255, 255, 0)
COLOR_GREEN = pygame.Color(0, 255, 0)
COLOR_BLUE = pygame.Color(0, 0, 255)
COLOR_PURPLE = pygame.Color(127, 0, 255)
COLOR_TURQUOISE = pygame.Color(64, 224, 208)

color_dict = {
            "S": COLOR_GREEN,
            "L": COLOR_BLUE,
            "J": COLOR_ORANGE,
            "I": COLOR_TURQUOISE,
            "T": COLOR_PURPLE,
            "Z": COLOR_RED,
            "O": COLOR_YELLOW,
        }

class UserView:
    def __init__(self):
        self._running = True
        self.game = model.ColumnGame()
        self._count = 0
        self._next_image = pygame.image.load("next_piece.png")
        self._score_img = pygame.image.load("score.png")

    def run(self) -> None:
        """This runs the game"""
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        #start_sound = pygame.mixer.Sound('start_game.wav')
        #start_sound.play()
        
        try:
            self._resize_surface((600, 600))

            clock1 = pygame.time.Clock()

            while self._running:
                clock1.tick(60)
                self._handle_events()
                self._redraw()
                if self._count == 0:
                    self.game.play_game()
                    self._count = 60
                else:
                    self._count -= 1
        except game_logic.GameOverError:
            self._running = False
            self.draw_game_over(pygame.display.get_surface())
            time.sleep(5)
        finally:
            pygame.mixer.quit()
            pygame.font.quit()
            pygame.quit()

    def _handle_events(self) -> None:
        """This will handle the events of quitting and resizing"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._end_game()
            elif event.type == pygame.VIDEORESIZE:
                self._resize_surface(event.size)
            elif event.type == pygame.KEYDOWN:
                try:
                    if event.key == pygame.K_LEFT:
                        self.game.faller.move_faller_left()
                    if event.key == pygame.K_RIGHT:
                        self.game.faller.move_faller_right()
                    if event.key == pygame.K_z:
                        self.game.faller.rotate_faller_left()
                    if event.key == pygame.K_x:
                        self.game.faller.rotate_faller_right()
                except (game_logic.InvalidMoveError, AttributeError):
                    pass
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self._count = min(self._count, 5)

    def _redraw(self) -> None:
        """This will get the surface, fill in the background"""
        surface = pygame.display.get_surface()

        # Fills the surface with the entire screen
        surface.fill(BACKGROUND_COLOR)
        
        # Creates the background of the board in a 6:13 ratio
        left, top, width, height = self._get_surface_board()
        board_outline = pygame.Rect(left, top, width, height)
        pygame.draw.rect(surface, COLOR_BLACK, board_outline)

        # Draws in the board pieces
        self._draw_pieces(surface, left, width, height)

        # Draws the lines into the board
        self._draw_board_lines(surface, left, width, height)

        # Draws the score
        self.draw_score(surface, left)

        pygame.display.flip()

    def _get_surface_board(self) -> tuple[float, float, float, float]:
        """This will return the location of where to draw the background of the board"""
        surface = pygame.display.get_surface()
        width = surface.get_width()*.6
        height = surface.get_height()
        width = min(width, height * 10 / 20)
        height = min(height, width * 20 / 10)
        left = (surface.get_width() - width) / 2
        top = 0
        return (left, top, width, height)

    def _draw_board_lines(
        self, surface: pygame.Surface, left: float, width: float, height: float
    ) -> None:
        """This will draw the lines in the board"""
        horizontal_diff = height / 20
        start = 0
        for i in range(20):
            pygame.draw.line(surface, COLOR_WHITE, (left, start), (left + width, start), 3)
            start += horizontal_diff
        vertical_diff = width / 10
        start = left
        for i in range(10):
            pygame.draw.line(surface, COLOR_WHITE, (start, 0), (start, height), 3)
            start += vertical_diff

    def _end_game(self) -> None:
        """This will make the game loop end"""
        self._running = False

    def _resize_surface(self, size: tuple[int, int]) -> None:
        """This will resize the pygame window appropriately"""
        pygame.display.set_mode(size, pygame.RESIZABLE)

    def _draw_pieces(
        self, surface: pygame.Surface, left: float, width: float, height: float
    ) -> None:
        """This will draw the pieces in the board"""
        board = self.game._game.board
        start_left = left
        horizontal_diff = height / 20
        vertical_diff = width / 10
        #match_sound = pygame.mixer.Sound('match.wav')
        #match_sound.set_volume(0.2)
        #landed_sound = pygame.mixer.Sound('landed.wav')
        #landed_sound.set_volume(0.4)
        for col in range(len(board)):
            start_top = 0
            for row in range(2, len(board[col])):
                val = board[col][row].val
                if val != "_":
                    color = color_dict.get(val)
                    rect = pygame.Rect(start_left, start_top, vertical_diff, horizontal_diff)
                    pygame.draw.rect(surface, color, rect)
                start_top += horizontal_diff
            start_left += vertical_diff
        # if landed:
        #     landed_sound.play()
        # if matched:
        #     match_sound.play()
        # Draws the next piece in the top left
        # top_left = left/2-vertical_diff/2
        # top_height = surface.get_height() * .4
        # for index, letter in enumerate(self._game_object._next_faller._letters):
        #     color = color_dict.get(letter)
        #     rect = pygame.Rect(
        #             top_left,
        #             top_height,
        #             vertical_diff,
        #             horizontal_diff)
        #     pygame.draw.rect(surface, color, rect)
        #     top_height += horizontal_diff
        # top_height = surface.get_height() * .4
        # pygame.draw.line(surface, COLOR_BLACK, (top_left, top_height), (top_left, top_height + 3*horizontal_diff), 3)
        # pygame.draw.line(surface, COLOR_BLACK, (top_left+vertical_diff, top_height), (top_left+vertical_diff, top_height + 3*horizontal_diff), 3)
        # for i in range(4):
        #     pygame.draw.line(surface, COLOR_BLACK, (top_left, top_height), (top_left + vertical_diff, top_height), 3)
        #     top_height += horizontal_diff
        # self._next_image = pygame.transform.scale(
        #     self._next_image, (left/2, horizontal_diff*2)
        # )
        # surface.blit(self._next_image, (left/4, surface.get_height()*.2))

    def draw_score(self, surface: pygame.Surface, left: float) -> None:
        size = int(surface.get_height()/15)
        font = pygame.font.SysFont('Comic Sans MS', size)
        score = font.render(str(self.game._score), False, COLOR_WHITE)
        surface.blit(score, (surface.get_width() - left/1.2, surface.get_height()*.4))
        self._score_img = pygame.transform.scale(self._score_img, ((left/2, surface.get_height()/13*2)))
        surface.blit(self._score_img, (surface.get_width() - left + left/4, surface.get_height()*.2))

    def draw_game_over(self, surface: pygame.Surface) -> None:
        self._image = pygame.image.load("non_python_files/game_over.png")
        self._image = pygame.transform.scale(
            self._image, (surface.get_width(), surface.get_height())
        )
        surface.blit(self._image, (0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    UserView().run()