import pygame

class Ship:
    """Klasa przeznaczona do zarządzania statkiem kosmicznym"""
    def __init__(self, ai_game):
        """Inicjalizacja statku kosmicznego i jego położenie początkowe"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Wczytywanie obrazu statku kosmicznego i pobranie jego prostokąta.
        self.image = pygame.image.load('C:/Users/maksy/Desktop/alien_invasion/images/DurrrSpaceShip.bmp')
        self.rect = self.image.get_rect()

        #Każdy nowy statek kosmiczne pojawia się na dole ekranu.
        self.rect.midbottom = self.screen_rect.midbottom

        #Opcje wskazujące na poruszanie się statku
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Uaktualnienie położenia statku na podstawie opcji wskazującej na jego ruch"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1


    def blitme(self):
        """Wyświetlenie statku kosmicznego w jego aktualnym położeniu"""
        self.screen.blit(self.image, self.rect)


    
# class AlienShip:
#     """Klasa statku obcych"""
#     def __init__(self, ai_game):
#         """Inicjalizacja statku obcych"""
#         self.screen = ai_game.screen
#         self.screen_rect = ai_game.screen.get_rect()

#         # Wczytanie obrazu statku obcych (zmień na odpowiednią grafikę)
#         self.image = pygame.image.load('C:/Users/maksy/Desktop/alien_invasion/images/alien.bmp')
#         self.rect = self.image.get_rect()

#         # Ustawienie pozycji na górze ekranu (np. na środku)
#         self.rect.midtop = self.screen_rect.midtop

#     def blitme(self):
#         """Rysowanie statku obcych w aktualnym miejscu"""
#         self.screen.blit(self.image, self.rect)  <-- Do utworzenia klasy obcego