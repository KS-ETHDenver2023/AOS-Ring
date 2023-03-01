
const EthUtil = require('ethereumjs-util');
const EthTx = require('ethereumjs-tx');

function getPubKey(_txSigned){
    const tx = new EthTx(_txSigned); 
    const address = EthUtil.bufferToHex(tx.getSenderAddress()); 
    const publicKey = EthUtil.bufferToHex(tx.getSenderPublicKey()); 

    console.log(address)
    console.log(publicKey)
    return (publicKey); 
}

getPubKey("0xf86d8201e1843b9aca00825208940000000044008b8ac792ef23261e05ffab590c90880ad83c657caa27be802ea099d2aee2dbbba44c27918f20fa0a91d7c2870a553ef9d1c0b2fc92de671dcf2ba03bb62b0c282195e095592b11184461ac4f66c27192034f4059457d835774c6f4")
