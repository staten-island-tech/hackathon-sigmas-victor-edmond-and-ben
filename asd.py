
import pygame
import random
import sys
import time


# Initialize Pygame
pygame.init()


# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("4-Key Rhythm Game")


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


# Define note settings
NOTE_WIDTH = 200
NOTE_HEIGHT = 100
NOTE_SPEED = 5
KEYS = ['z', 'x', 'c', 'b','n','m']
KEYS_POS = [200, 400, 600, 800, 1000, 1200]  # Positions for 'A', 'S', 'D', 'F'


# Set up fonts
font = pygame.font.SysFont("Arial", 24)


# Game variables
score = 0
falling_notes = []
difficulty=input("difficulty what diffuculty easy, medium, hard: \n")
if difficulty=="hard":
    note_spawn_time=0.1
elif difficulty =="medium":
    note_spawn_time =0.5
elif difficulty == "easy":
    note_spawn_time=1
pygame.display.set_caption("Question Prompt")
note_spawn_time=0.1


# Main game loop
clock = pygame.time.Clock()


def spawn_note():
    """Function to spawn a note at random position."""
    key = random.choice(KEYS)
    x_pos = KEYS_POS[KEYS.index(key)]
    note = {'key': key, 'x': x_pos, 'y': 0, 'color': BLUE}
    falling_notes.append(note)


def draw_notes():
    """Draw all falling notes on the screen."""
    for note in falling_notes:
        pygame.draw.rect(screen, note['color'], (note['x'], note['y'], NOTE_WIDTH, NOTE_HEIGHT))


def check_input():
    """Check if the player presses the correct key."""
    global score
    keys = pygame.key.get_pressed()
    for note in falling_notes[:]:
        if note['y'] > SCREEN_HEIGHT - NOTE_HEIGHT:
            if keys[pygame.K_z] and note['key'] == 'z':
                score += 1
            elif keys[pygame.K_x] and note['key'] == 'x':
                score += 1
            elif keys[pygame.K_c] and note['key'] == 'c':
                score += 1
            elif keys[pygame.K_b] and note['key'] == 'b':
                score += 1
            elif keys[pygame.K_n] and note['key'] == 'n':
                score += 1
            elif keys[pygame.K_m] and note['key'] == 'm':
                score += 1
            falling_notes.remove(note)  # Remove note after it's hit


def update_notes():
    """Update the position of all falling notes."""
    for note in falling_notes:
        note['y'] += NOTE_SPEED


def draw_score():
    """Draw the current score on the screen."""
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))


def game_over():
    """Display game over text."""
    game_over_text = font.render("Game Over! Press R to Restart", True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))


def main():
    global score, falling_notes, note_spawn_time
    last_spawn_time = time.time()


    while True:
        screen.fill(BLACK)


        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Restart the game
                    score = 0
                    falling_notes = []


        # Spawn notes at a timed interval
        if time.time() - last_spawn_time > note_spawn_time:
            spawn_note()
            last_spawn_time = time.time()


        # Update note positions
        update_notes()


        # Check for player input
        check_input()


        # Draw notes and score
        draw_notes()
        draw_score()


        # Game Over condition
        for note in falling_notes:
            if note['y'] > SCREEN_HEIGHT:
                game_over()
                pygame.display.update()
                time.sleep(2)
                score = 0
                falling_notes = []
                last_spawn_time = time.time()  # Reset the spawn timer
                break


        # Update screen
        pygame.display.update()


        # Frame rate (frames per second)
        clock.tick(60)


if __name__ == "__main__":
    main()
