<img src="assets/logo.png" width="96" align="right" alt="logo">

# SVG Varyant Üretici

Şablon dosyalarındaki (Illustrator `.ai` / `.eps` ya da `.svg`) isimlendirilmiş yazı katmanlarını bir tablodaki verilerle doldurup her satır için ayrı dosya (EPS, PDF, AI ya da SVG) üreten Windows masaüstü programı. Forma, tişört, yaka kartı gibi isim/numara baskılı işlerde tek tek elle yazmak yerine kullanılır.

## Nasıl çalışır

1. Şablonlarda değişecek yazı katmanlarına `ALAN_ŞABLON` biçiminde isim verin. Dosya adı şablonun adıdır.

   | Dosya | Katman isimleri | Alanlar |
   |---|---|---|
   | `M.ai` | `NAME_M`, `NUMBER_M` | NAME, NUMBER |
   | `XL.eps` | `NAME_XL`, `NUMBER_XL` | NAME, NUMBER |

   İsim, yazı nesnesinin kendisine ya da içinde yalnızca o yazının bulunduğu katmana/gruba verilebilir.

2. Programda şablon klasörünü seçip **Analiz Et**'e basın; alanlar otomatik bulunur.
3. Veri tablosunu doldurun: elle, çoklu satır yapıştırarak ya da Excel/CSV/TXT yükleyerek.
4. Dosya adı kalıbını ve seçenekleri belirleyin, **Kontrol Et** ile deneyin, **ÜRET** ile dosyaları yazın.

## Illustrator şablonları (.ai / .eps)

`.ai` ve `.eps` şablonlar, bilgisayarda kurulu Illustrator'a arka planda bağlanılarak (COM + ExtendScript) açılır ve düzenlenir. Paragraf hizası, kerning, font, efektler ve alan yazıları Illustrator'da nasılsa öyle kalır. Çıktı biçimi 3. sekmeden seçilir:

- **EPS** (varsayılan): fontlar gömülür.
- **PDF**: Illustrator'da düzenlenebilir kalır.
- **AI**

Orijinal şablon hiçbir zaman kaydedilmez; üretimde şablon bir kez açılır, her satır "farklı kaydet" ile yazılır ve sonunda kaydetmeden kapatılır. Şablon o sırada Illustrator'da açıksa üretim durur ve kapatılması istenir. Analiz sonuçları dosya değişene kadar saklanır (`svg-varyant-ai-onbellek.json`); bu yüzden program açılışında ve **Kontrol Et**'te Illustrator gerekmez. Aynı klasörde aynı adlı `.ai` ve `.svg` varsa Illustrator dosyası kullanılır.

## Özellikler

- **Analiz:** Klasördeki AI, EPS ve SVG şablonları tarar, isimli yazı katmanlarını ve hangi şablonda eksik olduklarını gösterir. Bir üründe birden fazla değişken alan olabilir (isim, numara, kan grubu…).
- **Toplu giriş:** Beden sütunu ve şablonda bulunan her alan ayrı bir kutudur; her kutuya satır başına bir değer yazılır ya da yapıştırılır. Excel'den birlikte kopyalanan sütunlar kutulara dağıtılır. Tablodaki sütun başlığına tıklamak o sütunun toplu girişini açar.
- **Veri girişi:** Düzenlenebilir tablo, Excel/CSV/TXT içe aktarma, otomatik sütun eşleştirme. `2XL` yazılan beden `XXL` şablonunu (ve tersini) bulur.
- **Excel:** Boş veri şablonu indirme, tabloyu Excel'e aktarma.
- **Dosya adı:** `{Beden}_{NAME}`, `{sıra:03}`, `{tarih}` gibi kalıplar; kalıpta `/` ile alt klasör; isteğe bağlı olarak tablodaki "Dosya Adı" sütunundan.
- **Alan ayarları:** Harf dönüşümü (Türkçe İ/ı uyumlu), önek/sonek, boş değer davranışı.
- **Hizalama:** `.ai`/`.eps` şablonlarda Illustrator'daki paragraf hizası korunur; "Ortalı"/"Sağa yaslı" ayrıca yeni yazıyı örnek yazının ortasına/sağ kenarına oturtur. SVG şablonlarda Illustrator ortalı yazıyı sol başlangıç noktasıyla kaydeder. Alan "Ortalı" ya da "Sağa yaslı" seçilirse yeni yazı, şablondaki örnek yazının fonttan ölçülen ortasına/sağ kenarına göre yerleşir; böylece isim ve numara birbirine ortalı kalır.
- **Kodlama (SVG):** `iso-8859-1` gibi Türkçe harfleri içermeyen kodlamayla kaydedilmiş şablonlarda ı, ş, ğ, İ sayısal karakter başvurusu olarak yazılır.
- **Font küçültme:** Yazı belirlenen karakter sayısını aşarsa font boyutu orantılı küçültülür, alt sınır yüzdesiyle.
- **Font denetimi:** Şablondaki fontu bilgisayarda bulup yazıdaki her harfin fontta olup olmadığına bakar (ör. Türkçe İ, Ğ, Ş). Analiz tablosunda fontun Türkçe desteği görünür. Harfi eksik ya da karakter sınırını aşan çıktılar üretimde sorularak `KONTROL-EDILECEK` klasörüne ayrılır.
- **Güvenlik:** Orijinal şablonları koruma, mevcut dosyalar için üzerine yaz / atla / numara ekle.
- **Rapor:** Şablonu eksik satırlar, küçültülen fontlar, boş alanlar ve üretilen dosyalar.
- **Proje dosyası:** Tüm ayarlar ve tablo `.svgproje` olarak kaydedilir.

## Çalıştırma

Python 3.10+ ile (`.ai`/`.eps` şablonlar için Illustrator kurulu olmalı):

```
pip install -r requirements.txt
python svg_varyant.pyw
```

Taşınabilir tek dosyalık exe üretmek için `build.bat` dosyasını çalıştırın; çıktı `dist\SVG-Varyant-Uretici.exe` olur. Exe, ayarlarını kendi yanındaki `svg-varyant-oturum.json` dosyasında tutar.

## Sınırlar

- Katman canlı yazı olmalıdır; outline'a çevrilmiş yazılar değiştirilemez.
- Yeni yazı, şablondaki yazının ilk harfinin biçimini alır (karışık biçimli yazılar tek biçime iner).
- SVG'de birden fazla parçadan (`<tspan>`) oluşan yazılarda yeni metin ilk parçaya yazılır, diğerleri silinir.
- Font küçültme gerçek genişliğe değil karakter sayısına bakar.
- SVG çıktılarda fontların baskı bilgisayarında kurulu olması gerekir (EPS'de fontlar gömülür).
