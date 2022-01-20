import sys, pygame, math, json, random
pygame.init()
quests = json.load(open('questions.json'))

size = WIDTH, HEIGHT = 1080, 720

BACK = 0, 0, 0
GREY = 110, 110, 110
WHITE = 255,255,255
GREEN = 0,255,0
RED = 255,0,0

DISPLAY = pygame.display
screen = DISPLAY.set_mode(size)
CENTER = (WIDTH/2, HEIGHT/2)
QUESTION = (WIDTH/2, HEIGHT/4)
btns = []
BUTTON1 = (WIDTH/2, HEIGHT/2+40)
TITLE = list(quests.keys())[0]

font = "Comic Sans MS"
fonts = []
for i in range(1, 181):
    fonts.append(pygame.font.SysFont(font, i))

def fadeoutText(text, colour, size, location):
    r,g,b = colour
    step = 100
    while step > 0:
        tinystep = step/100
        colour = r*tinystep, g*tinystep, b*tinystep
        print(size + step)
        finfont = fonts[size + round(step/100*60)].render(text, False, colour)

        finlocation = (
            location[0] - finfont.get_width()/2, 
            location[1] - finfont.get_height()/2
        )
        pygame.draw.rect(screen,BACK,(finlocation[0],finlocation[1],finfont.get_width(),finfont.get_height()))
        screen.blit(finfont, finlocation)
        DISPLAY.flip()
        step -= 1
        pygame.time.wait(10)
    return finfont

def fadeinText(text, colour, size, location):
    r,g,b = colour
    step = 0
    while step < 100:
        tinystep = step/100
        colour = r*tinystep, g*tinystep, b*tinystep
        print(size + step)
        finfont = fonts[size + round(step/100*60)].render(text, False, colour)

        finlocation = (
            location[0] - finfont.get_width()/2, 
            location[1] - finfont.get_height()/2
        )
        pygame.draw.rect(screen,BACK,(finlocation[0],finlocation[1],finfont.get_width(),finfont.get_height()))
        screen.blit(finfont, finlocation)
        DISPLAY.flip()
        step += 1
        pygame.time.wait(10)
    return finfont

def finish():
    print("nice")
    quit()

def checkAnswer(question):
    print("bla")
def placebtns(txts, size, origin, color, count):
    btnpos = origin[1]
    for a in txts: 
        finpos = (
            origin[0],
            btnpos
        )
        btns.append(Button(a, size, finpos, count))
        btnpos += size  

def displayNextQuestion(index):
    keys = list(quests[TITLE].keys())
    if(index == len(keys)):
        finish()
        return
    key=keys[index]
    screen.fill(BACK)
    btns = []
    allanswers = []
    fadeinText(key, WHITE, 20, QUESTION)
    allanswers = quests[TITLE][key]["n"]
    allanswers.extend(quests[TITLE][key]["y"])
    #allanswers.sort(key=shuffle)
    random.shuffle(allanswers)    
    placebtns(allanswers, 60, BUTTON1, WHITE, index+1)

class Button():
    def __init__(self, text, size, pos, count):
        self.txt = text
        self.size = size
        self.fade = fadeinText(text, WHITE, 60-self.size, pos)
        self.pos = pos
        self.font = fonts[self.size]
        self.count = count

    def mouseOver(self):
        mouse = pygame.mouse.get_pos()
        return self.pos[0]-self.fade.get_width()/2 <= mouse[0] <= self.pos[0]+self.fade.get_width()/2 and self.pos[1]-self.fade.get_height()/2 <= mouse[1] <= self.pos[1]+self.fade.get_height()/2

    def isClicked(self):
        if self.mouseOver():
                checkAnswer(self.txt)
                displayNextQuestion(self.count)
    def isHovered(self):
        nonhvr = self.fade
        centerpos = (
            self.pos[0] - nonhvr.get_width()/2, 
            self.pos[1] - nonhvr.get_height()/2
        )

        if self.mouseOver():
            hvr = self.font.render(self.txt, False, GREY)
            screen.blit(hvr, centerpos)
        else:
            screen.blit(nonhvr, centerpos)



def shuffle(e):
    return random.randint(1,100)

DISPLAY.set_caption('learnin\' ' + TITLE + '!')

# show title
#fadeinText(TITLE, WHITE, 80, CENTER)
pygame.time.wait(500)
#fadeoutText(TITLE, WHITE, 80, CENTER)
screen.fill(BACK)
DISPLAY.flip()

#show question and possible answers
displayNextQuestion(0)
        

while True:
    # stores the (x,y) coordinates into
    # the variable as a tuple
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for b in btns:
                b.isClicked()
    

    #hover
    for b in btns:
        b.isHovered()
    DISPLAY.flip()

    
    
