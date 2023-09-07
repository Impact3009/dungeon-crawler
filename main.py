@namespace
class SpriteKind:
    Teleporter = SpriteKind.create()
    Weapon = SpriteKind.create()
    wee = SpriteKind.create()
    Boss = SpriteKind.create()

def on_overlap_tile(sprite, location):
    mySprite.vy += -550
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile19
    """),
    on_overlap_tile)

def on_up_pressed():
    if mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
        mySprite.vy += -115
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile2(sprite2, location2):
    global Level, spawn_boss
    Level += 1
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    pause(100)
    spawn_boss = 1
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile15
    """),
    on_overlap_tile2)

def on_a_pressed():
    global fire_ball
    fire_ball = sprites.create(assets.image("""
        Fireball
    """), SpriteKind.projectile)
    fire_ball.set_position(mySprite.x, mySprite.y)
    if Direction > 0:
        fire_ball.set_image(assets.image("""
            Fireball
        """))
    if Direction < 0:
        fire_ball.set_image(assets.image("""
            myImage3
        """))
    fire_ball.ax += Direction
    fire_ball.set_flag(SpriteFlag.DESTROY_ON_WALL, True)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite3, otherSprite):
    HEALTH_BAR.value += randint(-15, -5)
    sprites.destroy(Boss_Projectile)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.player, on_on_overlap)

def on_left_pressed():
    global Direction
    Direction = -400
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_released():
    global Direction
    Direction = randint(200, 400)
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    global Direction
    Direction = randint(-400, -200)
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_on_zero(status):
    sprites.destroy(myEnemy)
statusbars.on_zero(StatusBarKind.enemy_health, on_on_zero)

def on_on_zero2(status2):
    global Deaths
    Deaths += 1
    tiles.place_on_random_tile(mySprite, assets.tile("""
        myTile3
    """))
    HEALTH_BAR.value = 100
statusbars.on_zero(StatusBarKind.health, on_on_zero2)

def on_overlap_tile3(sprite4, location3):
    HEALTH_BAR.value += -5
    mySprite.vy += 115
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile16
    """),
    on_overlap_tile3)

def on_right_pressed():
    global Direction
    Direction = 400
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap2(sprite5, otherSprite2):
    global Boss_dead
    Boss_health.value += randint(-2, -1)
    if Boss_health.value <= 0:
        sprites.destroy(Boss2)
        Boss_dead = 1
sprites.on_overlap(SpriteKind.Weapon, SpriteKind.Boss, on_on_overlap2)

def on_overlap_tile4(sprite6, location4):
    HEALTH_BAR.value += -5
    mySprite.vy += -120
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile5
    """),
    on_overlap_tile4)

def on_on_overlap3(sprite7, otherSprite3):
    Enemy_health.value += randint(-15, -5)
    if Enemy_health.value <= 1:
        sprites.destroy(myEnemy, effects.disintegrate, 500)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap3)

def on_overlap_tile5(sprite8, location5):
    tiles.place_on_random_tile(mySprite, assets.tile("""
        myTile13
    """))
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_insignia,
    on_overlap_tile5)

def on_on_overlap4(sprite9, otherSprite4):
    if PLAYER_COLLECT_SHIELD == 1:
        HEALTH_BAR.value += -2
    if PLAYER_COLLECT_SHIELD == 0:
        HEALTH_BAR.value += -5
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap4)

PLAYER_COLLECT_SWORD = 0
Boss_projectile_spawn = 0
PLAYER_COLLECT_SHIELD = 0
Enemy_health: StatusBarSprite = None
Boss2: Sprite = None
Boss_health: StatusBarSprite = None
myEnemy: Sprite = None
Boss_Projectile: Sprite = None
fire_ball: Sprite = None
Boss_dead = 0
Direction = 0
HEALTH_BAR: StatusBarSprite = None
mySprite: Sprite = None
spawn_boss = 0
story.set_sound_enabled(True)
spawn_boss = 0
Level = 1
if Level == 1:
    tiles.set_current_tilemap(tilemap("""
        level4
    """))
mySprite = sprites.create(assets.image("""
    Spirit
"""), SpriteKind.player)
mySprite.set_stay_in_screen(True)
HEALTH_BAR = statusbars.create(20, 4, StatusBarKind.health)
story.print_text("Welcome Spirit", mySprite.x + 10, mySprite.y + 10)
HEALTH_BAR.attach_to_sprite(mySprite, 0, 0)
HEALTH_BAR.value = 100
HEALTH_BAR.set_bar_border(1, 15)
HEALTH_BAR.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, False)
HEALTH_BAR.set_color(7, 15, 2)
tiles.place_on_random_tile(mySprite, assets.tile("""
    myTile3
"""))
scene.camera_follow_sprite(mySprite)
mySprite.set_bounce_on_wall(False)
music.play(music.string_playable("E B C5 A B G A F ", 120),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
Deaths = 0
game.set_game_over_message(False, "Body Desecrated")
SWORD = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . f . . 
            . . . . . . . . . . . f f f f . 
            . . . . . . . . . f f f 2 1 f . 
            . . . . . . . . f f 1 2 2 1 f . 
            . . . . . . . . f 1 2 2 2 1 f . 
            . . . . . . . f f 1 2 2 1 f . . 
            . . . . . . f f 1 2 2 1 f . . . 
            . . . . . f 1 1 2 2 1 f . . . . 
            . . . f f 1 2 2 2 1 f . . . . . 
            . . f 5 4 2 2 2 1 f . . . . . . 
            . f f 5 2 2 2 1 f . . . . . . . 
            . f 5 5 5 2 f f . . . . . . . . 
            f 5 f f 5 5 f . . . . . . . . . 
            f f . . f f . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.Weapon)
Shield = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . f f f f f f f f . . . . 
            . . . f 7 7 7 7 7 7 7 7 f . . . 
            . . . f 6 6 6 6 6 6 6 6 f . . . 
            . . . f 6 6 6 6 6 6 6 6 f . . . 
            . . . f 6 6 6 6 6 6 6 6 f . . . 
            . . . f 7 7 7 7 7 7 7 7 f . . . 
            . . . f 7 7 7 7 7 7 7 7 f . . . 
            . . . . f 7 7 7 7 7 7 f . . . . 
            . . . . . f 6 6 6 6 f . . . . . 
            . . . . . . f f f f . . . . . .
    """),
    SpriteKind.Weapon)
tiles.place_on_random_tile(SWORD, assets.tile("""
    myTile6
"""))
tiles.place_on_random_tile(Shield, assets.tile("""
    myTile6
"""))
HEALTH_BAR.set_label("HP")
mySprite.ay = 294
Render.set_view_mode(ViewMode.TILEMAP_VIEW)
Direction = 0
Boss_dead = 0
fire_ball = sprites.create(assets.image("""
    Fireball
"""), SpriteKind.projectile)

def on_update_interval():
    global myEnemy, Enemy_health
    myEnemy = sprites.create(img("""
            ........................
                    ........................
                    ........................
                    ........................
                    ..........ffff..........
                    ........ff1111ff........
                    .......fb111111bf.......
                    .......f11111111f.......
                    ......fd11111111df......
                    ......fd11111111df......
                    ......fddd1111dddf......
                    ......fbdbfddfbdbf......
                    ......fcdcf11fcdcf......
                    .......fb111111bf.......
                    ......fffcdb1bdffff.....
                    ....fc111cbfbfc111cf....
                    ....f1b1b1ffff1b1b1f....
                    ....fbfbffffffbfbfbf....
                    .........ffffff.........
                    ...........fff..........
                    ........................
                    ........................
                    ........................
                    ........................
        """),
        SpriteKind.enemy)
    tiles.place_on_random_tile(myEnemy, assets.tile("""
        myTile9
    """))
    Enemy_health = statusbars.create(20, 4, StatusBarKind.enemy_health)
    Enemy_health.max = 30
    myEnemy.follow(mySprite, randint(45, 70))
    Enemy_health.attach_to_sprite(myEnemy, 0, 0)
    Enemy_health.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)
    animation.run_image_animation(myEnemy,
        [img("""
                ........................
                        ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f11111111f.......
                        ......fd11111111df......
                        ......fd11111111df......
                        ......fddd1111dddf......
                        ......fbdbfddfbdbf......
                        ......fcdcf11fcdcf......
                        .......fb111111bf.......
                        ......fffcdb1bdffff.....
                        ....fc111cbfbfc111cf....
                        ....f1b1b1ffff1b1b1f....
                        ....fbfbffffffbfbfbf....
                        .........ffffff.........
                        ...........fff..........
                        ........................
                        ........................
                        ........................
                        ........................
            """),
            img("""
                ........................
                        ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f11111111f.......
                        ......fd11111111df......
                        ......fd11111111df......
                        ......fddd1111dddf......
                        ......fbdbfddfbdbf......
                        ......fcdcf11fcdcf......
                        .......fb111111ffff.....
                        ......fffcdb1bc111cf....
                        ....fc111cbfbf1b1b1f....
                        ....f1b1b1ffffbfbfbf....
                        ....fbfbfffffff.........
                        .........fffff..........
                        ..........fff...........
                        ........................
                        ........................
                        ........................
                        ........................
            """),
            img("""
                ........................
                        ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f11111111f.......
                        ......fd11111111df......
                        ......fd11111111df......
                        ......fddd1111dddf......
                        ......fbdbfddfbdbf......
                        ......fcdcf11fcdcf......
                        .......fb111111bf.......
                        ......fffcdb1bdffff.....
                        ....fc111cbfbfc111cf....
                        ....f1b1b1ffff1b1b1f....
                        ....fbfbffffffbfbfbf....
                        .........ffffff.........
                        ...........fff..........
                        ........................
                        ........................
                        ........................
                        ........................
            """),
            img("""
                ........................
                        ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f11111111f.......
                        ......fd11111111df......
                        ......fd11111111df......
                        ......fddd1111dddf......
                        ......fbdbfddfbdbf......
                        ......fcdcf11fcdcf......
                        .....ffff111111bf.......
                        ....fc111cdb1bdfff......
                        ....f1b1bcbfbfc111cf....
                        ....fbfbfbffff1b1b1f....
                        .........fffffffbfbf....
                        ..........fffff.........
                        ...........fff..........
                        ........................
                        ........................
                        ........................
                        ........................
            """)],
        500,
        True)
game.on_update_interval(2000, on_update_interval)

def on_forever():
    global Boss_projectile_spawn, Boss2, Boss_health, spawn_boss, PLAYER_COLLECT_SWORD, PLAYER_COLLECT_SHIELD
    if Level == 1:
        tiles.set_current_tilemap(tilemap("""
            level4
        """))
        controller.move_sprite(mySprite, 100, 0)
    if Level == 2:
        tiles.set_current_tilemap(tilemap("""
            level1
        """))
        controller.move_sprite(mySprite, 100, 100)
    if Level == 3:
        tiles.set_current_tilemap(tilemap("""
            level
        """))
        story.print_dialog("Congrats you won", 80, 90, 50, 300000)
        game.game_over(True)
    if spawn_boss == 1:
        Boss_projectile_spawn = 1
        Boss2 = sprites.create(assets.image("""
            myImage4
        """), SpriteKind.Boss)
        tiles.place_on_random_tile(Boss2, assets.tile("""
            myTile10
        """))
        Boss_health = statusbars.create(20, 4, StatusBarKind.enemy_health)
        Boss_health.max = 1000000000000000000
        spawn_boss = 0
        Boss_health.attach_to_sprite(Boss2, -44, 0)
        Boss2.set_velocity(100, -100)
        Boss2.change_scale(7, ScaleAnchor.MIDDLE)
        Boss2.set_bounce_on_wall(True)
    if mySprite.overlaps_with(SWORD):
        SWORD.set_position(mySprite.x, mySprite.y)
        PLAYER_COLLECT_SWORD = 1
    if Shield.overlaps_with(SWORD):
        if PLAYER_COLLECT_SWORD == 0:
            tiles.place_on_random_tile(Shield, assets.tile("""
                myTile6
            """))
    if mySprite.overlaps_with(Shield):
        Shield.set_position(mySprite.x, mySprite.y)
        PLAYER_COLLECT_SHIELD = 1
    if PLAYER_COLLECT_SWORD == 1:
        SWORD.set_position(mySprite.x + randint(-30, 30), mySprite.y + randint(-5, 10))
        SWORD.set_bounce_on_wall(True)
    if PLAYER_COLLECT_SHIELD == 1:
        Shield.set_position(mySprite.x, mySprite.y)
        Shield.set_bounce_on_wall(True)
    if Deaths > 2:
        HEALTH_BAR.max += 300
        HEALTH_BAR.value += 300
    if Direction > 0:
        animation.run_image_animation(mySprite,
            assets.animation("""
                heroWalkShieldRight
            """),
            100,
            True)
    if Direction < 0:
        animation.run_image_animation(mySprite,
            assets.animation("""
                heroWalkLeft
            """),
            100,
            True)
forever(on_forever)

def on_update_interval2():
    global Boss_Projectile
    if Boss_projectile_spawn == 1:
        if Level == 2:
            if Boss_dead == 1:
                Boss_Projectile = sprites.create(assets.image("""
                    myImage6
                """), SpriteKind.projectile)
                Boss_Projectile.follow(mySprite, 400)
                tiles.place_on_random_tile(Boss_Projectile, assets.tile("""
                    myTile10
                """))
    if SWORD.overlaps_with(myEnemy):
        Enemy_health.value += randint(-15, -5)
    if Shield.overlaps_with(myEnemy):
        Enemy_health.value += randint(-15, -5)
    if Enemy_health.value <= 1:
        sprites.destroy(myEnemy)
game.on_update_interval(100, on_update_interval2)
