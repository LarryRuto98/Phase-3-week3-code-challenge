from CAL.db_connection import fetch_one

class Concert:
    @staticmethod
    def band(concert_id):
        query = "SELECT * FROM bands WHERE id = (SELECT band_id FROM concerts WHERE id = ?);"
        return fetch_one(query, (concert_id,))

    @staticmethod
    def venue(concert_id):
        query = "SELECT * FROM venues WHERE id = (SELECT venue_id FROM concerts WHERE id = ?);"
        return fetch_one(query, (concert_id,))

    @staticmethod
    def hometown_show(concert_id):
        query = """
            SELECT CASE 
                WHEN (SELECT hometown FROM bands WHERE id = concerts.band_id) = 
                     (SELECT city FROM venues WHERE id = concerts.venue_id) 
                THEN 1 ELSE 0 END 
            FROM concerts WHERE id = ?;
        """
        return fetch_one(query, (concert_id,))[0] == 1

    @staticmethod
    def introduction(concert_id):
        query = """
            SELECT 'Hello ' || v.city || '!!!!! We are ' || b.name || ' and we\'re from ' || b.hometown 
            FROM concerts c
            JOIN bands b ON c.band_id = b.id
            JOIN venues v ON c.venue_id = v.id
            WHERE c.id = ?;
        """
        return fetch_one(query, (concert_id,))[0]
