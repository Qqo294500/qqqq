import time
import os
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
import random
import string
import ctypes
import requests
from discord_webhook import DiscordWebhook

class NitroGen:
    def __init__(self):
        self.fileName = "Discord_Nitro.txt"
    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if os.name == "nt":
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW("Дискорд генереатор и чекер от beent")
        else:
            print(f'\33]0;Дискорд генереатор и чекер от beent\a', end='', flush=True)
        print("""
        ╔══╗╔╗╔╗
        ║╔╗║║║║║
        ║╚╝╚╣╚╝║
        ║╔═╗╠═╗║
        ║╚═╝║╔╝║
        ╚═══╝╚═╝
        ╔══╗╔═══╦═══╦╗─╔╦════╗
        ║╔╗║║╔══╣╔══╣╚═╝╠═╗╔═╝
        ║╚╝╚╣╚══╣╚══╣╔╗─║─║║
        ║╔═╗║╔══╣╔══╣║╚╗║─║║
        ║╚═╝║╚══╣╚══╣║─║║─║║
        ╚═══╩═══╩═══╩╝─╚╝─╚╝""")
        time.sleep(2)
        print("Создатель - beent")
        time.sleep(3)
        num = int(input("\nВведите количество кодов для генерации и проверки: "))
        url = input("\nВы хотите использовать Discord Webhook?\nЕсли да, введите его здесь или нажмите Enter, чтобы игнорировать: ")
        print("")
        webhook = url if url != "" else None
        valid = []
        invalid = 0
        for i in range(num):
            try:
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))
                url = f"https://discord.gift/{code}"
                result = self.qchkr(url, webhook)
                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except Exception as e:
                print(f"Ошибка | {url} ")
            if os.name == "nt":
                ctypes.windll.kernel32.SetConsoleTitleW(f"Действ. - {len(valid)} || Не действ. - {invalid}")
                print("")
            else:
                print(f'\33]0;Действ. - {len(valid)} || Не действ. - {invalid}\a', end='', flush=True)
        print(f"""
============================================= Результат: =============================================
 - Действ-ых: {len(valid)}
 - Не действ-ых: {invalid}
=====================================================================================================
 - Действ-е коды: {', '.join(valid )}
======================================================================================================""")
        os.system('pause')
    def ggg(self, amount):
        with open(self.fileName, "w", encoding="utf-8") as file:
            print("Генерация началась. Подождите пожалуйста...")
            start = time.time()
            for i in range(amount):
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))
                file.write(f"https://discord.gift/{code}\n")
            print(f"Ген. коды {amount} | Затраченное время: {round(time.time() - start, 5)}s\n")
    def chkr(self, notify = None):
        valid = []
        invalid = 0
        with open(self.fileName, "r", encoding="utf-8") as file:
            for line in file.readlines():
                nitro = line.strip("\n")
                url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
                response = requests.get(url)
                if response.status_code == 200:
                    print(f" + {nitro} ")
                    valid.append(nitro)

                    if notify is not None:
                        DiscordWebhook(
                            url = notify,
                            content = f"Обнаружен действительный код Nitro! @everyone \n{nitro}"
                        ).execute()
                    else:
                        break
                else:
                    print(f" - {nitro} ")
                    invalid += 1

        return {"Действ." : valid, "Не действ." : invalid}
    def qchkr(self, nitro, notify = None):
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            print(f" Действ. - {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            with open("Discord_Nitro.txt", "w") as file:
                file.write(nitro)

            if notify is not None:
                DiscordWebhook(
                    url = notify,
                    content = f"Обнаружен действительный код Nitro! @everyone \n{nitro}"
                ).execute()
            return True
        else:
            print(f" Не действ. - {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            return False
if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()
