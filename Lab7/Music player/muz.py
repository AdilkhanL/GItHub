import pygame

songs_list = ["Қызыл+өрік.mp3", "Кайрат Нуртас - Қызыл Гүлім-Ай.mp3", "abai-begey-aspanga-karaymyn.mp3"]
current_index = 0

pygame.init()

is_play = False

RES = HEIGHT, WIDTH = 225, 225
surface = pygame.display.set_mode(RES)

def  play_song(index):
    
    pygame.mixer.music.load(songs_list[index])
    pygame.mixer.music.play()

def next_song():
    global current_index
    current_index = (current_index + 1) % len(songs_list)
    play_song(current_index)

def perv_song():
    global current_index
    current_index = (current_index - 1) % len(songs_list)
    play_song(current_index)





image = pygame.image.load('Наушник.jpeg')
image = pygame.transform.scale(image, RES)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
          
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not is_play:
                play_song(current_index)
                is_play = True
            elif is_play:
                pygame.mixer.music.stop()
                is_play = False
                
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            next_song()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            perv_song()
        if event.type == pygame.USEREVENT:
            next_song()


    surface.blit(image,(0,0))

    pygame.display.flip()