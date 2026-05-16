import math

class Category:
    """
    Represents a single budget category.
    Demonstrates OOP: Encapsulation of data (ledger) and behavior (methods).
    """
    def __init__(self, name):
        # Instance attributes define the state of each object
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        """Records a positive transaction in the ledger."""
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """
        Records a negative transaction if funds are available.
        Returns True if successful, False otherwise.
        """
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """Returns the current total balance of the category."""
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, other_category):
        """
        Moves money from this category to another instance of Category.
        Demonstrates interaction between different objects.
        """
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        """Helper method to check if a specific amount can be withdrawn."""
        return amount <= self.get_balance()

    def __str__(self):
        """
        Custom string representation of the object.
        Demonstrates manual string formatting and alignment.
        """
        # Create centered title line
        res = self.name.center(30, "*") + "\n"
        
        # Format each ledger entry
        for entry in self.ledger:
            description = entry["description"][:23].ljust(23)
            amount = "{:.2f}".format(entry["amount"]).rjust(7)
            res += f"{description}{amount}\n"
            
        res += f"Total: {self.get_balance():.2f}"
        return res

def create_spend_chart(categories):
    """
    Standalone function to create a bar chart from a list of Category objects.
    Shows the percentage of total spending per category.
    """
    # Calculate spending per category (ignore deposits)
    spent_list = []
    for cat in categories:
        spent = sum(abs(i["amount"]) for i in cat.ledger if i["amount"] < 0)
        spent_list.append(spent)
    
    total_spent = sum(spent_list)
    
    # Calculate percentages (rounded down to nearest 10)
    # Using integer math for floor rounding
    percs = [int((s / total_spent) * 10) * 10 for s in spent_list]

    chart = "Percentage spent by category\n"
    
    # Build y-axis and bars
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for p in percs:
            chart += "o  " if p >= i else "   "
        chart += "\n"

    # Add separator line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Build vertical labels for x-axis
    max_len = max(len(c.name) for c in categories)
    for i in range(max_len):
        chart += "     "
        for cat in categories:
            if i < len(cat.name):
                chart += f"{cat.name[i]}  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"

    return chart