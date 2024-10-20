import asyncio
from bleak import BleakScanner, BleakClient
from cheshire.compiler.state import LightState
from cheshire.generic.command import *
from cheshire.hal.devices import Connection, connect_to_ble_device


async def main():
    device = await BleakScanner.find_device_by_name(name='KS03~0698BB')

    if connection := await connect_to_ble_device(device):
        print(f"Connected to {device.name}")

    state = LightState()
    state.update(SwitchCommand(on=True))
    state.update(BrightnessCommand(0xff))
    state.update(RGBCommand(0xff, 0x40, 0x01))

    await connection.apply(state)

asyncio.run(main())
