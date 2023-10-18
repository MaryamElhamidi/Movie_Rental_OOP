import movieStore

class MovieRentalApp:
    def run(self):
        return print(" Welcome to Maryam's Movie Rental Store")
    
    def setup(self):
        return print("Project Setup Complete.")
    
"""1. (8 Points) Create an object of the "MovieStore" class by accepting the required data from the end- user.
2. (2 Points) Print the details of the movie store, including the store name, total number of movies, rental fee per movie, and late fee per day.
Commit the changes done so far, with a message “Created instance of MovieStore”
3. (8 Points) Ask the user if they wish to rent or return movies.
a. For renting, accept the number of movies to rent and update the available movies. Display the total fee due if renting was successful. If renting is not successful display, show an appropriate error message.
b. For returning, accept the number of movies returned, and if any movies returns are overdue, calculate and display the late fee.
4. (2 Points) Update the movie rental fee to 75% of the original price.
Commit the changes done so far, with a message “User interaction implemented.”"""

user1 = ("maryam", 40, 15, 2.99, 0.99)
#Bonus
class Bonus:
    def userList(self):
        return
"""present a menu to the user with three options of 
renting movies, return movies, calculating late fees, 
and exiting"""
