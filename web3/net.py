from web3.module import (
    Module,
)


class Net(Module):
    @property
    async def listening(self):
        return await self.web3.manager.request_blocking("net_listening", [])

    @property
    async def peerCount(self):
        return await self.web3.manager.request_blocking("net_peerCount", [])

    @property
    def chainId(self):
        return None

    @property
    async def version(self):
        return await self.web3.manager.request_blocking("net_version", [])
