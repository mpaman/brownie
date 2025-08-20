from brownie import accounts, MockToken, network, Wei

def main():
    print(f"Active network: {network.show_active()}")

    sender = accounts.load("holesky_deployer")  # โหลด account ที่ save ไว้
    print(f"Sender: {sender}")

    recipient = input("Enter recipient address: ").strip()
    amount_str = input("Enter amount of MTK to send (e.g., 10 ether): ").strip()

    try:
        amount = Wei(amount_str)
    except Exception:
        print("❌ Invalid amount format. Example: 10 ether")
        return

    token = MockToken[-1]

    balance = token.balanceOf(sender)
    if balance < amount:
        print(f"❌ Not enough balance. You have {balance}, need {amount}")
        return

    print(f"Transferring {amount} MTK from {sender} -> {recipient}")
    tx = token.transfer(recipient, amount, {"from": sender})
    tx.wait(1)

    print("✅ Transaction successful!")
    print("TX hash:", tx.txid)
    print("Recipient balance:", token.balanceOf(recipient))

