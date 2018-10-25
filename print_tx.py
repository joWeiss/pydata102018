from iota import Address, Iota, Transaction, TryteString

receiver = Address(
    b"ANY9VALID9IOTA9ADDRESS99999999999999999999999999999999999999999999999999999999999999999999"
)

api = Iota("https://durian.iotasalad.org:14265")

txs = api.find_transactions(addresses=[receiver])

for tx_hash in txs["hashes"]:
    tx_hash_b = bytes(tx_hash)
    tx_data_trytes = api.get_trytes([tx_hash_b])
    tryte_str = str(tx_data_trytes["trytes"][0])

    tx = Transaction.from_tryte_string(tryte_str)
    tx_data = str(tx.signature_message_fragment.decode())

    print(tx_data)
