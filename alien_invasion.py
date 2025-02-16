import sys 
import pygame
from settings import Settings
from ship import Ship #,AlienShip <-- Do utworzenia obcego 

class AlienInvasion:

    def __init__(self):
        """Inicjalizacja ry i utworzenie jej zasobów"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Inwazja obcych")
        self.ship = Ship(self)
        #self._alien_ship_ = AlienShip(self) <- Do utworzenia obcego 

    def run_game(self):
        """Rozpoczęcie pętli głównej gry"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiaturę i mysz"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
    
    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        #self._alien_ship_.blitme() <- do utworzenia obcego
        
        pygame.display.flip()

if __name__ == '__main__':
    #Utwozenie egzemplarza gry i jej uruchomienie
    ai = AlienInvasion()
    ai.run_game()