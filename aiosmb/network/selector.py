from aiosmb.commons.connection.proxy import SMBProxyType
from aiosmb.network.tcp import TCPSocket
from aiosmb.network.socks5 import Socks5ProxyConnection
from aiosmb.network.multiplexornetwork import MultiplexorProxyConnection



class NetworkSelector:
    def __init__(self):
        pass

    @staticmethod
    async def select(target):
        if target.proxy is None:
            return TCPSocket(target = target)
        elif target.proxy.type in [SMBProxyType.SOCKS5, SMBProxyType.SOCKS5_SSL]:
            return Socks5ProxyConnection(target = target)

        elif target.proxy.type in [SMBProxyType.MULTIPLEXOR, SMBProxyType.MULTIPLEXOR_SSL]:
            mpc = MultiplexorProxyConnection(target)
            socks_proxy = await mpc.connect()
            return socks_proxy

        return None