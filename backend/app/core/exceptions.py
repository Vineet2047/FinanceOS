class AccountAlreadyExistsError(Exception):
    """Raised when an account with the same name already exists."""

class AccountNotFoundError(Exception):
    """Raised when an account cannot be found."""
