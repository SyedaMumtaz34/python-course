print("===== Inventory Stock Counter =====")

box_sizes = [20, 10, 5, 1]

products_counted = 0
total_items = 0
log = []

num_products = int(input("Enter number of products: "))

while products_counted < num_products:

    product = input("\nEnter product name: ")
    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Invalid quantity!")
        continue

    total_items += quantity
    remaining = quantity
    breakdown = {}

    i = 0
    while i < len(box_sizes):
        size = box_sizes[i]
        boxes = remaining // size
        remaining = remaining % size
        breakdown[size] = boxes
        i += 1

    log.append((product, breakdown))
    products_counted += 1

print("\n===== Product Breakdown =====")

for item in log:
    print("\nProduct:", item[0])
    for size in box_sizes:
        print("Box", size, ":", item[1][size])

print("\n===== Final Report =====")

for size in box_sizes:
    total_boxes = 0
    for item in log:
        total_boxes += item[1][size]
    print("Box", size, "used:", total_boxes)

print("\nTotal Products:", products_counted)
print("Total Items:", total_items)
