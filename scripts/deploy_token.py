from brownie import accounts, MockToken, network

def main():
    # Load account
    acct = accounts.load("holesky_deployer")

    # Token parameters
    name = "MyToken"
    symbol = "MTK"
    initial_supply = 1000 * 10**18  # 1000 tokens

    # Deploy contract
    token = MockToken.deploy(
        name,
        symbol,
        initial_supply,
        {"from": acct}
    )

    print(f"✅ Token deployed at: {token.address}")
