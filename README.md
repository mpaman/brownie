brownie networks add Ethereum holesky host=https://ethereum-holesky.publicnode.com chainid=17000 explorer=https://holesky.etherscan.io/api

brownie run scripts/transfer_back.py --network holesky

brownie networks add Ethereum holesky host=https://rpc.testnet.holesky.org chainid=315 name="Holesky Testnet"

brownie accounts new holesky_deployer
