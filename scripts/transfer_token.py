import os
from brownie import accounts, MockToken, network, Wei

def main():
    sender = accounts[0]
    recipient = os.getenv("RECIPIENT")
    assert recipient, "Set RECIPIENT env var to the target address"

    token = MockToken[-1]  # ใช้สัญญา MTK ล่าสุดที่ดีพลอย
    amount = Wei(os.getenv("AMOUNT", "1000 ether"))
    print(f"Network: {network.show_active()}")
    print(f"Transferring {amount} MTK from {sender} -> {recipient}")
    tx = token.transfer(recipient, amount, {"from": sender})
    print("TX:", tx.txid)
    print("Recipient MTK balance:", token.balanceOf(recipient))
