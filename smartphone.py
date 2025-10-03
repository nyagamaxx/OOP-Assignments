# Assignment 1: Design Your Own Class - Smartphone Example

# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"Device: {self.brand} {self.model}"


# Child Class (Inheritance from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Call parent constructor
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        return f"📞 Calling {number} from {self.brand} {self.model}..."

    def take_photo(self):
        return f"📸 Taking a photo with {self.brand} {self.model}!"

    def phone_info(self):
        return (f"{self.device_info()} | Storage: {self.storage}GB | "
                f"Battery: {self.battery}mAh")


# Example Usage
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "Galaxy S24", 256, 5000)
    phone2 = Smartphone("Apple", "iPhone 15", 128, 4200)

    print(phone1.phone_info())
    print(phone1.make_call("0712345678"))
    print(phone2.take_photo())
