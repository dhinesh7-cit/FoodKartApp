class Restaurant:
    def __init__(self, phone, name):
        self.phone = phone
        self.name = name
        self.dish = None
        self.ratings = []
    
    def add_dish(self, dish):
        self.dish = dish
        print(f"Dish '{dish}' added to restaurant '{self.name}'.")

    def get_dish(self):
        return self.dish
    
    def rate(self, rating):
        self.ratings.append(rating)
    
    def get_average_rating(self):
        if self.ratings:
            return sum(self.ratings) / len(self.ratings)
        return None


class Customer:
    def __init__(self, phone, name):
        self.phone = phone
        self.name = name
        self.order_history = []
    
    def place_order(self, restaurant, quantity):
        if restaurant.dish:
            print(f"Order placed for {quantity}x '{restaurant.dish}' from '{restaurant.name}'.")
            self.order_history.append((restaurant.name, restaurant.dish, quantity))
        else:
            print(f"Restaurant '{restaurant.name}' has no dish available.")
    
    def view_order_history(self):
        if not self.order_history:
            print("No order history yet.")
        else:
            print("Order History:")
            for i, (rest, dish, quantity) in enumerate(self.order_history, 1):
                print(f"{i}. {quantity}x {dish} from {rest}")

    def rate_restaurant(self, restaurant):
        rating = int(input(f"How would you rate '{restaurant.name}' out of 5? "))
        if 1 <= rating <= 5:
            restaurant.rate(rating)
            print(f"Thanks for rating '{restaurant.name}'!")
        else:
            print("Invalid rating. Please give a rating between 1 and 5.")


class FoodKart:
    def __init__(self):
        self.restaurants = {}
        self.customers = {}

    def register_restaurant(self):
        print("\n--- Restaurant Registration ---")
        phone = input("Enter restaurant phone number: ")
        if phone in self.restaurants:
            print("Restaurant already registered.")
            return
        name = input("Enter restaurant name: ")
        restaurant = Restaurant(phone, name)
        dish = input("Enter the dish served by the restaurant: ")
        restaurant.add_dish(dish)
        self.restaurants[phone] = restaurant
        print(f"Restaurant '{name}' registered successfully.")

    def register_customer(self):
        print("\n--- Customer Registration ---")
        phone = input("Enter customer phone number: ")
        if phone in self.customers:
            print("Customer already registered.")
            return
        name = input("Enter customer name: ")
        customer = Customer(phone, name)
        self.customers[phone] = customer
        print(f"Welcome, {name}! You're now registered.")

    def login_restaurant(self):
        print("\n--- Restaurant Login ---")
        phone = input("Enter restaurant phone number: ")
        if phone in self.restaurants:
            return self.restaurants[phone]
        else:
            print("Restaurant not found. Please register first.")
            return None

    def login_customer(self):
        print("\n--- Customer Login ---")
        phone = input("Enter customer phone number: ")
        if phone in self.customers:
            return self.customers[phone]
        else:
            print("Customer not found. Please register first.")
            return None

    def show_restaurants(self):
        if not self.restaurants:
            print("No restaurants available.")
        else:
            print("Available Restaurants:")
            for i, restaurant in enumerate(self.restaurants.values(), 1):
                avg_rating = restaurant.get_average_rating()
                rating_text = f" - Avg Rating: {avg_rating:.1f}/5" if avg_rating else " - No ratings yet"
                print(f"{i}. {restaurant.name} - {restaurant.dish}{rating_text}")

    def main(self):
        print("Welcome to FoodKart!")
        while True:
            print("\n--- Main Menu ---")
            print("1. Register as Restaurant")
            print("2. Register as Customer")
            print("3. Login as Restaurant")
            print("4. Login as Customer")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.register_restaurant()
            elif choice == "2":
                self.register_customer()
            elif choice == "3":
                restaurant = self.login_restaurant()
                if restaurant:
                    print(f"Welcome, {restaurant.name}!")
                    while True:
                        print("\n--- Restaurant Dashboard ---")
                        print("1. View Dish")
                        print("2. Logout")
                        r_choice = input("Choose an option: ")
                        if r_choice == "1":
                            print(f"Your dish: {restaurant.get_dish()}")
                        elif r_choice == "2":
                            print("Logging out...")
                            break
                        else:
                            print("Invalid option. Try again.")
            elif choice == "4":
                customer = self.login_customer()
                if customer:
                    print(f"Welcome, {customer.name}!")
                    while True:
                        print("\n--- Customer Dashboard ---")
                        print("1. Browse Restaurants")
                        print("2. Place an Order")
                        print("3. View Order History")
                        print("4. Rate a Restaurant")
                        print("5. Logout")
                        c_choice = input("Choose an option: ")

                        if c_choice == "1":
                            self.show_restaurants()
                        elif c_choice == "2":
                            self.show_restaurants()
                            rest_index = int(input("Enter the restaurant number to order from: ")) - 1
                            if 0 <= rest_index < len(self.restaurants):
                                restaurant = list(self.restaurants.values())[rest_index]
                                quantity = int(input(f"Enter the quantity for '{restaurant.dish}': "))
                                customer.place_order(restaurant, quantity)
                            else:
                                print("Invalid restaurant number.")
                        elif c_choice == "3":
                            customer.view_order_history()
                        elif c_choice == "4":
                            self.show_restaurants()
                            rest_index = int(input("Enter the restaurant number to rate: ")) - 1
                            if 0 <= rest_index < len(self.restaurants):
                                restaurant = list(self.restaurants.values())[rest_index]
                                customer.rate_restaurant(restaurant)
                            else:
                                print("Invalid restaurant number.")
                        elif c_choice == "5":
                            print("Logging out...")
                            break
                        else:
                            print("Invalid option.")
            elif choice == "5":
                print("Thank you for using FoodKart. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    app = FoodKart()
    app.main()
