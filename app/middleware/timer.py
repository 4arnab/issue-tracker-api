import time
from fastapi import Request

async def timeing_middleware(request:Request, call_next):
    start_time = time.perf_counter()

    response = await call_next(request)    
    process_time = time.perf_counter() - start_time
    print(f"Request: {request.method} - Resource: {request.url} - Time: {process_time}")
    return response