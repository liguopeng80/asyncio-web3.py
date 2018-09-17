import asyncio
from web3 import Web3, HTTPProvider


async def print_latest_block():
    eth_node_url = "http://127.0.0.1:8545"

    w3 = Web3(HTTPProvider(eth_node_url))
    block = await w3.eth.getBlock('latest')

    print(block)


async def monitor():
    eth_node_url = "http://127.0.0.1:8545"

    w3 = Web3(HTTPProvider(eth_node_url))
    filt = await w3.eth.filter('latest')

    while True:
        entries = await filt.get_new_entries()
        if entries:
            print("got:", entries)
        await asyncio.sleep(1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.run_until_complete(print_latest_block())
    loop.run_until_complete(monitor())

    loop.close()
