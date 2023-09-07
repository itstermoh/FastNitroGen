import asyncio
import random
import string
import aiohttp
from colorama import Fore
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

async def checko(session, code):
    url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    async with session.get(url) as response:
        status = response.status
        if status == 200:
            print(f"{bcolors.OKGREEN} WORKING | {code} ")
            return True
        elif status == 405:
            print(f"{bcolors.FAIL} NOT ALLOWED | {code}")
        elif status == 404:
            print(f"{bcolors.BOLD}{bcolors.FAIL}404 NOT FOUND | {code}")
        else:
            print(Fore.RED + f"NOT WORKING | {code} ")
        return False

async def main():
    async with aiohttp.ClientSession() as session:
        while True:
            start_time = 0
            tasks = []
            for i in range(1000):
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))
                task = asyncio.ensure_future(checko(session, code))
                tasks.append(task)
            await asyncio.gather(*tasks)
            elapsed_time = 0

asyncio.run(main())
