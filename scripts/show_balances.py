import os
from brownie import accounts, MockToken, web3, Wei

def main():
    target = os.getenv("TARGET")
    assert target, "Set TARGET env var to the address you want to inspect"

    eth_balance = web3.eth.get_balance(target)
    print("Address:", target)
    print("ETH:", Wei(eth_balance).to('ether'), "ETH")

    if len(MockToken) > 0:
        token = MockToken[-1]
        print("MTK:", Wei(token.balanceOf(target)).to('ether'), "MTK")
    else:
        print("MTK: (token not deployed yet)")

