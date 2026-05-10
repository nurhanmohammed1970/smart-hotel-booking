from abc import ABC, abstractmethod

# ================== Requirement 1: Blueprint ==================
class BookableItem(ABC):
    def __init__(self, item_id, name, base_price):
        self._item_id = item_id
        self._name = name
        self.__base_price = base_price  # protected

    def get_price(self):
        return self.__base_price

    def set_price(self, price):
        if price > 0:
            self.__base_price = price
        else:
            print("Invalid price!")

    def get_name(self):
        return self._name

    def get_id(self):
        return self._item_id

    @abstractmethod
    def calculate_item_cost(self):
        pass

    @abstractmethod
    def display_details(self):
        pass


# ================== Requirement 2: Specialization ==================
class Room(BookableItem):
    def __init__(self, item_id, name, base_price, bed_size):
        super().__init__(item_id, name, base_price)
        self.bed_size = bed_size

    def calculate_item_cost(self):
        return self.get_price() * 1.15  # 15% tax

    def display_details(self):
        print(f"[{self.get_id()}] Room: {self.get_name()} | Bed: {self.bed_size} | Price: {self.get_price()}")


class Service(BookableItem):
    def __init__(self, item_id, name, base_price, duration):
        super().__init__(item_id, name, base_price)
        self.duration = duration

    def calculate_item_cost(self):
        return self.get_price() * 1.20  # 20% gratuity

    def display_details(self):
        print(f"[{self.get_id()}] Service: {self.get_name()} | Duration: {self.duration} mins | Price: {self.get_price()}")


# ================== Requirement 4: Smart Reservation ==================
class CustomerReservation:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print("Item added successfully!")

    def view_reservation(self):
        if not self.items:
            print("Reservation is empty.")
            return
        for item in self.items:
            item.display_details()

    def print_bill(self):
        if not self.items:
            print("No items to bill.")
            return

        total = 0
        print("\n===== FINAL BILL =====")
        for item in self.items:
            cost = item.calculate_item_cost()
            print(f"{item.get_name()} -> {cost:.2f}")
            total += cost

        print("----------------------")
        print(f"TOTAL: {total:.2f}")
        print("======================\n")


# ================== Data ==================
items = [
    Room(1, "Deluxe Room", 1000, "King"),
    Room(2, "Standard Room", 600, "Queen"),
    Service(3, "Spa Session", 300, 60),
    Service(4, "Dinner Buffet", 250, 90)
]

reservation = CustomerReservation()


# ================== Requirement 5: Terminal ==================
def show_menu():
    print("\n===== HOTEL SYSTEM =====")
    print("1. View Offerings")
    print("2. Add to Reservation")
    print("3. View Reservation")
    print("4. Print Final Bill")
    print("5. Exit")


while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        for item in items:
            item.display_details()

    elif choice == "2":
        try:
            item_id = int(input("Enter item ID: "))
            found = False
            for item in items:
                if item.get_id() == item_id:
                    reservation.add_item(item)
                    found = True
                    break
            if not found:
                print("Item not found.")
        except:
            print("Invalid input!")

    elif choice == "3":
        reservation.view_reservation()

    elif choice == "4":
        reservation.print_bill()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")