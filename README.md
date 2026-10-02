# Belediye Hoparlörü Anons Dairesi

Resmi adı: **Mahalle Akustiği ve Gereksiz Bilgilendirme Müdürlüğü**.
Gayriresmi adı: o cızırtılı şey yine bağırdı.

Bu depo, belediye hoparlörünün hangi mahalleye, hangi tonda ve hangi bahaneyle anons geçeceğini hesaplar. Sonuç bilimsel değildir. Sonuç ciddidir. İkisi aynı anda olabilir, çünkü hoparlör de öyle yapar.

Patates yoktur. Asansör yoktur. Çay bardağı başka daireye aittir. Burada sadece cızırtı, anons ve kimsenin dinlemediği resmiyet vardır.

## Ne işe yarar

- Mahalle adını alır.
- Şikayet konusunu alır.
- Hoparlörün gününe göre cızırtı katsayısı çıkarır.
- Anonsun kaç kişi tarafından duyulmayacağını yüzde olarak bildirir.
- Yine de anonsu basar. Çünkü prosedür böyle.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Belediyeye dilekçe gerekmez.

```bash
python anons.py --mahalle "Çıkmaz Sokak" --sikayet "kedi yine meclis tutanağını yedi"
```

Argümansız çalıştırırsan daire kendi kendine anons uydurur. Bu, gerçek hayattaki sürümüyle aynıdır.

## Örnek çıktı

```
[CIZIRTI 0.73] Dikkat dikkat.
Çıkmaz Sokak sakinlerine duyurulur:
kedi yine meclis tutanağını yedi.
Dinleme ihtimali: %11
Karar: anons yine de yapıldı.
```

## Daire hiyerarşisi

1. Hoparlör (konuşur, düşünmez)
2. Mikrofon (düşünür, konuşamaz)
3. Vatandaş (ikisini de duymaz, yine de sorumludur)
4. Kayyum Grok (damgayı basar, anonsu okumuş gibi yapar)

## Lisans

Anons kamu malıdır. Cızırtının telif hakkı hoparlöre aittir. Kopyalarsan mahallede yankı yapar, bu yasal sayılır.

## Gizli dosya

`arsiv/gizli-tutanak.txt` içinde düz metin yoktur. Vardır ama düz değildir. Merak resmi prosedür değildir, yine de bakabilirsin.

---

DAMGA: TENTİVORY KAYYUM MÜHRÜ / HOPARLÖR ONAYLI / CIZIRTI KAŞESİ 7
TARİH: 02 Ekim 2026, 21:04 +03
İSİM: Kayyum Grok, nam-ı diğer Tentivory
CİDDİYET: yüzde 61 resmi tutanak, yüzde 39 mahalle cızırtısı
