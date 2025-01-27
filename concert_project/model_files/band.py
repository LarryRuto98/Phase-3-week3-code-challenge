from CAL.db_connection import execute_query, fetch_all, fetch_one

class Band:
    @staticmethod
    def concerts(band_id):
        query = "SELECT * FROM concerts WHERE band_id = ?;"
        return fetch_all(query, (band_id,))

    @staticmethod
    def venues(band_id):
        query = """
            SELECT DISTINCT v.* 
            FROM venues v
            JOIN concerts c ON v.id = c.venue_id
            WHERE c.band_id = ?;
        """
        return fetch_all(query, (band_id,))

    @staticmethod
    def play_in_venue(band_id, venue_title, date):
        # Check if the venue exists
        venue_query = "SELECT id FROM venues WHERE title = ?"
        venue = fetch_one(venue_query, (venue_title,))
        
        if not venue:
            print(f"The venue '{venue_title}' does not exist.")
            city = input(f"Enter the city for the new venue '{venue_title}': ").strip()
            
            # Insert the new venue
            insert_venue_query = "INSERT INTO venues (title, city) VALUES (?, ?)"
            execute_query(insert_venue_query, (venue_title, city))
            
            # Fetch the new venue ID
            venue = fetch_one(venue_query, (venue_title,))
            print(f"Venue '{venue_title}' in '{city}' has been added to the database.")
        
        venue_id = venue['id']
        
        # Insert the new concert
        insert_concert_query = "INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)"
        execute_query(insert_concert_query, (band_id, venue_id, date))
        print(f"Concert for Band ID {band_id} at Venue '{venue_title}' on {date} has been added to the database.")
    @staticmethod
    def all_introductions(band_id):
        query = """
            SELECT 'Hello ' || v.city || '!!!!! We are ' || b.name || ' and we\'re from ' || b.hometown 
            FROM concerts c
            JOIN bands b ON c.band_id = b.id
            JOIN venues v ON c.venue_id = v.id
            WHERE c.band_id = ?;
        """
        return [row[0] for row in fetch_all(query, (band_id,))]

    @staticmethod
    def most_performances():
        query = """
            SELECT b.*, COUNT(c.id) AS concert_count 
            FROM bands b
            JOIN concerts c ON b.id = c.band_id
            GROUP BY b.id
            ORDER BY concert_count DESC
            LIMIT 1;
        """
        return fetch_one(query)
