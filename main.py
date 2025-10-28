from settings import *
from game import Game
from startscreen import Start

screen = pygame.display.set_mode(SC_SIZE)
icon = pygame.image.load(path.join("assets","boobooz-black","booboozBlack6.png")).convert_alpha()
pygame.display.set_caption("Don’t lose your innocence")
pygame.display.set_icon(icon)

clock = pygame.time.Clock() 
start = Start(screen)
game = Game(display_surface=screen) # pygame.init here
game.load()

running = start.show_start_screen()
while running:
    
    
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                game.player.teleport()
            if event.key == K_ESCAPE:
                game.isGamePause = not game.isGamePause
                running = game.game_pause()
            if event.key == K_r:
                game.reset()
     
         
    if game.isGameOver:
        running = game.game_over()               
    game.update()

        
    clock.tick(FPS)
    

game.quitgame() # pygame.quit here