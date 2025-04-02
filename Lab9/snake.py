import pygame
import random
import sys
import time

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20  # Размер одной клетки на поле

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Настройки скорости
START_SPEED = 10
LEVEL_UP_FOOD = 3  # Количество еды для повышения уровня

# Экран и шрифт
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.Font(None, 30)

# Класс Змейки
class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]  # Начальная длина змеи
        self.direction = "RIGHT"
        self.grow = False
    
    def move(self):
        x, y = self.body[0]
        if self.direction == "UP":
            y -= CELL_SIZE
        elif self.direction == "DOWN":
            y += CELL_SIZE
        elif self.direction == "LEFT":
            x -= CELL_SIZE
        elif self.direction == "RIGHT":
            x += CELL_SIZE
        
        new_head = (x, y)
        
        # Проверка на столкновение со стенами
        if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT:
            return False  # Игра окончена
        
        # Проверка на столкновение с самим собой
        if new_head in self.body:
            return False
        
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        
        return True
    
    def change_direction(self, new_direction):
        opposite_directions = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction
    
    def grow_snake(self):
        self.grow = True
    
    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

# Класс Еды
class Food:
    def __init__(self, snake_body):
        self.position = self.generate_food_position(snake_body)
        self.weight = random.choice([1, 2, 3])  # Случайный вес еды
        self.spawn_time = time.time()  # Время появления еды
    
    def generate_food_position(self, snake_body):
        while True:
            x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in snake_body:
                return (x, y)
    
    def should_disappear(self):
        # Еда исчезает через 5 секунд
        return time.time() - self.spawn_time > 5
    
    def draw(self):
        # Разные цвета для еды в зависимости от веса
        if self.weight == 1:
            color = RED
        elif self.weight == 2:
            color = YELLOW
        elif self.weight == 3:
            color = BLUE
        pygame.draw.rect(screen, color, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

# Функция для начала игры
def start_game():
    snake = Snake()
    food = Food(snake.body)
    clock = pygame.time.Clock()
    speed = START_SPEED
    score = 0
    level = 1

    while True:
        screen.fill(WHITE)
        
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")
        
        # Движение змеи
        if not snake.move():
            break  # Конец игры
        
        # Проверка на поедание еды
        if snake.body[0] == food.position:
            snake.grow_snake()
            score += food.weight  # Увеличиваем счёт на вес еды
            food = Food(snake.body)
            
            # Увеличение уровня и скорости
            if score % LEVEL_UP_FOOD == 0:
                level += 1
                speed += 2
        
        # Проверка, должна ли еда исчезнуть
        if food.should_disappear():
            food = Food(snake.body)
        
        # Отрисовка объектов
        snake.draw()
        food.draw()
        
        # Отображение счета и уровня
        score_text = font.render(f"Score: {score}", True, BLACK)
        level_text = font.render(f"Level: {level}", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (SCREEN_WIDTH - 100, 10))
        
        pygame.display.flip()
        clock.tick(speed)
    
    print(f"Game Over! Final Score: {score}, Level: {level}")

# Ожидание нажатия ENTER для начала игры
while True:
    screen.fill(WHITE)
    start_text = font.render("Press ENTER to Start", True, BLACK)
    screen.blit(start_text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2))
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start_game()