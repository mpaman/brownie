
from brownie import accounts, MockToken, network, Wei


def main():
    print(f"Active network: {network.show_active()}")


    # โหลด account ที่ใช้ส่ง
    sender = accounts.load("holesky_deployer")
    print(f"Sender: {sender}")


    recipient = input("Enter recipient address: ").strip()
    amount_str = input("Enter amount of MTK to send (e.g., 10 ether): ").strip()


    try:
        amount = Wei(amount_str)
    except Exception:
        print("❌ Invalid amount format. Example: 10 ether")
        return


    # ใช้ MockToken ที่ deploy ไว้แล้ว
    token_address = "0x97d1727326931bCE5d121C8EcD76434627f8b8bE"
    token = MockToken.at(token_address)


    balance = token.balanceOf(sender)
    print(f"Your MTK balance: {balance}")


    if balance < amount:
        print(f"❌ Not enough balance. You have {balance}, need {amount}")
        return


    print(f"🚀 Transferring {amount} MTK from {sender} -> {recipient}")
    tx = token.transfer(recipient, amount, {"from": sender})
    tx.wait(1)


    print("✅ Transaction successful!")
    print("TX hash:", tx.txid)
    print("Recipient balance:", token.balanceOf(recipient))
