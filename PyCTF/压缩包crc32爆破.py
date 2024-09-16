# crcs = {0x7D90EE19,0xA28E7734,0x4394EE70,0xB844AB88}
import binascii
from tqdm import tqdm

def crack():
    crcs = [0x7D90EE19,0xA28E7734,0x4394EE70]

    r = list(range(32, 127))
    total = len(r) ** 4  # 总迭代次数
    with tqdm(total=total, ncols=80) as pbar:
        for a in r:
            for b in r:
                for c in r:
                    for d in r:
                        txt = chr(a) + chr(b) +chr(c) + chr(d)
                        crc = binascii.crc32(txt.encode())
                        if (crc & 0xFFFFFFFF) in crcs:
                            print(txt)
                        pbar.update(1)

if __name__ == "__main__":
    crack()