import pygame
import random
import math

WIDTH = 500
HEIGHT = 500
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

fon = pygame.image.load('fly.png')

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("swamp")
clock = pygame.time.Clock()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (x, y)
        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0] / length, self.dir[1] / length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))

        self.image = pygame.Surface((15, 20)).convert_alpha()
        self.image.fill(WHITE)

        self.image = pygame.transform.rotate(self.image, angle)

        self.speed = 9
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def update(self):
        self.pos = (self.pos[0] + self.dir[0] * self.speed,
                    self.pos[1] + self.dir[1] * self.speed)
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[0]

    def draw(self, surf):
        bullet_rect = self.bullet.get_rect(center=self.pos)
        surf.blit(self.bullet, bullet_rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        # key = pygame.key.get_pressed()
        # mouse = pygame.mouse.get_pressed()
        # pos = pygame.mouse.get_pos()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        key = pygame.key.get_pressed()
      #  mouse = pygame.mouse.get_pressed()
     #   pos = pygame.mouse.get_pos()
        # keystate = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.speedx = -8
        if key[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 5)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 5)
            self.speedx = random.randrange(-3, 3)

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
sprites = pygame.sprite.Group()
player = Player( )
#pos = (0, 470) # неработает тут
all_sprites.add(player)
for i in range(20):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False
      #  elif event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_SPACE:
            #     player.shoot()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            b=Bullet(player.rect.x,player.rect.y)
            all_sprites.add(b)
            bullets.add(b)

    # Обновление ВСЕГО
    all_sprites.update()

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    # Проверка, не ударил ли моб игрока
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False

    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
