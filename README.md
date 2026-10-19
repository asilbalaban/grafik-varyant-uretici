<img src="assets/logo.png" width="96" align="right" alt="logo">

# Grafik Varyant Üretici

Şablon grafik dosyalarındaki isimlendirilmiş yazı alanlarını bir tablodaki verilerle doldurup her satır için ayrı dosya üreten Windows masaüstü programı. Forma, tişört, yaka kartı gibi isim/numara baskılı işlerde tek tek elle yazmak yerine kullanılır.

Program üç sekmeden oluşur; her sekme bir şablon türüdür ve kendi klasörlerini, alan ayarlarını ve veri tablosunu ayrı tutar:

| Sekme | Şablon | Çıktı | Gereken |
|---|---|---|---|
| **SVG** | `.svg` | SVG | – |
| **EPS (Illustrator ile)** | `.ai`, `.eps` | EPS (varsayılan), PDF, AI ya da TIFF | Bilgisayarda kurulu Illustrator |
| **PDF (Illustrator'süz)** | `.pdf` | PDF | Yazıdaki fontun bilgisayarda kurulu olması |

## Nasıl çalışır

1. Şablonlarda değişecek yazılara `ALAN_ŞABLON` biçiminde isim verin. Dosya adı şablonun (bedenin) adıdır.

   | Dosya | İsimler | Alanlar |
   |---|---|---|
   | `M.ai` | `NAME_M`, `NUMBER_M` | NAME, NUMBER |
   | `XL.ai` | `NAME_XL`, `NUMBER_XL` | NAME, NUMBER |

2. Şablon türünün sekmesinde şablon klasörünü seçip **Analiz Et**'e basın; alanlar otomatik bulunur.
3. Veri tablosunu doldurun: elle, çoklu satır yapıştırarak ya da Excel/CSV/TXT yükleyerek.
4. Dosya adı kalıbını ve seçenekleri belirleyin, **Kontrol Et** ile deneyin, **ÜRET** ile dosyaları yazın.

## SVG

Yazı katmanlarına Illustrator'da `NAME_M` gibi isim verip SVG olarak kaydedin. Illustrator ortalı yazıyı SVG'ye sol başlangıç noktasıyla kaydettiği için, alan "Ortalı" ya da "Sağa yaslı" seçilirse yeni yazı şablondaki örnek yazının fonttan ölçülen ortasına/sağ kenarına göre yerleşir. `iso-8859-1` gibi Türkçe harfleri içermeyen kodlamayla kaydedilmiş şablonlarda ı, ş, ğ, İ sayısal karakter başvurusu olarak yazılır. Çıktıdaki fontların baskı bilgisayarında kurulu olması gerekir.

## EPS (Illustrator ile)

`.ai` ve `.eps` şablonlar, bilgisayarda kurulu Illustrator'a arka planda bağlanılarak (COM + ExtendScript) açılır ve düzenlenir. Paragraf hizası, kerning, font, efektler ve alan yazıları Illustrator'da nasılsa öyle kalır. İsim, yazı nesnesinin kendisine ya da içinde yalnızca o yazının bulunduğu katmana/gruba verilebilir. Çıktı biçimi 3. sekmeden seçilir:

- **EPS** (varsayılan): fontlar gömülür.
- **PDF**: Illustrator'da düzenlenebilir kalır.
- **AI**
- **TIFF**: Illustrator'ın kendi dışa aktarmasıyla, çalışma yüzeyi sınırında ve LZW sıkıştırmalı. Çözünürlük (dpi) ve renk modu (CMYK / RGB) aynı bölümden seçilir.

Daha önce üretilmiş EPS'ler için **4. Üret** sekmesindeki **Hazır EPS / AI dosyalarını TIFF'e çevir** bölümü kullanılır: bir klasör (ör. export) seçilir, içindeki her `.eps` / `.ai` Illustrator'da açılıp yanına aynı adlı `.tif` olarak dışa aktarılır. İstenirse alt klasörler de taranır ve TIFF'i zaten olan dosyalar atlanır. Kaynak dosyalar kaydedilmez.

Orijinal şablon hiçbir zaman kaydedilmez; üretimde şablon bir kez açılır, her satır "farklı kaydet" ile yazılır ve sonunda kaydetmeden kapatılır. Şablon o sırada Illustrator'da açıksa üretim durur ve kapatılması istenir. Analiz sonuçları dosya değişene kadar saklanır (`grafik-varyant-ai-onbellek.json`); bu yüzden program açılışında ve **Kontrol Et**'te Illustrator gerekmez.

## PDF (Illustrator'süz)

PDF şablonlar Illustrator olmadan, doğrudan düzenlenir. PDF'te nesne isimleri saklanmadığı için alanlar iki yolla bulunur:

- **Yer tutucu:** Şablonda yazıyı `{NAME}` gibi süslü parantez içinde yazın.
- **Katman:** Yazıyı `NAME_M` adlı ayrı bir katmana koyun ve PDF'i Illustrator'da "Üst düzey katmanlardan Acrobat katmanları oluştur" seçeneğiyle kaydedin.

Yeni yazı, PDF'in içerik akışında eski yazının yerine konur; böylece renk (CMYK dahil), saydamlık, katman ve konum korunur. PDF'e gömülü font yalnızca şablonda kullanılan harfleri içerdiği için yeni yazı, aynı fontun bilgisayarda kurulu tam haliyle yazılır ve çıktıya yalnızca kullanılan harfleri gömülür. PDF'te paragraf hizası bilgisi olmadığından alanlar varsayılan olarak "Ortalı" gelir: yeni yazı örnek yazının ortasına yerleşir (sola/sağa yaslı da seçilebilir). Illustrator'ın PDF içindeki kendi düzenleme verisi çıktıdan silinir; çıktı Illustrator'da açıldığında yeni yazı görünür.

## Özellikler

- **Analiz:** Klasördeki şablonları tarar, isimli yazı alanlarını ve hangi şablonda eksik olduklarını gösterir. Bir üründe birden fazla değişken alan olabilir (isim, numara, kan grubu…).
- **Toplu giriş:** Beden sütunu ve şablonda bulunan her alan ayrı bir kutudur; her kutuya satır başına bir değer yazılır ya da yapıştırılır. Excel'den birlikte kopyalanan sütunlar kutulara dağıtılır. Tablodaki sütun başlığına tıklamak o sütunun toplu girişini açar.
- **Veri girişi:** Düzenlenebilir tablo, Excel/CSV/TXT içe aktarma, otomatik sütun eşleştirme. `2XL` yazılan beden `XXL` şablonunu (ve tersini) bulur.
- **Excel:** Boş veri şablonu indirme, tabloyu Excel'e aktarma.
- **Dosya adı:** `{Beden}_{NAME}`, `{sıra:03}`, `{tarih}` gibi kalıplar; kalıpta `/` ile alt klasör; isteğe bağlı olarak tablodaki "Dosya Adı" sütunundan.
- **Alan ayarları:** Harf dönüşümü (Türkçe İ/ı uyumlu), önek/sonek, boş değer davranışı, hizalama.
- **Font küçültme:** Yazı belirlenen karakter sayısını aşarsa font boyutu orantılı küçültülür, alt sınır yüzdesiyle.
- **Font denetimi:** Şablondaki fontu bilgisayarda bulup yazıdaki her harfin fontta olup olmadığına bakar (ör. Türkçe İ, Ğ, Ş). Analiz tablosunda fontun Türkçe desteği görünür. Harfi eksik ya da karakter sınırını aşan çıktılar üretimde sorularak `KONTROL-EDILECEK` klasörüne ayrılır.
- **Güvenlik:** Orijinal şablonları koruma, mevcut dosyalar için üzerine yaz / atla / numara ekle.
- **Rapor:** Şablonu eksik satırlar, küçültülen fontlar, boş alanlar ve üretilen dosyalar.
- **Proje dosyası:** Bir sekmenin tüm ayarları ve tablosu `.svgproje` olarak kaydedilir; açılınca kendi sekmesine yüklenir.

## Çalıştırma

Python 3.10+ ile:

```
pip install -r requirements.txt
python grafik_varyant.pyw
```

Taşınabilir tek dosyalık exe üretmek için `build.bat` dosyasını çalıştırın; çıktı `dist\Grafik-Varyant-Uretici.exe` olur. Exe, ayarlarını kendi yanındaki `grafik-varyant-oturum.json` dosyasında tutar (programın eski adıyla kalmış `svg-varyant-oturum.json` varsa ilk açılışta ondan okur).

## Sınırlar

- Yazı canlı olmalıdır; outline'a çevrilmiş yazılar değiştirilemez.
- Yeni yazı, şablondaki yazının ilk harfinin biçimini alır (karışık biçimli yazılar tek biçime iner).
- SVG'de birden fazla parçadan (`<tspan>`) oluşan yazılarda yeni metin ilk parçaya yazılır, diğerleri silinir.
- PDF'te yazı tek satır olarak yazılır; fontu bilgisayarda kurulu olmayan alan yazılamaz (raporda belirtilir).
- Font küçültme gerçek genişliğe değil karakter sayısına bakar.
