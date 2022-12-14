import pygame
import cursor
from draggable import Draggable

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

size = [SCREEN_WIDTH, SCREEN_HEIGHT]


class Box(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/box.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 1.75)
        self.rect = self.image.get_rect(center=(100, 100))


class Game:
    def __init__(self):
        self.game_over = False

        # Set Cursor Sprite
        self.cursor_sprite = pygame.sprite.GroupSingle()

        self.boxes = pygame.sprite.Group()
        
        self.cursor = cursor.Cursor()

        for i in range(3):
            box = Draggable(Box())
            box.rect.x += 150 * i

            self.boxes.add(box)
        self.cursor_sprite.add(self.cursor)
        


    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.MOUSEMOTION:
                for obj in self.boxes:
                    if pygame.sprite.collide_rect(obj, self.cursor):
                        self.cursor.isHovering = True
                    else:
                        self.cursor.isHovering = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                flag = True
                for obj in self.boxes:
                    if pygame.sprite.collide_rect(obj, self.cursor) and flag:
                        flag = False

                        self.cursor.mouse_interact(obj)


            self.cursor.mouse_click(event)

            
    def run_logic(self):
        if not self.game_over:
            self.boxes.update()
            self.cursor_sprite.update()

    def display_frame(self, screen):
        screen.fill("Black")
        if not self.game_over:
            self.boxes.draw(screen)
            self.cursor_sprite.draw(screen)


def main():
    pygame.init()

    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Cursor Test")
    pygame.mouse.set_visible(False)

    done = False
    clock = pygame.time.Clock()

    game = Game()

    while not done:
        
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        
        pygame.display.update()
        clock.tick(60)


    pygame.quit()        


if __name__ == "__main__":
    main()
