import json
import time
import requests
import asyncio
from hashlib import md5
from requests.exceptions import HTTPError, Timeout, RequestException


# 成功返回结果，失败返回None
def make_request(req, cur_index=0):
    api = req.get("api", None)
    method = req.get("method", "get")
    params = req.get("params", {})
    headers = req.get("headers", {})
    maxtime = req.get("maxtime", 3)
    timeout = req.get("timeout", 10)
    http_method = getattr(requests, method, requests.get)

    def retry_request():
        if cur_index <= maxtime:
            return make_request(req, cur_index + 1)
        else:
            return None

    try:
        response = http_method(api, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()
    except (HTTPError, Timeout, RequestException) as err:
        print("[request_by_rank]网络请求异常", err)
        return retry_request()

    if response.ok:
        return response.json()

    # 请求失败，重复maxtime次
    return retry_request()


async def make_request_async(req):
    if req.get("sleep", 0) != 0:
        await time.sleep(req.get("sleep"))

    print("睡醒干活", req.get("sleep"))
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, make_request, req)
    return result


# 按照次序发送N个请求，前面的成功后面的才发出。
# 如果前面的失败超过N次，那么失败的返回None。
def request_by_rank(reqs, interval=0):
    if len(reqs) == 0:
        raise ValueError("[request_by_rank]请求队列为空")

    res_list = []

    for req in reqs:
        res_list.append(make_request(req))
        # 如果调用的外部接口存在访问评率限制，请加上时间间隔
        interval and time.sleep(interval)

    return res_list


# 发起所有请求，直到所有请求都成功。
# 如果存在一个请求，始终无法成功，超过最大重试次数，那么返回其他成功的结果，并将失败的请求也一起返回
# 适用场景: 请求之间没有关系，成功的结果可以利用，失败的待后续处理
# batch_num: 每批次同时发起的请求
async def request_parallel(reqs):
    async_tasks = [make_request_async(req) for req in reqs]
    return await asyncio.gather(*async_tasks)


if __name__ == "__main__":
    # print("---------- 按顺序请求5次接口 ----------")
    # reqs = (
    #     {"api": "https://jsonplaceholder.typicode.com/todos/1", "method": "get"},
    #     {"api": "https://jsonplaceholder.typicode.com/todos/2", "method": "get"},
    #     {"api": "https://jsonplaceholder.typicode.com/todos/3", "method": "get"},
    #     {"api": "https://jsonplaceholder.typicode.com/todos/4", "method": "get"},
    #     {"api": "https://jsonplaceholder.typicode.com/todos/5", "method": "get"},
    # )
    # request_by_rank(reqs)

    # print("---------- 按顺序请求5次接口，其中第三次接口一定失败 ----------")
    # reqs = (
    #     {"api": "https://jsonplaceholder.typicode.com/todos/1", "method": "get"},
    #     {"api": "https://jsonplaceholder.typicode.com/todos/2", "method": "get"},
    #     {"api": "https://xxjsonplaceholder.typicode.com/todos/3", "method": "get"},
    #     {"api": "https://jsonplaceholder.typicode.com/todos/4", "method": "get"},
    #     {"api": "https://jsonplaceholder.typicode.com/todos/5", "method": "get"},
    # )
    # response = request_by_rank(reqs)
    # print("response", response)

    print("---------- 同时请求5次接口 ----------")
    reqs = (
        {
            "api": "https://jsonplaceholder.typicode.com/todos/1",
            "method": "get",
            "sleep": 1,
        },
        {
            "api": "https://jsonplaceholder.typicode.com/todos/2",
            "method": "get",
            "sleep": 2,
        },
        {
            "api": "https://jsonplaceholder.typicode.com/todos/3",
            "method": "get",
            "sleep": 3,
        },
        {
            "api": "https://jsonplaceholder.typicode.com/todos/4",
            "method": "get",
            "sleep": 4,
        },
        {
            "api": "https://jsonplaceholder.typicode.com/todos/5",
            "method": "get",
            "sleep": 5,
        },
    )
    # asyncio.run(request_parallel(reqs, batch_num=3))
    asyncio.run(request_parallel(reqs))
