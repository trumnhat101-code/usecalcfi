# TOOL SITE — Project Brief & Kickoff

> **Mục đích file này:** tài liệu bàn giao đầy đủ để bắt đầu một **phiên chat mới** trong **folder riêng cho dự án tool site**. Copy cả thư mục `toolsite-starter/` này sang folder mới rồi mở chat mới trỏ vào đó. File tự chứa đủ ngữ cảnh — không cần đọc lại lịch sử chat cũ.

---

## 0. TL;DR (đọc 30 giây)

Xây **website công cụ (tool site)** — cụm **máy tính tài chính cho thị trường US** (mortgage, auto loan, paycheck, tax, retirement…). Mỗi tool là 1 trang tĩnh nhắm 1 từ khóa, chạy JS client-side. **Kiếm tiền 2 lớp: Affiliate (chính, tài chính payout cao) + Google AdSense (phủ)**. Traffic từ **SEO** (intent tìm kiếm). Lên Mediavine/Raptive khi đủ traffic.

**Chỉ traffic THẬT.** Không bot/nick farmed/tự click → AdSense ban vĩnh viễn. Đây là dự án "content/SEO sạch", tách hoàn toàn khỏi mọi công cụ automation/antidetect.

---

## 1. Mục tiêu

- Tạo nguồn thu thụ động qua tool site, scale được, vốn thấp (host tĩnh rẻ).
- Bắt đầu với **1 cụm ngách** (finance calculators US) để xây authority, không làm "tool tổng hợp gì cũng có".
- Milestone đầu: 10–15 tool Ưu tiên 1 + nội dung hỗ trợ + deploy + Search Console.

## 2. Mô hình kinh doanh & monetization

- **Sản phẩm:** trang công cụ miễn phí giải quyết nhu cầu tìm kiếm lặp lại (evergreen).
- **Lớp tiền 1 — Affiliate** (ăn chính ở tool tài chính): mortgage→LendingTree/Credible; auto→MyAutoLoan/Carvana; personal/debt→SoFi/LendingClub; student→SoFi/Earnest; tax→TurboTax/H&R Block; investing/retirement→Betterment/M1/Empower; savings→Raisin/banks; budgeting→YNAB/Monarch.
- **Lớp tiền 2 — AdSense** (đặt vừa phải) → khi traffic đủ thì chuyển **Mediavine/Raptive/Ezoic** (RPM cao hơn nhiều).
- **CTA affiliate đặt ngay sau kết quả tool** = chuyển đổi cao nhất.

## 3. Vì sao chọn hướng này (đã phân tích & chốt)

- **POD/Dropship** bán intent qua cộng đồng FB — hướng khác, đã có tài liệu riêng. **AdSense/tool site** bán sự chú ý qua **SEO**, hợp người thích làm nội dung/kỹ thuật.
- **Tool site** ưu điểm: content nhẹ (không viết blog dài), traffic evergreen + lặp lại, dễ thành linkable asset.
- **Chọn cụm tài chính** vì: cầu khổng lồ + **RPM cao** (US/UK) + **affiliate béo**. Đây là điểm giao tốt nhất giữa "dễ làm + traffic + tiền".
- Điểm yếu tool site (bounce cao, 1 pageview/phiên, RPM thấp với tool dev) → khắc phục bằng: nhiều tool cùng cụm + internal link + ưu tiên tool tài chính/thuế.

## 4. Ngách & danh sách tool

**Cụm:** Finance Calculators (US). **Danh sách đầy đủ 32 tool + từ khóa + cầu/RPM/cạnh tranh + affiliate + ưu tiên** nằm trong file kèm: **`Tool-Site-Finance-Calculators-US.xlsx`**.

**Top ƯU TIÊN 1 (làm trước — cầu cao + RPM cao + affiliate tốt):**

| Tool | Từ khóa chính | Affiliate |
|---|---|---|
| Mortgage Calculator | mortgage calculator | LendingTree, Credible |
| Home Affordability | how much house can i afford | Mortgage lenders |
| Refinance Calculator | mortgage refinance calculator | Credible, LendingTree |
| Auto Loan Calculator | auto loan calculator | MyAutoLoan, Carvana |
| Personal Loan Calculator | personal loan calculator | SoFi, LendingClub |
| Student Loan Calculator | student loan calculator | SoFi, Earnest |
| Debt Snowball Calculator | debt snowball calculator | Achieve, SoFi |
| Credit Card Payoff | credit card payoff calculator | Balance-transfer cards |
| Paycheck Calculator | paycheck calculator | Gusto, TurboTax |
| Income Tax Calculator | income tax calculator | TurboTax, H&R Block |
| Tax Refund Estimator | tax refund calculator | TurboTax, H&R Block |
| Self-Employment Tax | self employment tax calculator | Keeper, QuickBooks |
| Retirement Calculator | retirement calculator | Betterment, Empower |
| 401(k) Calculator | 401k calculator | Empower, brokerages |
| Compound Interest | compound interest calculator | Acorns, M1 |

> **Lưu ý:** Cầu/RPM/cạnh tranh là **định tính theo kinh nghiệm** — validate volume thật bằng Google Keyword Planner/Ahrefs/Semrush trước khi build. Cụm THUẾ bùng nổ Q1 (Jan–Apr).

## 5. Kiến trúc kỹ thuật (tóm tắt)

Chi tiết đầy đủ: **`KIEN-TRUC-TOOL-SITE.md`** (kèm theo).

- **Mỗi tool = 1 trang tĩnh, nhắm 1 từ khóa, logic JS client-side.** Host tĩnh.
- **Stack:** bắt đầu HTML thuần (template kèm theo) → khuyến nghị **Astro** (hoặc 11ty) khi scale; nếu quen React thì **Next.js static export**. Tránh SPA nặng (xấu SEO).
- **Bố cục mỗi trang:** tool above-the-fold → CTA affiliate ngay sau kết quả → AdSense in-content/sidebar → nội dung SEO (how to use, formula, example, FAQ) → related tools (internal link).
- **SEO:** title/meta/canonical, 1×H1, JSON-LD (WebApplication + FAQPage), sitemap.xml, Search Console.
- **Hiệu năng:** JS tối thiểu, không jQuery, ảnh WebP/lazy, ô ad cố định (CLS tốt). Mục tiêu Lighthouse ≥90 mobile.
- **Deploy:** Cloudflare Pages / Netlify / Vercel (free, CDN) + domain .com.

## 6. Template khởi đầu (đã có, chạy được)

**`mortgage-calculator.html`** — mở bằng trình duyệt là chạy ngay. Công thức đã test chuẩn ($300k @6% 30y = $1.798,65). Có sẵn: tool + kết quả PITI + bố cục SEO + schema + chỗ đặt AdSense/affiliate (đánh dấu `TODO`). **Dùng làm khuôn:** copy → đổi title/từ khóa/schema → thay hàm `calc()` cho tool khác.

## 7. Lộ trình build (milestones)

1. **Validate** 10–15 tool Ưu tiên 1 bằng keyword tool (volume + độ khó SERP).
2. **Dựng layout + tool mẫu** (mortgage) → deploy thử lên Cloudflare/Netlify.
3. **Tách component** (chuyển Astro): ToolLayout + AdSlot + AffiliateCTA + Faq.
4. **Làm 10–15 tool Ưu tiên 1**, mỗi cái + nội dung hỗ trợ + internal link.
5. **SEO ops:** sitemap, Search Console, theo dõi & tối ưu trang gần top.
6. **Monetize:** đăng ký affiliate → gắn CTA; bật AdSense; sau đó nhắm Mediavine.
7. **Scale:** nhân bản dạng tool rank tốt; mở thêm cụm liền kề.

## 8. Tuân thủ (bắt buộc)

- **Chỉ traffic thật từ SEO/owned.** KHÔNG tự click, KHÔNG nick farmed/bot/mua traffic → **AdSense khóa vĩnh viễn + giữ tiền**. Mọi công cụ automation/antidetect **KHÔNG** liên quan tới dự án này.
- Nội dung **gốc & hữu ích** (tránh thin page/AI spam → Google deindex).
- 1 người 1 tài khoản AdSense. Tuân thủ chính sách affiliate (disclosure, `rel="sponsored nofollow"`).

## 9. Tài sản kèm theo (trong folder này)

- `00-PROJECT-BRIEF.md` — file này (bàn giao tổng).
- `Tool-Site-Finance-Calculators-US.xlsx` — 32 tool + từ khóa + affiliate + ưu tiên (3 sheet).
- `KIEN-TRUC-TOOL-SITE.md` — kiến trúc kỹ thuật chi tiết.
- `mortgage-calculator.html` — template tool chạy được.

## 10. Gợi ý câu mở đầu cho PHIÊN CHAT MỚI

> Copy nội dung dưới làm tin nhắn đầu trong chat mới (folder đã chứa các file trên):

```
Mình đang xây một TOOL SITE: cụm máy tính tài chính cho thị trường US,
kiếm tiền bằng Affiliate + Google AdSense, traffic từ SEO.
Bối cảnh & kế hoạch đầy đủ ở file 00-PROJECT-BRIEF.md trong folder này
(kèm Tool-Site-Finance-Calculators-US.xlsx, KIEN-TRUC-TOOL-SITE.md,
và template mortgage-calculator.html).

Hãy đọc các file đó rồi giúp mình [CHỌN 1]:
- dựng layout component Astro (ToolLayout + AdSlot + AffiliateCTA), hoặc
- làm thêm 3 tool Ưu tiên 1 (Auto Loan + Paycheck + Retirement) theo khuôn template, hoặc
- lập kế hoạch SEO + validate từ khóa cho 15 tool đầu.
```

---

*Lưu ý: các con số RPM/cầu/ngưỡng (YouTube, Mediavine…) có thể đã thay đổi — luôn kiểm chứng số liệu hiện hành trước khi quyết định.*
