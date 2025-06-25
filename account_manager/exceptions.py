from models.validation_model import HTTPValidationError


class ClientException(Exception):
    def __init__(self, validation_error: HTTPValidationError):
        errors = [f"{e.loc}: {e.msg} : {e.type}" for e in validation_error.detail]
        self.message = "Validation failed:\n" + "\n".join(errors)
        super().__init__(self.message)


class ClientConfigException(Exception):
    def __init__(self, config_name: str):
        self.message = f"{config_name} must not be empty"
        super().__init__(self.message)


class TokenRequired(Exception):
    def __init__(self):
        super().__init__("Token is required")
