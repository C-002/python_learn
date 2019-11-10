import pygame

class Message:
    def __init__(self, screen, text):
        self.screen = screen
        self.text = text
    
    def settext(self, text):
        self.text = text

    def gettext(self):
        return self.text

    def blit(self):
        font = pygame.font.SysFont('宋体', 40)
        self.surface = font.render(self.text, True, (0, 0, 255))
        self.rect = self.surface.get_rect()
        self.rect.left = 20
        self.rect.top = 50
        self.screen.blit(self.surface, self.rect)

