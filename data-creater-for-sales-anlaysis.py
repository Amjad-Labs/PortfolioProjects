import pandas as pd 
import numpy as np
import random
from faker import Faker

# Set up Faker and random seeds
fake = Faker()
random.seed(42)
np.random.seed(42)

# Number of customers to generate
num_customers = 1000
customer_data = []

# Function to optionally mess up a name
def modify_name(name: str) -> str:
    rand = random.random()
    
    if rand < 0.025:
        return ""  # 2.5% chance of being blank
    elif rand < 0.325:
        return name.lower()  # 30% chance lowercase
    elif rand < 0.625:
        return name.upper()  # 30% chance uppercase
    else:
        return name  # 37.5% chance unchanged

# Generate customer data
for customer_id in range(1000, 1000 + num_customers):
    raw_name = fake.name()
    name = modify_name(raw_name)
    customer_data.append([customer_id, name])

# Create DataFrame
df_customers = pd.DataFrame(customer_data, columns=["Customer_ID", "Name"])
df_customers.to_csv("C:/Users/aafre/Videos/Captures/Amjad Files/Desktop/ecommerce-sales-dataset/customers.csv", index=False)

# Products Data are real Like iphone 14 price is $799.
products = [
    "Electronics : Apple : iPhone 14 (128GB) : $799",
    "Electronics : Samsung : Galaxy S23 Ultra : $1,199",
    "Electronics : Sony : WH-1000XM5 Wireless Headphones : $348",
    "Electronics : Samsung : 65-inch QLED 4K Smart TV : $1,199",
    "Electronics : Canon : EOS 90D DSLR Camera : $1,199",
    "Electronics : Apple : MacBook Air M2 (256GB) : $1,099",
    "Footwear : Nike : Air Force 1 Sneakers : $90",
    "Home Appliances : Instant Pot : Duo 7-in-1 Pressure Cooker : $89",
    "Fitness : Fitbit : Charge 5 Fitness Tracker : $129.95",
    "Electronics : Bose : SoundLink Flex Bluetooth Speaker : $129.99",
    "Furniture : IKEA : Hemnes 8-Drawer Dresser : $399",
    "Electronics : Sony : PlayStation 5 Console : $499",
    "Electronics : Microsoft : Xbox Series X Console : $499",
    "Electronics : Apple : AirPods Pro (2nd Generation) : $249",
    "Electronics : Samsung : Galaxy Watch 5 Pro : $399",
    "Home Appliances : Dyson : V11 Torque Drive Cordless Vacuum Cleaner : $599",
    "Electronics : LG : 55-inch OLED 4K Smart TV : $1,299",
    "Footwear : Adidas : Ultraboost 22 Sneakers : $180",
    "Home Appliances : Shark : Navigator Lift-Away Professional Vacuum : $169",
    "Kitchen : Vitamix : 5200 Blender : $449",
    "Electronics : Bose : QuietComfort 45 Wireless Headphones : $329",
    "Electronics : Apple : iPad Pro (12.9-inch, 256GB) : $1,099",
    "Home Appliances : Keurig : K-Elite Coffee Maker : $169",
    "Sports : Garmin : Forerunner 245 GPS Running Watch : $299.99",
    "Toys : LEGO : Creator Expert Roller Coaster : $379.99",
    "Beauty : Estée Lauder : Double Wear Foundation : $43",
    "Beauty : Clinique : Moisture Surge 72-Hour Auto-Replenishing Hydrator : $39.50",
    "Clothing : Levi's : 501 Original Fit Jeans : $59.99",
    "Clothing : Under Armour : Tech 2.0 T-Shirt : $24.99",
    "Electronics : Amazon : Kindle Paperwhite (8GB) : $139.99",
    "Electronics : Logitech : MX Master 3S Wireless Mouse : $99",
    "Electronics : HP : Spectre x360 Laptop : $1,299",
    "Home Appliances : Breville : BES870XL Barista Express Espresso Machine : $699",
    "Furniture : Wayfair : DHP Emily Futon Sofa Bed : $199.99",
    "Sports : Nike : Air Zoom Pegasus 39 Running Shoes : $120",
    "Electronics : GoPro : HERO11 Black Camera : $399",
    "Home Appliances : Cuisinart : 14-Cup Food Processor : $199.95",
    "Clothing : Nike : Dri-FIT Legend Training T-Shirt : $25",
    "Sports : Fitbit : Versa 3 Smartwatch : $229.95",
    "Kitchen : Nespresso : VertuoPlus Coffee Machine : $189.99",
    "Beauty : Tarte : Shape Tape Concealer : $27",
    "Clothing : Adidas : Supercourt Sneakers : $85",
    "Electronics : Apple : MacBook Pro 14-inch (512GB) : $1,899",
    "Electronics : Samsung : Galaxy Tab S8 (128GB) : $699",
    "Home Appliances : Frigidaire : 36-inch French Door Refrigerator : $2,299",
    "Electronics : Canon : EOS Rebel T7 DSLR Camera : $549",
    "Home Appliances : Breville : The Smart Oven Air Fryer : $399",
    "Sports : Peloton : Bike+ Exercise Bike : $2,495",
    "Fitness : Bowflex : SelectTech Dumbbells (5-52.5 lbs) : $399",
    "Home Appliances : KitchenAid : Artisan 5-Quart Stand Mixer : $429",
    "Electronics : Sony : 1000XM4 Noise Cancelling Headphones : $348",
    "Beauty : Lancôme : Advanced Génifique Serum : $105",
    "Electronics : Apple : Mac Mini M2 (256GB) : $699",
    "Electronics : Samsung : 32-inch Curved Monitor : $249",
    "Home Appliances : Samsung : Powerbot R7040 Robot Vacuum : $349",
    "Fitness : Peloton : Treadmill : $2,495",
    "Clothing : Columbia : Watertight II Jacket : $99",
    "Clothing : North Face : Denali Fleece Jacket : $179.99",
    "Sports : Adidas : Adizero Boston 11 Running Shoes : $140",
    "Home Appliances : Roomba : i7+ Robot Vacuum with Clean Base : $799",
    "Beauty : MAC Cosmetics : Studio Fix Fluid Foundation : $36",
    "Electronics : Nintendo : Switch OLED Console : $349",
    "Electronics : Razer : BlackWidow V3 Mechanical Gaming Keyboard : $129.99",
    "Home Appliances : Ninja : Foodi 5-in-1 Indoor Grill : $169.99",
    "Electronics : Samsung : Galaxy Buds 2 Pro : $229.99",
    "Home Appliances : iRobot : Braava Jet M6 Robot Mop : $499",
    "Electronics : Apple : iMac 24-inch (256GB) : $1,299",
    "Furniture : Amazon : Rivet Aiden Mid-Century Modern Sofa : $599",
    "Beauty : Urban Decay : Naked3 Eyeshadow Palette : $54",
    "Clothing : Calvin Klein : Modern Cotton Bralette : $22.50",
    "Electronics : Fitbit : Luxe Fitness and Wellness Tracker : $149.95",
    "Sports : Garmin : Venu 2S GPS Smartwatch : $249.99",
    "Home Appliances : Smeg : Retro 50's Style Toaster : $149",
    "Kitchen : Ninja : Professional 1000-Watt Blender : $89.99",
    "Furniture : Ashley Furniture : Signature Design Queen Bed : $499.99",
    "Electronics : Sony : Alpha 7C Mirrorless Camera : $1,798",
    "Fitness : NordicTrack : Commercial 1750 Treadmill : $1,599",
    "Electronics : Apple : Apple Watch Ultra : $799",
    "Electronics : Samsung : Galaxy Z Fold 4 : $1,799",
    "Clothing : Columbia : Silver Ridge Convertible Pants : $50",
    "Kitchen : KitchenAid : 4.5-Quart Tilt-Head Stand Mixer : $259",
    "Beauty : Olay : Regenerist Micro-Sculpting Cream : $26.97",
    "Clothing : Patagonia : Better Sweater Fleece Jacket : $139",
    "Electronics : Acer : Predator Helios 300 Gaming Laptop : $1,299",
    "Home Appliances : Hamilton Beach : 12-Cup Coffee Maker : $39.99",
    "Beauty : Drunk Elephant : C-Firma Day Serum : $78",
    "Fitness : Apple : Fitness+ Subscription (Monthly) : $9.99",
    "Electronics : LG : 27-inch 4K UHD Monitor : $349",
    "Home Appliances : Black+Decker : 12-Cup Programmable Coffee Maker : $34.99",
    "Sports : Nike : Zoom Fly 5 Running Shoes : $150",
    "Electronics : Sonos : One SL Smart Speaker : $179",
    "Home Appliances : Bissell : CrossWave Pet Pro Wet Dry Vacuum : $319.99",
    "Furniture : Pottery Barn : PB Essential Desk : $299",
    "Kitchen : Breville : Smart Oven Pro : $269",
    "Clothing : Champion : Reverse Weave Hoodie : $60",
    "Electronics : Samsung : 980 PRO SSD (1TB) : $129.99",
    "Home Appliances : Ninja : DualBrew Pro Coffee Maker : $229.99",
    "Sports : Adidas : Adizero Adios Pro 2 Running Shoes : $180",
    "Beauty : Tatcha : The Water Cream : $68",
    "Electronics : MSI : GE66 Raider Gaming Laptop : $1,699",
    "Home Appliances : Dyson : Supersonic Hair Dryer : $399",
    "Sports : Wilson : Evolution Basketball : $59.99",
    "Clothing : Tommy Hilfiger : Slim Fit Polo Shirt : $45",
    "Fitness : NordicTrack : Rowing Machine : $699",
    "Electronics : Apple : AirPods Max : $549",
    "Home Appliances : GE : 24-inch Dishwasher : $549",
    "Furniture : West Elm : Mid-Century Modern Sofa : $1,299",
    "Electronics : Asus : ROG Strix G15 Gaming Laptop : $1,149",
    "Beauty : Kiehl's : Ultra Facial Cream : $36"]
    

# Generate messy transactions
num_sales = 5000
sales_data = []

# Possible date formats to simulate messy data
date_formats = ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%B %d, %Y", "%Y/%m/%d"]

# Skewed weights: popular products appear more often
product_weights = [5 if "Apple" in p else 3 if "Nike" in p else 1 for p in products]

for trans_id in range(1, num_sales + 1):
    transaction_id = f"T{str(trans_id).zfill(5)}"
    customer_id = random.randint(1000, 1000 + 999)

    # Basket size: 1–5 products
    basket_size = random.randint(1, 5)
    basket_products = random.choices(products, weights=product_weights, k=basket_size)

    # Generate messy purchase date
    purchase_date = fake.date_between(start_date='-2y', end_date='today')
    date_format = random.choice(date_formats)
    date_str = purchase_date.strftime(date_format)

    # For each product in basket, append transaction line
    for product in basket_products:
        quantity = random.choice([1, 2, 3]) if random.random() < 0.95 else None
        sales_data.append([
            transaction_id,
            customer_id,
            product,
            date_str,
            quantity
        ])


# Create DataFrame
df_sales = pd.DataFrame(sales_data, columns=[
    "Transaction_ID", "Customer_ID", "Product", "Purchase_Date", "Quantity"
])

df_sales.to_csv("C:/Users/aafre/Videos/Captures/Amjad Files/sales-dataset/sales.csv", index=False)

print("Dataset creation: SUCCESS!")

