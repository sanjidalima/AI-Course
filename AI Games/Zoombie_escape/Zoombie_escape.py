import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 500, 500
GRID_SIZE = 5
CELL_SIZE = WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Escape")
font = pygame.font.SysFont('Arial', 32)
emoji_font = pygame.font.SysFont('Segoe UI Emoji', 40)

class Game:
    def __init__(self):
        self.reset_game()
        
    def reset_game(self):
        self.player_pos = [0, 0]
        self.zombie_pos = [GRID_SIZE-1, GRID_SIZE-1]
        self.player_path = []
        self.game_over = False
        self.winner = None
        
    def draw_grid(self):
        screen.fill(WHITE)
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, BLACK, rect, 1)
                
        
        exit_rect = pygame.Rect((GRID_SIZE-1)*CELL_SIZE, (GRID_SIZE-1)*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, GREEN, exit_rect, 3)
        
        
        player_text = emoji_font.render("🧑", True, BLACK)
        screen.blit(player_text, (
            self.player_pos[1]*CELL_SIZE + CELL_SIZE//4,
            self.player_pos[0]*CELL_SIZE + CELL_SIZE//5
        ))
        
       
        zombie_text = emoji_font.render("🧟", True, BLACK)
        screen.blit(zombie_text, (
            self.zombie_pos[1]*CELL_SIZE + CELL_SIZE//4,
            self.zombie_pos[0]*CELL_SIZE + CELL_SIZE//5
        ))
        
        
        instr = font.render("U/D/L/R to move | S to restart", True, BLACK)
        screen.blit(instr, (10, HEIGHT-40))
        
        if self.game_over:
            msg = "You Escaped!" if self.winner == "player" else "Zombie Got You!"
            text = font.render(msg, True, BLACK)
            text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
            pygame.draw.rect(screen, WHITE, (WIDTH//2-150, HEIGHT//2-30, 300, 60))
            screen.blit(text, text_rect)
            
            restart = font.render("Press S to restart", True, BLACK)
            screen.blit(restart, (WIDTH//2-100, HEIGHT//2+30))
    
    def move_player(self, direction):
        if self.game_over:
            return
            
        direction = direction.upper()
        self.player_path.append(direction)
        
        
        if direction == "W" and self.player_pos[0] > 0:
            self.player_pos[0] -= 1
        elif direction == "S" and self.player_pos[0] < GRID_SIZE-1:
            self.player_pos[0] += 1
        elif direction == "A" and self.player_pos[1] > 0:
            self.player_pos[1] -= 1
        elif direction == "D" and self.player_pos[1] < GRID_SIZE-1:
            self.player_pos[1] += 1
            
       
        if self.player_pos == [GRID_SIZE-1, GRID_SIZE-1]:
            self.game_over = True
            self.winner = "player"
            return
            
     
        if self.player_path:
            zombie_move = max(set(self.player_path), key=self.player_path.count)
            
            if zombie_move == "W" and self.zombie_pos[0] > 0:
                self.zombie_pos[0] -= 1
            elif zombie_move == "S" and self.zombie_pos[0] < GRID_SIZE-1:
                self.zombie_pos[0] += 1
            elif zombie_move == "A" and self.zombie_pos[1] > 0:
                self.zombie_pos[1] -= 1
            elif zombie_move == "D" and self.zombie_pos[1] < GRID_SIZE-1:
                self.zombie_pos[1] += 1
        
        
        if self.player_pos == self.zombie_pos:
            self.game_over = True
            self.winner = "zombie"


def main():
    clock = pygame.time.Clock()
    game = Game()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and game.game_over:
                    game.reset_game()
                elif not game.game_over:
                    if event.key == pygame.K_u:
                        game.move_player("W")
                    elif event.key == pygame.K_d:
                        game.move_player("S")
                    elif event.key == pygame.K_l:
                        game.move_player("A")
                    elif event.key == pygame.K_r:
                        game.move_player("D")
        
        game.draw_grid()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
