<<<<<<< HEAD
    def save_purchase(self, purchase):
        try:
            with open(self.history_filename, "a") as file:
                # Format the purchase data in the new format
                purchase_data = f"username: {purchase['username']}; model: {purchase['model']}; storage: {purchase['storage']}; item: {purchase['item']}; subtotal: {purchase['subtotal']}\n"
                file.write(purchase_data)
        except Exception as e:
            print(f"Error saving purchase to file {e}.")

    def load_purchase(self):
        try:    
            with open(self.history_filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:  # Skip empty lines
                        continue

                    # Split the line by '; ' to separate each field
                    if "; " in line:
                        parts = line.split("; ")
                        purchase_data = {}
                        for part in parts:
                            if ":" in part:  # Ensure the part contains a key-value pair
                                key, value = part.split(": ")
                                purchase_data[key.strip()] = value.strip()  # Remove extra spaces if any

                        # Add the purchase to the list and update the total_amount
                        self.purchases.append(purchase_data)
                        self.total_amount += float(purchase_data["subtotal"])  
        except Exception as e:
            print(f"Error occur {e}")
=======
# self.load_users()
>>>>>>> 1ed95e557068fa42e92e33673312a2f9d13632ff
