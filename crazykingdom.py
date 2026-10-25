import pygame
import random
pygame.init()
pygame.mixer.init()
scr = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Rule the Kingdom")

pygame.mixer.music.load(".\\animation\\game-over-252897.mp3")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

def show_text(msg, x, y, color, size):
    fontobj = pygame.font.SysFont("freesans", size)
    msgobj = fontobj.render(msg, False, color)
    scr.blit(msgobj, (x, y))

BackGround = pygame.image.load(".\\animation\\freetileset\\png\\BG\\BG.png")
BackGround = pygame.transform.scale(BackGround, (900, 900))

Char_1 = pygame.image.load(".\\animation\\redhatfiles\\png\\Idle (1).png")
Char_1 = pygame.transform.scale(Char_1, (200, 300))

Char_2 = pygame.image.load(".\\animation\\templerun\\Idle__001.png")
Char_2 = pygame.transform.scale(Char_2,(200,300))

Char_3 = pygame.image.load(".\\animation\\freeknight\\png\\Idle (1).png")
Char_3 = pygame.transform.scale(Char_3,(200,300))

Char_4 = pygame.image.load(".\\animation\\adventure_girl\\png\\Idle (1).png")
Char_4 = pygame.transform.scale(Char_4,(200,300))

Characters=[Char_1,Char_2,Char_3,Char_4]

SpeechBubble = pygame.image.load(".\\animation\\speech-bubble-145979_1280.png")
SpeechBubble = pygame.transform.scale(SpeechBubble,(110,100))

Color_1 = (46, 139, 87)

Color_2 = (184, 134, 11)

resources = {"gold": 60, "materials": 60, "people": 60, "happiness": 60}
requests = [
    {"text": "Can I borrow 20 gold to start a bakery?",
"accept": {"gold": -20, "happiness": +10},
"decline": {"happiness": -10}},
    
    {"text": "A panda requests 20 materials to build a bamboo park. Should we invest?",
"accept": {"materials": -20, "happiness": +20},
"decline": {"happiness": -10}},
    
    {"text": "A trader offers rare goods for double the price. Should we buy?",
"accept": {"materials": +25, "gold": -25},
"decline": {"happiness": -15}},
    
    {"text": "The dragon wants to join the kingdom. Should we let him in?",
"accept": {"people": -10},
"decline": {"people": +20}},
    
    {"text": "A jester wants funding for a comedy festival. Should we give?",
"accept": {"gold": -15, "happiness": +20},
"decline": {"happiness": -15}},

    {"text": "A mysterious wizard offers to increase your population for 30 gold. Accept?",
"accept": {"gold": -30, "people": +25},
"decline": {"happiness": -10}},

    {"text": "The farmers request 15 materials to repair the barns. Help them?",
"accept": {"materials": -15, "happiness": +15},
"decline": {"happiness": -10, "people": -5}},

    {"text": "A merchant ship arrives, offering 30 gold for 20 materials. Trade?",
"accept": {"materials": -20, "gold": +30},
"decline": {"happiness": -5}},

    {"text": "The knights demand a bonus of 25 gold to improve morale. Pay them?",
"accept": {"gold": -25, "happiness": +20},
"decline": {"happiness": -20}},

    {"text": "A wandering healer offers to boost happiness for 20 gold. Hire them?",
"accept": {"gold": -20, "happiness": +25},
"decline": {"happiness": -10}},

    {"text": "A volcano nearby threatens the village. Spend 30 materials on defenses?",
"accept": {"materials": -30, "people": +15},
"decline": {"people": -20, "happiness": -15}}
]
screen = "Introduction"
Question = random.choice(requests)
Current_Char = random.choice(Characters)
running=True
Count=0
while running==True:
    if screen == "Introduction":
        scr.blit(BackGround, (0, 0))
        show_text("Hello there! The Kingdom of Eldralore needs your help!", 40, 55, "black", 25)
        show_text("They have lost their emperor, and so now you must help bring peace!", 40, 105, "black", 25)
        show_text("You must balance the kingdom's resources and make your subjects happy!", 40, 155, "black", 25)
        show_text("Are you ready to be king/queen?", 40, 205, "black", 25)
        Play = pygame.draw.rect(scr, Color_1, (50, 600, 250, 125))
        show_text("Yes!", 65, 610, "black", 60)
        Quit = pygame.draw.rect(scr, Color_2, (550, 600, 250, 125))
        show_text("No", 565, 610, "black", 60)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Play.collidepoint(event.pos):
                    screen = "Game"
                if Quit.collidepoint(event.pos):
                    running = False
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    elif screen == "Game":
        scr.blit(BackGround, (0, 0))
        show_text("gold: " + str(resources["gold"]), 40, 40, "black", 30)
        show_text("people: " + str(resources["people"]), 175, 40, "black", 30)
        show_text("materials: " + str(resources["materials"]), 340, 40, "black", 30)
        show_text("happiness: " + str(resources["happiness"]), 530, 40, "black", 30)

        scr.blit(Current_Char,(300,200))
        scr.blit(SpeechBubble,(500,300))

        show_text(Question["text"], 50, 150, "black", 30)
        Yes = pygame.draw.rect(scr, Color_1, (50, 600, 200, 100))
        show_text("Yes!", 100, 615, "black", 70)
        No = pygame.draw.rect(scr, Color_2, (500, 600, 200, 100))
        show_text("No!", 550, 615, "black", 70)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Yes.collidepoint(event.pos):
                    the_keys = list(Question["accept"].keys())
                    for i in the_keys:
                        resources[i] += Question["accept"][i]
                    Question = random.choice(requests)
                    Current_Char = random.choice(Characters)
                    Count+=1
                if No.collidepoint(event.pos):
                    the_keys = list(Question["decline"].keys())
                    for i in the_keys:
                        resources[i] += Question["decline"][i]
                    Question = random.choice(requests)
                    Current_Char = random.choice(Characters)
                    Count+=1
            if event.type == pygame.QUIT:
                running = False
        if (resources["gold"] <= 0 or resources["happiness"] <= 0 or
                resources["materials"] <= 0 or resources["people"] <= 0):
            screen = "Lost"
        elif Count>=10:
            screen="Win"
        pygame.display.update()
    elif screen=="Win":
        scr.blit(BackGround, (0, 0))

        show_text("You have successfully ruled the kingdom! You are the best ruler!",100,100,"black",30)
        show_text("Would you like to continue to rule?",100,300,"black",30)

        Play = pygame.draw.rect(scr, Color_1, (50, 600, 250, 125))
        show_text("Yes!", 65, 610, "black", 60)
        Quit = pygame.draw.rect(scr, Color_2, (550, 600, 250, 125))
        show_text("No", 565, 610, "black", 60)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Play.collidepoint(event.pos):
                    screen = "Game"
                    # resources = {"gold": 60, "materials": 60, "people": 60, "happiness": 60}
                    Count=0
                    Question = random.choice(requests)
                if Quit.collidepoint(event.pos):
                    running = False
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    elif screen == "Lost":
        scr.blit(BackGround, (0, 0))
        show_text("You have lost! You failed to rule the kingdom! Wanna try again?", 100, 100, "black", 25)
        Play = pygame.draw.rect(scr, Color_1, (50, 600, 250, 125))
        show_text("Yes!", 65, 610, "black", 60)
        Quit = pygame.draw.rect(scr, Color_2, (550, 600, 250, 125))
        show_text("No", 565, 610, "black", 60)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Play.collidepoint(event.pos):
                    screen = "Game"
                    resources = {"gold": 60, "materials": 60, "people": 60, "happiness": 60}
                    Count=0
                    Question = random.choice(requests)
                if Quit.collidepoint(event.pos):
                    running = False
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
