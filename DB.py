from core.globalVars import FROM
from core.globalVars import ZERO_ADDRESS
class DB:
    blockNumber: int
    hash: str
    nonce: int
    blockHash: str
    transactionIndex: int
    confirmations: int
    contractAddress: str
    cumulativeGasUsed: int
    from_: str # because "from" is reserved keyword
    functionName: str
    gas: int
    gasPrice: int
    gasUsed: int
    hash: str
    input: str
    isError: int
    methodId: str
    timeStamp: int
    to: str
    transactionIndex: int
    txreceipt_status: str
    value: int
    size: int # not part of EVM tx

    def __init__(
        self,
        hash: str = None,
        nonce: int = None,
        blockHash: str = None,
        transactionIndex: int = None,
        confirmations: int = None,
        contractAddress: str = None,
        cumulativeGasUsed: int = None,
        from_: str = ZERO_ADDRESS,
        functionName: str = None,
        gas: int = None,
        gasPrice: int = None,
        gasUsed: int = None,
        input: str = None,
        isError: int = None,
        methodId: str = None,
        timeStamp: int = None,
        to: str = ZERO_ADDRESS,
        txreceipt_status: str = None,
        value: int = None,
        blockNumber: int = None,
        size: int = 0
    ):
        self.blockNumber = blockNumber
        self.hash = hash
        self.nonce = nonce
        self.blockHash = blockHash
        self.transactionIndex = transactionIndex
        self.confirmations = confirmations
        self.contractAddress = contractAddress
        self.cumulativeGasUsed = cumulativeGasUsed
        self.from_ = from_
        setattr(self, FROM, from_)  
        self.functionName = functionName
        self.gas = gas
        self.gasPrice = gasPrice
        self.gasUsed = gasUsed
        self.input = input
        self.isError = isError
        self.methodId = methodId
        self.timeStamp = timeStamp
        self.to = to
        self.txreceipt_status = txreceipt_status
        self.value = value
        self.size = size 

    def print_details(self):
        print("blockNumber:", self.blockNumber)
        print("hash:", self.hash)
        print("nonce:", self.nonce)
        print("blockHash:", self.blockHash)
        print("transactionIndex:", self.transactionIndex)
        print("confirmations:", self.confirmations)
        print("contractAddress:", self.contractAddress)
        print("cumulativeGasUsed:", self.cumulativeGasUsed)
        print("from_:", self.from_)
        print("functionName:", self.functionName)
        print("gas:", self.gas)
        print("gasPrice:", self.gasPrice)
        print("gasUsed:", self.gasUsed)
        print("input:", self.input)
        print("isError:", self.isError)
        print("methodId:", self.methodId)
        print("timeStamp:", self.timeStamp)
        print("to:", self.to)
        print("txreceipt_status:", self.txreceipt_status)
        print("value:", self.value)

    def set_attr(self, attr, value):
        if attr == "from":
            setattr(self, FROM, value)
        setattr(self, attr, value)
        pass
