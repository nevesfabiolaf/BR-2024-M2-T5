import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

FONT_STYLE = 'freesansbold.ttf'


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0
        self.high_score = 0
        self.death_count = 0

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
                
        pygame.display.quit()
        pygame.quit() 

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.score = 0
        self.game_speed = 20
        self.obstacle_manager.reset_obstacles()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 5 
        if self.score > self.high_score:
            self.high_score = self.score            

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()    

    def draw_text(self, text, position):
        font = pygame.font.Font(FONT_STYLE, 22)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = position
        self.screen.blit(text_surface, text_rect)

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_widht = SCREEN_WIDTH // 2
        
        if self.death_count == 0:
            self.draw_text("Press any key to start", (half_screen_widht, half_screen_height))
        else:                       
            self.screen.blit(ICON, (half_screen_widht - 20, half_screen_height - 140))    
            self.draw_text("Press any key to restart", (half_screen_widht, half_screen_height))
            self.draw_text(f"Score: {self.score}", (half_screen_widht, half_screen_height - 200))
            self.draw_text(f"Death Count: {self.death_count}", (half_screen_widht, half_screen_height - 240))
            self.draw_text(f"High Score: {self.high_score}", (half_screen_widht, half_screen_height - 170))
           
        pygame.display.update()
        
        self.handle_events()