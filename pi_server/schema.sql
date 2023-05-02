-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS inventory;

CREATE TABLE inventory (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  item_name TEXT UNIQUE NOT NULL,
  container TEXT NOT NULL,
  tags TEXT
);