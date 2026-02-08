import numpy as np


def encode_impedance(z):
    """
    Encode complex surface impedance into
    log10(|Z|), cos(angle), sin(angle)

    Parameters
    ----------
    z : array-like of complex
        Complex surface impedance

    Returns
    -------
    log_mag : ndarray
    cos_phase : ndarray
    sin_phase : ndarray
    """
    z = np.asarray(z, dtype=np.complex128)

    magnitude = np.abs(z)
    phase = np.angle(z)

    log_mag = np.log10(np.maximum(magnitude, 1e-12))
    cos_phase = np.cos(phase)
    sin_phase = np.sin(phase)

    return log_mag, cos_phase, sin_phase


def decode_impedance(log_mag, cos_phase, sin_phase):
    """
    Reconstruct complex surface impedance from
    log10(|Z|), cos(angle), sin(angle)
    """
    log_mag = np.asarray(log_mag, dtype=float)
    cos_phase = np.asarray(cos_phase, dtype=float)
    sin_phase = np.asarray(sin_phase, dtype=float)

    magnitude = 10.0 ** log_mag
    phase = np.arctan2(sin_phase, cos_phase)

    return magnitude * (np.cos(phase) + 1j * np.sin(phase))
