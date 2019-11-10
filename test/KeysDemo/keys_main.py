import pygame
from message import Message
import functions as func

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("按键测试")

    message = Message(screen, 'Press a key...')

    while True:
        func.check_events(message)
        func.update_screen(screen, message)

main()