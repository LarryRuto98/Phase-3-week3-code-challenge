from CAL.db_connection import fetch_all, fetch_one

class Venue:
    @staticmethod
    def concerts(venue_id):
        query = "SELECT * FROM concerts WHERE venue_id = ?;"
        return fetch_all(query, (venue_id,))

    @staticmethod
    def bands(venue_id):
        query = """
            SELECT DISTINCT b.* 
            FROM bands b
            JOIN concerts c ON b.id = c.band_id
            WHERE c.venue_id = ?;
        """
        return fetch_all(query, (venue_id,))

    @staticmethod
    def concert_on(venue_id, date):
        query = "SELECT * FROM concerts WHERE venue_id = ? AND date = ? LIMIT 1;"
        return fetch_one(query, (venue_id, date))

    @staticmethod
    def most_frequent_band(venue_id):
        query = """
            SELECT b.*, COUNT(c.id) AS performance_count 
            FROM bands b
            JOIN concerts c ON b.id = c.band_id
            WHERE c.venue_id = ?
            GROUP BY b.id
            ORDER BY performance_count DESC
            LIMIT 1;
        """
        return fetch_one(query)
