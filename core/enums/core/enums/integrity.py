from enum import Enum

class OriginalityTier(str, Enum):
    VERIFIED = "verified"     # Passes all 3 shields
    CAUTION = "caution"       # Minor structural matches
    RECONSTRUCTED = "reconstructed"  # Likely AI-paraphrased
    FLAGGED = "flagged"       # Direct matches found
