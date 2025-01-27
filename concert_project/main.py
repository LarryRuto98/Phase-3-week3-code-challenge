from model_files.band import Band
from model_files.venue import Venue
from model_files.concert import Concert

def main():
    print("Welcome to the Concert Tracker!")
    
    while True:
        print("\nChoose an option:")
        print("1. View all concerts for a band")
        print("2. View all venues for a band")
        print("3. Add a concert")
        print("4. Find the band with the most performances")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            band_id = int(input("Enter Band ID: "))
            print(Band.concerts(band_id))
        elif choice == "2":
            band_id = int(input("Enter Band ID: "))
            print(Band.venues(band_id))
        elif choice == "3":
            band_id = int(input("Enter Band ID: "))
            venue_title = input("Enter Venue Title: ").strip()
            date = input("Enter Date (YYYY-MM-DD): ").strip()
            Band.play_in_venue(band_id, venue_title, date)
            print("Concert added successfully!")
        elif choice == "4":
            print("Band with most performances:", Band.most_performances())
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
