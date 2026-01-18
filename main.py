import pygame
import sys
import random
from wordlist import word_list

class WordleGame:
    def __init__(self):
        pygame.init()
        
        # Screen settings
        self.WIDTH = 800
        self.HEIGHT = 900
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Wordle Clone")
        self.clock = pygame.time.Clock()
        
        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (128, 128, 128)
        self.LIGHT_GRAY = (200, 200, 200)
        self.GREEN = (76, 175, 80)
        self.YELLOW = (255, 193, 7)
        self.RED = (244, 67, 54)
        self.DARK_GRAY = (50, 50, 50)
        
        # Fonts
        self.title_font = pygame.font.Font(None, 60)
        self.word_font = pygame.font.Font(None, 50)
        self.small_font = pygame.font.Font(None, 24)
        
        # Game state
        self.answer = random.choice(word_list)
        self.guesses = []
        self.current_input = ""
        self.game_over = False
        self.won = False
        self.debug_mode = '-d' in sys.argv
        
        if self.debug_mode:
            self.show_popup("Debug Mode", f"Answer: {self.answer.upper()}")
    
    def check_word(self, word):
        """Returns list of colors for each letter: 0=gray, 1=yellow, 2=green"""
        result = [0] * 5
        word_list_copy = list(self.answer)
        
        # First pass: mark greens
        for i in range(5):
            if word[i] == self.answer[i]:
                result[i] = 2
                word_list_copy[i] = None
        
        # Second pass: mark yellows
        for i in range(5):
            if result[i] == 0 and word[i] in word_list_copy:
                result[i] = 1
                word_list_copy[word_list_copy.index(word[i])] = None
        
        return result
    
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if len(self.current_input) == 5:
                    if self.current_input.lower() not in word_list:
                        self.show_popup("Invalid Word", f"'{self.current_input.upper()}' is not a valid word")
                    else:
                        self.submit_guess(self.current_input.lower())
                else:
                    self.show_popup("Invalid Length", "Word must be exactly 5 letters")
            elif event.key == pygame.K_BACKSPACE:
                self.current_input = self.current_input[:-1]
            elif len(self.current_input) < 5 and event.unicode.isalpha():
                self.current_input += event.unicode.lower()
    
    def submit_guess(self, word):
        colors = self.check_word(word)
        self.guesses.append((word, colors))
        self.current_input = ""
        
        if word == self.answer:
            self.game_over = True
            self.won = True
            self.show_popup("Congratulations!", f"You found the word: {self.answer.upper()}\nAttempts: {len(self.guesses)}")
        elif len(self.guesses) >= 6:
            self.game_over = True
            self.won = False
            self.show_popup("Game Over", f"The word was: {self.answer.upper()}")
    
    def show_popup(self, title, message):
        """Display a popup dialog"""
        popup_width = 400
        popup_height = 200
        popup_x = (self.WIDTH - popup_width) // 2
        popup_y = (self.HEIGHT - popup_height) // 2
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False
            
            # Draw semi-transparent overlay
            overlay = pygame.Surface((self.WIDTH, self.HEIGHT))
            overlay.set_alpha(200)
            overlay.fill(self.BLACK)
            self.screen.blit(overlay, (0, 0))
            
            # Draw popup box
            pygame.draw.rect(self.screen, self.WHITE, (popup_x, popup_y, popup_width, popup_height))
            pygame.draw.rect(self.screen, self.BLACK, (popup_x, popup_y, popup_width, popup_height), 3)
            
            # Draw title
            title_surf = self.title_font.render(title, True, self.BLACK)
            title_rect = title_surf.get_rect(center=(self.WIDTH // 2, popup_y + 30))
            self.screen.blit(title_surf, title_rect)
            
            # Draw message (with line wrapping)
            lines = message.split('\n')
            y_offset = popup_y + 70
            for line in lines:
                msg_surf = self.small_font.render(line, True, self.BLACK)
                msg_rect = msg_surf.get_rect(center=(self.WIDTH // 2, y_offset))
                self.screen.blit(msg_surf, msg_rect)
                y_offset += 30
            
            # Draw instruction
            inst_surf = self.small_font.render("Press any key to continue", True, self.GRAY)
            inst_rect = inst_surf.get_rect(center=(self.WIDTH // 2, popup_y + popup_height - 30))
            self.screen.blit(inst_surf, inst_rect)
            
            pygame.display.flip()
            self.clock.tick(60)
        
        return True
    
    def draw(self):
        self.screen.fill(self.DARK_GRAY)
        
        # Draw title
        title = self.title_font.render("WORDLE", True, self.WHITE)
        title_rect = title.get_rect(center=(self.WIDTH // 2, 30))
        self.screen.blit(title, title_rect)
        
        # Draw attempts counter
        attempts_text = self.small_font.render(f"Attempts: {len(self.guesses)}/6", True, self.WHITE)
        self.screen.blit(attempts_text, (20, 100))
        
        # Draw previous guesses
        y_pos = 150
        for word, colors in self.guesses:
            for i, letter in enumerate(word):
                if colors[i] == 2:  # Green
                    color = self.GREEN
                elif colors[i] == 1:  # Yellow
                    color = self.YELLOW
                else:  # Gray
                    color = self.GRAY
                
                # Draw letter box
                box_x = 150 + i * 60
                pygame.draw.rect(self.screen, color, (box_x, y_pos, 50, 50))
                pygame.draw.rect(self.screen, self.WHITE, (box_x, y_pos, 50, 50), 2)
                
                # Draw letter
                letter_surf = self.word_font.render(letter.upper(), True, self.WHITE)
                letter_rect = letter_surf.get_rect(center=(box_x + 25, y_pos + 25))
                self.screen.blit(letter_surf, letter_rect)
            
            y_pos += 70
        
        # Draw current input
        if not self.game_over:
            input_y = 150 + len(self.guesses) * 70
            for i in range(5):
                box_x = 150 + i * 60
                if i < len(self.current_input):
                    pygame.draw.rect(self.screen, self.LIGHT_GRAY, (box_x, input_y, 50, 50))
                    pygame.draw.rect(self.screen, self.WHITE, (box_x, input_y, 50, 50), 2)
                    letter_surf = self.word_font.render(self.current_input[i].upper(), True, self.BLACK)
                    letter_rect = letter_surf.get_rect(center=(box_x + 25, input_y + 25))
                    self.screen.blit(letter_surf, letter_rect)
                else:
                    pygame.draw.rect(self.screen, self.GRAY, (box_x, input_y, 50, 50))
                    pygame.draw.rect(self.screen, self.WHITE, (box_x, input_y, 50, 50), 2)
            
            # Draw instructions
            inst_text = self.small_font.render("Type a 5-letter word and press ENTER", True, self.WHITE)
            self.screen.blit(inst_text, (150, 800))
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if not self.game_over:
                        self.handle_input(event)
                    else:
                        # Restart game on any key press after game over
                        self.__init__()
            
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()


if __name__ == '__main__':
    game = WordleGame()
    game.run()
        
        
        
        
            