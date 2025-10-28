from settings import *
from player import Player
from boobooz import Boobooz

class Game():
    def __init__(self,display_surface):
        pygame.init()
        
        self.display_surface = display_surface
        
        # round generator must fill it
        self.boobooz_colors = []
        self.boobooz_count = BOOBOOZ_STARTING_COUNT
            
        
        
        self.score = 0
        self.last_reset_time = 0
        self.round_timer = 0
        self.paused_time_holder = 0
        self.round = 1
        self.current_haram = None
        
        self.isGameOver = False
        self.isGamePause = False
        

    def drawzone(self,zone_clr):
        pygame.draw.line(self.display_surface, zone_clr, (0,SAFEZONE_HEIGHT_TOP-4),(SC_WIDTH,SAFEZONE_HEIGHT_TOP-4), width=4)
        pygame.draw.line(self.display_surface, zone_clr, (0,SAFEZONE_HEIGHT_BOTTOM+4),(SC_WIDTH,SAFEZONE_HEIGHT_BOTTOM+4), width=4)
        pygame.draw.line(self.display_surface, zone_clr, (1,SAFEZONE_HEIGHT_TOP-4),(1,SAFEZONE_HEIGHT_BOTTOM+4), width = 4)
        pygame.draw.line(self.display_surface, zone_clr, (SC_WIDTH-3,SAFEZONE_HEIGHT_TOP-4),(SC_WIDTH-3,SAFEZONE_HEIGHT_BOTTOM+4), width = 4)

        
    def load_boobooz(self,count):
        for i in range(count):
            self.boobooz = Boobooz()
            self.boobooz_colors.append(self.boobooz.getColor())
            self.group_boobooz.add(self.boobooz)
            
    
    def chooseHaram(self,colors):
        if colors != []:
            self.current_haram = choice(colors)
            self.image_haram , self.zone_clr = Boobooz.getImage(self.current_haram)
            self.image_haram = pygame.transform.scale(self.image_haram,(40,40))
               
        return self.image_haram
        
            
    def load(self):
        """ loads game assets """
        self.image_bg = pygame.image.load(path.join("assets","BG.png"))
        
        self.group_player = pygame.sprite.Group()
        self.player = Player(x=SC_WIDTH//2,y=SC_HEIGHT-SPRITE_SIZE)
        self.group_player.add(self.player)
        
        self.group_boobooz = pygame.sprite.Group()
        self.load_boobooz(count = BOOBOOZ_STARTING_COUNT)
            
        self.pixel_font = pygame.font.Font(path.join("assets","font","PixeloidSans.ttf"),22)
        self.pixel_font_large = pygame.font.Font(path.join("assets","font","PixeloidSans.ttf"),64)
        
        self.text_score = self.pixel_font.render(f"Score: {self.score}",True,COLOR_TEXT)
        self.rect_score = self.text_score.get_rect()
        self.rect_score.topleft = (4, 2)       
        
        self.text_lives = self.pixel_font.render("Lives:",True,COLOR_TEXT)
        self.rect_lives = self.text_lives.get_rect()
        self.rect_lives.topleft = (4, 24)     
        
        self.text_round = self.pixel_font.render(f"Round: {self.round}",True,COLOR_TEXT)
        self.rect_round = self.text_round.get_rect()
        self.rect_round.topleft = (4, 48)
        
        self.text_roundTimer = self.pixel_font.render("[0] Round Time",True,COLOR_TEXT)
        self.rect_roundTimer = self.text_roundTimer.get_rect()
        self.rect_roundTimer.topright = (SC_WIDTH-4, 2)      
        
        self.text_teleports = self.pixel_font.render(f"[{self.player.getTeleports()}] teleports left",True,COLOR_TEXT)
        self.rect_teleports = self.text_teleports.get_rect()
        self.rect_teleports.topright = (SC_WIDTH-4, 48)
        
        self.text_isHaram = self.pixel_font.render("this is Haram",True,COLOR_DRED)
        self.rect_isHaram = self.text_isHaram.get_rect()
        self.rect_isHaram.centerx = SC_WIDTH//2
        self.rect_isHaram.top = 4
        
        self.image_haram = self.chooseHaram(self.boobooz_colors)
        self.rect_haram = self.image_haram.get_rect()
        self.rect_haram.centerx = SC_WIDTH//2
        self.rect_haram.top = 32
        
        self.text_Gameover = self.pixel_font_large.render("Game Over",True,COLOR_BLACK)
        self.rect_Gameover = self.text_Gameover.get_rect()
        self.rect_Gameover.center = (SC_WIDTH//2, SC_HEIGHT//2)
        
        self.text_pressR = self.pixel_font.render("press \"R\" to restart",True,COLOR_BLACK)
        self.rect_pressR = self.text_pressR.get_rect()
        self.rect_pressR.center = (SC_WIDTH//2, (SC_HEIGHT//2)+80)
        
        self.text_Paused = self.pixel_font_large.render("PAUSED", True, COLOR_BLACK)
        self.rect_Paused = self.text_Paused.get_rect()
        self.rect_Paused.center = (SC_WIDTH//2, SC_HEIGHT//2)
        
        self.text_pressQ = self.pixel_font.render("Press \"Q\" to Quit", True, COLOR_BLACK)
        self.rect_pressQ = self.text_pressQ.get_rect()
        self.rect_pressQ.center = (SC_WIDTH//2, (SC_HEIGHT//2)+60)
        
        self.text_pressESC = self.pixel_font.render("Press \"ESC\" to Resume", True, COLOR_BLACK)
        self.rect_pressESC = self.text_pressESC.get_rect()
        self.rect_pressESC.center = (SC_WIDTH//2, (SC_HEIGHT//2)+80)

        
    def update(self):
        """ update game display """
        
        self.display_surface.blit(self.image_bg,(0,0))
        self.drawzone(self.zone_clr)
        
        self.text_score = self.pixel_font.render(f"Score: {self.score}",True,COLOR_TEXT)
        self.display_surface.blit(self.text_score, self.rect_score)
        lives_text = ""
        for i in range(self.player.lives):
            lives_text += " *"
        self.text_lives = self.pixel_font.render(f"Lives: {lives_text}",True,COLOR_TEXT)
        self.display_surface.blit(self.text_lives, self.rect_lives)
        
        self.round_timer = ((pygame.time.get_ticks()-self.paused_time_holder) - self.last_reset_time)//1000
        
        self.text_roundTimer = self.pixel_font.render(f"{self.round_timer}s Round Time",True,COLOR_TEXT)
        self.text_round = self.pixel_font.render(f"Round: {self.round}",True,COLOR_TEXT)
        self.display_surface.blit(self.text_round, self.rect_round)
        self.display_surface.blit(self.text_roundTimer, self.rect_roundTimer)
        self.text_teleports = self.pixel_font.render(f"[{self.player.getTeleports()}] teleports left",True,COLOR_TEXT)
        self.display_surface.blit(self.text_teleports, self.rect_teleports)
        self.display_surface.blit(self.text_isHaram, self.rect_isHaram)
        self.display_surface.blit(self.image_haram, self.rect_haram)
        
        self.group_player.update()
        self.group_player.draw(self.display_surface)     
        self.group_boobooz.update()  
        self.group_boobooz.draw(self.display_surface)
        
        self.check_collision(playerSprite=self.player, enemyGroup=self.group_boobooz)
        
        if self.player.lives == 0:
            self.isGameOver = True
        
        self.round_up()
        pygame.display.update()
        
    
    def reset_timer(self):
        self.last_reset_time = pygame.time.get_ticks()
        if self.last_reset_time < 0:
            self.last_reset_time = 0
            
    def round_up(self):
        if self.boobooz_colors == []:
            self.round += 1
                   
            self.boobooz_count += 1
            if self.boobooz_count > 100:
                print("limited performance")
                exit()
            self.score += POINTS_ROUND
            
            self.load_boobooz(self.boobooz_count) # here list of colors will be filled againt
            self.chooseHaram(self.boobooz_colors)
            self.player.rect.x = SC_WIDTH//2
            self.player.rect.y = SC_HEIGHT-SPRITE_SIZE
            self.player.teleports += 1
            self.player.in_dangerzone = not self.player.in_dangerzone
        
    def check_collision(self,playerSprite,enemyGroup):
        #pygame.sprite.groupcollide(groupa=player,groupb=enemy,dokilla=False,dokillb=True)
        collided_enemy = pygame.sprite.spritecollideany(sprite = playerSprite, group = enemyGroup)
        
        if str(collided_enemy) == "<Boobooz Sprite(in 1 groups)>":
            enemyGroup.remove(collided_enemy)      
            self.boobooz_colors.remove(collided_enemy.boobooz_color) 
            if collided_enemy.boobooz_color == self.current_haram:
                self.image_haram = self.chooseHaram(self.boobooz_colors)
                self.score += POINTS_KILL
            else:
                self.player.lives -= 1
        
    def game_pause(self):
        pause_start_time = pygame.time.get_ticks()
        while self.isGamePause: 
            self.blit_overlay(self.display_surface,COLOR_OVERLAY_PAUSE,opacity=2)
            self.display_surface.blit(self.text_Paused,self.rect_Paused)
            self.display_surface.blit(self.text_pressQ,self.rect_pressQ)
            self.display_surface.blit(self.text_pressESC,self.rect_pressESC)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                    self.isGamePause = not self.isGamePause
                    return False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.isGamePause = not self.isGamePause
                        pause_end_time = pygame.time.get_ticks()
                        total_pause_time = pause_end_time - pause_start_time
                        self.paused_time_holder += total_pause_time
        return True
        
        
    def game_over(self):
        self.paused_time_holder = 0
        while self.isGameOver: 
            self.blit_overlay(self.display_surface,COLOR_OVERLAY_GAMEOVER,opacity=3)
            self.display_surface.blit(self.text_Gameover,self.rect_Gameover)
            self.display_surface.blit(self.text_pressQ,self.rect_pressQ)
            self.display_surface.blit(self.text_pressR,self.rect_pressR)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                    self.isGameOver = not self.isGameOver
                    return False
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        self.reset()
                        self.isGameOver = not self.isGameOver
                        

        return True
    
    def blit_overlay(self,surface,color,opacity):
        pos = (0,0)
        overlay = pygame.Surface(size = (surface.get_width(),surface.get_height()))  
        overlay.fill(color)
        overlay.set_alpha(opacity)
        surface.blit(overlay,pos)
    
    def reset(self):
        self.boobooz_count = BOOBOOZ_STARTING_COUNT
        self.boobooz_colors = []
        self.load()
        self.score = 0
        self.round = 1
        self.reset_timer()
        self.player.reset()
        self.update()
        
        

    def quitgame(self):
        pygame.quit()
        
        
        