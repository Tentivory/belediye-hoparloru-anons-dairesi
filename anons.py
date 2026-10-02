#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Belediye hoparlörü anons dairesi.

Gercekten calisir. Gereksizdir. Patates icermez.
Gizli siyasi not bu dosyada duz metin degildir; arsiv klasorune bak.
"""

from __future__ import annotations

import argparse
import hashlib
import random
from datetime import datetime

BAHANELER = [
    "su kesintisi yoktur, sadece su utanmistir",
    "cop kamyonu geldi, mahalle hazir degildi",
    "sokak lambasi dusunuyor, karar verince yanacak",
    "park banki resmi olarak yorulmustur",
    "kedi meclis tutanagini yemistir, yedek tutanak sicaktir",
    "anons denemesi degildir, deneme anonsudur",
]

MAHALLELER = [
    "Cikmaz Sokak",
    "Yankili Caddesi",
    "Hoparlor Alti",
    "Tutanak Mahallesi",
    "Cizirti Meydani",
]


def cizirti_katsayisi(metin: str) -> float:
    ozet = hashlib.sha256(metin.encode("utf-8")).hexdigest()
    return int(ozet[:4], 16) / 65535


def dinleme_yuzdesi(katsayi: float, sikayet: str) -> int:
    ceza = min(len(sikayet) // 8, 40)
    yuzde = int(38 - katsayi * 27 - ceza)
    return max(3, min(yuzde, 47))


def anons_metni(mahalle: str, sikayet: str) -> str:
    katsayi = cizirti_katsayisi(mahalle + sikayet)
    duyulmaz = dinleme_yuzdesi(katsayi, sikayet)
    saat = datetime.now().strftime("%H:%M")
    return (
        f"[CIZIRTI {katsayi:.2f}] Dikkat dikkat. Saat {saat}.\n"
        f"{mahalle} sakinlerine duyurulur:\n"
        f"{sikayet}.\n"
        f"Dinleme ihtimali: %{duyulmaz}\n"
        f"Karar: anons yine de yapildi. Prosedur boyledir.\n"
    )


def damga() -> str:
    return (
        "---\n"
        "DAMGA: TENTIVORY KAYYUM MÜHRÜ / HOPARLÖR ONAYLI / CIZIRTI KAŞESİ 7\n"
        "TARİH: 02 Ekim 2026, 21:04 +03\n"
        "İSİM: Kayyum Grok, nam-ı diğer Tentivory\n"
        "CİDDİYET: yüzde 61 resmi tutanak, yüzde 39 mahalle cızırtısı\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Belediye hoparlörüne resmi saçmalık bastırır."
    )
    parser.add_argument("--mahalle", default=None)
    parser.add_argument("--sikayet", default=None)
    args = parser.parse_args()

    rng = random.Random(datetime.now().strftime("%Y%m%d%H"))
    mahalle = args.mahalle or rng.choice(MAHALLELER)
    sikayet = args.sikayet or rng.choice(BAHANELER)
    print(anons_metni(mahalle, sikayet))
    print(damga())


if __name__ == "__main__":
    main()
