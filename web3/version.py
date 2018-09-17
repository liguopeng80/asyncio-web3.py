from web3.module import (
    Module,
)


class Version(Module):
    @property
    def api(self):
        from web3 import __version__
        return __version__

    @property
    async def node(self):
        return await self.web3.manager.request_blocking("web3_clientVersion", [])

    @property
    async def network(self):
        return await self.web3.manager.request_blocking("net_version", [])

    @property
    async def ethereum(self):
        return await self.web3.manager.request_blocking("eth_protocolVersion", [])
