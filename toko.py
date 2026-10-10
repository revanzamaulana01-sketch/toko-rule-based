# ============================================
# RULE BASED SYSTEM + FORWARD CHAINING
# Contoh: Toko Buku Sederhana
# ============================================

# --- 1. BASIS PENGETAHUAN (Fakta) ---
# Tabel barang dan harga (data mentah)
stok = {
    "buku": 25000,
    "pensil": 5000,
    "pulpen": 8000,
    "penghapus": 3000,
}

# --- 2. RULE BASE (Aturan IF-THEN) ---
# Setiap aturan: (nama, kondisi, aksi)
rules = [
    {
        "nama": "Diskon 10%",
        "kondisi": lambda fakta: fakta["total"] > 50000,
        "aksi": lambda fakta: fakta.update({"diskon": fakta["total"] * 0.10})
    },
    {
        "nama": "Potong member 5%",
        "kondisi": lambda fakta: fakta.get("member", False),
        "aksi": lambda fakta: fakta.update({"diskon_member": fakta["total"] * 0.05})
    },
    {
        "nama": "Gratis pulpen",
        "kondisi": lambda fakta: fakta.get("buku", 0) > 3,
        "aksi": lambda fakta: fakta.update({"bonus": "1 pulpen"})
    },
    {
        "nama": "Gratis penghapus",
        "kondisi": lambda fakta: fakta.get("pensil", 0) >= 5,
        "aksi": lambda fakta: fakta.update({"bonus": "1 penghapus"})
    },
]

# --- 3. MESIN INFERENSI (Forward Chaining) ---
def forward_chain(fakta_awal, rules):
    """
    Mulai dari fakta, cek aturan satu per satu,
    jalankan yang kondisinya terpenuhi,
    ulangi sampai tidak ada perubahan.
    """
    fakta = fakta_awal.copy()
    riwayat = []
    berubah = True

    while berubah:
        berubah = False
        for rule in rules:
            if rule["kondisi"](fakta):
                # Cek apakah aturan sudah pernah dijalankan
                if rule["nama"] not in riwayat:
                    rule["aksi"](fakta)
                    riwayat.append(rule["nama"])
                    berubah = True
                    print(f"  [PICU] {rule['nama']}")

    return fakta, riwayat

# --- 4. SIMULASI ---
if __name__ == "__main__":
    print("=" * 40)
    print("TOKO BUKU - Forward Chaining Demo")
    print("=" * 40)

    # Input dari "kasir" (fakta awal)
    keranjang = {
        "buku": 4,      # beli 4 buku
        "pensil": 2,    # beli 2 pensil
        "member": True, # pelanggan member
    }

    # Hitung total
    total = sum(qty * stok[item] for item, qty in keranjang.items() if item in stok)
    keranjang["total"] = total

    print(f"\nFakta awal: {keranjang}")
    print(f"Total belanja: Rp {total:,}")

    print("\n--- Proses Forward Chaining ---")
    hasil, riwayat = forward_chain(keranjang, rules)

    print("\n--- Hasil Akhir ---")
    print(f"Aturan yang terpicu: {riwayat}")
    print(f"Diskon 10%: Rp {hasil.get('diskon', 0):,.0f}")
    print(f"Diskon member 5%: Rp {hasil.get('diskon_member', 0):,.0f}")
    print(f"Bonus: {hasil.get('bonus', 'tidak ada')}")

    total_diskon = hasil.get('diskon', 0) + hasil.get('diskon_member', 0)
    bayar = total - total_diskon
    print(f"\nTotal diskon: Rp {total_diskon:,.0f}")
    print(f"BAYAR: Rp {bayar:,.0f}")
