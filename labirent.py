from pygame import*
from time import time as timer

import pygame #Yorumlayıcının bu işlevi pygame zaman modülünde aramasını önlemek


#sprite için ebeveyn sınıf
class GameSprite(sprite.Sprite):
    #yapıcı metot
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(52,48))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))



#2.hafta
#oyuncu sprite için ardıl sınıfı (oklarıyla kontrol edilir)
class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width -80:
           self.rect.x += self.speed
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height -80:
           self.rect.y += self.speed


#düşman ve sprite için olan ardıl sınıf (kendi başına hareket eder)
class Enemy(GameSprite):


    direction = "left"
    direction2= "yukarı"
    direction3 = "left" 
    direction4 = "left"
    def update(self):
        if self.rect.x <= 400:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"


        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    
    def update2(self):
       if self.rect.y <= 380:
           self.direction2 = "aşağı"
       if self.rect.y >= 620:
           self.direction2 = "yukarı"


       if self.direction2 == "yukarı":
           self.rect.y -= self.speed
       else:
           self.rect.y += self.speed


    def update3(self):
        if self.rect.x <= 10:
            self.direction = "right"
        if self.rect.x >= win_width - 600:
            self.direction = "left"


        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


    def update4(self):
        if self.rect.x <= 125:
            self.direction = "right"
        if self.rect.x >= win_width - 370:
            self.direction = "left"


        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed



    #--


#3.hafta 
# engeller için sprite sınıfı oluştur

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1    
        self.color_2 = color_2
        self.color_3 = color_3   
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3)) 
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x , self.rect.y))



#oyun sahnemiz
win_width=900
win_height=680
window=display.set_mode((win_width,win_height))
display.set_caption("Labirent")
background=transform.scale(image.load("arkaplan.jpg"),(win_width,win_height))


#2.hafta güncelleme
#Oyunun karakterleri
player = Player('prensahtapot.png', 10, win_height - 580, 3)
monster = Enemy('denizcanavarı.png', win_width - 80, 296, 2)
monster2 = Enemy('denizcanavarı.png', win_width - 220, 500, 3)
monster3 = Enemy('denizcanavarı.png', win_width  - 900, 300, 2)
monster4 = Enemy('denizcanavarı.png', win_width  - 500, 500, 2)
final = GameSprite('prensesahtopot.png', win_width - 90, win_height - 90, 2)
#--
game=True
clock=time.Clock()
fps=60
finish = False
run = True





#3.hafta duvar nesnelerini oluştur  (color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height)
w1 = Wall(168, 153, 143, 0, 70 , 900, 7)#yatay üst köşe
w2 = Wall(168, 153, 143, 278, 185 , 23, 90)#DİKEY DUVAR
w3 = Wall(168, 153, 143, 0, 170 , 85, 15)
w4 = Wall(168, 153, 143, 200, 170 , 180, 15)
w5 = Wall(168, 153, 143, 490, 170 , 150, 15)
w6 = Wall(168, 153, 143, 770, 170 , 150, 15)
w7 = Wall(168, 153, 143, 120, 260 , 390, 15)
w8 = Wall(168, 153, 143, 0, 360 , 85, 15)
w9 = Wall(168, 153, 143, 370, 270 , 23, 100)#DİKEY DUVAR
w10 = Wall(168, 153, 143, 200, 360 , 245, 15)
w11 = Wall(168, 153, 143, 320, 375 , 23, 105)#DİKEY DUVAR
w12 = Wall(168, 153, 143, 120, 470 , 275, 15)
w13 = Wall(168, 153, 143, 100, 470 , 23, 80)#DİKEY DUVAR
w14 = Wall(168, 153, 143, 0, 70 , 7, 630)#dikey sol köşe
w15 = Wall(168, 153, 143, 0, 673 , 900, 7)#yatay alt köşe
w16 = Wall(168, 153, 143, 893, 70 , 7, 630)#dikey sağ köşe
w17 = Wall(168, 153, 143, 640, 260 , 300, 15)
w18 = Wall(168, 153, 143, 550, 360 , 200, 15)
w19 = Wall(168, 153, 143, 873, 360 , 20, 85)#DİKEY DUVAR
w20 = Wall(168, 153, 143, 750, 360 , 15, 85)#DİKEY DUVAR
w21 = Wall(168, 153, 143, 750, 430 , 200, 15)
w22 = Wall(168, 153, 143, 100, 658 , 400, 15)
w23 = Wall(168, 153, 143, 190, 635 , 270, 23)
w24 = Wall(168, 153, 143, 600, 460 , 15, 240)#DİKEY DUVAR
w25 = Wall(168, 153, 143, 515, 460 , 100, 15)



font.init()
font = font.Font(None,100)
win = font.render('YOU WIN' ,True, (255,215,0))
lose = font.render('YOU LOSE', True, (180,0,0))

#müzik
mixer.init()
mixer.music.load('arkases.mpeg')
mixer_music.set_volume(0.6)
mixer.music.play()

kazanma = mixer.Sound('kazanma.mpeg')
kazanma.set_volume(0.5)
kaybetme = mixer.Sound('kaybetme.mpeg')
kaybetme.set_volume(0.4)



while game:
    for e in event.get():
        if e.type ==QUIT:
            game=False


    
    #2.hafta
    if finish != True:
        window.blit(background,(0,0))
        player.update()
        monster.update()
        monster2.update2()
        monster3.update3()
        monster4.update4()

      
        player.reset()
        monster.reset()
        monster2.reset()
        monster3.reset()
        monster4.reset()
        final.reset()


        #3.hafta
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w13.draw_wall()
        w14.draw_wall()
        w15.draw_wall()
        w16.draw_wall()
        w17.draw_wall()
        w18.draw_wall()
        w19.draw_wall()
        w20.draw_wall()
        w21.draw_wall()
        w22.draw_wall()
        w23.draw_wall()
        w24.draw_wall()
        w25.draw_wall()
        

        duvar = []
        duvar.append(w1)
        duvar.append(w2)
        duvar.append(w3)
        duvar.append(w4)
        duvar.append(w5)
        duvar.append(w6)
        duvar.append(w7)
        duvar.append(w8)
        duvar.append(w9)
        duvar.append(w10)
        duvar.append(w11)
        duvar.append(w12)
        duvar.append(w13)
        duvar.append(w14)
        duvar.append(w15)
        duvar.append(w16)
        duvar.append(w17)
        duvar.append(w18)
        duvar.append(w19)
        duvar.append(w20)
        duvar.append(w21)
        duvar.append(w22)
        duvar.append(w23)
        duvar.append(w24)
        duvar.append(w25)




    #kaybetme durumunu kontrol et.
    for x in duvar:
        if sprite.collide_rect(player, x):
            kaybetme.play()
            finish = True
            window.blit(lose, (270,350))


    #kazanma durumu
    if sprite.collide_rect(player, final):
        kazanma.play()
        finish = True
        window.blit(win,(270,350))

    

    #canavara değerse ölme durumu
    if sprite.collide_rect(player, monster):
        kaybetme.play()
        finish = True
        window.blit(lose, (270,350))

    if sprite.collide_rect(player, monster2):
        kaybetme.play()
        finish = True
        window.blit(lose, (270,350))

    if sprite.collide_rect(player, monster3):
        kaybetme.play()
        finish = True
        window.blit(lose, (270,350))

    if sprite.collide_rect(player, monster4):
        kaybetme.play()
        finish = True
        window.blit(lose, (270,350))

                


    #--

    
    display.update()
    clock.tick(fps)  