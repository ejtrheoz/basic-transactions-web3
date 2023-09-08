from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://rpc-mainnet.maticvigil.com/'))
private_key = "your private key"
account = "your metamask"


contract_addr = '0x9cfEAdcC38377283aDB944205c5238d04d4dD8A1'
abi = '[{"inputs":[{"internalType":"address","name":"_bentoBox","type":"address"},{"internalType":"address[]","name":"priviledgedUserList","type":"address[]"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"address","name":"tokenIn","type":"address"},{"indexed":true,"internalType":"address","name":"tokenOut","type":"address"},{"indexed":false,"internalType":"uint256","name":"amountIn","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amountOut","type":"uint256"}],"name":"Route","type":"event"},{"inputs":[],"name":"bentoBox","outputs":[{"internalType":"contract IBentoBoxMinimal","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address","name":"tokenOut","type":"address"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"route","type":"bytes"}],"name":"processRoute","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"resume","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"},{"internalType":"bool","name":"priviledge","type":"bool"}],"name":"setPriviledge","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address payable","name":"transferValueTo","type":"address"},{"internalType":"uint256","name":"amountValueTransfer","type":"uint256"},{"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address","name":"tokenOut","type":"address"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"route","type":"bytes"}],"name":"transferValueAndprocessRoute","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"int256","name":"amount0Delta","type":"int256"},{"internalType":"int256","name":"amount1Delta","type":"int256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"uniswapV3SwapCallback","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'
contract = w3.eth.contract(address = contract_addr, abi = abi)

route = "0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270"

swap_transaction = contract.functions.processRoute(
    "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",
    0.05 * 10**18,
    "0x0b3F868E0BE5597D5DB7fEB59E1CADBb0fdDa50a",
    0.046 * 10**18,
    'v',
    route
).buildTransaction({
    'nonce': w3.eth.get_transaction_count(account),
    'gas': 21000,
    'gasPrice': w3.eth.gas_price,
    'from': account,
    'value': 0.05 * 10**18,
})

signed_transaction = w3.eth.account.sign_transaction(swap_transaction, private_key)
transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)

print(transaction_hash.hex())


