"""
Network name: Cronos Mainnet
New RPC URL: https://evm-cronos.crypto.org
Chain ID: 25
Currency symbol: cro
Block explorer URL: https://cronos.crypto.org/explorer/
"""

from web3 import Web3
from dotenv import load_dotenv
load_dotenv()
import os



def send_cro(to_address: str,
             value: float = 1,
             gas_price: str = '0.000005',
             gas: int = 21_000,
             node_rpc: str = "https://evm-cronos.crypto.org",
             block_explorer: str = "https://cronos.crypto.org/explorer/tx/"
             ) -> str:
    from_address = os.environ.get('FROM_ADDRESS')
    key = os.environ.get('KEY')
    # Convert address to ensure format
    from_address = Web3.toChecksumAddress(from_address)
    to_address = Web3.toChecksumAddress(to_address)

    # Connect to node
    web3 = Web3(Web3.HTTPProvider(node_rpc))

    # Convert to Wei
    gas_price = web3.toWei(gas_price, 'ether')
    value = web3.toWei(value, 'ether')

    # Random number
    nonce = web3.eth.getTransactionCount(from_address)

    # Tx params
    tx = {
        'nonce': nonce,
        'to': to_address,
        'value': value,
        'gas': gas,
        'gasPrice': gas_price
    }

    # Sign transaction
    signed_tx = web3.eth.account.sign_transaction(tx, key)

    # send transaction
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = web3.toHex(tx_hash)

    # prints block explorer link
    tx_link = f"{block_explorer}{tx_hash}"
    print(tx_link)

    return tx_hash


# if __name__ == "__main__":
#     key = "12d86e292734a24719a6b6cfdb3c7e78fb88971a74c9df69b576c33b3aa09ebb"
#     from_address = "0x75cbd961b2c7403737ca73309bae5679d8605e0f"
#     to_address = "0xC828448e49AbdB9f2C0210bD195F27038a5E11B0"
#     send_cro(from_address, key, to_address)


