import requests,websocket,nextcord,json,threading,time,re
from nextcord.ext import commands

def runserver():
    cookies = {
        'PHPSESSID': '4ih145elu4ob203obcvgtb15u6',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': 'PHPSESSID=4ih145elu4ob203obcvgtb15u6',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://magmanode.com/server?id=420916',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'id': '420916',
        'action': 'start',
    }

    response = requests.get('https://magmanode.com/power', params=params, cookies=cookies, headers=headers)
    print(response.status_code)




def status():
    cookies = {
        'PHPSESSID': '4ih145elu4ob203obcvgtb15u6',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': 'PHPSESSID=4ih145elu4ob203obcvgtb15u6',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://magmanode.com/server?id=420916',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'id': '420916',
        'success': '4',
    }

    response = requests.get('https://magmanode.com/server', params=params, cookies=cookies, headers=headers)
    # print(response.text)
    lines = response.text.splitlines()
    
    # Tìm dòng chứa chuỗi cụ thể
    target_line = None
    for line in lines:
        if "socket.send('{\"event\":\"auth\",\"args\":[" in line:
            target_line = line.strip()
            break
    if target_line:
        with open('target_line.txt', 'w', encoding='utf-8') as file:
            file.write(target_line)
            print('da luu')
    # Đọc nội dung từ file
    with open('target_line.txt', 'r', encoding='utf-8') as file:
        line = file.readline().strip()  # Đọc dòng đầu tiên

    print(line[38:740])
    return line[38:740]

import websocket
import json
import threading

def checker():
    cpu_usage = None  # Biến để lưu giá trị CPU
    disk_usage = None  # Biến để lưu giá trị Disk

    def on_message(ws, message):
        nonlocal cpu_usage, disk_usage  # Sử dụng biến ngoài hàm
        message_data = json.loads(message)

        if message_data.get("event") == "stats":
            stats = json.loads(message_data["args"][0])  # Giả sử args là mảng
            cpu_usage = stats["cpu_absolute"]
            disk_usage = stats["disk_bytes"]

            print(f"Current CPU Usage: {cpu_usage:.2f}%")
            print(f"Current Disk Usage: {disk_usage} bytes")
            ws.close()  # Đóng kết nối sau khi nhận giá trị

    def on_error(ws, error):
        print(f"Error: {error}")

    def on_close(ws, close_status_code, close_msg):
        print("Connection closed")
    aaaaaa=status()
    def on_open(ws):
        auth_message = {
            "event": "auth",
            "args": [f"{aaaaaa}"]  # Thay thế bằng token của bạn
        }
        ws.send(json.dumps(auth_message))

    # Thay đổi URL websocket của bạn
    websocket_url = "wss://azurite.magmanode.com:8080/api/servers/6e59d2eb-8e02-43a5-b34c-08f8d69763ca/ws"
    
    ws = websocket.WebSocketApp(websocket_url,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever()  # Chạy websocket cho đến khi kết nối đóng

    return cpu_usage, disk_usage  # Trả về cả giá trị CPU và Disk

# Sử dụng hàm
if __name__ == "__main__":
    cpu_value, disk_value = checker()
    print(f"Returned CPU Usage: {cpu_value}")
    print(f"Returned Disk Usage: {disk_value} bytes")

def stop():

    cookies = {
        'PHPSESSID': '4ih145elu4ob203obcvgtb15u6',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': 'PHPSESSID=4ih145elu4ob203obcvgtb15u6',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://magmanode.com/server?id=420916',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'id': '420916',
        'action': 'stop',
    }

    response = requests.get('https://magmanode.com/power', params=params, cookies=cookies, headers=headers)


intents = nextcord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Sự kiện khi bot đã sẵn sàng
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Lệnh !server
@bot.command(name="server", help="Mở server")
async def server(ctx):
    await ctx.send("Đang mở server")
    runserver()
@bot.command(name="status", help="Gửi lời chào")
async def server(ctx):
    cpu_value, disk_value = checker()
    await ctx.send(f'CPU: {cpu_value}%\nDisk_usage: {disk_value}MB')
@bot.command(name="stop", help="Gửi lời chào")
async def server(ctx):
    stop()
    await ctx.send("Đang tắt server")
bot.run('MTI4NTk3MDY0OTIyNzA3MTUyOQ.G0iJk2.9GLNf2Oc-UcJL9yx6coyOchEBUkJEyaALdOidc')



