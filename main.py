import pygame # imports pygame
import scene_manager as SM # imports the scene manager class
#-------------------------------------------------------------------------
pygame.init() # initialize pygame

# Function that checks if the game is running; if not running, close game/app.
def check_if_running(event, running_test):
        # did the user click the window close button? if so, stop the loop
        if event.type == pygame.QUIT:
            running_test = False
            return running_test
            
        # did the user hit a key?
        if event.type == pygame.KEYDOWN:
            # was it the Escape Key? if so, stop the loop
            if event.key == pygame.K_ESCAPE:
                running_test = False
                return running_test
        
        else:
            running_test = True
            return running_test

# create variables
running = True # variable to keep the main loop running

# object creation
the_game = SM.Scenes()

if __name__ == "__main__":
    # Main Loop
    while running: 
        # grab the event
        event = pygame.event.wait()
        # check if running 
        running = check_if_running(event, running)
        # checks what scene it is currently and draws it
        the_game.scene_manager(event)
        # update the display
        pygame.display.flip()
    pygame.quit()

