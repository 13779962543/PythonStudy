import requests
import asyncio
import time
#使用该模块中的ClientSession
import aiohttp

start=time.time()
urls=[
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/lei',
    'http://127.0.0.1:5000/bai',
]
async def get_page(url):
    # print('正在下载',url)
    #requests请求是基于同步的,必须使用基于异步网络请求模块进行值得url的发送请求
    #aiohttp:基于异步网络同步模块
    # response=requests.get(url=url)
    # print('下载完毕:',response.text)
    async with aiohttp.ClientSession() as session:
        async with await session.get(url) as response:
            #text()方法返回字符串形式的响应数据
            #read()返回的是二进制形式的响应数据
            #json()返回的就是json对象
            page_text=await response.text()
            print(page_text)

tasks=[]
for url in urls:
    c=get_page(url)
    task=asyncio.ensure_future(c)
    tasks.append(task)

loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end=time.time()
print('总耗时:',end-start)