from web3 import Web3
from eth_account.messages import encode_defunct


web3 = Web3(Web3.HTTPProvider("https://polygon-rpc.com/"))
private_key = "your private key"
account = "your account"

transaction = {
      'chainId': web3.eth.chain_id,
      'from': account,
      'to': "another account",
      'value': 1 * 10**17,
      'nonce': web3.eth.get_transaction_count(account), 
      'gasPrice': web3.eth.gas_price,
      'gas': 21000,
    }



signed_transaction = web3.eth.account.sign_transaction(transaction, private_key)
transaction_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)

print(transaction_hash.hex())