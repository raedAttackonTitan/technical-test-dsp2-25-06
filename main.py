from pprint import pprint

from account_manager import AccountClient
from models.token_model import BodyGetTokenOAuthTokenPost

if __name__ == "__main__":
    client = AccountClient()

    token_request1 = BodyGetTokenOAuthTokenPost(
        scope="stet ob", username="mdupuis", password="111111"
    )
    token_request2 = BodyGetTokenOAuthTokenPost(
        scope="stet ob", username="agribard", password="222222"
    )
    token = client.get_token(token_request1)
    print("\nToken1=")
    pprint(token.model_dump(), indent=4)

    identity = client.get_identity(token)
    print(
        "\nidentity=",
    )

    pprint(identity.model_dump(), indent=4)

    account = client.get_accounts(token)
    print("\naccount=")
    pprint(account, indent=4)
    accout_id = account[0].id

    account_info = client.get_account_id(token, accout_id)
    print(
        "\naccount_info=",
    )
    pprint(account_info.model_dump(), indent=4)

    balance = client.get_account_balance(token, accout_id)
    print("\nbalance=")
    pprint(balance, indent=4)

    transaction = client.get_account_transaction(token, accout_id)
    print("\ntransaction=")
    pprint(transaction, indent=4)
