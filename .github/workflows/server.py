# ——————————————导入库——————————————
import uvicorn
from fastapi import FastAPI
import os

# ——————————————创建app——————————————
import uvicorn
from fastapi import FastAPI
app = FastAPI()

# ——————————————get——————————————
@app.get("/aaa")
async def root():
    return {"message": "this is aaa"}


# ——————————————启动服务——————————————
if __name__ == "__main__":
    port = int(os.getenv("PORT", 7004)) # 端口
    host = os.getenv("HOST", "0.0.0.0") # 主机

    uvicorn.run("server:app", host=host, port=port,reload=True) # 启动服务