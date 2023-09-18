import pygame

from dino_runner.utils.constants import BG, ICON, START, RESTART, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, DEAD, OVER, CLOUD_DEAD
from dino_runner.utils.text_utils import draw_text
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.cloud.cloud import Cloud


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
        self.power_up_manager = PowerUpManager()
        self.cloud = Cloud()

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
        self.power_up_manager.reset_power_ups()
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
        self.cloud.update(self.game_speed)
        self.update_score()
        self.power_up_manager.update(self)      
         
    def update_score(self):
        if self.game_speed < 40:
            self.score += 1
        elif (self.game_speed > 40) and (self.game_speed < 50):
            self.score += 10
        else:
            self.score += 1
   
        if self.score % 100 == 0:
            self.game_speed += 2
        if self.score > self.high_score:
            self.high_score = self.score            

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.draw_speed()
        self.cloud.draw(self.screen)
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
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
        draw_text(
            f"Score: {self.score}",
            self.screen, 
            pos_x_center=1000,
            pos_y_center=50
        )
        
    def draw_speed(self):
        draw_text(
            f"Speed: {self.game_speed}",
            self.screen, 
            pos_x_center=1000,
            pos_y_center=68
        )    

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_text(
                    f"{self.player.type} enable for {time_to_show} seconds",
                    self.screen,
                    font_size = 18,
                    pos_x_center = 500,
                    pos_y_center = 50
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()    

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_widht = SCREEN_WIDTH // 2
        
        if self.death_count == 0:
            draw_text(
                "Press any key to start",
                self.screen,
                pos_y_center=half_screen_height + 100
            )
            self.screen.blit(START, (half_screen_widht - 50, half_screen_height - 50))
        else:                       
            draw_text(
                "Press any key to restart",
                self.screen,
                pos_y_center=half_screen_height + 50
            )
            draw_text(
                f"Your Score: {self.score}",
                self.screen,
                pos_x_center=1000,
                pos_y_center=50
            )
            draw_text(
                f"Death Count: {self.death_count}",
                self.screen,
                pos_x_center=1000,
                pos_y_center=89
            )
            draw_text(
                f"High Score: {self.high_score}",
                self.screen,
                pos_x_center=1000,
                pos_y_center=69
            )
            self.screen.blit(RESTART, (half_screen_widht - 50, half_screen_height - 50))
            self.screen.blit(OVER, (half_screen_widht - 200, half_screen_height - 100))
            self.screen.blit(DEAD, (80, 310))
            self.screen.blit(CLOUD_DEAD, (145, 350))
            self.screen.blit(CLOUD_DEAD, (30, 400))

        pygame.display.update()
        
        self.handle_events()