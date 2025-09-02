brownie networks add Ethereum holesky host=https://ethereum-holesky.publicnode.com chainid=17000 explorer=https://holesky.etherscan.io/api

brownie run scripts/transfer_back.py --network holesky

brownie networks add Ethereum holesky host=https://rpc.testnet.holesky.org chainid=315 name="Holesky Testnet"

brownie accounts new holesky_deployer

5bc397d597d8adaf69eaf8ac5e58e56d4121ff4fb022f06973bf6d92fdcb4add
