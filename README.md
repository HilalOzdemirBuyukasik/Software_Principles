Software Principles: DRY, WET, SOC, SRP, OCP, LSP

This project demonstrates key software engineering principles in Python, including DRY (Don't Repeat Yourself), WET (Write Everything Twice), SOC (Separation of Concerns), and SRP (Single Responsibility Principle). 
The code includes examples of discount price calculation and user registration, showcasing how these principles can be applied in real-world scenarios.

WET: The code for calculating the areas of a rectangle and a square is repeated. Separate functions are written for each, even though they share similar logic, demonstrating the WET (Write Everything Twice) principle.

SRP: The user registration process is divided into functions, each handling a single task. For example, one function validates the username, another checks the password strength, and a third adds the user to the database, adhering to the SRP (Single Responsibility Principle).

SOC: The responsibilities for retrieving user data and displaying it are separated into distinct functions. One function gathers the user details, while the other function is responsible for displaying this data, reflecting the SOC (Separation of Concerns) principle.

DRY: The discount calculation logic is abstracted into a single function and reused across multiple products, avoiding repetition and following the DRY (Don't Repeat Yourself) principle.

Each of these principles is demonstrated through practical examples, such as calculating discounted prices and handling user registrations, showing how they help create cleaner and more maintainable code.

OCP: The Open-Closed Principle is demonstrated through a shape area calculation system. An abstract Shape class defines the interface, while concrete classes like Circle and Square implement their own area methods. The AreaCalculator class calculates the area without knowing the specific type of shape, and without needing modification when new shapes are added. This showcases how code can be open for extension but closed for modification, following the OCP principle.

LSP: The Liskov Substitution Principle is demonstrated through a bird sound generation system. The Bird class is the base class, and the Sparrow and Duck classes are derived from it. The play_bird_sound function can accept any object of the Bird class, and both the Sparrow and Duck classes can replace the Bird class without affecting the behavior of the program. This ensures that the program remains correct and behaves as expected, no matter which subclass is used.
