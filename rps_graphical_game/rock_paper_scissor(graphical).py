import pygame
from random import randint

pygame.init()

class Game():
    
    def __init__(self,d_w,d_h):
        self.display_width = d_w
        self.display_height = d_h
        self.game_display = pygame.display.set_mode((self.display_width,self.display_height))
        pygame.display.set_caption("Rock Paper scissor")

        self.player_point = self.cpu_point = 0
        self.player_choice = 100
        self.win_streak = ["" , 0]

        self.button_rock = Button(0,60,420,self.game_display)
        self.button_paper = Button(1,360,420,self.game_display)
        self.button_scissor = Button(2,660,420,self.game_display)

        #**********************************color*************************
        self.BLUE = (0,0,255)
        self.BLACK = (0,0,0)
        self.YELLOW = (255,255,0)
        self.WHITE = (255,255,255)
        self.RED = (255,0,0)
        self.DRED = (150,0,0)
        self.GREEN = (0,255,0)
        self.DGREEN = (0,150,0)
        self.GRAY = (200,200,200)
        self.PINK = (255,20,147)
        self.LGREEN = (10,255,10)
        
    def message_display(self,text,textsize,textcolor,location):
        """if you need print text in display you can use this function"""
        largeFont = pygame.font.Font("fonts\\freesansbold.ttf",textsize)         
        textSurf  = largeFont.render(text,True,textcolor)         
        textRect  = textSurf.get_rect()         
        textRect.center = (location)         
        self.game_display.blit(textSurf,textRect)   

    def welcome(self):
        """To greet the player"""
        self.game_display.fill(self.GRAY)
        self.message_display("Welcome",100,self.BLACK,(self.display_width/2,self.display_height/2-200))
        self.message_display("To",100,self.RED,(self.display_width/2,self.display_height/2-100))
        self.message_display("Rock Paper Scissor",70,self.YELLOW,(self.display_width/2,self.display_height/2))
        self.message_display("Let's Play",100,self.BLUE,(self.display_width/2,self.display_height/2+100))
        pygame.display.update()
        pygame.time.wait(3000)
        self.game_display.fill(self.BLUE)

    def show_point(self):
        """show round and player point and cpu point"""
        self.message_display("win streak:"+self.win_streak[0],25,self.BLUE,(self.display_width/2,20))
        self.message_display("streak point:"+str(self.win_streak[1]),25,self.BLUE,(self.display_width/2,50))
        self.message_display("your point:"+str(self.player_point),25,self.BLUE,(90,20))
        self.message_display("cpu point:"+str(self.cpu_point),25,self.BLUE,(810,20))

    def picture_battle_player(self,choice):
        """use picture in battle page for player"""
        if choice == "rock":
            Button(0,self.display_width/2-350,self.display_height/2-100,self.game_display).button_draw("small")

        elif choice == "paper":
            Button(1,self.display_width/2-350,self.display_height/2-100,self.game_display).button_draw("small")

        else:
            Button(2,self.display_width/2-350,self.display_height/2-100,self.game_display).button_draw("small")

        self.message_display(choice,50,self.PINK,(self.display_width/2-260,self.display_height/2+150))

    def picture_battle_cpu(self,choice):
        """use picture in battle page for cpu"""
        if choice == "rock":
            Button(0,self.display_width/2+170,self.display_height/2-100,self.game_display).button_draw("small")

        elif choice == "paper":
            Button(1,self.display_width/2+170,self.display_height/2-100,self.game_display).button_draw("small")

        else:
            Button(2,self.display_width/2+170,self.display_height/2-100,self.game_display).button_draw("small")

        self.message_display(choice,50,self.LGREEN,(self.display_width/2+260,self.display_height/2+150))

    def game_wineer(self):
        """when battle is over Checks if you won or not"""
        self.game_display.fill(self.BLACK)
        if self.player_point > self.cpu_point or self.win_streak[0] == "You!!" :
            self.message_display("You Win The Game !!",80,self.GREEN,(self.display_width/2,self.display_height/2-100))

        else:
            self.message_display("You Lose !!",100,self.GREEN,(self.display_width/2,self.display_height/2-100))
        
        self.message_display("GG WP!!",100,self.RED,(self.display_width/2,self.display_height/2+100))
        pygame.display.update()
        pygame.time.wait(4000)
        pygame.quit()
        quit()

    def add_point(self , winner):

        if self.win_streak[0] == winner :
            self.win_streak[1] += 1
        else :
            self.win_streak[0] = winner
            self.win_streak[1] = 1

        if winner == "You!!" :
            self.player_point += (2 ** (self.win_streak[1]-1))
        else :
            self.cpu_point += (2 ** (self.win_streak[1]-1))

    def battle(self):
        """battle for win"""
        winer = ""
        self.game_display.fill(self.BLUE)
        values = ["rock","paper","scissor"]
        cpu_choice = randint(3,5)
        self.message_display("you choice",50,self.PINK,(self.display_width/2-250,self.display_height/2-200))
        self.message_display("cpu choice",50,self.LGREEN,(self.display_width/2+250,self.display_height/2-200))
        self.message_display("VS",50,self.YELLOW,(self.display_width/2,self.display_height/2))
        self.picture_battle_player(values[self.player_choice])
        self.picture_battle_cpu(values[cpu_choice-3])
        pygame.display.update()
        pygame.time.wait(3000)

        self.message_display("Winner",50,self.BLACK,(self.display_width/2,self.display_height/2+200))
        if abs (self.player_choice - cpu_choice) == 3 :
            winer = "Tie!!"

        elif abs (self.player_choice - cpu_choice) in (2, 5) :
            winer = "You!!"
            self.add_point(winer)

        elif abs (self.player_choice - cpu_choice) in (1,4) :
            winer = "Cpu!!"
            self.add_point(winer)

        self.message_display(winer,50,self.RED,(self.display_width/2,self.display_height/2+250))
        pygame.display.update()
        pygame.time.wait(2000)

    def game_loop(self):
        while abs(self.player_point - self.cpu_point) < 50 and self.win_streak[1] != 5 :
            while self.player_choice == 100 :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                self.game_display.fill(self.GRAY)
                self.button_rock.action_button()
                self.button_paper.action_button()
                self.button_scissor.action_button()

                self.show_point()  
                pygame.display.update()

            self.battle()

            self.player_choice = 100

        self.game_wineer()

class Button():
    """create and activate button for choice"""
    def __init__(self,name,x,y,display):
        self.name = name
        self.y = y 
        self.x = x
        self.display = display
        self.large_Paper = pygame.image.load("images\\largePaper1.png")
        self.large_Rock = pygame.image.load("images\\largeRock1.png")
        self.large_Scissor = pygame.image.load("images\\largeScissor1.png")
        self.small_Paper = pygame.image.load("images\\smallPaper.png")
        self.small_Rock = pygame.image.load("images\\smallRock.png")
        self.small_Scissor = pygame.image.load("images\\smallScissor.png")

        self.large_width = self.large_height = 200
        self.small_width = self.small_height = 180

    def button_draw(self,b_type):
        if self.name == 0 :
            if b_type == "large":
                self.display.blit(self.large_Rock,(self.x-10,self.y-10))
            else:
                self.display.blit(self.small_Rock,(self.x,self.y))

        if self.name == 1 :
            if b_type == "large":
                self.display.blit(self.large_Paper,(self.x-10,self.y-10))
            else:
                self.display.blit(self.small_Paper,(self.x,self.y))

        if self.name == 2 :
            if b_type == "large":
                self.display.blit(self.large_Scissor,(self.x-10,self.y-10))
            else:
                self.display.blit(self.small_Scissor,(self.x,self.y))

    def action_button(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x <= mouse[0] <= self.x+self.small_width and self.y <= mouse[1] <= self.y+self.small_height :
            self.button_draw("large")

            if click[0] == True  :
                game.player_choice = self.name
        else:
            self.button_draw("small")


#***********************************************main******************************************

game = Game(900,700)
game.welcome()
game.game_loop()
