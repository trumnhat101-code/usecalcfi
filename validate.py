"""
validate.py - Pre-work & pre-push validator for usecalcfi.com
Run: python3 validate.py
Run on 1 file: python3 validate.py mortgage-calculator.html

STALE CACHE WARNING:
  Files edited via Windows Edit/Write tools may appear stale in bash.
  Run this validator primarily AFTER bash Python writes.
  For Windows-edited files, use Grep/Read tools (D:\\ paths) to verify.
"""

import os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
SKIP = {'validate.py', 'CLAUDE.md', 'sitemap.xml', 'robots.txt', '_headers'}


def get_files(target=None):
    if target:
        return [target]
    return sorted(
        f for f in os.listdir(BASE)
        if f.endswith('.html') and f not in SKIP
    )


def check_file(fname):
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        return ['FILE NOT FOUND: ' + fname], []

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    errors = []
    warnings = []
    stripped = content.strip()

    # 1. File must end with </body></html> (with or without newline between tags)
    ok_end = stripped.endswith('</body></html>') or stripped.endswith('</body>\n</html>')
    if not ok_end:
        tail = stripped[-80:]
        errors.append('TRUNCATED — tail: ' + repr(tail))

    # 2. Only 1 closing </html> per file
    html_closes = stripped.count('</html>')
    if html_closes > 1:
        errors.append('DUPLICATE CLOSE: ' + str(html_closes) + 'x </html> in file')

    # 3. No raw content after the final </html>
    last_close = stripped.rfind('</html>')
    if last_close != -1:
        after = stripped[last_close + 7:].strip()
        if len(after) > 5:
            errors.append('CONTENT AFTER CLOSE: ' + repr(after[:80]))

    # 4. Balanced <script> / </script> tags
    opens = len(re.findall(r'<script[\s>]', content, re.IGNORECASE))
    closes = len(re.findall(r'</script>', content, re.IGNORECASE))
    if opens != closes:
        errors.append('SCRIPT MISMATCH: ' + str(opens) + ' <script> vs ' + str(closes) + ' </script>')

    # 5. No placeholder AdSense publisher ID
    if 'ca-pub-XXXXXXXX' in content:
        errors.append('ADSENSE PLACEHOLDER: ca-pub-XXXXXXXX still present')

    # 6. No nested HTML comment (fast O(n) check — split on --> and count <!--)
    parts = content.split('-->')
    for part in parts[:-1]:
        if part.count('<!--') > 1:
            errors.append('COMMENT BUG: nested <!-- inside HTML comment (causes visible text leak)')
            break

    # 7. No premature </script></body></html> inside JS functions
    if re.search(r'</script>\s*\n\s*</body></html>\)', content):
        errors.append('INJECT BUG: premature </script></body></html> inside JS code')

    # 8. <footer> must appear before </body>
    footer_pos = content.rfind('<footer')
    body_pos = content.rfind('</body>')
    if footer_pos != -1 and body_pos != -1 and footer_pos > body_pos:
        errors.append('STRUCTURE: <footer> appears AFTER </body>')

    # --- WARNINGS ---

    # 9. Must have <title>
    if not re.search(r'<title>', content, re.IGNORECASE):
        warnings.append('MISSING <title>')

    # 10. Must have meta description
    if not re.search(r'<meta\s+name=["\']description["\']', content, re.IGNORECASE):
        warnings.append('MISSING meta description')

    # 11. Must have canonical link
    if not re.search(r'<link\s+rel=["\']canonical["\']', content, re.IGNORECASE):
        warnings.append('MISSING canonical link')

    # 12. Related Tools should NOT be inside sidebar
    side_match = re.search(
        r'<(?:div|aside)\s+class="side">(.*?)</(?:div|aside)>\s*</div>\s*</(?:main|div)>',
        content, re.DOTALL
    )
    if side_match and 'class="rel"' in side_match.group(1):
        warnings.append('LAYOUT: Related Tools (.rel) still inside sidebar')

    # 13. AdSense placeholder text
    if 'AdSense — sidebar' in content or 'AdSense — leaderboard' in content:
        warnings.append('ADSENSE: placeholder ad text (not a real ad unit)')

    # 14. Balanced <div> tags (large mismatch = structural bug)
    div_opens = len(re.findall(r'<div[\s>]', content))
    div_closes = len(re.findall(r'</div>', content))
    diff = abs(div_opens - div_closes)
    if diff > 3:
        warnings.append('DIV MISMATCH: ' + str(div_opens) + ' <div> vs ' + str(div_closes) + ' </div> (diff=' + str(diff) + ')')

    return errors, warnings


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else None
    files = get_files(target)

    total_errors = 0
    total_warnings = 0
    failed_files = []

    print('')
    print('=' * 60)
    print('  UseCalcFi Validator — ' + str(len(files)) + ' file(s)')
    print('=' * 60)
    print('')

    for fname in files:
        errs, warns = check_file(fname)

        if errs or warns:
            print('[' + fname + ']')
            for e in errs:
                print('  ERROR: ' + e)
            for w in warns:
                print('  WARN:  ' + w)
            print('')

        total_errors += len(errs)
        total_warnings += len(warns)
        if errs:
            failed_files.append(fname)

    print('=' * 60)
    if total_errors == 0 and total_warnings == 0:
        print('  ALL CLEAR — ' + str(len(files)) + ' files passed')
    else:
        print('  ' + str(total_errors) + ' error(s) in ' + str(len(failed_files)) + ' file(s)')
        print('  ' + str(total_warnings) + ' warning(s)')
        if failed_files:
            print('')
            print('  Fix before pushing:')
            for f in failed_files:
                print('    - ' + f)
    print('=' * 60)
    print('')

    return 1 if total_errors > 0 else 0


if __name__ == '__main__':
    sys.exit(main())
