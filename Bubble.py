import pygame
import random
import sys

# Constants
WIDTH, HEIGHT = 800, 400
BG_COLOR = (255, 255, 255)
BAR_COLOR = (0, 0, 0)
BAR_WIDTH = 10
GAP = 2

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Sort Visualization")

# Generate a list of random heights for the bars
bar_heights = [random.randint(50, 350) for _ in range(WIDTH // (BAR_WIDTH + GAP))]

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                draw_bars(arr, j, j + 1)
                pygame.time.delay(20)  # Add a 0.02-second delay

# Draw the bars on the screen
def draw_bars(arr, idx1, idx2):
    screen.fill(BG_COLOR)

    for i, height in enumerate(arr):
        color = BAR_COLOR
        if i == idx1 or i == idx2:
            color = (255, 0, 0)  # Highlight the bars being compared
        pygame.draw.rect(
            screen, color, (i * (BAR_WIDTH + GAP), HEIGHT - height, BAR_WIDTH, height)
        )

    pygame.display.update()

# Main loop
running = True
sorted = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not sorted:
        bubble_sort(bar_heights)
        sorted = True

pygame.quit()
sys.exit()
