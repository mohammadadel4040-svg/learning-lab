import logging

# Configuring logging system
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Discount rules
category_discount = {
    "Electronics": 10,
    "Clothing": 15,
    "Books": 5,
    "Home": 12
}

tier_discount = {
    "Premium": 5,
    "Standard": 0,
    "Budget": 2
}


def calculate_discount(category, tier):
    return category_discount.get(category, 0) + \
           tier_discount.get(tier, 0)


def process_products():

    products = []
    total_discount = 0

    try:
        with open("products.txt", "r") as file:

            for line_number, line in enumerate(file, 1):

                try:
                    name, price, category, tier = line.strip().split(",")

                    base_price = float(price)
                    discount = calculate_discount(category, tier)

                    discount_amount = base_price * discount / 100
                    final_price = base_price - discount_amount

                    products.append(
                        (name, base_price, discount,
                         discount_amount, final_price)
                    )

                    total_discount += discount

                except ValueError:
                    logging.error(
                        f"Line {line_number}: Invalid price"
                    )

        with open("pricing_report.txt", "w") as report:

            report.write("PRICING REPORT\n")
            report.write("=" * 70 + "\n")

            for p in products:
                report.write(
                    f"{p[0]} | ${p[1]:.2f} | "
                    f"{p[2]}% | ${p[3]:.2f} | "
                    f"${p[4]:.2f}\n"
                )

        avg_discount = total_discount / len(products)

        print("Products processed:", len(products))
        print("Average discount:", round(avg_discount, 2), "%")

    except FileNotFoundError:
        logging.error("products.txt not found")


if __name__ == "__main__":
    process_products()
