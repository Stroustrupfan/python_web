import random
import string
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

with open('contract.abi', 'r') as file:
    contract_address = file.read().strip()
contract = w3.eth.contract(address = contract_address, abi = contract_abi)

def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    random_string = ''.join(random.choice(characters)) for _ in range(length)
    
    return random_string

for _ in range(1000):
    inputs=[random.randint(0, 100) for _ in range(10)]
    try:
        tx_hash = contract.functions.functionName(*inputs).transact()
    except Exception as e:
        print(f'Exception occurred: {e}')
        continue
    
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)