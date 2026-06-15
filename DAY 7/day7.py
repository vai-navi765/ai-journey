import matplotlib.pyplot as plt

cleansers = ["Cetaphil", "Minimalist", "Dot&Key", "Lakme"]
prices = [390, 284, 214, 132]
sizes = [125, 100, 100, 60]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0][0].bar(cleansers, prices)
axes[0][0].set_title("Price Comparison")
axes[0][0].set_xlabel("Cleanser")
axes[0][0].set_ylabel("Price (Rs)")

axes[0][1].bar(cleansers, sizes)
axes[0][1].set_title("Size Comparison")
axes[0][1].set_xlabel("Cleanser")
axes[0][1].set_ylabel("Size (ml)")

axes[1][0].scatter(sizes, prices)
axes[1][0].set_title("Size vs Prices")
axes[1][0].set_xlabel("size")
axes[1][0].set_ylabel("price")

axes[1][1].barh(cleansers, prices)
axes[1][1].set_title("Cleanser In Affordable Prices")
axes[1][1].set_xlabel("cleansers")
axes[1][1].set_ylabel("prices")

plt.tight_layout()
plt.show()