import pygame, time
import sys

def print_key():
    pygame.init()
    BLACK = (0,0,0)
    WIDTH = 300
    HEIGHT = 200
    surface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    surface.fill(BLACK)
    
    bra = 0.0

    while True:
        for event in pygame.event.get():
            print("get event!")
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print("get key!")
                if (chr(event.key) == 's'):
                    bra += 0.02
                
                

        print(bra)

        time.sleep(0.5)

if __name__=='__main__':
    print_key()
    




