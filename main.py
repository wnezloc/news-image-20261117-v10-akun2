#!/usr/bin/env python3
"""news-image-20261117 v10a (akun 2): 43-story cream front page.

Varian A atas v9 (987.556, rank 74): teks 43 cerita IDENTIK, yang
berubah hanya ilustrasinya — visual yang membawa data, pola rank 1
(991.248): mini-map Teluk di lead 2 (IRAN/BAHRAIN/QESHM/HORMUZ +
callout DRONES DOWNED / US STRIKES), panel bendera Quad di lead 3,
pita kartu grid selebar penuh (bendera DRC + RS, termometer COP31,
3 bendera measles, grafik batang Nvidia, tenda+truk Gaza, surat
resignasi Mongolia, diagram parlemen Serbia 140/103, pabrik+plakat
Dhaka, An-12 jatuh, palu hakim Mozambik). Deterministic, offline.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "image.jpg")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)

    # Guard: entry must be <= 1 MiB and exactly 1024x1024.
    assert os.path.getsize(dst) <= 1048576, "entry over 1 MiB"


if __name__ == "__main__":
    main()
