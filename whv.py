# Sub page Program Pendampingan Pra-ballot WHV 2026 Australia + pop up promo di main page.
# Konten mengikuti MASTER BRIEF. Angka/kuota dibaca dari config.json (kunci whv_kuota).
import json, re
from html import escape as e

SLUG = '/whv_2026/'
OFFICIAL = 'https://immi.homeaffairs.gov.au/what-we-do/whm-program/status-of-country-caps'
WA_MSG = ('Halo AVis, saya tertarik dengan Program Pendampingan Pra-ballot WHV 2026 Australia.\n\n'
          'Saya ingin mengetahui cakupan program, dokumen yang perlu dipersiapkan, '
          'dan ketentuan harga early bird Rp999.000.\n\n'
          'Mohon informasi lebih lanjut. Terima kasih.')
DISCLAIMER = 'Tidak menjamin terpilih dalam ballot atau memperoleh visa Australia.'


def kuota_text(C):
    return 'Kuota terbatas: maksimal %d peserta per periode, agar kualitas pendampingan tetap terjaga.' % C.get('whv_kuota', 30)


def promo(C):
    k = C.get('whv_kuota', 30)
    return ('<div class="pm" id="promo" role="dialog" aria-modal="true" aria-labelledby="pmt" aria-hidden="true">'
            '<div class="pmc"><button class="pmx" type="button" data-x aria-label="Tutup">&times;</button>'
            '<div class="pmh"><span class="pmb2">PROMO EARLY BIRD</span>'
            '<h2 id="pmt">Program Pendampingan Pra-ballot WHV 2026 Australia</h2></div>'
            '<div class="pmbd"><p class="pmp"><s>Rp1.499.000</s> <b>Rp999.000</b></p>'
            '<p class="pms">Termasuk biaya registrasi ballot resmi. Hemat Rp500.000.</p>'
            '<p class="pmq">Kuota terbatas: maksimal %d peserta per periode.</p>'
            '<a class="btn pmb" href="%s?utm_source=website&amp;utm_medium=popup&amp;utm_campaign=whv_2026">Lihat Program</a>'
            '<button class="pml" type="button" data-x>Nanti saja</button>'
            '<p class="pmd">%s</p></div></div></div>') % (k, SLUG, DISCLAIMER)


def build(C, D, page, wa, w, ld, art, flag, urls):
    link = wa(WA_MSG)
    kt = e(kuota_text(C))

    def cta(label, cls=''):
        return '<a class="btn %s" href="%s" target="_blank" rel="noopener">%s</a>' % (cls, link, label)

    # ---------- FRAME 1: HERO ----------
    hero = ('<section class="hero wh"><div class="w whg"><div class="whc">'
            '<p class="tag">PROGRAM PENDAMPINGAN PRA-BALLOT WHV 2026 AUSTRALIA</p>'
            '<h1>Persiapan WHV Australia Lebih Praktis. Dokumen Dibantu, Registrasi Didampingi.</h1>'
            '<p class="sub">Persiapkan dokumen dan proses registrasi ballot WHV Australia bersama AVis. '
            'Kami membantu menyiapkan dokumen terkait dan menangani proses registrasi sesuai prosedur, '
            'sementara Anda tetap menandatangani sendiri dokumen yang memerlukan tanda tangan pribadi.</p>'
            '<div class="whpr"><span class="whlb">EARLY BIRD</span>'
            '<div class="whnum"><s>Rp1.499.000</s><b>Rp999.000</b></div>'
            '<small>Termasuk biaya registrasi ballot resmi.</small></div>'
            '<p class="whq">%s</p>%s'
            '<p class="note">%s</p></div>'
            '<div class="whv" aria-hidden="true">%s<span class="fl"><img src="%s" alt="" width="48" height="48"></span></div>'
            '</div></section>') % (kt, cta('KONSULTASI WHV SEKARANG'), DISCLAIMER, art('australia'), flag('au'))

    # ---------- FRAME 2: MASALAH ----------
    masalah = [('Dokumen', 'Bingung dokumen apa yang perlu dipersiapkan.'),
               ('Persiapan', 'Khawatir ada informasi yang tidak konsisten atau terlewat.'),
               ('Registrasi', 'Tidak yakin bagaimana mengikuti prosedur resmi dengan benar.')]
    f2 = ('<section><div class="t"><h2>Banyak yang Ingin Ikut WHV Australia, tetapi Bingung Harus Mulai dari Mana.</h2></div>'
          '<div class="w whcards">%s</div>'
          '<p class="whend w">AVis membantu menyiapkan dokumen dan menangani proses registrasi sesuai cakupan program, '
          'sehingga Anda tidak harus mengurus seluruh persiapan sendirian.</p></section>') % ''.join(
        '<div class="whcard rv"><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in masalah)

    # ---------- FRAME 3: SOLUSI ----------
    manfaat = [('01', 'Persiapan dokumen', 'AVis membantu menyiapkan dokumen terkait sesuai kebutuhan program.'),
               ('02', 'Pemeriksaan dokumen', 'Dokumen diperiksa agar informasi dan kelengkapannya sesuai dengan persyaratan yang berlaku.'),
               ('03', 'Proses registrasi ballot', 'AVis membantu menangani proses registrasi sesuai prosedur resmi dan batas kewenangan yang berlaku.'),
               ('04', 'Tanda tangan tetap oleh klien', 'Dokumen yang membutuhkan tanda tangan pribadi tetap ditandatangani oleh klien.')]
    f3 = ('<section><div class="t"><h2>Bukan Sekadar Konsultasi. AVis Membantu Menyiapkan Dokumen dan Proses Registrasi Ballot.</h2></div>'
          '<div class="w whcards whc4">%s</div></section>') % ''.join(
        '<div class="whcard rv"><span class="whn">%s</span><h3>%s</h3><p>%s</p></div>' % (n, e(a), e(b)) for n, a, b in manfaat)

    # ---------- FRAME 4: HARGA & PAKET ----------
    tabel = [('Penyusunan dokumen', 'Dibantu AVis'),
             ('Pemeriksaan dokumen', 'Dibantu AVis'),
             ('Proses registrasi ballot', 'Dibantu AVis sesuai prosedur'),
             ('Tanda tangan dokumen', 'Dilakukan klien jika diperlukan'),
             ('Biaya registrasi ballot resmi', 'Termasuk dalam harga early bird'),
             ('Hasil ballot', 'Tidak dijamin'),
             ('Persetujuan visa', 'Tidak dijamin')]
    f4 = ('<section id="harga"><div class="t"><h2>Satu Program untuk Membantu Persiapan Pra-ballot WHV Australia.</h2></div>'
          '<div class="w"><div class="whcmp"><div><small>Harga normal</small><s>Rp1.499.000</s></div>'
          '<div class="whe"><small>Harga early bird</small><b>Rp999.000</b></div></div>'
          '<p class="whsv">Hemat Rp500.000.</p><p class="whq c">%s</p>'
          '<div class="whtb"><table><thead><tr><th>Komponen</th><th>Cakupan</th></tr></thead><tbody>%s</tbody></table></div>'
          '<p class="fnote">Biaya di luar cakupan program dijelaskan terpisah saat konsultasi.</p>'
          '<div class="whctr">%s</div></div></section>') % (
        kt, ''.join('<tr><td>%s</td><td>%s</td></tr>' % (e(a), e(b)) for a, b in tabel),
        cta('SAYA INGIN MENGIKUTI PROGRAM WHV'))

    # ---------- FRAME 5: CARA KERJA ----------
    langkah = [('Konsultasi awal', 'Calon peserta menjelaskan kebutuhan dan kesiapan awal.'),
               ('Konfirmasi program', 'AVis menjelaskan cakupan layanan, biaya, dan dokumen yang diperlukan.'),
               ('Persiapan dokumen', 'Klien memberikan informasi yang benar dan dokumen yang dibutuhkan. AVis membantu menyiapkan serta memeriksanya.'),
               ('Persetujuan dan registrasi', 'Klien menandatangani dokumen yang memerlukan tanda tangan pribadi. Proses registrasi ditangani sesuai prosedur resmi dan kewenangan yang berlaku.'),
               ('Konfirmasi status registrasi', 'Status registrasi dikonfirmasi berdasarkan bukti resmi yang tersedia.')]
    f5 = ('<section id="cara-kerja"><div class="t"><h2>Dari Persiapan Dokumen hingga Registrasi Ballot, Ada AVis yang Mendampingi.</h2></div>'
          '<div class="steps whst rv">%s</div>'
          '<p class="whnote w"><b>Penting:</b> konfirmasi registrasi tidak sama dengan terpilih dalam ballot atau memperoleh visa.</p></section>') % ''.join(
        '<div class="st"><b>%d</b><h3>%s</h3><p>%s</p></div>' % (i, e(a), e(b)) for i, (a, b) in enumerate(langkah, 1))

    # ---------- FRAME 6: KEPERCAYAAN ----------
    trust = [('Cakupan transparan', 'Pelanggan mengetahui apa yang termasuk dalam program.'),
             ('Proses terarah', 'Pelanggan mengetahui tahapan dan dokumen yang perlu disiapkan.'),
             ('Ekspektasi realistis', 'Registrasi ballot tidak sama dengan terpilih dalam ballot atau memperoleh visa.')]
    f6 = ('<section><div class="t"><h2>Pendampingan yang Jelas, Tanpa Janji Hasil yang Tidak Bisa Dijamin.</h2></div>'
          '<div class="w whcards">%s</div></section>') % ''.join(
        '<div class="whcard rv"><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in trust)

    # ---------- FRAME 7: FAQ ----------
    faqs = [('Apakah Rp999.000 sudah termasuk biaya registrasi ballot?',
             'Ya. Harga early bird Rp999.000 sudah termasuk biaya registrasi ballot resmi sesuai cakupan program. Biaya lain di luar cakupan harus dijelaskan terpisah.'),
            ('Apakah AVis membantu menyiapkan dokumen?',
             'Ya. AVis membantu menyiapkan dan memeriksa dokumen terkait sesuai kebutuhan program.'),
            ('Apakah AVis menangani proses registrasi?',
             'AVis membantu menangani proses registrasi sesuai prosedur resmi dan batas kewenangan yang berlaku. Klien tetap melakukan tindakan pribadi yang diwajibkan oleh sistem.'),
            ('Apakah saya pasti terpilih dalam ballot?',
             'Tidak. Pemilihan peserta ballot tidak dapat dijamin oleh AVis.'),
            ('Apakah program ini menjamin visa disetujui?',
             'Tidak. Keputusan visa berada pada otoritas Australia.'),
            ('Kapan ballot dibuka?',
             'Mengikuti pengumuman resmi Department of Home Affairs Australia. Pantau status terbarunya di '
             '<a href="%s" target="_blank" rel="noopener"><u>halaman resmi Home Affairs</u></a>.' % OFFICIAL)]
    f7 = ('<section id="faq"><div class="t"><h2>Pertanyaan yang Sering Diajukan</h2></div><div class="w faq">%s</div></section>') % ''.join(
        '<details><summary>%s</summary><div class="a">%s</div></details>' % (e(q), a) for q, a in faqs)

    # ---------- FRAME 8: CTA PENUTUP ----------
    f8 = ('<section class="whfin"><div class="w"><h2>Ingin Mempersiapkan WHV Australia dengan Lebih Praktis?</h2>'
          '<p>Mulai dengan konsultasi awal untuk memahami cakupan program, dokumen yang diperlukan, dan proses yang harus dijalani.</p>'
          '<p class="whfp">Early bird Rp999.000 &mdash; termasuk biaya registrasi ballot resmi.</p>'
          '<p class="whq c">%s</p>%s<p class="note">Program tidak menjamin hasil ballot maupun persetujuan visa.</p></div></section>') % (
        kt, cta('KONSULTASI VIA WHATSAPP'))

    body = '<main>%s%s%s%s%s%s%s%s</main>' % (hero, f2, f3, f4, f5, f6, f7, f8)

    title = 'Program Pendampingan Pra-ballot WHV 2026 Australia | AVis'
    desc = ('Pendampingan persiapan dokumen dan registrasi ballot WHV Australia 2026 bersama AVis. '
            'Early bird Rp999.000, termasuk biaya registrasi ballot resmi. Tidak menjamin hasil ballot atau visa.')
    fq = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": q,
                          "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a)}} for q, a in faqs]}
    h = page(SLUG, title, desc, body, ld(fq))
    # semua tombol/link WA umum di halaman ini (header, footer, tombol melayang) memakai pesan WHV
    h = h.replace(wa('Halo AVis, saya mau konsultasi visa.'), link)
    urls.append(SLUG)
    w(SLUG[1:] + 'index.html', h)
