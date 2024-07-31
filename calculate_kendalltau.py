import numpy as np
from scipy.stats import kendalltau
import matplotlib.pyplot as plt

# Adding the ablation called A_DOSER_PRIO
# Re-import necessary packages and redefine vectors due to the reset environment

def bootstrap_kendall_tau(reference, prediction, n=1000, confidence_level=0.90):
    tau_values = []
    n_samples = len(reference)
    for _ in range(n):
        indices = np.random.randint(0, n_samples, n_samples)
        sample_ref = np.array(reference)[indices]
        sample_pred = np.array(prediction)[indices]
        tau, _ = kendalltau(sample_ref, sample_pred)
        tau_values.append(tau)
    # Calculate mean and confidence interval
    tau_mean = np.mean(tau_values)
    lower_bound = np.percentile(tau_values, (1 - confidence_level) / 2 * 100)
    upper_bound = np.percentile(tau_values, (1 + confidence_level) / 2 * 100)
    return tau_values, tau_mean, lower_bound, upper_bound

if __name__ == "__main__":

    #Vectors:
    Eclipse = [1, 2, 3, 4, 2, 1, 3, 4, 2, 3, 4, 1, 4, 1, 3, 2, 3, 2, 1, 4, 4, 1, 3, 2, 1, 3, 2, 4, 2, 3, 1, 4, 1, 3, 2, 4, 4, 1, 3, 2, 3, 1, 4, 2, 1, 3, 2, 4, 3, 4, 2, 1]
    DL= [1, 2, 3, 4, 1, 2, 3, 4, 1, 4, 2, 3, 3, 2, 1, 4, 3, 4, 2, 1, 4, 3, 1, 2, 1, 3, 2, 4, 4, 3, 2, 1, 1, 2, 3, 4, 1, 4, 2, 3, 4, 1, 3, 2, 4, 3, 1, 2, 1, 3, 2, 4]
    R01=[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 1, 2, 3, 3, 4, 2, 1, 3, 4, 2, 1, 1, 4, 2, 3, 2, 3, 4, 1, 2, 1, 3, 4, 2, 3, 4, 1, 4, 3, 2, 1, 4, 3, 1, 2, 1, 2, 3, 4]
    R02=[2, 4, 3, 1, 1, 2, 4, 3, 1, 2, 3, 4, 3, 1, 2, 4, 4, 3, 2, 1, 1, 2, 3, 4, 1, 4, 2, 3, 4, 3, 2, 1, 1, 2, 3, 4, 2, 3, 1, 4, 2, 1, 4, 3, 3, 4, 1, 2, 1, 2, 4, 3]
    R03=[2, 4, 3, 1, 1, 3, 2, 4, 1, 2, 4, 3, 4, 1, 2, 3, 4, 3, 2, 1, 4, 2, 3, 1, 1, 4, 2, 3, 4, 3, 2, 1, 2, 1, 3, 4, 1, 2, 3, 4, 2, 1, 4, 3, 3, 4, 1, 2, 1, 2, 3, 4]
    R04=[[1, 2, 4, 3, 1, 4, 3, 2, 1, 4, 3, 1, 4, 2, 1, 3, 4, 3, 2, 1, 1, 3, 2, 1, 2, 4, 1, 3, 4, 3, 2, 1, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 1, 3, 4, 2, 1, 1, 2, 3, 4]]

    # Plotting
    plt.figure(figsize=(12, 8))

    # Plot the CDF for all comparisons in one plot with assigned colors
    plt.plot(kendalls_tau_sorted, cdf, marker='.', linestyle='none', color='orange', label='Eclipse vs DL')
    plt.plot(kendalls_tau_sorted_r01, cdf_r01, marker='.', linestyle='none', color='blue', label='Eclipse vs R01')
    plt.plot(kendalls_tau_sorted_r02, cdf_r02, marker='.', linestyle='none', color='purple', label='Eclipse vs R02')
    plt.plot(kendalls_tau_sorted_r03, cdf_r03, marker='.', linestyle='none', color='red', label='Eclipse vs R03')
    plt.plot(kendalls_tau_sorted_r04, cdf_r04, marker='.', linestyle='none', color='pink', label='Eclipse vs R04')

    plt.xlim(min_tau_dl, max_tau_dl)

    plt.title('Cumulative Distribution of Kendall\'s Tau Values\n(Eclipse vs Predictions from Bootstrapping)')
    plt.xlabel('Kendall\'s Tau Value')
    plt.ylabel('CDF')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()

    # Redefine vectors
    Eclipse = [1, 2, 3, 4, 2, 1, 3, 4, 2, 3, 4, 1, 4, 1, 3, 2, 3, 2, 1, 4, 4, 1, 3, 2, 1, 3, 2, 4, 2, 3, 1, 4, 1, 3, 2, 4, 4, 1, 3, 2, 3, 1, 4, 2, 1, 3, 2, 4, 3, 4, 2, 1]
    A_DOSER_PRIO = [1, 2, 3, 4, 2, 3, 1, 4, 1, 4, 2, 3, 4, 3, 1, 2, 3, 4, 2, 1, 3, 4, 1, 2, 1, 4, 2, 3, 4, 2, 3, 1, 2, 1, 3, 4, 1, 3, 2, 4, 2, 1, 4, 3, 3, 4, 1, 2, 1, 4, 2, 3]

    # Perform bootstrapping analysis
    # Calculate bootstrap for Eclipse vs A-DOSER-PRIO
    tau_values_a_doser_prio, _, _, _ = bootstrap_kendall_tau(Eclipse, A_DOSER_PRIO)

    # Calculate bootstrap for Eclipse vs DL for comparison
    DL = [1, 2, 3, 4, 1, 2, 3, 4, 1, 4, 2, 3, 3, 2, 1, 4, 3, 4, 2, 1, 4, 3, 1, 2, 1, 3, 2, 4, 4, 3, 2, 1, 1, 2, 3, 4, 1, 4, 2, 3, 4, 1, 3, 2, 4, 3, 1, 2, 1, 3, 2, 4]
    tau_values_dl, _, _, _ = bootstrap_kendall_tau(Eclipse, DL)

    # Plot CDF for DL and A-DOSER-PRIO
    plt.figure(figsize=(10, 6))

    # DL
    sorted_dl = np.sort(tau_values_dl)
    cdf_dl = np.arange(1, len(sorted_dl)+1) / len(sorted_dl)
    plt.plot(sorted_dl, cdf_dl, label='Eclipse vs DL', color='orange')

    # A-DOSER-PRIO
    sorted_a_doser_prio = np.sort(tau_values_a_doser_prio)
    cdf_a_doser_prio = np.arange(1, len(sorted_a_doser_prio)+1) / len(sorted_a_doser_prio)
    plt.plot(sorted_a_doser_prio, cdf_a_doser_prio, label='Eclipse vs A-DOSER-PRIO', color='green')

    plt.xlabel('Kendall’s Tau')
    plt.ylabel('Cumulative Distribution')
    plt.title('CDF of Kendall’s Tau Values for Bootstrapping Comparisons')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Replotting

    plt.figure(figsize=(10, 6))

    # DL (now represented as "Eclipse vs. A-DOSER")
    plt.plot(sorted_dl, cdf_dl, label='Eclipse vs. A-DOSER', color='orange', linestyle='-')

    # A-DOSER-PRIO (now represented as "Eclipse vs. A-DOSER-No-PRIO" with dotted lines)
    plt.plot(sorted_a_doser_prio, cdf_a_doser_prio, label='Eclipse vs. A-DOSER-No-PRIO', color='orange', linestyle=':')

    plt.xlabel('Kendall’s Tau')
    plt.ylabel('Cumulative Distribution')
    plt.title('CDF of Kendall’s Tau Values for Bootstrapping Comparisons')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Prompt: Compute Kendall's Tau ranking correlation and use bootstrapping with 1000 resampling and 90% confidence interval. Provide mean and CI values evaluating the reference against each prediction.
    plt.figure(figsize=(10, 6))

    # Calculate the CDF for Kendall's Tau values from bootstrapping for Eclipse vs DL
    kendalls_tau_eclipse_dl = bootstrap_samples['DL']
    kendalls_tau_sorted = np.sort(kendalls_tau_eclipse_dl)

    # Calculate the CDF values
    cdf = np.arange(1, len(kendalls_tau_sorted) + 1) / len(kendalls_tau_sorted)

    # Plot the CDF
    plt.plot(kendalls_tau_sorted, cdf, marker='.', linestyle='none')

    plt.title('Cumulative Distribution of Kendall\'s Tau Values\n(Eclipse vs DL from Bootstrapping)')
    plt.xlabel('Kendall\'s Tau Value')
    plt.ylabel('CDF')
    plt.grid(True)
    plt.tight_layout()

    plt.show()