

import pygame
import random
import sys
import time




# Initialize Pygame
pygame.init()




# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("4-Key Rhythm Game")




# Colors
color1 = (random.randint(10,255), random.randint(10,255), random.randint(10,255))
WHITE = (255, 255, 255)
color3 = (random.randint(10,255), random.randint(10,255), random.randint(10,255))
black = (0,0,0)


# Define note settings
NOTE_WIDTH = 100
NOTE_HEIGHT = 150
NOTE_SPEED = 4  # Default speed
KEYS = ['z', 'x', 'c', 'b', 'n', 'm']  # 6 keys
KEYS_POS = [0, 100, 200, 300, 400, 500]  # Positions for 'Z', 'X', 'C', 'B', 'N', 'M'




# Set up fonts
font = pygame.font.SysFont("Impact", 24)
font2 = pygame.font.SysFont("Impact", 40)




# Game variables
score = 0
lives = 3  # Player starts with 3 lives
falling_notes = []
note_spawn_time = 0.5  # Default spawn time
num_notes = 5  # Default number of notes
hit_sound = pygame.mixer.Sound("ding.mp3")
miss_sound = pygame.mixer.Sound("womp.mp3")
game_over_sound=pygame.mixer.Sound("game ober.mp3")



# Clock
clock = pygame.time.Clock()




# Line position where notes should be hit
LINE_Y = SCREEN_HEIGHT - 200  # Position of the line where input happens




def spawn_note():
    """Function to spawn a note at a random position."""
    key = random.choice(KEYS)
    x_pos = KEYS_POS[KEYS.index(key)]
    note = {'key': key, 'x': x_pos, 'y': 0, 'color': color3}
    falling_notes.append(note)




def draw_notes():
    """Draw all falling notes on the screen."""
    for note in falling_notes:
        pygame.draw.rect(screen, WHITE, (note['x'] - 5, note['y'] - 5, NOTE_WIDTH + 10, NOTE_HEIGHT + 10), 5)
        pygame.draw.rect(screen, note['color'], (note['x'], note['y'], NOTE_WIDTH, NOTE_HEIGHT))




def draw_line():
    """Draw the line where players should press the key."""
    pygame.draw.line(screen, WHITE, (0, LINE_Y), (SCREEN_WIDTH, LINE_Y), 5)


def draw_column_lines():
    """Draw vertical lines separating the columns of notes."""
    for x_pos in KEYS_POS:
        pygame.draw.line(screen, WHITE, (x_pos, 0), (x_pos, SCREEN_HEIGHT), 5)




def check_input():
    """Check if the player presses the correct key."""
    global score
    keys = pygame.key.get_pressed()
    for note in falling_notes[:]:
        if note['y'] > LINE_Y:
            if keys[pygame.K_z] and note['key'] == 'z':
                score += 1
                hit_sound.play()
                falling_notes.remove(note)  # Remove the note after it is hit
            elif keys[pygame.K_x] and note['key'] == 'x':
                score += 1
                hit_sound.play()
                falling_notes.remove(note)
            elif keys[pygame.K_c] and note['key'] == 'c':
                score += 1
                hit_sound.play()
                falling_notes.remove(note)
            elif keys[pygame.K_b] and note['key'] == 'b':
                score += 1
                hit_sound.play()
                falling_notes.remove(note)
            elif keys[pygame.K_n] and note['key'] == 'n':
                score += 1
                hit_sound.play()
                falling_notes.remove(note)
            elif keys[pygame.K_m] and note['key'] == 'm':
                score += 1
                hit_sound.play()
                falling_notes.remove(note)




def update_notes():
    """Update the position of all falling notes."""
    for note in falling_notes:
        note['y'] += NOTE_SPEED




def draw_score():
    """Draw the current score on the screen."""
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))




def draw_lives():
    """Draw the current lives on the screen."""
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(lives_text, (SCREEN_WIDTH - 150, 10))




def game_over():
    """Display game over text."""
    game_over_text = font.render("Game Over! Press R to Restart", True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))




def ask_for_input():
    """Ask user for input values: number of notes."""
    global num_notes




    # Prompt text
    prompt_text = font.render("Enter number of notes (5-20):", True, WHITE)
    screen.blit(prompt_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 3))
    pygame.display.update()




    num_notes_input = get_user_input()
    num_notes = int(num_notes_input) if num_notes_input.isdigit() else 5




def get_user_input():
    """Function to get user input in pygame."""
    input_text = ''
    font = pygame.font.SysFont("Arial", 24)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # User presses Enter to submit
                    return input_text
                elif event.key == pygame.K_BACKSPACE:  # User presses backspace to remove a character
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode  # Append the character
        # Display the input text
        screen.fill(color1)
        prompt_text = font.render("Enter number of notes:", True, WHITE)
        screen.blit(prompt_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 3))
        input_display = font.render(input_text, True, WHITE)
        screen.blit(input_display, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        pygame.display.update()


def z():
    score_text = font2.render("Z", True, WHITE)
    screen.blit(score_text, (50, 900))




def x():
    score_text = font2.render("X", True, WHITE)
    screen.blit(score_text, (150, 900))




def c():
    score_text = font2.render("C", True, WHITE)
    screen.blit(score_text, (250, 900))




def b():
    score_text = font2.render("B", True, WHITE)
    screen.blit(score_text, (350, 900))




def n():
    score_text = font2.render("N", True, WHITE)
    screen.blit(score_text, (450, 900))




def m():
    score_text = font2.render("M", True, WHITE)
    screen.blit(score_text, (550, 900))




def main():
    global score, falling_notes, lives, note_spawn_time, NOTE_SPEED, num_notes
    last_spawn_time = time.time()




    # Get user input before starting the game
    ask_for_input()




    while True:
        screen.fill(color1)




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()




            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Restart the game
                    score = 0
                    lives = 3
                    falling_notes = []




        # Spawn notes based on user-defined spawn time and number of notes
        if time.time() - last_spawn_time > note_spawn_time:
            if len(falling_notes) < num_notes:  # Limit the number of notes
                spawn_note()
            last_spawn_time = time.time()




        update_notes()
        check_input()




        draw_notes()
        draw_score()
        draw_lives()
        draw_line()
        draw_column_lines()
        z()
        x()
        c()
        b()
        n()
        m()


        if score>=100:
            NOTE_SPEED+=1
        if lives==0:
            NOTE_SPEED=4




        for note in falling_notes[:]:
            if note['y'] > SCREEN_HEIGHT:
                lives -= 1  # Player loses a life if the note reaches the bottom
                miss_sound.play()
                falling_notes.remove(note)  # Remove the note after it reaches the bottom
                if lives <= 0:
                    game_over_sound.play()
                    game_over()
                    pygame.display.update()
                    time.sleep(2)
                    score = 0
                    lives = 3
                    falling_notes = []
                    last_spawn_time = time.time()  # Reset the spawn timer
                    break




        pygame.display.update()




        clock.tick(60)




if __name__ == "__main__":
    main()