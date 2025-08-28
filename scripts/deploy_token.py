from brownie import accounts, MockToken, network, config

def main():
    print(f"Active network: {network.show_active()}")
    # ใช้ private key ของคุณ
    pk = "PRIVATE_KEY_HERE"
    acct = accounts.add(pk)
    
    # Deploy token
    token = MockToken.deploy("MyToken", "MTK", 18, 1000 * 10**18, {"from": acct})
    print("Deployed at:", token.address)
