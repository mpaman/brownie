from brownie import accounts, MockToken, Wei

def test_eth_transfer():
    a0, a1 = accounts[0], accounts[1]
    before = a1.balance()
    tx = a0.transfer(a1, Wei("0.2 ether"))
    assert a1.balance() - before == Wei("0.2 ether")
    assert tx.status == 1

def test_token_transfer():
    a0, a1 = accounts[0], accounts[1]
    token = MockToken.deploy("MockToken", "MTK", Wei("10000 ether"), {"from": a0})
    before = token.balanceOf(a1)
    tx = token.transfer(a1, Wei("500 ether"), {"from": a0})
    assert token.balanceOf(a1) - before == Wei("500 ether")
    assert tx.status == 1
