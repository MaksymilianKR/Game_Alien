import sys 
import pygame
from settings import Settings
from ship import Ship #,AlienShip <-- Do utworzenia obcego 
from bullet import Bullet

class AlienInvasion:

    def __init__(self):
        """Inicjalizacja ry i utworzenie jej zasobów"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Inwazja obcych")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        #self._alien_ship_ = AlienShip(self) <- Do utworzenia obcego 

    def run_game(self):
        """Rozpoczęcie pętli głównej gry"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiaturę i mysz"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_elemens(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_elemens(event)

    def _check_keydown_elemens(self, event):
        """Reakcja na naciśnięcie klawisza"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_elemens(self, event):
        """Reakcja na zwolnienie klawisza"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Utworzenie nowego pocisku i dodanie go do grupy pocisków"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
    
    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        #self._alien_ship_.blitme() <- do utworzenia obcego
        
        pygame.display.flip()

if __name__ == '__main__':
    #Utwozenie egzemplarza gry i jej uruchomienie
    ai = AlienInvasion()
    ai.run_game()