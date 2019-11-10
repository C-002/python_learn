import sys
import pygame

def check_events(message):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            message.settext('Keychar: ' + chr(event.key) + ', keycode: ' + str(event.key))

def update_screen(screen, message):
    screen.fill((230, 230, 230))
    message.blit()
    pygame.display.flip()