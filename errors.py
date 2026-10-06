class BioMiniError(Exception):
    """Base exception for BioMini."""


class ValidationError(BioMiniError, ValueError):
    """Raised when domain or data inputs fail validation."""


class SerializationError(BioMiniError):
    """Raised when serialized data cannot be safely restored."""


class ModelPersistenceError(BioMiniError):
    """Raised when a model artifact cannot be saved or restored."""


class FastaFormatError(BioMiniError, ValueError):
    """Raised when FASTA text violates the supported BioMini format."""


class DataError(BioMiniError, ValueError):
    """Raised when a dataset cannot support the requested operation."""
