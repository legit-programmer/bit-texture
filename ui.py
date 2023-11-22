import pygame


class Components:
    def __init__(self, window) -> None:
        self.window = window
        self.buttons = list()

    def Button(self, name: str, pos: tuple, color:tuple=None):
        top, left = pos
        rect = pygame.Rect(top, left, 75, 50)
        self.buttons.append(rect)
        return rect

    def drawAllComponents(self):
        for button in self.buttons:
            pygame.draw.rect(self.window, (230, 230, 230), button)


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
