from settings import *


class Boobooz(pygame.sprite.Sprite):
    boobooz_frames =  {"Black":[pygame.image.load(path.join("assets","boobooz-black",f"booboozBlack{i+1}.png")) for i in range(BOOBOOZ_FRAMES)],
                        "Cyan":[pygame.image.load(path.join("assets","boobooz-cyan",f"booboozCyanF{i+1}.png")) for i in range(BOOBOOZ_FRAMES)],
                        "Gold":[pygame.image.load(path.join("assets","boobooz-gold",f"booboozGoldF{i+1}.png")) for i in range(BOOBOOZ_FRAMES)],
                        "Magenta":[pygame.image.load(path.join("assets","boobooz-magenta",f"booboozMagentaF{i+1}.png")) for i in range(BOOBOOZ_FRAMES)],
                        "Red":[pygame.image.load(path.join("assets","boobooz-red",f"booboozRedF{i+1}.png")) for i in range(BOOBOOZ_FRAMES)],
                        "White":[pygame.image.load(path.join("assets","boobooz-white",f"booboozWhiteF{i+1}.png")) for i in range(BOOBOOZ_FRAMES)]}
    def __init__(self):
        super().__init__()
        
        self.boobooz_color = choice(["Black", "Cyan", "Gold", "Magenta", "Red", "White"])
        self.ani_boobooz = Boobooz.boobooz_frames[self.boobooz_color]
        self.image = self.ani_boobooz[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (random()*(SC_WIDTH-SPRITE_SIZE), (random()*(DANGERZONE_HEIGHT- SPRITE_SIZE) + SAFEZONE_HEIGHT_TOP))
        
        self.prev_time = pygame.time.get_ticks()
        self.current_frame = 0
        
    
        self.velocity = randint(BOOBOOZ_VELOCITY_MIN,BOOBOOZ_VELOCITY_MAX)
        self.directionx = self.getDir()
        self.directiony = self.getDir()

    
        
    
    def update(self):
        self.update_boobooz_frame()
        self.image = self.ani_boobooz[self.current_frame]
        self.movement()
        
        
    def update_boobooz_frame(self):
        frame_time = 200
        current_time = pygame.time.get_ticks()
        if current_time - self.prev_time >= frame_time:
            self.prev_time = current_time
            self.current_frame = (self.current_frame+1) % len(self.ani_boobooz)
            
    
    def movement(self):
        self.rect.x += self.directionx * self.velocity
        self.rect.y += self.directiony * self.velocity
 
        direction = self.getDir()
        if self.rect.top < SAFEZONE_HEIGHT_TOP or self.rect.bottom > SAFEZONE_HEIGHT_BOTTOM:
            while self.directiony == direction:
                direction = self.getDir()
            else:
                self.directiony = direction
        if self.rect.left < 0 or self.rect.right > SC_WIDTH:
            while self.directionx == direction:
                direction = self.getDir()
            else:
                self.directionx = direction
            
            
    def reset(self):
        self.rect.topleft = (random()*(SC_WIDTH-SPRITE_SIZE), (random()*(DANGERZONE_HEIGHT- SPRITE_SIZE) + SAFEZONE_HEIGHT_TOP))

        
            
    @staticmethod
    def getImage(color):
        """ gets color name -> return image and color code as tuple """
        match color:
            case "Black":
                return (Boobooz.boobooz_frames["Black"][0] , COLOR_BLACK)
            case "Cyan":
                return (Boobooz.boobooz_frames["Cyan"][0] , COLOR_CYAN)
            case "Gold":
                return (Boobooz.boobooz_frames["Gold"][0] ,COLOR_GOLD)
            case "Magenta":
                return (Boobooz.boobooz_frames["Magenta"][0] , COLOR_MAGENTA)
            case "Red":
                return (Boobooz.boobooz_frames["Red"][0] , COLOR_LRED)
            case "White":
                return (Boobooz.boobooz_frames["White"][0] , COLOR_WHITE)

            
    getDir = lambda self: choice([-1,1])
    getColor = lambda self: self.boobooz_color
    