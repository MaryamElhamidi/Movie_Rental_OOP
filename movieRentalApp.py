from movieStore import MovieStore
class MovieRentalApp:
    def run():
        return print("Welcome to Maryam's Movie Rental Store")

# an object of the "MovieStore" class

print(MovieRentalApp.run())
customer_1 = MovieStore("maryam", 40, 15, 2.99, 0.99)
name = customer_1.getName()
print(f"The name of the store is: {name}")
movie_number = customer_1.getMovNum
print(f"Movies orignial count: {movie_number}")
update_movie = customer_1.getAvailMov
print(f"Available movies to rent: {update_movie}")
rent_fee = customer_1.getRentFee
print(f"This is the rent fee: {rent_fee}")
late_fee = customer_1.getLateFee
print(f"This is the late fee per day: {late_fee}")


user = input("Do you wish to rent or return movies?: (rent/return)").lower
if user == 'rent':
    print(customer_1.rentMovie)
else:
    print(customer_1.returnMovie())

customer_1 = MovieStore("maryam", 40, 15, 5.2325, 0.99)

#Bonus

class Bonus:
    welcome = input("Would you like to be presentended with a menu of three options' (yes/no): ").lower()
    if welcome == "yes":
        print("1. Rent Movies")
        print("2. Return Movies")
        print("3. Calculate Late Fees")
        print("4. Exit")
        choice = input("Pick from options 1,2,3,4: ")
        if choice == 1:
            print(customer_1.rentMovie())
        elif choice == 2:
            print(customer_1.returnMovie())
        elif choice == 3:
            print(customer_1.calculateLateFee)
        else:
            print("Goodbye.")
    else: 
        print("Ok. See you another time.")