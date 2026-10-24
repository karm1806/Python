import pygame
import random
import sys
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Interactive Dice Roller")
clock = pygame.time.Clock()
COLOR_BG = (28, 40, 51)
COLOR_DICE = (242, 243, 244)
COLOR_PIP = (35, 47, 62)
COLOR_TEXT = (255, 255, 255)
COLOR_BTN = (46, 204, 113)
COLOR_BTN_HOVER = (39, 174, 96)
font_title = pygame.font.SysFont("Helvetica", 36, bold=True)
font_btn = pygame.font.SysFont("Helvetica", 24, bold=True)
button_rect = pygame.Rect(200, 380, 200, 50)
dice_value = 1
is_rolling = False
roll_timer = 0
roll_duration = 20 
current_frame = 0
def draw_dice_face(x, y, size, value):
    """Procedurally renders a dice face with appropriate dot (pip) arrangements."""
    dice_rect = pygame.Rect(x, y, size, size)
    pygame.draw.rect(screen, COLOR_DICE, dice_rect, border_radius=15)
    center = x + size // 2, y + size // 2
    top_left = x + size // 4, y + size // 4
    top_right = x + 3 * (size // 4), y + size // 4
    mid_left = x + size // 4, y + size // 2
    mid_right = x + 3 * (size // 4), y + size // 2
    bottom_left = x + size // 4, y + 3 * (size // 4)
    bottom_right = x + 3 * (size // 4), y + 3 * (size // 4)
    pip_radius = size // 16
    pips = []
    if value == 1:
        pips = [center]
    elif value == 2:
        pips = [top_left, bottom_right]
    elif value == 3:
        pips = [top_left, center, bottom_right]
    elif value == 4:
        pips = [top_left, top_right, bottom_left, bottom_right]
    elif value == 5:
        pips = [top_left, top_right, center, bottom_left, bottom_right]
    elif value == 6:
        pips = [top_left, top_right, mid_left, mid_right, bottom_left, bottom_right]
    for pos in pips:
        pygame.draw.circle(screen, COLOR_PIP, pos, pip_radius)
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                if button_rect.collidepoint(mouse_pos) and not is_rolling:
                    is_rolling = True
                    current_frame = 0
    if is_rolling:
        current_frame += 1
        if current_frame % 3 == 0:
            dice_value = random.randint(1, 6)
        if current_frame >= roll_duration:
            dice_value = random.randint(1, 6)
            is_rolling = False
    screen.fill(COLOR_BG)
    title_surface = font_title.render("Pygame Dice Simulator", True, COLOR_TEXT)
    screen.blit(title_surface, (SCREEN_WIDTH // 2 - title_surface.get_width() // 2, 40))
    dice_size = 160
    dice_x = SCREEN_WIDTH // 2 - dice_size // 2
    dice_y = SCREEN_HEIGHT // 2 - dice_size // 2 - 20
    draw_dice_face(dice_x, dice_y, dice_size, dice_value)
    if button_rect.collidepoint(mouse_pos):
        btn_color = COLOR_BTN_HOVER
    else:
        btn_color = COLOR_BTN
    pygame.draw.rect(screen, btn_color, button_rect, border_radius=8)
    btn_text_str = "Rolling..." if is_rolling else "Roll Dice"
    btn_surface = font_btn.render(btn_text_str, True, COLOR_TEXT)
    screen.blit(btn_surface, (button_rect.centerx - btn_surface.get_width() // 2, 
                               button_rect.centery - btn_surface.get_height() // 2))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()