import numpy as np

def calculate_5k_time(vdot):
    """
    Calculate 5k time in seconds based on VDOT.
    :param vdot: VDOT value (float)
    :return: 5k time in seconds (float)
    """
    coefficients = [-6.77309805e-03, 1.43207286e+00, -1.13134611e+02, 4.11826781e+03]
    return np.polyval(coefficients, vdot)

def calculate_vdot_from_time(seconds):
    """
    Calculate VDOT based on a 5k time in seconds.
    Uses a numerical solver to find the best VDOT value.
    :param seconds: 5k time in seconds (float)
    :return: VDOT value (float)
    """
    from scipy.optimize import minimize_scalar

    def objective(vdot):
        return abs(calculate_5k_time(vdot) - seconds)

    result = minimize_scalar(objective, bounds=(30, 80), method='bounded')
    return result.x if result.success else None

# Example Usage
if __name__ == "__main__":
    # Calculate 5k time for a given VDOT
    vdot = 50
    time_seconds = calculate_5k_time(vdot)
    print(f"VDOT {vdot} corresponds to a 5k time of {int(time_seconds // 60)}:{int(time_seconds % 60):02d}")

    # Calculate VDOT for a given 5k time
    input_time_seconds = 19 * 60 + 57  # Example: 19:57
    vdot_estimated = calculate_vdot_from_time(input_time_seconds)
    print(f"A 5k time of 19:57 corresponds to an estimated VDOT of {vdot_estimated:.2f}")