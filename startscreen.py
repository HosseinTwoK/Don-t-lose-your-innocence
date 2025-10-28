from settings import *


class Start():
    def __init__(self,surface):
        pygame.init()
        self.screen = surface
        self.not_started_yet = True
        
        fontLarge = pygame.font.Font(path.join("assets","font","PixeloidSans.ttf"),50)
        fontMedium = pygame.font.Font(path.join("assets","font","PixeloidSans.ttf"),22)
        fontSmall = pygame.font.Font(path.join("assets","font","PixeloidSans.ttf"),16)
        
        self.text_Start = fontLarge.render("PRESS \"Enter\" to START",True,COLOR_BLACK)
        self.rect_Start = self.text_Start.get_rect()
        self.rect_Start.center = ((SC_WIDTH//2),(SC_HEIGHT//2)-60)
        
        self.text_pressQ = fontMedium.render("press\"Q\" to quit",True,COLOR_BLACK)
        self.rect_pressQ = self.text_pressQ.get_rect()
        self.rect_pressQ.center = ((SC_WIDTH//2),(SC_HEIGHT//2))
        
        self.text_Control = fontMedium.render("- - Game Control --",True,COLOR_BLACK)
        self.rect_Control = self.text_Control.get_rect()
        self.rect_Control.center = ((SC_WIDTH//2),(SC_HEIGHT//2)+100)
        
        self.text_W = fontMedium.render("W -> go up",True,COLOR_BLACK)
        self.rect_W = self.text_W.get_rect()
        self.rect_W.center = ((SC_WIDTH//2)-200,(SC_HEIGHT//2)+140)
        
        self.text_A = fontMedium.render("A -> go left",True,COLOR_BLACK)
        self.rect_A = self.text_A.get_rect()
        self.rect_A.center = ((SC_WIDTH//2)-200,(SC_HEIGHT//2)+170)
        
        self.text_S = fontMedium.render("S -> go down",True,COLOR_BLACK)
        self.rect_S = self.text_S.get_rect()
        self.rect_S.center = ((SC_WIDTH//2)-200,(SC_HEIGHT//2)+200)
        
        self.text_D = fontMedium.render("D -> go right",True,COLOR_BLACK)
        self.rect_D = self.text_D.get_rect()
        self.rect_D.center = ((SC_WIDTH//2)-200,(SC_HEIGHT//2)+230)
        
        
        self.text_SPACE = fontMedium.render("space -> teleport",True,COLOR_BLACK)
        self.rect_SPACE = self.text_SPACE.get_rect()
        self.rect_SPACE.center = ((SC_WIDTH//2)+200,(SC_HEIGHT//2)+140)
        
        self.text_ESCAPE = fontMedium.render("esc -> pause",True,COLOR_BLACK)
        self.rect_ESCAPE = self.text_ESCAPE.get_rect()
        self.rect_ESCAPE.center = ((SC_WIDTH//2)+200,(SC_HEIGHT//2)+170)
        
        
    def show_start_screen(self):
        show = True
        while show:
            for event in pygame.event.get():
                print(event)
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                    show = False
                    return False
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self.not_started_yet = False
                        show = False
                        return True
                    
            self.blit_text()
            pygame.display.update()
                    
    def blit_text(self):
        self.screen.fill(COLOR_DRED) 
        self.screen.blit(self.text_Start,self.rect_Start)
        self.screen.blit(self.text_pressQ,self.rect_pressQ)
        self.screen.blit(self.text_Control,self.rect_Control)
        self.screen.blit(self.text_W,self.rect_W)
        self.screen.blit(self.text_A,self.rect_A)
        self.screen.blit(self.text_S,self.rect_S)
        self.screen.blit(self.text_D,self.rect_D)
        self.screen.blit(self.text_SPACE,self.rect_SPACE)
        self.screen.blit(self.text_ESCAPE,self.rect_ESCAPE)
        