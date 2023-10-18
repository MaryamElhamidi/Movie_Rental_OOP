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

