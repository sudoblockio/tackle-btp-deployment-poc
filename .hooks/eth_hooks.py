from typing import Union
from pydantic import BaseModel

from web3 import Web3, HTTPProvider
from eth_account import Account
import secrets

from tackle import BaseHook, Field


class Web3ProviderMixin(BaseModel):
    # TODO: Figure out secure way of dealing with this token. Right now it is on free
    #  account so no risk but long term should have solution.
    rpc_url: str = "https://mainnet.infura.io/v3/66d8b3f1a5984c03a6b598fb175f845b"

    def get_web3_provider(self):
        return Web3(HTTPProvider(endpoint_uri=self.rpc_url))


class EthGetBlock(BaseHook, Web3ProviderMixin):
    """Get an eth block details."""
    hook_type: str = 'eth_get_block'

    block_number: Union[int, str] = Field(
        'latest', description="Either a number or blank for latest."
    )
    args: list = ['block_number']

    def exec(self) -> dict:
        w3 = self.get_web3_provider()
        block = dict(w3.eth.get_block(self.block_number))
        return block


class EthCreateAccount(BaseHook):
    """Create an eth account."""
    hook_type: str = 'eth_create_account'

    def exec(self) -> dict:
        priv = secrets.token_hex(32)
        private_key = "0x" + priv
        acct = Account.from_key(private_key)
        return {
            'address': acct.address,
            'privateKey': acct.privateKey,
        }
