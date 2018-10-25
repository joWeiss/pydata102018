from iota import Address, Iota, TryteString, ProposedTransaction
from datetime import datetime

SEED = b"THISISASEED9999999999999999999999999999999999999999999999999999999999999999999999999999999"

api = Iota("https://durian.iotasalad.org:14265" , seed=SEED)

message = TryteString.from_string(f"Hi PyDATA Hamburg. It's now {datetime.now()}.")

receiver = Address(b"ANY9VALID9IOTA9ADDRESS99999999999999999999999999999999999999999999999999999999999999999999")

tx = ProposedTransaction(address=receiver, value=0, message=message)

api.send_transfer(depth=3, transfers=[tx])
