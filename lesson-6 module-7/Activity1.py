# Import tkinter for GUI
import tkinter as tk
from tkinter import ttk, messagebox

# Import Pillow for handling images
from PIL import Image, ImageTk


# Define the RestaurantOrderManagement class
class RestaurantOrderManagement:

    # Initialize the application
    def __init__(self, root):

        self.root = root
        self.root.title("Restaurant Management App")

        # Set window size
        self.root.geometry("800x600")

        # Prevent window from becoming smaller than the background
        self.root.minsize(800, 600)

        # Dictionary to store menu items and prices
        self.menu_items = {
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESE BURGER": 2.5,
            "DRINKS": 1
        }

        # Exchange rate
        self.exchange_rate = 82

        # Set up background image
        self.setup_background()

        # Create a frame to hold the widgets
        frame = ttk.Frame(root)

        frame.place(
            relx=0.5,
            rely=0.5,
            anchor=tk.CENTER
        )

        # Heading label
        ttk.Label(
            frame,
            text="Restaurant Order Management",
            font=("Arial", 20, "bold")
        ).grid(
            row=0,
            columnspan=3,
            padx=10,
            pady=10
        )

        # Dictionaries to store widget references
        self.menu_labels = {}
        self.menu_quantities = {}

        # Create labels and entry boxes
        for i, (item, price) in enumerate(
            self.menu_items.items(),
            start=1
        ):

            # Menu item label
            label = ttk.Label(
                frame,
                text=f"{item} (${price}):",
                font=("Arial", 12)
            )

            label.grid(
                row=i,
                column=0,
                padx=10,
                pady=5
            )

            self.menu_labels[item] = label

            # Quantity entry
            quantity_entry = ttk.Entry(
                frame,
                width=5
            )

            quantity_entry.grid(
                row=i,
                column=1,
                padx=10,
                pady=5
            )

            self.menu_quantities[item] = quantity_entry

        # Currency selection
        self.currency_var = tk.StringVar()

        ttk.Label(
            frame,
            text="Currency:",
            font=("Arial", 12)
        ).grid(
            row=len(self.menu_items) + 1,
            column=0,
            padx=10,
            pady=5
        )

        # Currency dropdown
        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state="readonly",
            width=18,
            values=("USD", "INR")
        )

        currency_dropdown.grid(
            row=len(self.menu_items) + 1,
            column=1,
            padx=10,
            pady=5
        )

        # Default currency
        currency_dropdown.current(0)

        # Update prices when currency changes
        self.currency_var.trace_add(
            "write",
            self.update_menu_prices
        )

        # Place order button
        order_button = ttk.Button(
            frame,
            text="Place Order",
            command=self.place_order
        )

        order_button.grid(
            row=len(self.menu_items) + 2,
            columnspan=3,
            padx=10,
            pady=10
        )


    # ------------------------------------------------
    # Method to set up the background image
    # ------------------------------------------------
    def setup_background(self):

        bg_width = 800
        bg_height = 600

        # Create canvas
        self.canvas = tk.Canvas(
            self.root,
            width=bg_width,
            height=bg_height,
            highlightthickness=0
        )

        self.canvas.pack(
            fill="both",
            expand=True
        )

        # Open the PNG image
        original_image = Image.open("images.png")

        # Resize image to exactly 800 x 600
        original_image = original_image.resize(
            (bg_width, bg_height),
            Image.Resampling.LANCZOS
        )

        # Convert Pillow image to Tkinter image
        self.background_image = ImageTk.PhotoImage(
            original_image
        )

        # Display image
        self.canvas.create_image(
            0,
            0,
            anchor=tk.NW,
            image=self.background_image
        )


    # ------------------------------------------------
    # Method to update menu prices
    # ------------------------------------------------
    def update_menu_prices(self, *args):

        currency = self.currency_var.get()

        # Select currency symbol
        symbol = "₹" if currency == "INR" else "$"

        # Select conversion rate
        rate = self.exchange_rate if currency == "INR" else 1

        # Update every menu item's price
        for item, label in self.menu_labels.items():

            price = self.menu_items[item] * rate

            label.config(
                text=f"{item} ({symbol}{price}):"
            )


    # ------------------------------------------------
    # Method to place an order
    # ------------------------------------------------
    def place_order(self):

        total_cost = 0

        order_summary = "Order Summary:\n"

        # Get selected currency
        currency = self.currency_var.get()

        # Currency symbol
        symbol = "₹" if currency == "INR" else "$"

        # Conversion rate
        rate = self.exchange_rate if currency == "INR" else 1

        # Check every menu item
        for item, entry in self.menu_quantities.items():

            quantity = entry.get()

            # Check whether quantity is a number
            if quantity.isdigit():

                quantity = int(quantity)

                # Calculate price
                price = self.menu_items[item] * rate

                # Calculate cost
                cost = quantity * price

                total_cost += cost

                # Add ordered items to summary
                if quantity > 0:

                    order_summary += (
                        f"{item}: "
                        f"{quantity} x {symbol}{price} "
                        f"= {symbol}{cost}\n"
                    )

        # Show order if something was ordered
        if total_cost > 0:

            order_summary += (
                f"\nTotal Cost: {symbol}{total_cost}"
            )

            messagebox.showinfo(
                "Order Placed",
                order_summary
            )

        else:

            messagebox.showerror(
                "Error",
                "Please order at least one item."
            )


# ------------------------------------------------
# Main program
# ------------------------------------------------

if __name__ == "__main__":

    # Create main window
    root = tk.Tk()

    # Create application
    app = RestaurantOrderManagement(root)

    # Start GUI
    root.mainloop()