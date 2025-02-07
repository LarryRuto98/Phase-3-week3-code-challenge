CREATE TABLE IF NOT EXISTS concerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    band_id INTEGER NOT NULL,
    venue_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (band_id) REFERENCES bands (id),
    FOREIGN KEY (venue_id) REFERENCES venues (id)
);
