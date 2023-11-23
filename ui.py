import pygame

pygame.init()
font = pygame.font.Font(pygame.font.get_default_font(), 18)


class Components:
    def __init__(self, window: pygame.Surface) -> None:
        self.window = window
        self.buttons = list()

    def Button(self, name: str):
        rect = pygame.Rect(900, 10, 75, 50)
        if len(self.buttons) > 0:
            top, left = self.buttons[-1]['rect'].top, self.buttons[-1]['rect'].left
            rect = pygame.Rect(left, top+60, 75, 50)
        button = {'rect': rect, 'name': name}
        self.buttons.append(button)
        return button['rect']

    def drawAllComponents(self):
        for button in self.buttons:
            pygame.draw.rect(self.window, (230, 230, 230), button['rect'])
            text = font.render(button['name'], False, (0, 0, 0))
            self.window.blit(text, (button['rect'].left, button['rect'].top))


class ClickListener:
    def __init__(self) -> None:
        self.components = list()

    def addListener(self, component: pygame.Rect, callbackFn):
        self.components.append((component, callbackFn))

    def listenEvents(self):
        pos = pygame.mouse.get_pos()
        left, _, _ = pygame.mouse.get_pressed()
        for component in self.components:
            if pos[0] in range(component[0].left, component[0].left + component[0].width):
                if pos[1] in range(component[0].top, component[0].top + component[0].height) and left:
                    component[1]()
