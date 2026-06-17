# Kiến trúc kỹ thuật — Tool Site (Finance Calculators US)

Khung khởi động cho site công cụ kiếm tiền bằng AdSense + Affiliate. Kèm template `mortgage-calculator.html` (chạy được, đã test công thức).

---

## 1. Nguyên tắc kiến trúc

- **Mỗi tool = 1 trang tĩnh, nhắm 1 từ khóa.** Logic chạy **client-side (JS)** → không cần backend → host tĩnh rẻ/nhanh.
- **Tốc độ là SEO + tiền**: tải nhanh, không framework nặng, không thư viện thừa → Core Web Vitals tốt → rank cao + nhiều lượt xem ads.
- **Trên tool, dưới content**: công cụ above-the-fold (giữ chân), nội dung hữu ích phía dưới (thỏa "helpful content" của Google + chỗ đặt ads + từ khóa phụ).
- **Internal link** giữa các tool cùng cụm → tăng pageview/phiên (bù điểm yếu 1-pageview của tool site).

## 2. Chọn stack (theo trình độ)

| Mức | Stack | Khi nào |
|---|---|---|
| Đơn giản nhất | **HTML/CSS/JS thuần** (như template này) | Bắt đầu nhanh, ít tool, không cần build |
| Khuyến nghị | **Astro** (hoặc 11ty) | Nhiều tool, muốn component tái dùng + xuất HTML tĩnh siêu nhẹ |
| Nếu quen React | **Next.js (Static Export)** | Cần routing/được hệ sinh thái React, vẫn xuất tĩnh |

> Tránh SPA nặng (CSR thuần) cho tool site — xấu cho SEO + tốc độ. Ưu tiên **static/SSG**.

## 3. Cấu trúc thư mục (gợi ý, Astro)

```
src/
  layouts/ToolLayout.astro      # header, footer, SEO meta, schema, ad loader
  components/AdSlot.astro        # 1 component ad tái dùng (in-content/sidebar)
  components/AffiliateCTA.astro  # CTA affiliate tái dùng
  components/Faq.astro           # FAQ + tự sinh JSON-LD
  pages/
    index.astro                  # trang chủ liệt kê tool
    mortgage-calculator.astro
    auto-loan-calculator.astro
    ...
  tools/                         # logic JS từng tool (tách riêng, test được)
public/  (robots.txt, sitemap.xml, favicon)
```

Template HTML thuần kèm theo = phiên bản "tất cả trong 1 file" để bạn hiểu bố cục trước khi tách component.

## 4. Bố cục SEO mỗi trang (đã có trong template)

1. `<title>` + `<meta description>` chứa từ khóa chính, `<link canonical>`.
2. **1 `<h1>` duy nhất** = tên tool; `<h2>` cho các mục (how to use, formula, FAQ, related).
3. **Schema JSON-LD**: `WebApplication` + `FAQPage` (giúp rich result + hiểu trang).
4. **Nội dung quanh tool** ≥ vài trăm chữ: cách dùng, công thức, ví dụ, FAQ → tránh "thin page" bị Google phạt.
5. **Related tools** (internal link) + breadcrumb.
6. `sitemap.xml` + `robots.txt`; submit Google Search Console.

## 5. Chỗ đặt AdSense + Affiliate (theo template)

- **Affiliate CTA ngay sau kết quả tool** — chuyển đổi cao nhất (người dùng vừa thấy con số → đúng lúc "compare rates / get pre-approved"). Đây thường **kiếm hơn AdSense** ở tool tài chính.
- **AdSense in-content** sau khối kết quả + **in-article** giữa nội dung dài + **sidebar 300×250 / sticky** (desktop).
- **Đừng nhồi ads** phá trải nghiệm (vi phạm chính sách + tụt CWV). Cân bằng: 2–3 ad slot + 1–2 CTA affiliate/trang.
- Bắt buộc **Advertiser disclosure** gần link affiliate; dùng `rel="sponsored nofollow"`.

## 6. Hiệu năng & kỹ thuật

- CSS inline/critical, JS tối thiểu, không jQuery. Ảnh lazy-load + nén (WebP).
- Tránh layout shift (đặt kích thước ô ad cố định) → CLS tốt.
- Test: PageSpeed Insights, Lighthouse (mục tiêu ≥90 mobile).

## 7. Monetization 2 lớp

- **Affiliate** (lớp chính cho tool tài chính): mortgage→LendingTree/Credible; auto→MyAutoLoan; tax→TurboTax; investing→Betterment/M1 (xem file Excel "Affiliate Programs").
- **AdSense** (lớp phủ): bật khi có ≥ vài chục trang nội dung thật. Khi traffic lớn → **chuyển Mediavine/Raptive/Ezoic** (RPM cao hơn nhiều).

## 8. Deploy

- **Cloudflare Pages / Netlify / Vercel** (free tier, CDN toàn cầu, build từ Git).
- Domain riêng (.com), HTTPS mặc định.
- Quy trình: push Git → auto build → live. Thêm tool = thêm 1 file trang.

## 9. Lộ trình build

1. Dựng layout + 1 tool mẫu (file kèm theo) → deploy thử.
2. Tách `ToolLayout` + `AdSlot` + `AffiliateCTA` thành component (chuyển sang Astro).
3. Làm **10–15 tool Ưu tiên 1** (xem Excel), mỗi cái + nội dung hỗ trợ + internal link.
4. Submit sitemap, theo dõi Search Console, tối ưu trang gần top.
5. Đăng ký affiliate, gắn CTA; bật AdSense; mở rộng tool theo cái rank tốt.

## 10. ⚠️ Tuân thủ (nhắc lại)

Chỉ **traffic thật từ SEO/owned**. **KHÔNG** tự click, **KHÔNG** dùng nick farmed/bot/mua traffic → AdSense khóa vĩnh viễn + giữ tiền. Công cụ antidetect **không** dính vào luồng này. Nội dung phải gốc & hữu ích.

---

### File kèm theo
`mortgage-calculator.html` — mở bằng trình duyệt là chạy ngay (đã test: $300k @6% 30y = $1,798.65). Dùng làm khuôn: đổi tiêu đề/từ khóa/schema + thay hàm `calc()` cho tool khác (auto loan, paycheck, retirement...). Nhớ thay `ca-pub-XXXX`, link `#AFFILIATE`, và domain canonical.
