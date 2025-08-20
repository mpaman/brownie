import os
from brownie import accounts, network, Wei

def main():
    sender = accounts[0]
    recipient = os.getenv("RECIPIENT")
    assert recipient, "Set RECIPIENT env var to the target address"

    amount = Wei(os.getenv("AMOUNT", "0.1 ether"))
    print(f"Network: {network.show_active()}")
    print(f"Sending {amount} ETH from {sender} -> {recipient}")
    tx = sender.transfer(recipient, amount)
    print("TX:", tx.txid)
