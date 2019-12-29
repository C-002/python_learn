import pygame, time
import sys

class Message:
    def __init__(self, screen):
        self.screen = screen
        self.brake = 0.13
        self.throttle = 0.15
        self.steer = 0
        self.turnlight = 0
        self.gear = 0
        self.enable = 0
        self.gear_en = 0

        self.deltaAng = 10
        self.deltaBrake = 0.01
        self.deltaThrottle = 0.05
    
    def blit(self):
        self.position = 0
        self.font = pygame.font.SysFont('Arial', 16)
        self.line_height = self.font.get_linesize() * 2
        self.surface = self.font.render('Brake:     ' + str(self.brake), True, (0, 255, 0))
        self.screen.blit(self.surface, (0, self.position))
        self.position += self.line_height
        self.surface = self.font.render('Throttle:  ' + str(self.throttle), True, (0, 255, 0))
        self.screen.blit(self.surface, (0, self.position))
        self.position += self.line_height
        self.surface = self.font.render('Steer:     ' + str(self.steer), True, (0, 255, 0))
        self.screen.blit(self.surface, (0, self.position))
        self.position += self.line_height
        self.surface = self.font.render('TurnLight: ' + str(self.turnlight), True, (0, 255, 0))
        self.screen.blit(self.surface, (0, self.position))
        self.position += self.line_height
        self.surface = self.font.render('Gear:      ' + str(self.gear), True, (0, 255, 0))
        self.screen.blit(self.surface, (0, self.position))
    
    def setBrake(self, brake):
        self.brake = brake 
    def setThrottle(self, throttle):
        self.throttle = throttle
    def setSteer(self, steer):
        self.steer = steer
    def setTurnlight(self, turnlight):
        self.turnlight = turnlight
    def setGear(self, gear):
        self.gear = gear
    def reset(self):
        self.enable = 0
        self.turnlight = 0
        self.brake = 0.13
        self.throttle = 0.15
        self.steer = 0


    def PressKey_d(self):
        self.steer -= self.deltaAng
        if (self.steer <= -470):
            self.steer = -470
        
    def PressKey_a(self):
        self.steer += self.deltaAng
        if (self.steer >= 470):
            self.steer = 470

    def PressKey_w(self):
        self.brake = 0.13
        self.throttle += self.deltaThrottle
        if (self.throttle < 0.20):
            self.throttle = 0.20
        elif (self.throttle >= 0.85):
            self.throttle = 0.85

    def PressKey_s(self):
        self.throttle = 0.15
        self.brake += self.deltaBrake
        if (self.brake < 0.21):
            self.brake = 0.21
        elif (self.brake >= 0.26):
            self.brake = 0.26


def check_event(message):
    for event in pygame.event.get():
        print("get event!")
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print("get key!")
            if (chr(event.key) == ' '):
                message.reset()
            if (chr(event.key) == 'd'):
                message.PressKey_d()
            if (chr(event.key) == 'a'):
                message.PressKey_a()
            if (chr(event.key) == 'w'):
                message.PressKey_w()
            if (chr(event.key) == 's'):
                message.PressKey_s()
            if (chr(event.key) == '0'): 
                message.gear_en = 1
                message.gear = 0
            if (chr(event.key) == '1'): 
                message.gear_en = 1
                message.gear = 1
            if (chr(event.key) == '2'): 
                message.gear_en = 1
                message.gear = 2
            if (chr(event.key) == '3'): 
                message.gear_en = 1
                message.gear = 3
            if (chr(event.key) == '4'): 
                message.gear_en = 1
                message.gear = 4
            if (chr(event.key) == '5'): 
                message.gear_en = 1
                message.gear = 5
            if (chr(event.key) == 'q'): 
                if (message.turnlight != 1):
                    message.turnlight = 1
                else:
                    message.turnlight = 0
            if (chr(event.key) == 'e'):
                if (message.turnlight != 2):
                    message.turnlight = 2
                else:
                    message.turnlight = 0
            if (chr(event.key) == 'r'):
                if (message.turnlight != 3):
                    message.turnlight = 3
                else:
                    message.turnlight = 0
def update_screen(screen, message):
    screen.fill((0,0,0))
    message.blit()
    pygame.display.flip()

def playerOne():
    pygame.init()
    WIDTH = 300
    HEIGHT = 200
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    
    message = Message(screen)

    while True:
        check_event(message)
        update_screen(screen, message)            

        

        time.sleep(0.5)

if __name__=='__main__':
    playerOne()
    




