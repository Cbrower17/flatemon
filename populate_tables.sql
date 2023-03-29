INSERT INTO Pokedex (name, maxhp, attack,defence,speed,type) VALUES ('Bulbasaur',45,49,49,45,'Grass');
INSERT INTO Pokedex (name, maxhp, attack,defence,speed,type) VALUES ('Ivysaur',60,62,63,60,'Grass');
INSERT INTO Pokedex (name, maxhp, attack,defence,speed,type) VALUES ('Venusaur',80,82,83,80,'Grass');
INSERT INTO Pokedex (name, maxhp, attack,defence,speed,type) VALUES ('Charmander',39,52,43,65,'Fire');
INSERT INTO Pokedex (name, maxhp, attack,defence,speed,type) VALUES ('Charmeleon',58,64,58,80,'Fire');
INSERT INTO Pokedex (name, maxhp, attack,defence,speed,type) VALUES ('Charizard',78,84,78,100,'Fire');
INSERT INTO Pokedex (name, maxhp, attack,defence,speed,type) VALUES ('Squirtle',44,48,65,43,'Water');
INSERT INTO Pokedex (name, maxhp, attack,defence,speed,type) VALUES ('Wartortle',59,63,80,58,'Water');
INSERT INTO Pokedex (name, maxhp, attack,defence,speed,type) VALUES ('Blastoise',79,83,100,78,'Water');

INSERT INTO Move (move_name, move_type, damage, max_pp) VALUES ("Tackle","normal",40,35);
INSERT INTO Move (move_name, move_type, damage, max_pp) VALUES ('Bubble','water',40,25);
INSERT INTO Move (move_name, move_type, damage, max_pp) VALUES ('Ember','fire',40,25);
INSERT INTO Move (move_name, move_type, damage, max_pp) VALUES ('Vine Whip','grass',45,10);
INSERT INTO Move (move_name, move_type, damage, max_pp) VALUES ('Solar Beam','grass',120,5);
INSERT INTO Move (move_name, move_type, damage, max_pp) VALUES ('Fire Blast','fire',110,15);
INSERT INTO Move (move_name, move_type, damage, max_pp) VALUES ('Surf','water',90,10);
INSERT INTO Move (move_name, move_type, damage, max_pp) VALUES ('Thrash','normal',120,10);

INSERT INTO Trainer (name) VALUES ('Craig');
INSERT INTO Trainer (name) VALUES ('Shawn');

INSERT INTO MoveSet (move_1_id, move_2_id,move_3_id,move_4_id) VALUES (1,2,3,4);

INSERT INTO Pokemon (nickname, p_id, remaining_hp, trainer_id, move_set_id) VALUES ("Nick",1, 45, 1, 1);

INSERT INTO party (trainer_id) VALUES (1);

INSERT INTO Poke_Party (party_id, pokemon_id) VALUES (1,1);

INSERT INTO Pokemon_Party (pokemon_id, trainer_id) VALUES (1,1);