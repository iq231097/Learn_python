import sys
import pygame
from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    """Responds to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        # move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # move the ship to the left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet
        fire_bullets(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """respond to releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, enemy_ship, bullets):
    """update images on the screen and flip to the new screen. """
    # redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    # redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    enemy_ship.blitme()
    # hacer visible el ultimo dibujo mostrado en la pantalla
    pygame.display.flip()


def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullets(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet. """
    # create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)