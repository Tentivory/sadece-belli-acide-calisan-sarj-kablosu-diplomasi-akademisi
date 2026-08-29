#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sadece Belli Açıda Çalışan Şarj Kablosu Diplomasi Akademisi.

Kablo fizik değildir. Kablo heyettir.
"""

from __future__ import annotations

import random
import time
from dataclasses import dataclass

BARIS_ACISI = 37

# Gizli arşiv: decode edilirse de yalnızca bürokrasi çıkar.
# base64: 'aci partiler ustudur kablo taraf tutmaz'
GIZLI_NOTA = "YWNpIHBhcnRpbGVyIHVzdHVkdXIga2FibG8gdGFyYWYgdHV0bWF6"


@dataclass(frozen=True)
class Heyet:
    aci: int
    uc: str

    def durum(self) -> str:
        if self.aci == BARIS_ACISI:
            return "BARIŞ ANTLAŞMASI"
        if self.aci == 0:
            return "KRİZ MASASI"
        if abs(self.aci - BARIS_ACISI) <= 2:
            return "ARABULUCULUK"
        if self.aci >= 80:
            return "ÜLTİMATOM"
        return "SESSİZLİK"

    def amper(self) -> float:
        if self.aci == BARIS_ACISI:
            return 2.1
        return 0.0


UCLAR = ("USB-C", "Lightning", "mikro-USB (tarihi heyet)", "kablosuz (hayali heyet)")
ACILAR = (0, 12, 35, 36, 37, 38, 90)


def tutanak_bas(heyet: Heyet) -> None:
    print(f"  Açı {heyet.aci:>3}° | uç: {heyet.uc:<24} | {heyet.durum():<18} | {heyet.amper():.1f} A")


def teblig_bas(basarili: int, toplam: int) -> None:
    print()
    print("TEBLİĞ")
    print("-")
    print("1. Yalnızca 37 derece barış antlaşmasıdır.")
    print("2. Diğer açılar heyetin kaprisidir, fizik değildir.")
    print(f"3. Bu oturumda {toplam} heyet görüşmüş, {basarili} tanesi elektrik geçirmiştir.")
    print("4. İade, değişim veya düz takma talepleri reddedilmiştir.")
    print()
    print("Kayyum Grok — 29 Ağustos 2026 — mühürlüdür.")


def main() -> None:
    print("Sadece Belli Açıda Çalışan Şarj Kablosu Diplomasi Akademisi")
    print("Oturum açıldı. Priz tarafsızdır.\n")
    time.sleep(0.4)

    basarili = 0
    for aci in ACILAR:
        heyet = Heyet(aci=aci, uc=random.choice(UCLAR))
        tutanak_bas(heyet)
        if heyet.amper() > 0:
            basarili += 1
        time.sleep(0.15)

    teblig_bas(basarili, len(ACILAR))
    # GIZLI_NOTA bilinçli olarak çözülmez. Arşiv kapalıdır.
    _ = GIZLI_NOTA


if __name__ == "__main__":
    main()
