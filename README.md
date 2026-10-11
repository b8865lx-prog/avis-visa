# Situs AVis (avisgovisa.id)

Situs statis: Python generator, tanpa framework, hosting gratis di GitHub Pages. Data yang sering berubah dikelola lewat Google Sheets (CSV).

## Isi folder
- `build.py` : generator. Menghasilkan folder `dist/` (index, halaman negara, sitemap, robots, CNAME).
- `config.json` : domain, nomor WA, Instagram, dan link CSV Google Sheets.
- `data/` : `negara.csv`, `faq.csv`, `testimoni.csv` (cadangan kalau Sheets belum dipasang).
- `assets/` : `style.css`, `app.js`, logo, `img/` (foto negara), `testimoni/` (screenshot chat).
- `.github/workflows/deploy.yml` : build dan deploy otomatis ke GitHub Pages.

## Upload ke GitHub Pages
1. Ekstrak ZIP. Buat repo GitHub baru (public).
2. Upload **isi** folder `avisgovisa-site` (bukan folder luarnya) lewat Add file, Upload files, lalu Commit.
3. Pastikan file `.github/workflows/deploy.yml` ikut ke-upload. Kalau tidak ada, buat manual lewat Add file, Create new file, ketik path `.github/workflows/deploy.yml`, lalu salin isinya.
4. Settings, Pages, Source: pilih **GitHub Actions**.
5. Buka tab **Actions**, tunggu "Deploy" hijau. Kalau belum jalan, klik Run workflow.

## Domain avisgovisa.id
1. Settings, Pages, Custom domain: isi `avisgovisa.id`, Save.
2. Di DNS registrar, buat 4 record A untuk domain utama: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153. Lalu CNAME `www` ke `username.github.io`. Cek dokumentasi GitHub Pages kalau mau memastikan IP terbaru.
3. Tunggu DNS aktif (bisa beberapa menit sampai beberapa jam), lalu centang **Enforce HTTPS**.
4. Daftarkan `https://avisgovisa.id/sitemap.xml` di Google Search Console.

## Google Sheets
1. Buat Spreadsheet dengan 3 tab: `negara`, `faq`, `testimoni`. Kolom persis seperti file di `data/`:
   - negara: `slug,nama,kode,jenis,estimasi,badge`
   - faq: `pertanyaan,jawaban` (jawaban boleh HTML: `<b>`, `<i>`)
   - testimoni: `nama,negara,jenis,kutipan,screenshot`
2. File, Share, Publish to web. Pilih satu tab, format **CSV**, Publish, salin linknya. Ulangi untuk tiap tab.
3. Tempel link di `config.json` bagian `sheets`, lalu Commit.
4. Situs diperbarui otomatis tiap 6 jam, tiap ada commit, atau manual lewat Actions, Run workflow.

Catatan: `kode` negara pakai kode bendera 2 huruf (jp, kr, eu, au, ...). `slug` jadi alamat halaman, huruf kecil dan tanpa spasi (contoh `korea-selatan`). Negara baru di tab `negara` otomatis dapat halaman sendiri. Kolom `estimasi` kosong berarti tidak ditampilkan.

## Foto negara (pengganti ilustrasi)
Taruh foto bebas hak cipta (Unsplash/Pexels) di `assets/img/` dengan nama sesuai slug, misalnya `jepang.jpg`. Lebar sekitar 800 px, ukuran di bawah 150 KB. Otomatis dipakai menggantikan ilustrasi.

## Testimoni
Isi tab `testimoni`. Kalau ada screenshot chat WA (nama disamarkan), taruh di `assets/testimoni/` dan tulis nama file-nya di kolom `screenshot`. Kalau tab kosong, section testimoni otomatis tidak tampil.

## Mengubah teks lain
Teks beranda, cara kerja, dan footer ada di `build.py`. Warna dan tampilan ada di `assets/style.css`. Nomor WA, domain, dan Instagram ada di `config.json`.

## Kalau tampilan polos atau berantakan
- Pastikan memakai ZIP terbaru dan workflow Deploy sudah hijau.
- Refresh keras atau hapus cache browser.
- Kalau dibuka lokal, jalankan `python build.py`, lalu buka `dist/index.html` (folder `assets` harus tetap di sebelahnya).
- Bendera diambil dari flagcdn.com, jadi butuh internet.

## Cek versi build
Buka situs, klik kanan, View page source. Di baris atas harus ada `avis-build:v3-inline`. CSS, JS, dan logo sudah tertanam di tiap halaman, jadi tampilan tidak bergantung pada path folder `assets`.
