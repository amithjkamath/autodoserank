import numpy as np
from scipy.stats import kendalltau

def bootstrap_kendall_tau(reference, prediction, n=10000, confidence_level=0.90):
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
    return tau_mean, lower_bound, upper_bound

if __name__ == "__main__":

    #Vectors:
    Eclipse = [1, 2, 3, 4, 2, 1, 3, 4, 2, 3, 4, 1, 4, 1, 3, 2, 3, 2, 1, 4, 4, 1, 3, 2, 1, 3, 2, 4, 2, 3, 1, 4, 1, 3, 2, 4, 4, 1, 3, 2, 3, 1, 4, 2, 1, 3, 2, 4, 3, 4, 2, 1]
    DL= [1, 2, 3, 4, 1, 2, 3, 4, 1, 4, 2, 3, 3, 2, 1, 4, 3, 4, 2, 1, 4, 3, 1, 2, 1, 3, 2, 4, 4, 3, 2, 1, 1, 2, 3, 4, 1, 4, 2, 3, 4, 1, 3, 2, 4, 3, 1, 2, 1, 3, 2, 4]
    R01=[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 1, 2, 3, 3, 4, 2, 1, 3, 4, 2, 1, 1, 4, 2, 3, 2, 3, 4, 1, 2, 1, 3, 4, 2, 3, 4, 1, 4, 3, 2, 1, 4, 3, 1, 2, 1, 2, 3, 4]
    R02=[2, 4, 3, 1, 1, 2, 4, 3, 1, 2, 3, 4, 3, 1, 2, 4, 4, 3, 2, 1, 1, 2, 3, 4, 1, 4, 2, 3, 4, 3, 2, 1, 1, 2, 3, 4, 2, 3, 1, 4, 2, 1, 4, 3, 3, 4, 1, 2, 1, 2, 4, 3]
    R03=[2, 4, 3, 1, 1, 3, 2, 4, 1, 2, 4, 3, 4, 1, 2, 3, 4, 3, 2, 1, 4, 2, 3, 1, 1, 4, 2, 3, 4, 3, 2, 1, 2, 1, 3, 4, 1, 2, 3, 4, 2, 1, 4, 3, 3, 4, 1, 2, 1, 2, 3, 4]
    R04=[1, 2, 4, 3, 1, 4, 3, 2, 1, 4, 3, 1, 4, 2, 1, 3, 4, 3, 2, 1, 1, 3, 2, 1, 2, 4, 1, 3, 4, 3, 2, 1, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 1, 3, 4, 2, 1, 1, 2, 3, 4]

    tau_mean, lower, upper = bootstrap_kendall_tau(Eclipse, DL)
    print("Kendall's tau mean: " + str(tau_mean) + ", range: [" + str(lower) + ", " + str(upper) + "]")

    tau_mean, lower, upper = bootstrap_kendall_tau(Eclipse, R01)
    print("Kendall's tau mean: " + str(tau_mean) + ", range: [" + str(lower) + ", " + str(upper) + "]")

    tau_mean, lower, upper = bootstrap_kendall_tau(Eclipse, R02)
    print("Kendall's tau mean: " + str(tau_mean) + ", range: [" + str(lower) + ", " + str(upper) + "]")

    tau_mean, lower, upper = bootstrap_kendall_tau(Eclipse, R03)
    print("Kendall's tau mean: " + str(tau_mean) + ", range: [" + str(lower) + ", " + str(upper) + "]")

    tau_mean, lower, upper = bootstrap_kendall_tau(Eclipse, R04)
    print("Kendall's tau mean: " + str(tau_mean) + ", range: [" + str(lower) + ", " + str(upper) + "]")