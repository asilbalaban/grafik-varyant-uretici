<img src="assets/logo.png" width="96" align="right" alt="logo">

# SVG Varyant Üretici

Şablon SVG dosyalarındaki isimlendirilmiş yazı katmanlarını bir tablodaki verilerle doldurup her satır için ayrı SVG üreten Windows masaüstü programı. Forma, tişört, yaka kartı gibi isim/numara baskılı işlerde tek tek elle yazmak yerine kullanılır.

## Nasıl çalışır

1. Şablon SVG'lerde değişecek yazı katmanlarına `ALAN_ŞABLON` biçiminde isim verin. Dosya adı şablonun adıdır.

   | Dosya | Katman isimleri | Alanlar |
   |---|---|---|
   | `M.svg` | `NAME_M`, `NUMBER_M` | NAME, NUMBER |
   | `XL.svg` | `NAME_XL`, `NUMBER_XL` | NAME, NUMBER |

2. Programda şablon klasörünü seçip **Analiz Et**'e basın; alanlar otomatik bulunur.
3. Veri tablosunu doldurun: elle, çoklu satır yapıştırarak ya da Excel/CSV/TXT yükleyerek.
4. Dosya adı kalıbını ve seçenekleri belirleyin, **Kontrol Et** ile deneyin, **ÜRET** ile dosyaları yazın.

## Özellikler

- **Analiz:** Klasördeki SVG'leri tarar, isimli yazı katmanlarını ve hangi şablonda eksik olduklarını gösterir. Bir üründe birden fazla değişken alan olabilir (isim, numara, kan grubu…).
- **Toplu giriş:** Beden sütunu ve şablonda bulunan her alan ayrı bir kutudur; her kutuya satır başına bir değer yazılır ya da yapıştırılır. Excel'den birlikte kopyalanan sütunlar kutulara dağıtılır. Tablodaki sütun başlığına tıklamak o sütunun toplu girişini açar.
- **Veri girişi:** Düzenlenebilir tablo, Excel/CSV/TXT içe aktarma, otomatik sütun eşleştirme. `2XL` yazılan beden `XXL.svg` şablonunu (ve tersini) bulur.
- **Excel:** Boş veri şablonu indirme, tabloyu Excel'e aktarma.
- **Dosya adı:** `{Beden}_{NAME}`, `{sıra:03}`, `{tarih}` gibi kalıplar; kalıpta `/` ile alt klasör; isteğe bağlı olarak tablodaki "Dosya Adı" sütunundan.
- **Alan ayarları:** Harf dönüşümü (Türkçe İ/ı uyumlu), önek/sonek, boş değer davranışı.
- **Font küçültme:** Yazı belirlenen karakter sayısını aşarsa font boyutu orantılı küçültülür, alt sınır yüzdesiyle.
- **Güvenlik:** Orijinal şablonları koruma, mevcut dosyalar için üzerine yaz / atla / numara ekle.
- **Rapor:** Şablonu eksik satırlar, küçültülen fontlar, boş alanlar ve üretilen dosyalar.
- **Proje dosyası:** Tüm ayarlar ve tablo `.svgproje` olarak kaydedilir.

## Çalıştırma

Python 3.10+ ile:

```
pip install -r requirements.txt
python svg_varyant.pyw
```

Taşınabilir tek dosyalık exe üretmek için `build.bat` dosyasını çalıştırın; çıktı `dist\SVG-Varyant-Uretici.exe` olur. Exe, ayarlarını kendi yanındaki `svg-varyant-oturum.json` dosyasında tutar.

## Sınırlar

- Katman canlı yazı (`<text>`) olmalıdır; outline'a çevrilmiş yazılar değiştirilemez.
- Birden fazla parçadan (`<tspan>`) oluşan yazılarda yeni metin ilk parçaya yazılır, diğerleri silinir.
- Font küçültme gerçek genişliğe değil karakter sayısına bakar.
- Çıktıdaki fontların baskı bilgisayarında kurulu olması gerekir.
