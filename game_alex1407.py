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

# fon=pygame.image.load('fly and bobs/fon67.jpg')


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("swamp")
clock = pygame.time.Clock()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.pos = (x, y)
        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0] / length, self.dir[1] / length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))

        self.bullet = pygame.Surface((15, 20)).convert_alpha()
        self.bullet.fill((255, 255, 255))
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = 15

    def update(self):
        self.pos = (self.pos[0] + self.dir[0] * self.speed,
                    self.pos[1] + self.dir[1] * self.speed)

    def draw(self, surf):
        bullet_rect = self.bullet.get_rect(center=self.pos)
        surf.blit(self.bullet, bullet_rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        key = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
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
        mouse = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        # keystate = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
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
        self.speedy = random.randrange(1, 18)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 18)


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
sprites = pygame.sprite.Group()
player = Player()
pos = (250, 470)
all_sprites.add(player)
for i in range(20):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

running = True
while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullets.append(Bullet(*pos))
    for bullet in bullets[:]:
        bullet.update()
        if not screen.get_rect().collidepoint(bullet.pos):
            bullets.remove(bullet)

    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    screen.fill(BLACK)
    # screen.blit(fon,(0,0))
    for bullet in bullets:
        bullet.draw(screen)
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()