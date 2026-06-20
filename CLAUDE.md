# CLAUDE.md — Working Rules for usecalcfi.com

## ⚠️ READ THIS BEFORE DOING ANYTHING

**Always run the validator first:**
```
python validate.py                        # check all files
python validate.py mortgage-calculator.html  # check 1 file
```

Fix any ❌ errors shown before starting new work. ⚠️ warnings are OK to defer.

---

## Site Overview

- **URL**: usecalcfi.com
- **Stack**: Static HTML/CSS/JS on Cloudflare Pages (no build step)
- **Monetization**: Google AdSense `ca-pub-6004796759910209` + affiliate links
- **Analytics**: GA4 `G-C7MQVPYVTN`
- **Workspace**: `D:\Toolsite\toolsite-starter\`

---

## File Structure Rules

Every calculator page must follow this exact order:

```
<head> ... </head>
<body>
  <header>...</header>
  <main>
    <div class="layout">
      <div class="main">   ← calculator + old content (NO related tools here)
      </div>
      <div class="side">   ← CTAs + AdSense only (NO data tables, NO rel div)
      </div>
    </div>
  </main>

  [optional] <section style="max-width:1100px..."> ← new educational content
  </section>

  [optional] <div style="max-width:1100px;margin:0 auto;padding:8px 16px 20px">
    <h3>Related Tools</h3>
    <div class="rel">...</div>
  </div>

  <div style="background:#f7f8fc;border-top:2px solid #e5e7eb;padding:28px 16px 40px">
    📚 Related Guides
  </div>

  <footer>...</footer>

  <script>...</script>
</body></html>
```

**Never put:**
- Data tables inside `.side` sidebar (too narrow ~280px)
- `<div class="rel">` (Related Tools) inside `.side`
- `<section>` or content inside `<footer>`
- Any content after `</body></html>`

---

## Critical Technical Rules

### Bash vs File Tools
- **NEVER use bash to READ files** from `D:\` — bash reads a stale Linux cache
- Use `Read` tool or `Grep` tool with `D:\` paths for reliable reads
- Use bash Python only for WRITES (it writes to `/sessions/.../mnt/toolsite-starter/`)
- After any bash write, verify with `Grep`/`Read` using `D:\` path

### Editing Files Safely
1. **Read the file first** with Read tool before any edit
2. **Fix 1 file as a test**, verify with Grep/Read, then scale to others
3. **Use Edit tool** (not bash Python) for targeted single-file changes
4. **Print a diff preview** in any batch Python script before writing

### Script Safety Pattern
```python
# Always preview before writing:
print(f'BEFORE: {content[start-50:start]!r}')
print(f'REPLACING: {old_string!r}')
print(f'WITH: {new_string!r}')
print(f'AFTER: {content[end:end+50]!r}')
# Only write if preview looks correct
```

---

## Common Bugs & Root Causes

| Bug | Root Cause | Prevention |
|-----|-----------|------------|
| JS visible as text below footer | `</script></body></html>` injected mid-function | Validate before push |
| `-->` visible text on page | Nested HTML comment: `<!-- outer <!-- inner -->` closes outer | No `<!--` inside another comment |
| Content after footer | `<section>` placed inside `<footer>` | Always check structure order |
| Related Tools in sidebar | Batch fix script misidentified position | Read file, use Edit tool |
| File truncated mid-JS | File was cut during original creation, append hit wrong point | Run validate.py after every write |
| Premature `</body></html>` | Event listener block appended inside function body | Check with validate.py check #8 |

---

## Pre-Push Checklist

Run before every `git push`:

```bash
python validate.py
```

Expected output: `✅ ALL CLEAR — N files passed`

If any ❌ errors → fix them first. Do not push with errors.

---

## Footer Standard (copy-paste)

```html
<footer><div class="wrap" style="display:flex;flex-wrap:wrap;gap:6px 20px;align-items:center">
  <span>© 2026 UseCalcFi · Free financial calculators for Americans</span>
  <a href="/" style="color:var(--mut);text-decoration:none">All Calculators</a>
  <a href="/guides" style="color:var(--mut);text-decoration:none">Guides</a>
  <a href="/about" style="color:var(--mut);text-decoration:none">About</a>
  <a href="/contact" style="color:var(--mut);text-decoration:none">Contact</a>
  <a href="/privacy-policy" style="color:var(--mut);text-decoration:none">Privacy Policy</a>
  <a href="/disclaimer" style="color:var(--mut);text-decoration:none">Disclaimer</a>
  <span>Not financial advice</span>
</div></footer>
```

---

## Related Tools CSS (in `<style>` block of each page)

```css
.rel{display:flex;flex-wrap:wrap;gap:8px}
.rel a{background:#f5f3ff;color:var(--ac);text-decoration:none;padding:7px 12px;border-radius:20px;font-size:13px}
```
