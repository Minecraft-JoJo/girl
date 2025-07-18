import pygame as pg

# 一，初始化设置
pg.init()
window = pg.display.set_mode((1200, 600))
Clockk = pg.time.Clock()
pg.display.set_caption('刘善政做的超牛逼的游戏!')

# 一  1 .图片加载
icon_image = pg.image.load(r'resource\images\preview.jpg')

img_mouse = pg.image.load(r'resource\images\cursor.png')
img_mouse = pg.transform.rotozoom(img_mouse, 0, 0.3)

img_sky = pg.image.load(r'resource\images\background\Cielo pixelado.png')
img_sky = pg.transform.scale(img_sky, (1200, 600))
rect = img_sky.get_rect()
rect.center = window.get_rect().center


# 一  2 .音乐加载
pg.mixer.music.load(
    r"resource\sound\EssentialGameAudiopackFixed\FullScores\Orchestral Scores\Ove Melaa - Heaven Sings.mp3")

#  一  4 .文本渲染
font2 = pg.font.Font('C:\Windows\Fonts\包图小白体_0.ttf', 36)  # 默认字体，36大小 给别人玩一般要在文件里加字体
text_img = font2.render('Start', True, 'red')  # True抗锯齿开启


# 精灵： sprite   对可移动图形元素的总称，包括角色敌人等


class Player:
    def __init__(self):
        #    加载

        # 初始人物
        self.img_character = pg.image.load('resource\\character anime\\idle\\i1.png').convert_alpha()

        #  站立
        self.idle_frame = []
        for i in range(1, 3):
            img = pg.image.load(f'resource\\character anime\\idle\\i{i}.png').convert_alpha()
            img = pg.transform.rotozoom(img, 0, 0.3)
            self.idle_frame.append(img)

        #  跑步
        self.runs_frame = []
        for i in range(1, 9):
            img = pg.image.load(f'resource\\character anime\\run\\k{i}.png').convert_alpha()
            img = pg.transform.rotozoom(img, 0, 0.3)
            self.runs_frame.append(img)

        #  攻击
        self.attack_frame = []
        for i in range(1, 14):
            img = pg.image.load(f'resource\\character anime\\attack\\a{i}.png').convert_alpha()
            img = pg.transform.rotozoom(img, 0, 0.3)
            self.attack_frame.append(img)

        # 攻击音效
        self.attack_snd1 = pg.mixer.Sound(
            r'resource\sound\attack\male-attack-sounds\1.wav')
        self.attack_snd1.set_volume(0.4)

        self.attack_snd2 = pg.mixer.Sound(
            r'resource\sound\attack\male-attack-sounds\3.wav')
        self.attack_snd2.set_volume(0.4)

        self.attack_snd3 = pg.mixer.Sound(
            r'resource\sound\attack\male-attack-sounds\4.wav')
        self.attack_snd3.set_volume(0.4)



        self.attack_snd4 = pg.mixer.Sound(
            r'resource\sound\attack\melee sounds\melee sounds\animal melee sound.wav')
        self.attack_snd4.set_volume(0.3)

        self.attack_snd5 = pg.mixer.Sound(
            r'resource\sound\attack\melee sounds\melee sounds\melee sound.wav')
        self.attack_snd5.set_volume(0.3)

        self.attack_snd6 = pg.mixer.Sound(
            r'resource\sound\attack\melee sounds\melee sounds\onlinedo-output.wav')
        self.attack_snd6.set_volume(0.3)

        self.attack_sound = [self.attack_snd1, self.attack_snd2, self.attack_snd3, self.attack_snd4, self.attack_snd5, self.attack_snd6]



        #  人物碰撞
        self.img_character = pg.transform.rotozoom(self.img_character, 0, 0.3)
        self.rect = self.img_character.get_rect()
        self.rect.center = window.get_rect().center
        self.rect.y += 100

        # 参数：

        self.is_running = 0
        self.is_attack = 0

        # 跑步计时器
        self.counter = -1
        self.timer = 0

        # 站立计时器

        self.counter_idle = -1
        self.timer_idle = 0

        # 攻击计时器
        self.counter_attack = -1
        self.timer_attack1 = 0
        self.timer_attack2 = 0
        self.choice_attack = 0

        #  下标选择
        self.current_frame = 0
        self.current_frame_idle = 0
        self.current_frame_attack = 0

        # 朝向
        self.direction = 1

        # 行为与更新



    def attack(self):
        if not self.is_attack:
            self.choice_attack += 1
        if self.choice_attack == 4:
            self.choice_attack = 1
        if not self.is_attack:
            x = self.choice_attack - 1
            self.attack_sound[x].play()
            self.attack_sound[x + 3].play()
        self.is_attack = True



    def update(self):

        was_moving = self.is_running
        self.is_running = False


        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            self.is_running = True
            self.direction = -1

        if keys[pg.K_d]:
            self.is_running = True
            self.direction = 1

        if self.choice_attack == 1:
            self.timer_attack1 += 1
            if self.timer_attack1 >= 4:
                self.timer_attack1 = 0
                self.counter_attack += 1
                if self.current_frame_attack == 4:
                    self.counter_attack = -1
                    self.is_attack = False
                self.current_frame_attack = self.counter_attack % 5

        elif self.choice_attack == 2:
            self.timer_attack2 += 1
            if self.timer_attack2 >= 6:
                self.timer_attack2 = 0
                self.counter_attack += 1
                if self.current_frame_attack == 8:
                    self.counter_attack = -1
                    self.is_attack = False
                self.current_frame_attack = self.counter_attack % 4 + 5

        elif self.choice_attack == 3:
            self.timer_attack2 += 1
            if self.timer_attack2 >= 7:
                self.timer_attack2 = 0
                self.counter_attack += 1
                if self.current_frame_attack == 12:
                    self.counter_attack = -1
                    self.is_attack = False
                self.current_frame_attack = self.counter_attack % 4 + 9

        if self.is_running:
            self.timer += 1
            if self.timer >= 4:
                self.timer = 0
                self.counter += 1
                self.current_frame = self.counter % 8

        elif was_moving:  # 如果刚刚停止移动
            self.counter = -1
        else:
            self.timer_idle += 1
            if self.timer_idle >= 30:
                self.timer_idle = 0
                self.counter_idle += 1
                self.current_frame_idle = self.counter_idle % 2

    def draw(self):
        if self.is_attack:
            frame = pg.transform.flip(self.attack_frame[self.current_frame_attack], self.direction == -1, False)
            window.blit(frame, self.rect)

        elif self.is_running:
            frame = pg.transform.flip(self.runs_frame[self.current_frame], self.direction == -1, False)
            if self.direction == 1:
                self.rect.x += 10
            else:
                self.rect.x -= 10
            window.blit(frame, self.rect)


        else:
            frame = pg.transform.flip(self.idle_frame[self.current_frame_idle], self.direction == -1, False)
            window.blit(frame, self.rect)


player = Player()  # 创建精灵

#   初始设定

pg.mouse.set_visible(0)  # 隐藏光标

pg.display.set_icon(icon_image)  # 程序图标

pg.mixer.music.play(1, 3, 5000)  # 播放两次，从第三秒开始, 五秒之后恢复到正常音量
pg.mixer.music.set_volume(0.15)

# 初始参数
x, y = 400, 300

running = 1
while running:
    window.blit(img_sky, (rect))

    player.update()

    player.draw()


    #  事件
    for ev in pg.event.get():
        if ev.type == pg.MOUSEMOTION:
            x, y = pg.mouse.get_pos()
        if ev.type == pg.MOUSEBUTTONDOWN:  # 鼠标按下
            if ev.button == pg.BUTTON_LEFT:
                pg.mixer.music.pause()
            elif ev.button == pg.BUTTON_RIGHT:
                pg.mixer.music.unpause()

        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_j:
                player.attack()

        if ev.type == pg.QUIT:
            running = 0
            break


    window.blit(img_mouse, (x, y))
    pg.display.update()
    Clockk.tick(60)

print('quit')
pg.quit()
