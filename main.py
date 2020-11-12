from telethon import TelegramClient, events
import time, os
from config import cfg

# Remember to use your own values from my.telegram.org!
api_id = cfg["api_id"]
api_hash = cfg["api_hash"]
client = TelegramClient('anon', api_id, api_hash)

def callback(current, total):
    print('Uploaded', current, 'out of', total,
          'bytes: {:.2%}'.format(current / total))

def idget(data):
	if "/" in data:
		id = int((data.split("/"))[-1])
	else:
		id = int(data)
	return id

async def main():
    id_from = int(input("Chat ID> "))
    url_start = input("URL or ID Start> ")
    url_stop = input("URL or ID Stop> ")
    list = []
    id1 = idget(url_stop)
    id2 = idget(url_start)
    if id1 > id2:
    	count = id2
    	stoping = id1
    else:
    	count = id1
    	stoping = id2
    while True==True:
        list.append(str(count))
        count += 1
        if stoping  < count:
        	break
    async for message in client.iter_messages(id_from):
        if str(message.id) not in list:
            continue
        if int(message.id) < int(list[0]):
            break
        file_name = str(message.chat.id)
        os.makedirs("./downloads/"+file_name, mode=0o777, exist_ok=True)
        if message.photo:
            path = await message.download_media("./downloads/"+file_name)
            print('File saved to', path)


with client:
    client.loop.run_until_complete(main())

os.system('cls' if os.name == 'nt' else 'clear')
#-1001149528335

#await client.send_message("gfreeman_bot", 'Hello, group!', file="https://video-hw.xvideos-cdn.com/videos/mp4/c/9/3/xvideos.com_c9353fd3cd8b6603a3d09f53e3910e82.mp4?e=1604790553&h=8e96d286184d3d284be558010a43217f&download=1")
#await client.send_message(-1001242752198, 'Hello, group!', file="https://data.necrosis.ml/n2HqZkTDYmU5hEE7fx7L6x4ky3CBvbUVFctbKcFh/YYk4xTvFVWXrOA.mp4")
#await client.send_file(-1001374055263, 'cd_001.mp4', supports_streaming=True, progress_callback=callback)
#await client.send_file(-1001374055263, "https://vkvd170.mycdn.me/?sig=Mx8GZhlS62s&ct=0&srcIp=94.25.181.62&urls=185.226.53.165&expires=1605520980224&clientType=13&srcAg=UNKNOWN&fromCache=1&ms=45.136.21.172&appId=512000384397&id=695977446139&type=4", filename="d2854cf7gj.mp4", supports_streaming=True, progress_callback=callback)