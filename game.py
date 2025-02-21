import pygame  # Importation du module pygame
import random  # Importation du module random pour générer des valeurs aléatoires
import time  # Importation du module time pour gérer les pauses
from draw import draw_road, draw_start_end_lines  # Importation de fonctions pour dessiner la route

# Initialisation de pygame
pygame.init()

# Définition des constantes du jeu
WIDTH, HEIGHT = 800, 600  # Dimensions de la fenêtre
player_CAR_WIDTH, player_CAR_HEIGHT = 50, 90  # Taille de la voiture du joueur
computer_CAR_WIDTH, computer_CAR_HEIGHT = 100, 90  # Taille de la voiture ennemie

# Couleurs utilisées dans le jeu
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (169, 169, 169)

# Création de la fenêtre du jeu
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Définition de la fenêtre
pygame.display.set_caption("Racing Game")  # Définition du titre de la fenêtre

# Chargement et redimensionnement des images des voitures
player_car = pygame.image.load("assets/player_car.png")  # Chargement de l'image du joueur
player_car = pygame.transform.scale(player_car, (player_CAR_WIDTH, player_CAR_HEIGHT))  # Redimensionnement

enemy_car = pygame.image.load("assets/computer_car.png")  # Chargement de l'image de l'ennemi
enemy_car = pygame.transform.scale(enemy_car, (computer_CAR_WIDTH, computer_CAR_HEIGHT))  # Redimensionnement

# Variables du jeu
player_x, player_y = WIDTH // 3 + 80, HEIGHT - 120  # Position initiale du joueur
enemy_x, enemy_y = 2 * WIDTH // 3 - 80, HEIGHT - 120  # Position initiale de l'ennemi
player_speed = 5  # Vitesse du joueur
enemy_speed = 3  # Vitesse de l'ennemi
race_started = False  # État de la course
winner = None  # Variable pour stocker le gagnant

# Définition de la police d'écriture
font = pygame.font.Font(None, 50)

go_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 - 25, 100, 50)  # Bouton "GO"
restart_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 50, 140, 50)  # Bouton "Restart"

# Fonction pour afficher un compte à rebours avant le départ
def countdown():
    for i in range(3, 0, -1):  # Boucle de 3 à 1
        screen.fill(WHITE)  # Remplir l'écran en blanc
        draw_road()  # Dessiner la route
        draw_start_end_lines(screen, WIDTH, HEIGHT)  # Dessiner les lignes de départ et d'arrivée
        text = font.render(str(i), True, BLACK)  # Afficher le chiffre du compte à rebours
        screen.blit(text, (WIDTH // 2 - 10, HEIGHT // 2 - 50))  # Positionner le texte
        pygame.display.update()  # Mettre à jour l'affichage
        time.sleep(1)  # Attendre 1 seconde

# Boucle principale du jeu
running = True
clock = pygame.time.Clock()  # Création d'une horloge pour gérer la vitesse
# AJOUT DE LA BOUCLE PRINCIPALE DU  AVEC LA CONDITION QUI CONTROLE LE JEU
    screen.fill(WHITE)  # Effacer l'écran
    draw_road()  # Dessiner la route
    draw_start_end_lines(screen, WIDTH, HEIGHT)  # Dessiner les lignes de départ et d'arrivée
    
    for event in pygame.event.get():  # Gestion des événements
        if event.type == pygame.QUIT:  # Si l'utilisateur ferme la fenêtre
            running = False  # Arrêter le jeu
        if event.type == pygame.MOUSEBUTTONDOWN:  # Si un bouton de la souris est cliqué
            if go_button.collidepoint(event.pos):  # Si le bouton "GO" est cliqué
                countdown()  # Lancer le compte à rebours
                race_started = True  # Démarrer la course
                winner = None  # Réinitialiser le gagnant
                player_x, player_y = WIDTH // 4 + 110, HEIGHT - 80  # Réinitialiser la position du joueur
                enemy_x, enemy_y = (3 * WIDTH) // 4 -160, HEIGHT - 80  # Réinitialiser la position de l'ennemi
            if winner and restart_button.collidepoint(event.pos):  # Si "Restart" est cliqué après une course
                race_started = False  # Réinitialiser la course
                winner = None  # Effacer le gagnant
    
    if not race_started:  # Si la course n'a pas commencé
        pygame.draw.rect(screen, RED, go_button)  # Dessiner le bouton "GO"
        text = font.render("GO", True, WHITE)
        screen.blit(text, (go_button.x + 25, go_button.y + 10))
    else:
        if winner is None:  # Si la course est en cours
            keys = pygame.key.get_pressed()  # Vérifier les touches pressées
            if keys[pygame.K_LEFT] and player_x > WIDTH // 3:
                player_x -= player_speed  # Déplacer la voiture à gauche
            if keys[pygame.K_RIGHT] and player_x < 2 * WIDTH // 3 - player_CAR_WIDTH:
                player_x += player_speed  # Déplacer la voiture à droite
            if keys[pygame.K_UP] and player_y > 0:
                player_y -= player_speed  # Avancer
            if keys[pygame.K_DOWN] and player_y < HEIGHT - player_CAR_HEIGHT:
                player_y += player_speed  # Reculer
            
            enemy_y -= enemy_speed  # Faire avancer l'ennemi automatiquement
            
            if player_y <= 50:  # Vérifier si le joueur a gagné
                winner = "Joueur"
            if enemy_y <= 50:  # Vérifier si l'ennemi a gagné
                winner = "Ennemi"
        
        screen.blit(player_car, (player_x, player_y))  # Dessiner la voiture du joueur
        screen.blit(enemy_car, (enemy_x, enemy_y))  # Dessiner la voiture ennemie
        
        if winner:  # Si la course est terminée
            text = font.render(f"{winner} Gagne!", True, BLACK)
            screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))  # Afficher le gagnant
            pygame.draw.rect(screen, BLUE, restart_button)  # Dessiner le bouton "Restart"
            restart_text = font.render("Restart", True, WHITE)
            screen.blit(restart_text, (restart_button.x + 10, restart_button.y + 10))
    
    pygame.display.update()  # Mettre à jour l'écran
    clock.tick(30)  # Limiter la vitesse du jeu

pygame.quit()  # Quitter pygame
