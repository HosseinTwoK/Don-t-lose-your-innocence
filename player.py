from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.ani_player = [pygame.image.load(path.join("assets","muslim",f"muslimF{i+1}.png")) for i in range(PLAYER_FRAMES)]
        
        self.current_frame = 0     
        self.prev_time = pygame.time.get_ticks()
             
        self.image = self.ani_player[0]
        
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
        self.lives = PLAYER_LIVES
        self.velocity = PLAYER_VELOCITY
        self.teleports = PLAYER_TELEPORTS
        
        self.to_right = False
        self.in_dangerzone = False
        

    def update(self):
        self.update_player_frame()
        self.image = self.ani_player[self.current_frame]
        if self.to_right:
            self.image = pygame.transform.flip(self.image,True,False)
            
        if self.rect.bottom < SAFEZONE_HEIGHT_BOTTOM:
            self.in_dangerzone = True
            
        self.movement()

    
    
    def update_player_frame(self):
        """change the current_frame"""
        frame_duration = 150
        current_time = pygame.time.get_ticks()

        if current_time - self.prev_time >= frame_duration:
            self.prev_time = current_time
            self.current_frame = (self.current_frame+1) % len(self.ani_player)
    
    
    def movement(self):
        key = pygame.key.get_pressed()
        if not self.in_dangerzone:
            if key[K_w] and self.rect.top > 0:
                self.rect.centery -= self.velocity
            if key[K_s] and self.rect.bottom < SC_HEIGHT:
                self.rect.centery += self.velocity
            if key[K_a] and self.rect.left > 0:
                self.to_right = False
                self.rect.centerx -= self.velocity
            if key[K_d] and self.rect.right < SC_WIDTH:
                self.to_right = True
                self.rect.centerx += self.velocity
        else:
            if key[K_w] and self.rect.top > SAFEZONE_HEIGHT_TOP:
                self.rect.centery -= self.velocity
            if key[K_s] and self.rect.bottom < SAFEZONE_HEIGHT_BOTTOM:
                self.rect.centery += self.velocity
            if key[K_a] and self.rect.left > 0:
                self.to_right = False
                self.rect.centerx -= self.velocity
            if key[K_d] and self.rect.right < SC_WIDTH:
                self.to_right = True
                self.rect.centerx += self.velocity
                
    def teleport(self):
        "reset player pos"
        if self.teleports > 0 and self.in_dangerzone:
            self.rect.x = SC_WIDTH//2
            self.rect.y = SC_HEIGHT-SPRITE_SIZE
            self.teleports -= 1
            self.in_dangerzone = not self.in_dangerzone
        

    def reset(self):
        self.rect.x = SC_WIDTH//2
        self.rect.y = SC_HEIGHT-SPRITE_SIZE
        self.to_right = False
        self.in_dangerzone = False
        self.image = self.ani_player[0]
        self.lives = PLAYER_LIVES
        self.teleports = PLAYER_TELEPORTS
        
        
    getTeleports = lambda self: self.teleports

        
            
        