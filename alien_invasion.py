import sys 
import pygame
from settings import Settings

class AlienInvasion:

    def __init__(self):
        """Inicjalizacja ry i utworzenie jej zasobów"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Inwazja obcych")
        
        #zdefiniowanie koloru tła
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Rozpoczęcie pętli głównej gry"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Odświeżanie ekranu w trakcie każdej iteracji pętli
            self.screen.fill(self.settings.bg_color)

            #wyświetlenie ostatnio zmodyfikowanego ekranu
            pygame.display.flip()
            self.clock.tick(60)

    if __name__ == '__main__':
        #Utwozenie egzemplarza gry i jej uruchomienie
        ai = AlienInvasion()
        ai.run_game()