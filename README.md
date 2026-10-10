# Toko Rule Based System

Demo sederhana **Rule Based System** dengan **Forward Chaining** dalam Python.

## Cara Pakai

```bash
python3 toko.py
```

## Konsep

- **Basis Pengetahuan**: Tabel barang dan harga (fakta)
- **Rule Base**: Aturan IF-THEN (diskon, bonus)
- **Forward Chaining**: Mesin inferensi yang mengeksekusi aturan dari fakta menuju kesimpulan

## Contoh Output

```
========================================
TOKO BUKU - Forward Chaining Demo
========================================

Fakta awal: {'buku': 4, 'pensil': 2, 'member': True, 'total': 110000}
Total belanja: Rp 110,000

--- Proses Forward Chaining ---
  [PICU] Diskon 10%
  [PICU] Potong member 5%
  [PICU] Gratis pulpen

--- Hasil Akhir ---
Aturan yang terpicu: ['Diskon 10%', 'Potong member 5%', 'Gratis pulpen']
Diskon 10%: Rp 11,000
Diskon member 5%: Rp 5,500
Bonus: 1 pulpen

Total diskon: Rp 16,500
BAYAR: Rp 93,500
```
