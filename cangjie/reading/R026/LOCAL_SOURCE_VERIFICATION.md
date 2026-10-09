# R026｜用户私有 EPUB 来源核验（不可逆摘要公开版）

- private_file: 用户提供的《铁血残明》EPUB（不上传 GitHub）
- full_original_sha256: `9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf`
- range: original effective narrative ordinals 361—400 (40 chapters), including OPF non-narrative interposition before 387; ZIP paths and spine indices are taken from original frozen R002 CSV, **not guessed by display chapter number**.
- original_nonempty_paragraphs: **2731**; visible paragraph characters: **167878**; original sources read sequentially with `lxml.html.fromstring(raw).xpath('//body//p')` and body text check. ZIP member raw bytes match master CSV source hashes.
- close_read: **20** chapter-specific scene studies; full_text_read: **20** transitional/other chapters; total private paragraph locators: **80**, stored as SHA256 without exposing user EPUB text. Source anchor FNV1a32: `f0bcb91c`; member manifest FNV1a32: `003e2989`.
- A source: original SHA/40 ZIP-member SHA and 80 paragraph hash results locally obtained. B literature: chapter-specific observations and comparative essay PROVISIONAL (not peer blinded, not whole-book Adler). C independent original novel writing benefit: NOT_RUN. Official Cangjie Stage0 Stage gate not passed; Nuwa Phase1 not started.
- Public CI limitation: metadata and locally produced irreversible hashes verify SOURCE_STRUCTURE_ONLY in GitHub Actions without private user files; a successful public run **never certifies actual literary reading or mastery**.
- No original EPUB, long original quotation, paragraph text, or other copyrighted source uploaded to public repository.
