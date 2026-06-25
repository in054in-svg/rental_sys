# README - Car Agency Management System (Sale and Rent)

## General Description
This system is made to manage a car agency in a smart and easy way. The system supports two main things: selling cars and renting cars. It tracks the car inventory (available, rented, for sale), customer details, and provides an organized workflow for every action in the agency.

## System Structure (UML Classes)
The system uses Object-Oriented Programming (OOP) and includes these classes:

### 1. `Company` Class
The main class that runs the system and controls all activities.
*   **Attributes:**
    *   `name` (str): The name of the car agency.
    *   `inventory_sale` (dict): A dictionary with cars available for sale (`Sale_car` objects).
    *   `inventory_rental` (dict): A dictionary with cars available for rent (`Rental_car` objects).
    *   `inventory_rental_not_available` (dict): A dictionary with cars that are currently rented out (with customers).
*   **Main Methods:**
    *   `enter_inv_r()` / `enter_inv_s()`: Adds new cars to the rent and sale inventory.
    *   `rental_process()`: Manages the full car rental process.
    *   `return_car()`: Manages the process of getting a car back from a customer.
    *   `sale_process()`: Manages the full car sale process.
    *   `welcome()`: A welcome message.

### 2. `Customer` Class
Represents a user or customer in the system.
*   **Attributes:** `name`, `id_` (ID number), `age`, `tel` (telephone number).

### 3. `Car` Class (Parent Class)
The base class that has all the basic attributes and methods for all types of cars.
*   **Attributes:** `id_` (unique ID), `manufacturer`, `model`, `year`, `color`, `price`, `size` (large/small), `status` (availability status), `mile` (current mileage).

### 4. `Rental_car` Class
Inherits from the `Car` class. Adds specific attributes for renting.
*   **Special Attributes:** 
    *   `renter`: Saves a link to the `Customer` object who rents the car.
    *   `days_rent`: Number of rental days.
    *   `day_price`: Daily price.
    *   `mile_req`: The requested mileage limit.
    *   `mile_default`: The default daily mileage limit (300).
*   **Special Methods:** `calc_p(check_mile())` to calculate the final rental price (including extra miles), and `update_mile()` to update the mileage when the car is returned.

### 5. `Sale_car` Class
Inherits from the `Car` class. Made specifically for cars that are for sale.
*   **Special Attributes:** `sale_price` which sets the sale price (this might be affected by the `if_status()` function).

---

## System Workflows (Flowcharts)

### Startup and Login (Main Flowchart)
1. Create a `Company` object and enter the agency name.
2. Load data and fill the dictionaries with sale and rent cars.
3. Start the "WELCOME" mechanism to greet the customer.
4. The system asks the customer: Do you want a car **for sale** or **for rent**? The process continues based on their choice.

### 🚗 Renting and Returning a Car Process
**Renting Stage:**
1. The customer is asked about what they want: they choose the **car size** (small/large) and then the requested **manufacturer**.
2. The system shows the available cars that match the request, along with the price.
3. The customer chooses a specific car from the list.
4. **Internal Update:**
   * The customer object (`renter`) is updated inside the car object.
   * The car is moved from the available cars dictionary (`inventory_rental`) to the rented cars dictionary (`inventory_rental_not_available`).

**Returning Stage:**
1. When the car is received back from the customer, the return process happens (`return_car`).
2. The car is moved back from the rented cars dictionary to the available cars dictionary.
3. The renter field in the car is cleared (`renter = null`) to make it ready for the next person.

### 💰 Car Sale Process
1. The customer chooses the desired **car size**.
2. The customer chooses the **car manufacturer**.
3. The system shows the customer the options available in the sale inventory and their prices.
4. The customer selects the car they want to buy.
5. The purchase process happens, and the car is **deleted** from the available sale cars dictionary (`inventory_sale`).
