from game.EnemyShoot import EnemyShoot
from game.Const import WIN_WIDTH
from game.Enemy import Enemy
from game.Entity import Entity
from game.Player import Player
from game.PlayerShoot import PlayerShoot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        # Destrói Inimigos e Tiros Inimigos que saem pela ESQUERDA
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0

        # Destrói Tiros do Player que saem pela DIREITA
        if isinstance(ent, EnemyShoot):
            if ent.rect.right <= 0:
                ent.health = 0

        if isinstance(ent, PlayerShoot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        pass

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        # Tiro do Player acertando Inimigo (ou vice-versa)
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShoot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShoot) and isinstance(ent2, Enemy):
            valid_interaction = True

        # Tiro do Inimigo acertando o Player
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShoot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShoot) and isinstance(ent2, Player):
            valid_interaction = True

        # Player colidindo com o Inimigo (Batida de frente)
        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_interaction = True

        # 2. Se a interação é válida, checamos a matemática da colisão
        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                # 1. Aplica o dano (Números)
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage

                # 2. Registra a "Assinatura" de quem causou o dano (Strings)
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shoot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'Player2Shoot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        # Comparamos todos contra todos, sem repetir pares
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i+ 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)


    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for i in entity_list[:]:
            if i.health <= 0:
                if isinstance(i, Enemy):
                    EntityMediator.__give_score(i, entity_list)
                entity_list.remove(i)