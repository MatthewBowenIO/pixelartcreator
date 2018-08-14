import pygame, json, os

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (220,220,220)

WIDTH = 10
HEIGHT = 10

MARGIN = 1

grid = []
for row in range(32):
    grid.append([])
    for column in range(100):
        grid[row].append(0)

pygame.init()

WINDOW_SIZE = [1100, 355]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Pixel Art Creator")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif pygame.mouse.get_pressed()[0] or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            grid[row][column] = 0
            print("Click ", pos, "Grid coordinates: ", row, column)

            screen.fill(BLACK)

    for row in range(32):
        for column in range(100):
            color = GREY
            if grid[row][column] == 1:
                color = BLACK
            else:
                color = GREY
            pygame.draw.rect(screen,color, [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

    clock.tick(60)
    pygame.display.flip()

art = {}
art['output'] = []
for column in range(100):
    for row in range(32):
        if grid[row][column] == 1:
            art['output'].append([row, column])

with open('art.json', 'w') as ofile:
    json.dump(art, ofile)
    ofile.close()

os.execl('sh/test.sh', '')

pygame.quit()
