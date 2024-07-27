# Create a class for the hotel data
class Hotel:
    sortParam='name'
    def __init__(self) -> None:
        self.name = ''
        self.roomAvl = 0
        self.location = ''
        self.rating = int
        self.pricePr = 0
        
    def __lt__(self, other):
        getattr(self, Hotel.sortParam)<getattr(other, Hotel.sortParam)
    
    @classmethod
    def sortByName(self):
        self.sortParam = 'name'
    
    @classmethod
    def sortByRate(self):
        self.sortParam = 'rating'
    
    @classmethod    
    def sortByRoomAvailable(self):
        self.sortParam = 'roomAvl'
        
    def __repr__(self) -> str:
        return "HOTELS DATA:\nHotel Name: {}\nRoom Available: {}\nLocation: {}\nRating: {}\nPrice Per Room: {}".format(self.name, self.roomAvl, self.location, self.rating, self.pricePr)
    
class User:
    def __init__(self) -> None:
        self.uname = ''
        self.uid = 0
        self.cost = 0
        
    def __repr__(self) -> str:
        return "Username: {}\tUser ID: {}\tBooking Cost:{}".format(self.uname, self.uid, self.cost)
    
def PrintHotelData(hotels):
    for hotel in hotels:
        print(hotel)
        
# Sort Hotels by name
def SortHotelByName(hotels):
    print("SORT BY NAME:")
    
    Hotel.sortByName()
    hotels.sort()
    
    PrintHotelData(hotels)
    print()
    
# Sort Hotels by rating
def SortHotelByRating(hotels):
    print("SORT BY A RATING:")
 
    Hotel.sortByRate()
    hotels.sort()
     
    PrintHotelData(hotels)
    print()
    
def PrintHotelByCity(s, hotels):
    print("HOTELS FOR {} LOCATION ARE:".format(s))
    hotelByLoc = [hotel for hotel in hotels if hotel.location == s]
    
    PrintHotelData(hotelByLoc)
    print()
    
def SortByRoomAvailable(hotels):
    print("ROOM AVAILABLE IN EACH HOTEL:")
    Hotel.sortByRoomAvailable()
    
def PrintUserData(lusers):
    users = []
    for i in range(len(lusers)):
        user = User()
        user.uname = lusers[i]['userName']
        user.uid = lusers[i]['userId']
        
        users.append(user)
        
    for user in users:
        print(user)
    
def HotelManagement(lusers, lhotels):
    hotels = []
    
    for i in range(len(lhotels)):
        hotel = Hotel()
        hotel.name = lhotels[i]["hotelName"]
        hotel.roomAvl = lhotels[i]["rooms"]
        hotel.location = lhotels[i]["location"]
        hotel.rating = lhotels[i]["rating"]
        hotel.pricePr = lhotels[i]["price"]
        
        hotels.append(hotel)
    
    PrintHotelData(hotels)
    SortHotelByName(hotels)
    SortHotelByRating(hotels)
    PrintHotelByCity("Las Vegas", hotels)
    SortByRoomAvailable(hotels)
    PrintUserData(lusers)
    
if __name__ == "__main__":
    users = [{"userId": 2003, "userName": "Tom holland"},
            {"userId": 2004, "userName": "Richard Wingsklet"},
            {"userId": 2005, "userName": "Alric Saltzman"}]
    
    hotels = [{"hotelName": "Hotel Orion", "rooms": 65, "location": "Las Vegas", "rating": 5, "price":230},
              {"hotelName": "Hotel Lagoon", "rooms": 50, "location": "Los Angeles", "rating": 5, "price": 380},
              {"hotelName": "Westland Hotel", "rooms": 72, "location": "New Jersey", "rating": 4, "price": 210}]
    
    HotelManagement(users, hotels)