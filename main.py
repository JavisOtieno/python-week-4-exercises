from typing import Dict, Generator


def parse_txid(txid: str) -> tuple:
    """
    Breaks down a hex transaction ID string into pairs of bytes.
    Example: 'deadbeef' -> ('de', 'ad', 'be', 'ef')
    """
    # Split the txid into 2-character chunks
    return tuple(txid[i:i+2] for i in range(0, len(txid), 2))


def create_utxo(txid: str, vout: int, amount: int) -> dict:
    """
    Builds a UTXO dictionary with the specified transaction ID, output index, and satoshi amount.
    """
    return {'txid': txid, 'vout': vout, 'amount': amount}


def update_utxo(utxo: dict, new_amount: int) -> None:
    """
    Modifies the amount value of an existing UTXO in place.
    """
    utxo.update({'amount': new_amount})


def unpack_utxo(utxo: dict) -> str:
    """
    Converts a UTXO dictionary into a human-readable summary string.
    """
    txid, vout, amount = utxo.values()
    return f"TXID: {txid}, VOUT: {vout}, Amount: {amount} BTC"


def swap_addresses(addr1: str, addr2: str) -> tuple:
    """
    Exchanges two Bitcoin addresses and returns them in reverse order.
    """
    addr1, addr2 = addr2, addr1
    return (addr1, addr2)


def unique_addresses(addresses: list) -> set:
    """
    Returns a set containing only the distinct Bitcoin addresses from the input list.
    """
    return set(addresses)


class BitcoinWallet:
    def __init__(self):
        """
        Creates a new wallet starting with no unspent outputs.
        """
        self.utxos = {}
   
    def add_utxo(self, utxo: Dict) -> None:
        """
        Stores a new UTXO using a composite key of txid:vout.
        """
        key = f"{utxo['txid']}:{utxo['vout']}"
        self.utxos[key] = utxo
   
    def get_balance(self) -> float:
        """
        Calculates and returns the total value of all UTXOs held in the wallet.
        """
        return sum(utxo['amount'] for utxo in self.utxos.values())


class TransactionPool:
    def __init__(self):
        """
        Initializes an empty mempool for pending transactions.
        """
        self.tx_pool = set()
   
    def add_transaction(self, txid: str) -> bool:
        """
        Attempts to add a transaction ID to the pool.
        Returns True if it was newly added, False if already present.
        """
        if txid in self.tx_pool:
            return False
        self.tx_pool.add(txid)
        return True
   
    def get_pool_size(self) -> int:
        """
        Returns the current number of unique pending transactions.
        """
        return len(self.tx_pool)


def block_height_generator(start: int, end: int) -> Generator[int, None, None]:
    """
    Generates a sequence of block heights from start up to (but not including) end.
    """
    for height in range(start, end):
        yield height