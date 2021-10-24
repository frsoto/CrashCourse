# import the sys and pygame modules
import sys
import pygame
from settings import Settings


class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init() 
        # function initializes the background settings that Pygame needs to 
        # work properly
        
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # crea ventana con esa resolucion. surface
        # se asigna a un atributo para desp usarlo.
        
        pygame.display.set_caption("Alien Invasion Fernando")
        # titulo ventana
        
        # Set the background color.
        self.bg_color = (230, 230, 230)

    # Metotodo:
    def run_game(self): #controla el juego
        """Start the main loop for the game."""
        while True: #corre continuamente
            # Watch for keyboard and mouse events. An event is an action that 
            # the user performs while playing the game, such as pressing a key
            # or moving the mouse
            for event in pygame.event.get(): 
            # To access the events that Pygame detects, we’ll use the 
            # pygame.event.get() function. This function returns a list of 
            #  events that have taken place since the last time this function 
            # was called. Inside the loop, we’ll write a series of if
            #  statements to detect and respond to specific events. ejemplo 
            #  click en la x de la ventana
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            
            # Make the most recently drawn screen visible. refresca la pant.
            pygame.display.flip()

# instanciamos
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()