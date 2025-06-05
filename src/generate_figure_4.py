import numpy as np
from scipy.stats import kendalltau
import matplotlib.pyplot as plt

# Adding the ablation for with and without priority


def bootstrap_kendall_tau(reference, prediction, n=1000, confidence_level=0.90):
    tau_values = []
    n_samples = len(reference)
    for _ in range(n):
        indices = np.random.randint(0, n_samples, n_samples)
        sample_ref = np.array(reference)[indices]
        sample_pred = np.array(prediction)[indices]
        tau, _ = kendalltau(sample_ref, sample_pred)
        tau_values.append(tau)

    sorted_tau_values = np.sort(tau_values)
    cdf = np.arange(1, len(sorted_tau_values) + 1) / len(sorted_tau_values)
    return sorted_tau_values, cdf


if __name__ == "__main__":

    # Define vectors
    GT = [
        1,
        2,
        3,
        4,
        2,
        1,
        3,
        4,
        2,
        3,
        4,
        1,
        4,
        1,
        3,
        2,
        3,
        2,
        1,
        4,
        4,
        1,
        3,
        2,
        1,
        3,
        2,
        4,
        2,
        3,
        1,
        4,
        1,
        3,
        2,
        4,
        4,
        1,
        3,
        2,
        3,
        1,
        4,
        2,
        1,
        3,
        2,
        4,
        3,
        4,
        2,
        1,
    ]
    autodoserank_with_priority = [
        1,
        2,
        3,
        4,
        2,
        3,
        1,
        4,
        1,
        4,
        2,
        3,
        4,
        3,
        1,
        2,
        3,
        4,
        2,
        1,
        3,
        4,
        1,
        2,
        1,
        4,
        2,
        3,
        4,
        2,
        3,
        1,
        2,
        1,
        3,
        4,
        1,
        3,
        2,
        4,
        2,
        1,
        4,
        3,
        3,
        4,
        1,
        2,
        1,
        4,
        2,
        3,
    ]
    autodoserank_without_priority = [
        1,
        2,
        3,
        4,
        1,
        2,
        3,
        4,
        1,
        4,
        2,
        3,
        3,
        2,
        1,
        4,
        3,
        4,
        2,
        1,
        4,
        3,
        1,
        2,
        1,
        3,
        2,
        4,
        4,
        3,
        2,
        1,
        1,
        2,
        3,
        4,
        1,
        4,
        2,
        3,
        4,
        1,
        3,
        2,
        4,
        3,
        1,
        2,
        1,
        3,
        2,
        4,
    ]
    # Perform bootstrapping analysis
    sorted_with_priority, cdf_with_priority = bootstrap_kendall_tau(
        GT, autodoserank_with_priority
    )
    sorted_without_priority, cdf_without_priority = bootstrap_kendall_tau(
        GT, autodoserank_without_priority
    )

    plt.figure(figsize=(10, 6))
    plt.plot(
        sorted_without_priority,
        cdf_without_priority,
        label="GT vs. AutoDoseRank",
        color="orange",
        linestyle="-",
    )
    plt.plot(
        sorted_with_priority,
        cdf_with_priority,
        label="GT vs. AutoDoseRank-no-Priority",
        color="orange",
        linestyle=":",
    )

    plt.xlabel("Kendall’s Tau")
    plt.ylabel("Cumulative Distribution")
    plt.title("CDF of Kendall’s Tau Values for Bootstrapping Comparisons")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("src/images/figure_4.png", dpi=300)
    plt.close()
