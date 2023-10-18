class MovieStore:
#Part 2.1 Creating initializer
    def __init__(self, name, num_movie, avail_movies, rent_fee, late_fee):
        self.__self = self
        self.name = name
        self.num_movie = num_movie
        self.avail_movies = avail_movies
        self.rent_fee = rent_fee
        self.late_fee = late_fee
#Part 2.2 Define accessors and mutators
    def getName(self):
        return self.name
    def getMovNum(self):
        return self.num_movie
    def getAvailMov(self):
        return self.avail_movies
    def getRentFee(self):
        return self.rent_fee
    def getLateFee(self):
        return self.late_fee    
    

    def setRentFee(self):
        if self.rent_fee < 0:
            return print("Rejected: Invalid Fee")
        
    def calculateLateFee(self):
        days_overdue = float(input("Enter the number of days the movie is overdue: "))
        lateFee_Overdue = self.late_fee * days_overdue
        return print(f"The calculated late fee is {lateFee_Overdue()}")
   
    def rentMovie(self):
        selection = int(input("Request a number of movies: "))
        if selection > self.avail_movies:
            print("Invalid. The requested number of movies is greater than the available movies.")
            return False
        else:
            update = self.avail_movies - selection
            print("The updated number of available movies is: ", update)
            return True

    def returnMovie(self):
        movie_returns = input("Enter the amount of movies you are returning: ")
        new_avail_movies = movie_returns + self.avail_movies
        days_overdue = float(input("Enter the number of days the movie is overdue: "))
        lateFee_Overdue = self.late_fee * days_overdue
        if days_overdue > 0:
            print("Please pay your late fee. It is: ",lateFee_Overdue)
        else:
            print("Thank you. See you again.")