import requests
from requests import Response

from account_manager.exceptions import (
    ClientException,
    ClientConfigException,
    TokenRequired,
)
from models import (
    AccountSchema,
    BalanceSchema,
    HTTPValidationError,
    Token,
    BodyGetTokenOAuthTokenPost,
    TransactionSchema,
    UserIdentitySchema,
)
from settings import client_settings

TOKEN_API = "/oauth/token"
IDENTITY_API = "/stet/identity"
ACCOUNT_API = "/stet/account"
ACCOUNT_API_ID = "/stet/account/{account_id}"
BALANCE_API_ID = "/stet/account/{account_id}/balance"
TRANSACTION_API = "/stet/account/{account_id}/transaction"


class AccountClient:
    base_url: str

    def __init__(self):
        self.base_url = client_settings.baseUrl
        if not self.base_url:
            raise ClientConfigException("base_url")

    def get_token(self, request_data: BodyGetTokenOAuthTokenPost) -> Token:
        """
        access token
        :param request_data:
        :return: Token | None: object contain access_token, token_type
        """
        url = f"{self.base_url}{TOKEN_API}"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        response = requests.post(url, data=request_data.model_dump(), headers=headers)

        if response.status_code == 200:
            return Token(**response.json())

        raise self.get_errors(response)

    @staticmethod
    def get_token_str(token: Token):
        if not token:
            raise TokenRequired()
        return f"Bearer {token.access_token}"

    def get_identity(self, token: Token) -> UserIdentitySchema:
        """
        Return identity for current user
        :param token:
        :return: UserIdentitySchema | None: object
        """
        headers = {
            "accept": "application/json",
            "authorization": self.get_token_str(token),
        }
        response = requests.get(f"{self.base_url}{IDENTITY_API}", headers=headers)

        if response.status_code == 200:
            return UserIdentitySchema(**response.json())
        raise self.get_errors(response)

    def get_accounts(self, token: Token) -> list[AccountSchema]:
        """
        Return accounts for current user
        :param token:
        :return: list[AccountSchema] | None: List of account else None
        """
        headers = {
            "accept": "application/json",
            "authorization": self.get_token_str(token),
        }
        response = requests.get(f"{self.base_url}{ACCOUNT_API}", headers=headers)
        if response.status_code == 200:
            data = response.json()
            return [AccountSchema(**item) for item in data]
        raise self.get_errors(response)

    def get_account_id(self, token: Token, account_id: str) -> AccountSchema:
        """
        Return account information
        :param token:
        :param account_id:
        :return: AccountSchema Object
        """
        headers = {
            "accept": "application/json",
            "authorization": self.get_token_str(token),
        }
        response = requests.get(
            f"{self.base_url}{ACCOUNT_API_ID.format(account_id=account_id)}",
            headers=headers,
        )

        if response.status_code == 200:
            return AccountSchema(**response.json())
        raise self.get_errors(response)

    def get_account_balance(self, token: Token, account_id: str) -> list[BalanceSchema]:
        """
        Return balances for account
        :param token:
        :param account_id:
        :return:  list[BalanceSchema] | None: List of account else None
        """
        headers = {
            "accept": "application/json",
            "authorization": self.get_token_str(token),
        }
        response = requests.get(
            f"{self.base_url}{BALANCE_API_ID.format(account_id=account_id)}",
            headers=headers,
        )

        if response.status_code == 200:
            data = response.json()
            return [BalanceSchema(**item) for item in data]
        raise self.get_errors(response)

    def get_account_transaction(
        self, token: Token, account_id: str
    ) -> list[TransactionSchema]:
        """
        Return transactions for account
        :param token:
        :param account_id:
        :return: list[TransactionSchema] | None: List of account else None
        """
        headers = {
            "accept": "application/json",
            "authorization": self.get_token_str(token),
        }
        response = requests.get(
            f"{self.base_url}{TRANSACTION_API.format(account_id=account_id)}",
            headers=headers,
        )

        if response.status_code == 200:
            data = response.json()
            return [TransactionSchema(**item) for item in data]
        raise self.get_errors(response)

    @staticmethod
    def get_errors(response: Response) -> Exception:
        """
        raise exception when status_code =422 and 401
        :param response:
        """
        if response.status_code == 422:
            return ClientException(HTTPValidationError(**response.json()))
        if response.status_code == 401:
            return Exception(f"Error: {response.json()}")
        return Exception(
            f"unknown error: status_code={response.status_code}, text: response.text={response.text}"
        )
