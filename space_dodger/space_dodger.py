import pygame, sys, random
from pygame.locals import *

def enter_username():
    pygame.init()

    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("space_dodger")

    font = pygame.font.SysFont("comicsans", 30)
    text = font.render("Username: ", True, (255, 255, 255))

    typing = pygame.mixer.Sound("typing.mp3")

    error_msg = ""
    username = ""

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if username != "":
                        error_msg = ""
                        for num in range(10):
                            if username.find(str(num)) != -1:
                                error_msg = "#username cannot include numbers#"
                        if error_msg == "":
                            pygame.quit()
                            return username

                    else:
                        error_msg = "#please enter a username#"
                elif event.key == K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode
                    typing.play()
                    
                    


        screen.fill((0, 0, 0))
        screen.blit(text, (0, 100))
        pygame.draw.rect(screen, (100, 100, 100), (0, 150, 500, 40))
        error_text = font.render(error_msg, True, (255, 0, 0))
        screen.blit(error_text, (0, 200))
        username_text = font.render(username + "|", True, (0, 0, 50))
        screen.blit(username_text, (0, 150))

        pygame.display.update()
        pygame.time.Clock().tick(60)
        


def menu_win():
    pygame.init()
    clock = pygame.time.Clock()

    click = pygame.mixer.Sound("typing.mp3")

    file = open("highest_score.txt", "r")
    content = file.readlines()
    file.close()
    
    win = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("space dodger")
    
    
    menu = True
    while menu:
        clock.tick(60)
        global event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        menu_font = pygame.font.SysFont("terminal", 50)
        play_text = menu_font.render("PLAY", True, (255, 255, 255), (0, 255, 0))
        play_rect = play_text.get_rect()
        play_rect.center = (300, 100)

        quit_text = menu_font.render("QUIT", True, (255, 255, 255), (0, 255, 0))
        quit_rect = quit_text.get_rect()
        quit_rect.center = (300, 200)

        leader_board_text = menu_font.render("LEADER BOARD", True, (255, 255, 255), (0, 255, 0))
        leader_board_rect = leader_board_text.get_rect()
        leader_board_rect.center = (300, 300)
        
        mouse = pygame.mouse.get_pos()
        
        if play_rect.collidepoint((mouse[0], mouse[1])):
            play_text = menu_font.render("PLAY", True, (255, 255, 255), (0, 255, 255))
            if event.type == MOUSEBUTTONDOWN:
                menu = False
                pygame.quit()
                main()

        if quit_rect.collidepoint((mouse[0], mouse[1])):
            quit_text = menu_font.render("QUIT", True, (255, 255, 255), (0, 255, 255))
            if event.type == MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
                
        if leader_board_rect.collidepoint((mouse[0], mouse[1])):
            leader_board_text = menu_font.render("LEADER BOARD", True, (255, 255, 255), (0, 255, 255))
            if event.type == MOUSEBUTTONDOWN:
                click.play()
                    
                font = pygame.font.SysFont("terminal", 40)
                lb_text = font.render("LEADER BOARD", True, (255, 0, 0))
                content_list = []
                while True:
                    
                    clock.tick(60)
                    win.fill((0, 0, 0))
                    win.blit(lb_text, (0, 0))
                    
                    for a in range(2000):
                        for thing in content:
                            if thing.find(str(2000 - a)) != -1 and thing not in content_list:
                                content_list.append(thing)

                    try:
                        for i in range(12):
                            text = font.render(content_list[i], True, (255, 255, 255))
                            win.blit(text, (0, (i + 1) * 30))
                    except:
                        for i in range(len(content_list)):
                            text = font.render(content_list[i], True, (255, 255, 255))
                            win.blit(text, (0, (i + 1) * 30))
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == KEYDOWN:
                            menu_win()
                    
                    

        win.fill((0, 0, 0))
        win.blit(play_text, play_rect)
        win.blit(quit_text, quit_rect)
        win.blit(leader_board_text, leader_board_rect)



        pygame.display.update()
        
    
        
    

def main():

        name = enter_username()
        
        pygame.init()

        hit = pygame.mixer.Sound("hit.mp3")

        pygame.time.delay(1000)

        WIDTH, HEIGHT = 800, 800

        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("space dodger")

        FPS = 60
        clock = pygame.time.Clock()

        score = 0
        life = 3

        enemy_mins = 3
        enemy_maxs = 7

        score_font = pygame.font.SysFont("comicsnas", 40)
        lost_font = pygame.font.SysFont("terminal", 200)
        lost_text = lost_font.render("YOU LOST", False, (255, 255, 255))
        
        write_score = open("highest_score.txt", "a")

        class Player():
            def __init__(self, x, y, w, h, color, speed):
                self.x = x
                self.y = y
                self.w = w
                self.h = h
                self.color = color
                self.speed = speed

            def draw(self):
                self.obj = pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))

            def move(self):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT] and self.x > 0:
                    self.x -= self.speed
                if keys[pygame.K_RIGHT] and self.x < WIDTH - 20:
                    self.x += self.speed
                if keys[pygame.K_UP] and self.y > 0:
                    self.y -= self.speed
                if keys[pygame.K_DOWN] and self.y < HEIGHT - 20:
                    self.y += self.speed
                    


        class Enemy():
            def __init__(self, x, y, w, h, color, speed):
                self.x = x
                self.y = y
                self.w = w
                self.h = h
                self.color = color
                self.speed = speed

            def draw(self):
                self.obj = pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))

            def move(self):
                self.y += self.speed

            def collide(self):
                if self.obj.colliderect(player.obj):
                    self.y = random.randint(-200, -20)
                    self.x = random.randint(0, WIDTH)
                    self.speed = random.randint(enemy_mins, enemy_maxs)
                    return True

            def boundary(self):
                if self.y >= HEIGHT:
                    self.y = random.randint(-200, -20)
                    self.x = random.randint(0, WIDTH)
                    self.speed = random.randint(enemy_mins, enemy_maxs)
                    return True


        player = Player(400, 400, 20, 20, (255, 255, 255), 5)

        enemy = []
        for i in range(10):
            enemy.append(Enemy(random.randint(0, WIDTH), random.randint(-200, -20), 20, 20, (255, 0, 0), random.randint(enemy_mins, enemy_maxs)))

        time = 0

        while True:
                
            time += 1
            if time % 1000 == 0:
                enemy_mins += 1
                enemy_maxs += 1
                enemy.append(Enemy(random.randint(0, WIDTH), random.randint(-200, -20), 20, 20, (255, 0, 0), random.randint(enemy_mins, enemy_maxs)))

            score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))
            life_text = score_font.render("Life: " + str(life), True, (255, 255, 255))

            screen.fill((0, 0, 0))
                
            player.draw()
            player.move()
                
            for i in enemy:
                i.draw()
                i.move()

                if i.collide():
                    life -= 1
                    hit.play()
                    
                if i.boundary():
                    score += 1

            screen.blit(score_text, (0, 0))
            screen.blit(life_text, (0, 40))
                
                
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if life <= 0:
                
                write_score.write(name + ": " + str(score) + "\n")
                write_score.close()
                           
                pygame.time.delay(1000)
                screen.fill((0, 0, 0))
                screen.blit(lost_text, (0, 300))
                screen.blit(score_text, (0, 0))
                pygame.display.update()
                pygame.time.delay(3000)
                pygame.quit()
                menu_win()
                    

            clock.tick(FPS)
            pygame.display.update()

                    

if __name__ == "__main__":
    menu_win()

    
