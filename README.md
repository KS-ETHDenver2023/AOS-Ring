
# **Alice's ring - Cryptographic verifier**

This smart contract developed during the **ETHDenver 2023 hackathon** is a part of our solvency proof : This contract allow anyone to verify an AOS ring signature based on SECP256k1.

🎯 Building a simple SoulBound Token for our solvency proof.  

🎯 Use Infura and the Truffle suite of tools for L2 and Multi-Network Deployment.

## **Configuration** 📝

1. Clone this repo 
```
git clone https://github.com/KS-ETHDenver2023/AOS-Ring.git
```
2. Install npm
```
npm install 
```
3. Install truffle
```
npm i truffle
```
4. Install hdWallet
```
npm i @truffle/hdwallet-provider
```
5. Install open zeppelin libraries
```
npm i @openzeppelin/contracts
```
6. Set up your .env file in the truffle folder
```
MNEMONIC="Your mnemonic"
API_KEY="Your infura api key"
ETHERSCAN="Your etherscan api key"
POLYGONSCAN="Your polygonscan api key"
```
7. Compile using truffle 
```
truffle compile
```
8. Deploy using truffle 
```
truffle deploy --network matic
```
9. Verify your contract on etherscan
```
truffle run verify PoS_token --network matic
```

We use the **[React Truffle Box](https://trufflesuite.com/boxes/react/)** to write, compile, test, and deploy smart contracts, and interact with them from a React app. It's a great tool for every developer and it helps us a lot during our development journey.
You can install [**Ganache**](https://trufflesuite.com/ganache/) for local development and deployment.


## Challenges and benefits when using Infura and the Truffle suite of tools 💻
Challenges :

Our challenges were numerous during the design and implementation of our project.

 - First we had to create a portable, scalable and understandable development environment for the whole team but also in view of a future reuse of the project by other developers.
 - Our project and our smart contracts must be deployed and usable on different networks (L1, L2).
 - Test, correct, deploy... We needed to have a set of easily usable and implementable tools for these actions.

Benefits 🛰️:

1.  **Convenient access to blockchain networks** : Infura provides convenient access to various networks via L1 and L2 endpoints, so we don't need to set up and maintain our own node and configure our own RPC. This save us lot of time and resources, especially during hackathon.
2.  **Reliable and scalable infrastructure**: Infura is built on top of highly reliable and scalable infrastructure, which can help ensure that our dApp remains available and responsive to users.
3.  **Simplified deployment:** Using Infura and Truffle box simplify the process of deploying and testing our multichain dApp.
4.  **Integrated with Truffle:** Truffle provides built-in support for Infura, so it's easy to configure your Truffle project to use Infura's RPC. The process of RPC configuration inside the truffle-config.js is verry simple. 
5. **Truffle for VS Code:** As developers we love using VS Code. The Truffle extension for VS Code allowed us to simplify our development process.
6. **Documentation :** The infura and truffle documentation is very detailed and simply explains via concrete examples how to set up your project.

## **Smart contract architecture**📏
The only public function is "Verify". You provide the public keys of all the members of the ring, their tees, the seed of the signature and the signed message. If the signature is valid, the output is true.


## Technology 💻

 - [Tuffle Boxes](https://trufflesuite.com/boxes/)
 - [Infura RPC provider](https://www.infura.io/)
 - [Solidity](https://soliditylang.org/)
 - [OpenZeppelin](https://www.openzeppelin.com/)

	The use of Truffle boxes very easily allowed us to have a complete and intuitive front end to test our Smarts Contracts.
	Thanks to the large number of chains supported, we first used infura's RPCs for Polygon and Ethereum networks (mainnet&testnet).
	The infura and truffle tools were also useful for the deployment of multi-chain smart contracts.
	For Scroll and zkSync networks we used the RPCs provided in their respective documentations.

## Smart contract address

Polygon mainnet : 
```
0x7709708E7Aff121164bBA336aEb9653f7467cC2A
```
Polygon ZkEVM-Testnet : 
```
0x7709708E7Aff121164bBA336aEb9653f7467cC2A
```
Polygon mumbai : 
```
0x7709708E7Aff121164bBA336aEb9653f7467cC2A
```
Scroll Alpha Testnet : 
```
0x7709708E7Aff121164bBA336aEb9653f7467cC2A
```
Sepolia testnet: 
```
0xDf5564227440F5a7Fb2c500a23490F0F846309c6
```
Goerli testnet: 
```
0xD4088C08ab1Fac0DcD261f5582dF65B7C67C9bC8
```


## Contribute ✨

Our project is intended as open source and as a tool for the Ethereum community and all web3 users. 
Feel free to contribute!

**Maxime - Thomas - Nathan - Adam | KRYPTOSPHERE®**
