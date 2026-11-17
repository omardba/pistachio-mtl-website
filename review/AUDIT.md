# Pistachio website audit — review build (17 November 2026)

## Scope and limitations
Inspected repository directory metadata, reviewed the existing 12,556,188-byte `index.html` as a repository artifact, consulted the submitted bilingual official menu PDFs, and reviewed the user's Netlify HTTPS screenshots. The GitHub connector did **not** return the contents of the unusually large current `index.html`; consequently a line-by-line review of the existing application, live-browser regression tests, and exhaustive claims about pre-existing broken links or scripts are **not** possible yet. No production changes are made.

## Confirmed observations
1. Existing `index.html` is **12,556,188 bytes** in the GitHub repository. High initial page-size risk; actual transfer size and content split must be measured before quoting a load-time impact.
2. Netlify dashboard showed the production project deployed via **Netlify Drop**, implying a GitHub push may not deploy automatically. Do not treat PR merging as a deployment.
3. The `.ca` certificate was expired and then successfully renewed, as documented in screenshots. Netlify now reports HTTPS enabled and automatic renewal before 15 February 2027.
4. User supplied official English and French menu PDFs (four pages each), with newer brunch/focaccia items and menu prices.
5. GitHub repository has additional `videos/` assets; their loading, encoding, and effect on performance remain untested.

## Changes on this review branch
- Added `review/index.html`, a new **standalone review-only page**, without overwriting the existing `index.html` or video files.
- Accessible semantic navigation with keyboard focus, skip link, and a language switcher.
- Bilingual menu search, filters, approximate official product listing and CAD prices transcribed from the PDFs.
- Responsive olive-green/dark-green/dusty-pink styling inspired by the menus.
- Search text is HTML-escaped; no external script dependencies.
- Removed unsupported promises about delivery time and left unverified ordering links out of the preview.
- Explicit noindex directive to avoid indexing the review page.

## Not yet complete
- This review-page content is a **first pass**, not an exhaustive transcription of every menu flavor, beverage option or supplement. It does not yet reproduce individual menu product photographs, or all item descriptions.
- Existing page source could not be retrieved through the GitHub connector (large file), so no claim is made that bugs inside it were fixed.
- No mobile/desktop browser screenshot test of the GitHub branch, no external ordering-link tests, no Lighthouse audit and no end-to-end Netlify preview have been completed.
- Location details, availability, and integration URLs require business-owner verification before publishing.
- Verify locally by downloading `review/index.html` and opening it in a browser (it contains no external assets). It is not production ready.

## Before publishing
1. Obtain readable original source via a local clone/archive or split code/assets into separate files.
2. Reconcile all official menu products, flavors, descriptions, image rights and location details.
3. Test with Chrome/Safari on desktop and mobile; run Lighthouse and accessibility audits.
4. Fix confirmed issues in the original site source, not only the new preview page.
5. Produce an isolated Netlify deploy preview or manual staging deploy, obtain owner signoff, and only then update production.
