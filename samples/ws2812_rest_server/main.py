import uos
import gc
from wifi import connect_to_network
from rest_server_led import LedEffectsRESTServer

def print_device_memory():
    space = uos.statvfs('/')
    total = space[0] * space[2]
    free = space[0] * space[3]
    used = total - free
    print(f'{space}')
    print(f'Total space : {total} Free space : {free} Used space : {used}')

def print_ram_usage():
    gc.collect()
    free_memory = gc.mem_free()
    allocated_memory = gc.mem_alloc()
    total_memory = free_memory + allocated_memory

    print(f"Static RAM Usage:")
    print(f"  Total: {total_memory} bytes")
    print(f"  Free: {free_memory} bytes")
    print(f"  Used: {allocated_memory} bytes")


if __name__ == "__main__":

    print_device_memory()
    print_ram_usage()

    connect_to_network()

    led_server = LedEffectsRESTServer()
    led_server.server_run()