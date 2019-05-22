# John Dunne (jd5an) & Sohan Kabiraj (sk5gb)

import pygame, gamebox, random

# x= 0 is left of gamebox
# y = 0 is top of gamebox
time = 0
score = 0
hitlerspawn = 0
playercamera = gamebox.Camera(800, 600)
CHARACTERWIDTH, CHARACTERHEIGHT = 20, 20
row = 0
column = 0
title_screenbackground = gamebox.from_image(400, 300, "http://theliberatedlotus.com/wp-content/uploads/2013/04/stars-cosmos-space-2598.jpg")
play_screen_background = gamebox.from_image(400, 300, "http://c4depot.com/wp-content/uploads/2015/12/Asteroid-Belt-Frames0253.jpg")
start_screen = True
playership_sprite_sheet = gamebox.load_sprite_sheet("http://i.imgur.com/L1SrFk3.png", 3, 8)
playership = gamebox.from_image(400, 550, "https://1.bp.blogspot.com/-SqwrVIJoXXY/U9vXJm7TiiI/AAAAAAAABwU/DyQAiOXcIgU/s1600/blueships1.png")
laserlist = list()
debrislist = list()
hitlerlist = list()
playership.size = 50, 50
playership.rotate(90)
# asteroidimage = gamebox.from_image(200, 150, "http://i1.wp.com/helpmecodeswift.com/wp-content/uploads/2016/01/a10002.png?resize=320%2C240")
shield = 100
consumablelist = list()
counter = 0
laserammo = 25
alienorangelist = list()
alienbulletlist = list()
alienredlist = list()
alienbluelist = list()
batterylist = list()
twentyfivelist = list()
gameover = False
def tick(keys):
    global start_screen, time, play_screen_background, row, column, shield, random_y, random_x, consumablelist, newconsumable, counter
    global laserlist, laser, laserammo, laserheader, debrislist, shieldheader, alienorangelist, alienbulletlist, alienredlist, alienbluelist, score, gameover, batterylist, twentyfivelist
    # Start menu
    if start_screen == True:
        counter += 1
        names = gamebox.from_text(400, 150, "Sohan Kabiraj (sk5gb) & John Dunne (jd5an)", "arial", 18, "white")
        title = gamebox.from_text(400, 100, "The Little Spaceship That Could", "Magneto", 32, "white")
        InstructionsI = gamebox.from_text(400, 350, "The ship is controlled by five keys:", "Magneto", 18, "orange")
        InstructionsII = gamebox.from_text(400, 400, "'a' and 'b' to go left and right respectively", "Magneto", 18, "orange")
        InstructionsIII = gamebox.from_text(400, 450, "'w' and 's' to go up and down respectively, the space bar to fire", "Magneto", 18, "orange")
        if (counter//60) % 2 == 0:
            InstructionsIV = gamebox.from_text(400, 550, "Press 'l' to launch game...", "Magneto", 18, "yellow")
        else:
            InstructionsIV = gamebox.from_text(400, 550, "Press 'l' to launch game...", "Magneto", 18, "red", bold=True)
        playercamera.draw(title_screenbackground)
        playercamera.draw(names)
        playercamera.draw(title)
        playercamera.draw(InstructionsI)
        playercamera.draw(InstructionsII)
        playercamera.draw(InstructionsIII)
        playercamera.draw(InstructionsIV)
        if pygame.K_l in keys:
            start_screen = False
        playercamera.display()
    # The Rest of the game.
    elif start_screen == False and gameover == False:
        if laserammo < 10:
            laserammo += 0.1
        # I have the playercamera move with the ship, was thinking about making it ship focused and
        # having the ship move through the game box, and we can just have things randomly appear and disappear if it is within and outside of a certain radius of the playership.
        # All those True, False you see was just me starting to try to implement a sprite sheet movement-thing for the character....was spitballing an idea.
        play_screen_background.x = playercamera.x
        play_screen_background.y = playercamera.y
        playercamera.draw(play_screen_background)
        laser = gamebox.from_color(playership.x, playership.y, "red", 5, 10)
        time += (1 / 60)

        if pygame.K_d in keys:
            if playership.x < 785:
                playership.x += 5
            elif playership.x >= 780:
                playership.x += 0

        if pygame.K_a in keys:
            if playership.x > 20:
                playership.x += -5
            if playership.x <= 15:
                playership.x += 0

        if pygame.K_SPACE in keys:
            if laserammo >= 1:
                laserammo -= 1
                laserlist.append(laser)
        for laser in laserlist:
            laser.y -= 15
            if laser.y < -25:
                laserlist.remove(laser)
                try:
                    for a in alienredlist:
                        if laser.touches(a):
                            laserlist.remove(laser)
                except:
                    counter += 1
                try:
                    for a in alienbluelist:
                        if laser.touches(a):
                            laserlist.remove(laser)
                except:
                    counter += 1
                try:
                    for a in alienorangelist:
                        if laser.touches(a):
                            laserlist.remove(laser)
                except:
                    counter += 1
                try:
                    for d in debrislist:
                        if laser.touches(d):
                            debrislist.remove(d)
                except:
                    counter += 1

            playercamera.draw(laser)

        playercamera.draw(playership)

        random_spawn = random.randrange(0, 900)
        if random_spawn == 500:
            random_x = random.randrange(25, 785)
            newconsumable = gamebox.from_image(random_x, -50, "http://www.merixgames.com/case-studies/skytte/images/power_up_shield.png")
            newconsumable.scale_by(.50)
            consumablelist.append(newconsumable)
        for c in consumablelist:
            if c.y > 700:
                consumablelist.remove(c)
            c.y += 5
            if playership.touches(c):
                consumablelist.remove(c)
                if shield < 150:
                    shield += 25
                elif shield >= 150:
                    shield += 0
            playercamera.draw(c)

        random_25spawn = random.randrange(0, 1500)
        if random_25spawn == 500:
            random_26x = random.randrange(25, 785)
            twentyfive = gamebox.from_image(random_26x, -50, "http://theeconomiccollapseblog.com/wp-content/uploads/2013/04/100-Years-Old-And-Still-Killing-Us-America-Was-Much-Better-Off-Before-The-Income-Tax.png")
            twentyfive.scale_by(.05)
            twentyfivelist.append(twentyfive)
        for t in twentyfivelist:
            if t.y > 700:
                twentyfivelist.remove(t)
            t.y += 5
            try:
                if playership.touches(t):
                    twentyfivelist.remove(t)
                    score += 100
            except:
                score += 0
            playercamera.draw(t)

        random_batteryspawn = random.randrange(0, 900)
        if random_batteryspawn == 500:
            random_x25 = random.randrange(25, 785)
            battery = gamebox.from_image(random_x25, -50, "https://equipping4eministry.files.wordpress.com/2013/01/battery.png")
            battery.scale_by(.10)
            batterylist.append(battery)
        for b in batterylist:
            if b.y > 700:
                batterylist.remove(b)
            b.y += 5
            try:
                if playership.touches(b):
                    batterylist.remove(b)
                    laserammo += 50
            except:
                laserammo += 0
            playercamera.draw(b)

        randomdebrisspawn = random.randrange(0, 50)
        random_x2 = random.randrange(25, 785)
        if randomdebrisspawn == 25:
            random_x = random.randrange(25, 785)
            randomasteroidimage = random.randrange(-1, 2)
            if randomasteroidimage == 1:
                asteroid = gamebox.from_image(random_x2, -50, "http://icons.iconarchive.com/icons/zairaam/bumpy-planets/256/asteroid-icon.png")
                asteroid.scale_by(.15)
                debrislist.append(asteroid)
            if randomasteroidimage == 0:
                asteroid = gamebox.from_image(random_x2, -50, "http://deepspaceindustries.com/wp-content/uploads/2015/01/asteroid-png-0.png")
                asteroid.scale_by(.15)
                debrislist.append(asteroid)
        for asteroid in debrislist:
            if asteroid.y > 700:
                debrislist.remove(asteroid)
            asteroid.y += 7
            if playership.touches(asteroid):
                debrislist.remove(asteroid)
                shield -= 25
            playercamera.draw(asteroid)

        # Alien 1
        randomalienspawn1 = random.randrange(0, 200)
        if randomalienspawn1 == 50:
            random_y2 = random.randrange(25, 400)
            alienorange = gamebox.from_image(850, random_y2, "http://2.bp.blogspot.com/-Z4RDLpxRu50/Uc8316Abq4I/AAAAAAAAArc/5NMtXDFAARA/s302/aliensprite.png")
            alienorange.scale_by(.25)
            alienorangelist.append(alienorange)
        for alienorange in alienorangelist:
            if alienorange.x < -25:
                alienorangelist.remove(alienorange)
            alienorange.x -= 7
            for laser in laserlist:
                try:
                    if laser.touches(alienorange):
                        alienorangelist.remove(alienorange)
                        score += 5
                except:
                    score += 0
            playercamera.draw(alienorange)
        for alienorange in alienorangelist:
            randomfire1 = random.randrange(0, 20)
            if randomfire1 == 10:
                alienbulletorange = gamebox.from_color(alienorange.x, alienorange.y, "orange", 3, 5)
                alienbulletlist.append(alienbulletorange)

        # Alien 2
        randomalienspawn3 = random.randrange(0, 1000)
        if randomalienspawn3 == 500:
            random_y4 = random.randrange(25, 400)
            alienblue = gamebox.from_image(-50, random_y4, "https://i.stack.imgur.com/ELxFZ.png")
            alienblue.scale_by(.15)
            alienblue.rotate(180)
            alienredlist.append(alienblue)
        for alienblue in alienbluelist:
            if alienblue.x > 850:
                alienbluelist.remove(alienblue)
            alienblue.x += 7
            for laser in laserlist:
                try:
                    if laser.touches(alienblue):
                        alienbluelist.remove(alienblue)
                        score += 10
                except:
                    score += 0
            playercamera.draw(alienblue)
        for alienblue in alienbluelist:
            randomfire1 = random.randrange(0, 15)
            if randomfire1 == 5:
                alienbullet = gamebox.from_color(alienblue.x, alienblue.y, "blue", 3, 5)
                alienbulletlist.append(alienbullet)


        # Alien 3
        randomalienspawn2 = random.randrange(0, 1000)
        if randomalienspawn2 == 500:
            random_y3 = random.randrange(25, 400)
            alienred = gamebox.from_image(-50, random_y3, "https://s-media-cache-ak0.pinimg.com/originals/5b/d9/89/5bd98917f680e1330c1852ab8b979374.png")
            alienred.scale_by(.25)
            alienred.rotate(180)
            alienredlist.append(alienred)
        if randomalienspawn1 == 500:
            random_y3 = random.randrange(25, 400)
            alienred = gamebox.from_image(-50, random_y3,
                                          "https://vignette.wikia.nocookie.net/agk/images/3/3b/Hitler_Sprite.png/revision/latest?cb=20150321043434")
            alienred.scale_by(.25)
            alienred.rotate(180)
            alienredlist.append(alienred)
        for alienred in alienredlist:
            if alienred.x > 850:
                alienredlist.remove(alienred)
            alienred.x += 7
            for laser in laserlist:
                try:
                    if laser.touches(alienred):
                        alienredlist.remove(alienred)
                        score += 15
                except:
                    score += 0
            playercamera.draw(alienred)
        for alienred in alienredlist:
            randomfire1 = random.randrange(0, 5)
            if randomfire1 == 2:
                alienbullet = gamebox.from_color(alienred.x, alienred.y, "red", 3, 5)
                alienbulletlist.append(alienbullet)

        for bullets in alienbulletlist:
            if bullets.y > 625:
                alienbulletlist.remove(bullets)
            if playership.touches(bullets):
                shield -= 10
                alienbulletlist.remove(bullets)
            bullets.y += 3
            playercamera.draw(bullets)

        if shield > 100.01:
            shield -= 0.01

        if shield > 100:
            shieldheader = gamebox.from_text(150, 585, "Shield Integrity: " + str(int(shield)) + "%", "Magneto", 18, "green")
        elif shield > 40:
            shieldheader = gamebox.from_text(150, 585, "Shield Integrity: " + str(int(shield)) + "%", "Magneto", 18, "lightblue")
        elif shield <= 40 and shield >= 15:
            shieldheader = gamebox.from_text(150, 585, "Shield Integrity: " + str(int(shield)) + "%", "Magneto", 18, "orange")
        elif shield < 15:
            shieldheader = gamebox.from_text(150, 585, "Shield Integrity: " + str(int(shield)) + "%", "Magneto", 18, "red")

        laserheader = gamebox.from_text(650, 585, "Laser Battery: " + str(int(laserammo)), "Magneto", 24, "red")
        timeheader = gamebox.from_text(650, 50, "Time Survived: " + str(int(time)), "Magneto", 24, "white")
        scoreheader = gamebox.from_text(100, 50, "Score: " + str(int(score + time*2)), "Magneto", 24, "white")
        playercamera.draw(laserheader)
        playercamera.draw(timeheader)
        playercamera.draw(scoreheader)
        playercamera.draw(shieldheader)
    if shield <= 0:
        gameover = True
    playercamera.display()

    if gameover == True:
        gameoverscreen = gamebox.from_image(2500, 2500, "https://cdn.allwallpaper.in/wallpapers/800x600/15747/outer-space-supernova-constellations-800x600-wallpaper.jpg")
        finalheader = gamebox.from_text(2500, 2500, "Your Final Score: " + str(int(score + time*2)), "Magneto", 32, "black")
        playercamera.x = 2500
        playercamera.y = 2500
        playercamera.draw(gameoverscreen)
        playercamera.draw(finalheader)
        playercamera.display()

ticks_per_second = 60
gamebox.timer_loop(ticks_per_second, tick)