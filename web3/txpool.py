from web3.module import (
    Module,
)


class TxPool(Module):
    @property
    async def content(self):
        return await self.web3.manager.request_blocking("txpool_content", [])

    @property
    async def inspect(self):
        return await self.web3.manager.request_blocking("txpool_inspect", [])

    @property
    async def status(self):
        return await self.web3.manager.request_blocking("txpool_status", [])
