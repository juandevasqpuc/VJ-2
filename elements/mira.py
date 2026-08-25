if __name__ == "__main__":
    raise RuntimeError("\033c❌ ESTE ARCHIVO NO DEBE EJECUTARSE. EJECUTA main.py")
import pygame

miraPNG=pygame.image.load("assets/mira.png")
miraPNG_scaled=pygame.transform.scale(miraPNG, (26,14))

class mira(pygame.sprite.Sprite):
    def __init__(self, screen):

        # ? super().__init__() inicializa la clase padre (Sprite)
        super().__init__()

        self.image = mirapng_scaled
        self.rect = self.image.get_rect(
            center=(
                screen.get_width() + 100,
                random.randint(0, screen.get_height()),
            )
        )
        self.speed = random.randint(3, 5)

    
