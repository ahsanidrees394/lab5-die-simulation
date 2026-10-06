import numpy as np
import matplotlib.pyplot as plt


rolls = np.random.randint(1, 7, size=1000)

# 
# A. Print first 10 rolls

print("First 10 rolls:", rolls[:10])

# B. Count occurrences of each face


faces, counts = np.unique(rolls, return_counts=True)

print("\nFace Count Empirical P Theoretical P")

for face, count in zip(faces, counts):

    empirical_probability = count / 1000
    theoretical_probability = 1 / 6

    print(
        f"{face}    {count}    "
        f"{empirical_probability:.3f}       "
        f"{theoretical_probability:.4f}"
    )
# C. Plot histogram


plt.figure(figsize=(8, 5))

plt.hist(
    rolls,
    bins=np.arange(0.5, 7.5, 1),
    edgecolor="black"
)

plt.xticks(range(1, 7))

plt.xlabel("Die Face")
plt.ylabel("Frequency")

plt.title("1000 Fair Six-Sided Die Rolls")

plt.tight_layout()

# Save the plot
plt.savefig("die_rolls.png", dpi=150)

plt.show()

print("\nSaved die_rolls.png")