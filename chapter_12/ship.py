import pygame

class Ship:
    """A class to manage the ship."""
    
    def __init__(self, ai_game):
        # ai_game is a reference to the current instance of the AlienInvasion class
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        # we assign the screen to an attribute of Ship, so we can access it 
        # easily in all the methods in this class
        
        self.screen_rect = ai_game.screen.get_rect()
        # we access the screen’s rect attribute using the get_rect() method
        # and assign it to self.screen_rect. Doing so allows us to place the 
        # ship in the correct location on the screen
    

        self.image = pygame.image.load('images/ship.bmp')
        # carga la imagen
        
        self.rect = self.image.get_rect()
        
            
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
    
