import pygame

pygame.init()
font = pygame.font.Font(pygame.font.get_default_font(), 18)


class Components:
    def __init__(self, window: pygame.Surface) -> None:
        self.window = window
        self.buttons = list()

    def Button(self, name: str):
        text = font.render(name, False, (0, 0, 0))
        rect = pygame.Rect(900, 10, text.get_width(), 50)
        if len(self.buttons) > 0:
            top, left = self.buttons[-1]['rect'].top, self.buttons[-1]['rect'].left
            rect.top = top+60
        button = {'rect': rect, 'text': text}
        self.buttons.append(button)
        return button['rect']

    def drawAllComponents(self):
        for button in self.buttons:
            pygame.draw.rect(self.window, (230, 230, 230), button['rect'])

            self.window.blit(
                button['text'], (button['rect'].left, button['rect'].top + button['rect'].height / 2 - button['text'].get_height()/2))


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
                    pygame.mouse.set_pos(
                        (component[0].left-10, component[0].top-10))
