from deta import Deta
from os import getenv

deta = Deta(getenv("a03vyjl3_kXKgauR1j2cTFWMnqD6yo1JDZYP8CyGH")) 


def client_db():
    return deta.Base("client")


def notification_db():
    return deta.Base("notification")


def command_db():
    return deta.Base("command")


def auth_db():
    return deta.Base("auth")


async def tear_drive():
    return deta.Drive("teardroid")
