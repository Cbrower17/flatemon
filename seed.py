import sqlite3

# Connect to the database
conn = sqlite3.connect('pokemon.db')

# Create tables
conn.execute('''
CREATE TABLE Trainer (
  id INTEGER PRIMARY KEY,
  name TEXT
);
''')

conn.execute('''
CREATE TABLE Pokedex (
  id INTEGER PRIMARY KEY,
  name TEXT,
  maxhp INTEGER,
  attack INTEGER,
  defence INTEGER,
  speed INTEGER,
  type TEXT
);
''')

# conn.execute('''
# CREATE TABLE Pokemon_Party (
#   id INTEGER PRIMARY KEY,
#   pokemon_id INTEGER,
#   trainer_id INTEGER,
#   FOREIGN KEY(pokemon_id) REFERENCES Pokemon(id),
#   FOREIGN KEY(trainer_id) REFERENCES Trainer(id)
# );
# ''')
conn.execute('''
CREATE TABLE party (
  id INTEGER PRIMARY KEY,
  trainer_id INTEGER,
  FOREIGN KEY(trainer_id) REFERENCES Trainer(id)
);
''')

conn.execute('''
CREATE TABLE Poke_Party (
  id INTEGER PRIMARY KEY,
  party_id INTEGER,
  pokemon_id INTEGER,
  FOREIGN KEY(party_id) REFERENCES party(id),
  FOREIGN KEY(pokemon_id) REFERENCES Pokemon(id)
);
''')


conn.execute('''
CREATE TABLE Pokemon (
  id INTEGER PRIMARY KEY,
  nickname TEXT,
  p_id INTEGER,
  remaining_hp INTEGER,
  trainer_id INTEGER,
  move_set_id INTEGER,
  FOREIGN KEY(p_id) REFERENCES Pokedex(id),
  FOREIGN KEY(trainer_id) REFERENCES Trainer(id),
  FOREIGN KEY(move_set_id) REFERENCES MoveSet(id)
);
''')

conn.execute('''
CREATE TABLE MoveSet (
  id INTEGER PRIMARY KEY,
  move_1_id INTEGER,
  move_2_id INTEGER,
  move_3_id INTEGER,
  move_4_id INTEGER,
  FOREIGN KEY(move_1_id) REFERENCES Move(id),
  FOREIGN KEY(move_2_id) REFERENCES Move(id),
  FOREIGN KEY(move_3_id) REFERENCES Move(id),
  FOREIGN KEY(move_4_id) REFERENCES Move(id)
);
''')

conn.execute('''
CREATE TABLE Move (
  id INTEGER PRIMARY KEY,
  move_name TEXT,
  damage INTEGER,
  move_type TEXT,
  max_pp INTEGER
);
''')

# Commit the changes
conn.commit()

# Close the connection
conn.close()

