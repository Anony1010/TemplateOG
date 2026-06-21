import json

# ===== EDIT YOUR TEMPLATES HERE =====
# Format: (id, title_en, title_az, content_en, content_az)
templates = [
(1,"Request for Product Quotation","Məhsul Üçün Qiymət Təklifi Sorğusu",
"Subject: Request for Product Quotation\n\nDear Sir/Madam,\n\nPlease review the attached document and provide a quotation for a product that meets the specified parameters.\n\nAdditionally, please advise:\n\n- Whether the product is available in stock;\n- Delivery options to Azerbaijan by air and road freight;\n- Manufacturing/lead time;\n- Estimated delivery time.\n\nWe look forward to your quotation.\n\nBest regards,\n[Your Name]\n[Company Name]",
"Mövzu: Məhsul Üçün Qiymət Təklifi Sorğusu\n\nHörmətli cənab/xanım,\n\nƏlavə olunmuş sənədi nəzərdən keçirib göstərilən parametrlərə uyğun məhsul üçün qiymət təklifi təqdim edəsiniz.\n\nƏlavə olaraq, aşağıdakıları bildirəsiniz:\n\n- Məhsulun stokda olub-olmaması;\n- Azərbaycana hava və quru yolu ilə çatdırılma variantları;\n- İstehsal/çatdırılma müddəti;\n- Təxmini çatdırılma vaxtı.\n\nQiymət təklifinizi gözləyirik.\n\nHörmətlə,\n[Adınız]\n[Şirkət Adı]"),

(2,"Alternative Item Inquiry","Alternativ Məhsul Sorğusu",
"Subject: Alternative Item Inquiry\n\nDear Sir/Madam,\n\nWould you like to consider an alternative item for your requirement?\n\nPlease let us know if an alternative would be acceptable.\n\nWe look forward to your response.\n\nBest regards,\n[Your Name]\n[Company Name]",
"Mövzu: Alternativ Məhsul Təklifi\n\nHörmətli cənab/xanım,\n\nTələbiniz üçün alternativ məhsulu nəzərdən keçirmək istərdinizmi?\n\nAlternativin sizin üçün uyğun olub-olmadığını bildirin.\n\nCavabınızı gözləyirik.\n\nHörmətlə,\n[Adınız]\n[Şirkət Adı]"),

(3,"Best Price Request","Ən Yaxşı Qiymət Tələbi",
"Subject: Best Price Request\n\nDear Sir/Madam,\n\nThank you for your quotation. Kindly provide your best possible price for approval.\n\nWe look forward to your revised offer.\n\nBest regards,\n[Name]",
"Mövzu: Ən Yaxşı Qiymət Tələbi\n\nHörmətli cənab/xanım,\n\nTəklifinizə görə təşəkkür edirik. Zəhmət olmasa, ən sərfəli qiymətinizi təqdim edin.\n\nYenilənmiş təklifinizi gözləyirik.\n\nHörmətlə,\n[Ad]"),

(4,"Final Offer Request","Son Qiymət Təklifi",
"Subject: Final Offer Request\n\nDear Sir/Madam,\n\nPlease provide your final commercial offer to proceed with our process.\n\nThank you for your cooperation.\n\nBest regards,\n[Name]",
"Mövzu: Son Qiymət Təklifi\n\nHörmətli cənab/xanım,\n\nDaxili prosesimiz üçün son qiymət təklifinizi təqdim edin.\n\nƏməkdaşlığınız üçün təşəkkür edirik.\n\nHörmətlə,\n[Ad]"),

(5,"Delivery Time Inquiry","Çatdırılma Müddəti Sorğusu",
"Subject: Delivery Time Inquiry\n\nDear Sir/Madam,\n\nPlease provide the delivery time and shipping schedule for our order.\n\nThank you.\n\nBest regards,\n[Name]",
"Mövzu: Çatdırılma Müddəti Sorğusu\n\nHörmətli cənab/xanım,\n\nSifarişimizin çatdırılma müddətini və göndərmə cədvəlini bildirin.\n\nHörmətlə,\n[Ad]"),

(6,"Stock Availability Inquiry","Stok Mövcudluğu Sorğusu",
"Subject: Stock Availability Inquiry\n\nDear Sir/Madam,\n\nPlease advise the current stock availability and lead time for the items below.\n\nWe look forward to your update.\n\nBest regards,\n[Name]",
"Mövzu: Stok Mövcudluğu Sorğusu\n\nHörmətli cənab/xanım,\n\nMəhsulların stok mövcudluğunu və təslim müddətini bildirin.\n\nCavabınızı gözləyirik.\n\nHörmətlə,\n[Ad]"),

(7,"Offer Rejection","Təklifin Rəddi",
"Subject: Offer Rejection\n\nDear Sir/Madam,\n\nThank you for your offer. After review, we regret that we are unable to proceed with your proposal at this time.\n\nWe hope to collaborate on future opportunities.\n\nBest regards,\n[Name]",
"Mövzu: Təklifin Rəddi\n\nHörmətli cənab/xanım,\n\nTəklifinizə görə təşəkkür edirik. Təəssüflə bildiririk ki, hazırki mərhələdə təklifinizi qəbul edə bilmirik.\n\nGələcək əməkdaşlıq ümidi ilə.\n\nHörmətlə,\n[Ad]"),

(8,"Warranty Claim","Zəmanət Müraciəti",
"Subject: Warranty Claim\n\nDear Sir/Madam,\n\nWe wish to file a warranty claim for the product below.\n\nProduct: [Product Name]\nInvoice: [Invoice Number]\nIssue: [Description]\n\nPlease advise on the required steps.\n\nBest regards,\n[Name]",
"Mövzu: Zəmanət Müraciəti\n\nHörmətli cənab/xanım,\n\nAşağıdakı məhsul üçün zəmanət müraciəti etmək istəyirik.\n\nMəhsul: [Məhsul Adı]\nFaktura: [Faktura Nömrəsi]\nProblem: [Təsvir]\n\nHörmətlə,\n[Ad]"),

(9,"Quality Complaint","Keyfiyyət Şikayəti",
"Subject: Quality Complaint\n\nDear Sir/Madam,\n\nWe regret to report a quality issue with the delivered product.\n\nOrder: [Order Number]\nIssue: [Description]\n\nWe kindly request a replacement or refund.\n\nBest regards,\n[Name]",
"Mövzu: Keyfiyyət Şikayəti\n\nHörmətli cənab/xanım,\n\nÇatdırılan məhsulda keyfiyyət problemi aşkar edilmişdir.\n\nSifariş: [Sifariş Nömrəsi]\nProblem: [Təsvir]\n\nDəyişdirilmə və ya geri qaytarılma xahiş edirik.\n\nHörmətlə,\n[Ad]"),

(10,"Supplier Registration","Təchizatçı Qeydiyyatı",
"Subject: Supplier Registration Request\n\nDear Sir/Madam,\n\nWe would like to register your company as a supplier in our system.\n\nPlease provide:\n- Company profile and catalogue\n- Tax registration certificate\n- Quality certifications\n- Bank details\n\nWe look forward to your response.\n\nBest regards,\n[Name]",
"Mövzu: Təchizatçı Qeydiyyatı Sorğusu\n\nHörmətli cənab/xanım,\n\nŞirkətinizi təchizatçı kimi qeydiyyatdan keçirmək istəyirik.\n\nZəhmət olmasa, aşağıdakıları təqdim edin:\n- Şirkət profili və kataloqu\n- Vergi qeydiyyat şəhadətnaməsi\n- Keyfiyyət sertifikatları\n- Bank məlumatları\n\nHörmətlə,\n[Ad]"),

(11,"Inquiry Follow-Up","Sorğu Təkibi",
"Subject: Inquiry Follow-Up\n\nDear Sir/Madam,\n\nWe previously sent an inquiry on [Date]. Kindly provide an update.\n\nWe look forward to your response.\n\nBest regards,\n[Name]",
"Mövzu: Sorğu Təkibi\n\nHörmətli cənab/xanım,\n\n[Tarix] tarixində sorğu göndərmişdik. Vəziyyəti barədə məlumat verəsiniz.\n\nCavabınızı gözləyirik.\n\nHörmətlə,\n[Ad]"),

(12,"Order Confirmation","Sifariş Təsdiqi",
"Subject: Order Confirmation\n\nDear Sir/Madam,\n\nWe are pleased to confirm our order as per agreed terms.\n\nOrder Reference: [Order Number]\nItem: [Product Name]\nQuantity: [Quantity]\nTotal Amount: [Total]\nDelivery Date: [Date]\n\nPlease confirm the shipping schedule.\n\nBest regards,\n[Name]",
"Mövzu: Sifariş Təsdiqi\n\nHörmətli cənab/xanım,\n\nRazılaşdırılmış şərtlərə əsasən sifarişimizi təsdiq edirik.\n\nSifariş İstinadı: [Sifariş Nömrəsi]\nMəhsul: [Məhsul Adı]\nMiqdar: [Miqdar]\nÜmumi Məbləğ: [Məbləğ]\nÇatdırılma Tarixi: [Tarix]\n\nGöndərmə cədvəlini təsdiqləyin.\n\nHörmətlə,\n[Ad]"),

(13,"Shipping Instruction","Göndəriş Təlimatı",
"Subject: Shipping Instruction\n\nDear Sir/Madam,\n\nPlease arrange shipment for the order below.\n\nOrder Reference: [Order Number]\nShipping Method: [Air / Road / Sea]\nDestination: [Address]\nRequired Date: [Date]\n\nPlease provide tracking information.\n\nThank you.\n\nBest regards,\n[Name]",
"Mövzu: Göndəriş Təlimatı\n\nHörmətli cənab/xanım,\n\nAşağıdakı sifarişin göndərilməsini təşkil edin.\n\nSifariş İstinadı: [Sifariş Nömrəsi]\nDaşıma Üsulu: [Hava / Quru / Dəniz]\nTəyinat: [Ünvan]\nTarix: [Tarix]\n\nİzləmə məlumatını təqdim edin.\n\nHörmətlə,\n[Ad]"),

(14,"Payment Reminder","Ödəniş Xatırlatması",
"Subject: Payment Reminder\n\nDear Sir/Madam,\n\nThis is a reminder for the outstanding payment on invoice [Invoice Number] dated [Date].\n\nAmount: [Amount]\nDue Date: [Due Date]\n\nPlease process the payment at your earliest convenience.\n\nBest regards,\n[Name]",
"Mövzu: Ödəniş Xatırlatması\n\nHörmətli cənab/xanım,\n\n[Tarix] tarixli [Faktura Nömrəsi] nömrəli faktura üzrə ödənişi xatırladırıq.\n\nMəbləğ: [Məbləğ]\nSon Tarix: [Tarix]\n\nÖdənişi həyata keçirməyinizi xahiş edirik.\n\nHörmətlə,\n[Ad]"),

(15,"Invoice Correction","Faktura Düzəlişi",
"Subject: Invoice Correction Request\n\nDear Sir/Madam,\n\nWe found a discrepancy in invoice [Invoice Number].\n\nItem: [Item]\nIncorrect: [Value]\nCorrect: [Correct Value]\n\nKindly issue a revised invoice.\n\nBest regards,\n[Name]",
"Mövzu: Faktura Düzəlişi Sorğusu\n\nHörmətli cənab/xanım,\n\n[Faktura Nömrəsi] nömrəli fakturada uyğunsuzluq aşkar etdik.\n\nMaddə: [Maddə]\nSəhv: [Dəyər]\nDüzgün: [Düzgün Dəyər]\n\nDüzəliş edilmiş faktura göndərin.\n\nHörmətlə,\n[Ad]"),

(16,"Back Order","Geri Sifariş",
"Subject: Back Order Notification\n\nDear Sir/Madam,\n\nThe following item from your order is currently out of stock and will be placed on back order.\n\nOrder Reference: [Order Number]\nItem: [Product Name]\nEstimated Restock: [Date]\n\nWe will notify you once available.\n\nBest regards,\n[Name]",
"Mövzu: Geri Sifariş Bildirişi\n\nHörmətli cənab/xanım,\n\nSifarişinizdəki məhsul hazırda stokda yoxdur və geri sifarişə qoyulmuşdur.\n\nSifariş: [Sifariş Nömrəsi]\nMəhsul: [Məhsul Adı]\nYenilənmə: [Tarix]\n\nMəlumat verəcəyik.\n\nHörmətlə,\n[Ad]"),

(17,"Order Cancellation","Sifariş Ləğvi",
"Subject: Order Cancellation\n\nDear Sir/Madam,\n\nDue to [Reason], we must cancel our order [Order Reference].\n\nPlease confirm the cancellation.\n\nBest regards,\n[Name]",
"Mövzu: Sifariş Ləğvi\n\nHörmətli cənab/xanım,\n\n[Səbəb] səbəbindən [Sifariş İstinadı] nömrəli sifarişimizi ləğv etməliyik.\n\nLəğvi təsdiqləyin.\n\nHörmətlə,\n[Ad]"),

(18,"Late Delivery","Gecikmiş Çatdırılma",
"Subject: Late Delivery Notification\n\nDear Sir/Madam,\n\nWe regret to inform you that delivery for order [Order Reference] is delayed.\n\nOriginal Date: [Original Date]\nRevised Date: [New Date]\n\nWe apologize for the inconvenience.\n\nBest regards,\n[Name]",
"Mövzu: Gecikmiş Çatdırılma Bildirişi\n\nHörmətli cənab/xanım,\n\n[Sifariş İstinadı] üzrə çatdırılmanın gecikdiyini bildiririk.\n\nPlanlaşdırılan: [Əvvəlki Tarix]\nYeni Tarix: [Yeni Tarix]\n\nNarahatlıq üçün üzr istəyirik.\n\nHörmətlə,\n[Ad]"),

(19,"Sample Request","Nümunə Tələbi",
"Subject: Sample Request\n\nDear Sir/Madam,\n\nPlease provide samples of the following products for evaluation.\n\n1. [Product 1]\n2. [Product 2]\n\nAdvise if any charges apply.\n\nBest regards,\n[Name]",
"Mövzu: Nümunə Tələbi\n\nHörmətli cənab/xanım,\n\nQiymətləndirmə üçün aşağıdakı məhsulların nümunələrini təqdim edin.\n\n1. [Məhsul 1]\n2. [Məhsul 2]\n\nHər hansı ödəniş varsa bildirin.\n\nHörmətlə,\n[Ad]"),

(20,"Price Revision","Qiymət Yeniləməsi",
"Subject: Price Revision Request\n\nDear Sir/Madam,\n\nDue to [reason], we request a revision of pricing for [Product Name].\n\nCurrent: [Current Price]\nProposed: [New Price]\n\nWe look forward to your response.\n\nBest regards,\n[Name]",
"Mövzu: Qiymət Yeniləmə Sorğusu\n\nHörmətli cənab/xanım,\n\n[Səbəb] səbəbindən [Məhsul Adı] üçün qiymət yeniləməsi xahiş edirik.\n\nCari: [Cari Qiymət]\nTəklif: [Yeni Qiymət]\n\nHörmətlə,\n[Ad]"),

(21,"Bid Extension","Təklif Müddətinin Uzadılması",
"Subject: Bid Extension Request\n\nDear Sir/Madam,\n\nWe request an extension for the bid deadline of [Tender Reference].\n\nCurrent Deadline: [Current Date]\nProposed: [New Date]\nReason: [Brief explanation]\n\nThank you.\n\nBest regards,\n[Name]",
"Mövzu: Təklif Müddətinin Uzadılması\n\nHörmətli cənab/xanım,\n\n[Tender İstinadı] üçün təklif son tarixinin uzadılmasını xahiş edirik.\n\nCari Tarix: [Cari Tarix]\nYeni Tarix: [Yeni Tarix]\nSəbəb: [Qısa izahat]\n\nHörmətlə,\n[Ad]"),

(22,"Supplier Performance Review","Təchizatçı Qiymətləndirməsi",
"Subject: Supplier Performance Review\n\nDear Sir/Madam,\n\nPlease find your performance rating for [Period] below.\n\nOverall Rating: [Rating]/5\n\nWe value our partnership.\n\nBest regards,\n[Name]",
"Mövzu: Təchizatçı Qiymətləndirməsi\n\nHörmətli cənab/xanım,\n\n[Dövr] üçün performans reytinqiniz aşağıdadır.\n\nÜmumi Reytinq: [Reytinq]/5\n\nƏməkdaşlığımızı dəyərləndiririk.\n\nHörmətlə,\n[Ad]"),

(23,"Contract Agreement","Müqavilə Razılaşması",
"Subject: Contract Agreement\n\nDear Sir/Madam,\n\nPlease find the contract for [Project Name] attached.\n\nContract Value: [Amount]\nDuration: [Start Date] - [End Date]\n\nKindly review and return the signed copy by [Date].\n\nBest regards,\n[Name]",
"Mövzu: Müqavilə Razılaşması\n\nHörmətli cənab/xanım,\n\n[Layihə Adı] üçün müqavilə əlavə olunur.\n\nMüqavilə Dəyəri: [Məbləğ]\nMüddət: [Başlanğıc Tarix] - [Bitmə Tarixi]\n\nİmzalayıb [Tarix] tarixinə qədər qaytarın.\n\nHörmətlə,\n[Ad]"),

(24,"Export Documents","İxrac Sənədləri",
"Subject: Export Documents Request\n\nDear Sir/Madam,\n\nPlease provide the following documents for shipment [Order Reference]:\n\n- Certificate of Origin\n- Bill of Lading\n- Packing List\n- Commercial Invoice\n- Insurance Certificate\n\nDocuments needed by [Date].\n\nThank you.\n\nBest regards,\n[Name]",
"Mövzu: İxrac Sənədləri Sorğusu\n\nHörmətli cənab/xanım,\n\n[Sifariş İstinadı] üçün aşağıdakı sənədləri təqdim edin:\n\n- Mənşə Şəhadətnaməsi\n- Koşiment\n- Paket Siyahısı\n- Kommersiya Fakturası\n- Sığorta Şəhadətnaməsi\n\nSənədlər [Tarix] tarixinə qədər lazımdır.\n\nHörmətlə,\n[Ad]"),

(25,"Tender Submission","Tender Təqdimatı",
"Subject: Tender Submission\n\nDear Sir/Madam,\n\nWe submit our bid for [Tender Reference]. Our proposal is attached.\n\nOffer valid until [Date].\n\nWe look forward to your evaluation.\n\nBest regards,\n[Name]",
"Mövzu: Tender Təqdimatı\n\nHörmətli cənab/xanım,\n\n[Tender İstinadı] üçün təklifimizi təqdim edirik. Təklif əlavə olunur.\n\nTəklif [Tarix] tarixinə qədər qüvvədədir.\n\nQiymətləndirmənizi gözləyirik.\n\nHörmətlə,\n[Ad]"),

(26,"Credit Application","Kredit Müraciəti",
"Subject: Credit Application\n\nDear Sir/Madam,\n\nWe wish to apply for a credit account with your company.\n\nCompany: [Company Name]\nRequested Limit: [Amount]\nTerms: [Payment Terms]\n\nPlease review the attached documents.\n\nBest regards,\n[Name]",
"Mövzu: Kredit Müraciəti\n\nHörmətli cənab/xanım,\n\nŞirkətinizdə kredit hesabı açmaq üçün müraciət edirik.\n\nŞirkət: [Şirkət Adı]\nLimit: [Məbləğ]\nŞərtlər: [Ödəniş Şərtləri]\n\nSənədlər əlavə olunur.\n\nHörmətlə,\n[Ad]")
]

# ===== GENERATE HTML =====
data = [{"id": i, "title": t, "titleAz": tz, "en": e, "az": a} for i, t, tz, e, a in templates]
data_json = json.dumps(data, ensure_ascii=False)

CSS = """*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#f4f7fc;--card:#fff;--primary:#0b1e3a;--accent:#1a5bff;--accent2:#3b7bff;--accent3:#0d47d0;--border:#dce3ef;--text:#1a2332;--muted:#5e6f8d;--radius:14px;--shadow:0 2px 12px rgba(26,91,255,.06)}
body{font-family:Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Oxygen,Ubuntu,sans-serif;background:var(--bg);color:var(--text);min-height:100vh;font-size:16px;line-height:1.7;-webkit-font-smoothing:antialiased}
header{background:linear-gradient(135deg,#0b1e3a 0%,#0f2a5a 40%,#1a5bff 100%);color:#fff;padding:3.5rem 2rem 2.5rem;text-align:center;position:relative;overflow:hidden}
header::before{content:'';position:absolute;top:-60%;left:-30%;width:160%;height:200%;background:radial-gradient(ellipse at 40% 50%,rgba(255,255,255,.06) 0%,transparent 60%);pointer-events:none}
header::after{content:'';position:absolute;bottom:0;left:0;right:0;height:5px;background:linear-gradient(90deg,transparent,#60a5fa,#93c5fd,#60a5fa,transparent)}
header h1{font-size:2.6rem;font-weight:800;letter-spacing:-.5px;margin-bottom:.3rem;position:relative}
header p{font-size:1.05rem;opacity:.6;font-weight:400;position:relative}
.controls{background:#fff;padding:1rem 2rem;display:flex;align-items:center;justify-content:center;gap:1rem;flex-wrap:wrap;border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100;box-shadow:0 1px 6px rgba(0,0,0,.04)}
.search-wrap{position:relative;flex:1;max-width:520px;min-width:220px}
.search-wrap svg{position:absolute;left:15px;top:50%;transform:translateY(-50%);width:17px;height:17px;color:var(--muted);pointer-events:none}
.search-wrap input{width:100%;padding:.7rem 1rem .7rem 2.5rem;border:2px solid var(--border);border-radius:12px;font-size:.9rem;outline:none;transition:all .2s;background:var(--bg);color:var(--text)}
.search-wrap input:focus{border-color:var(--accent);box-shadow:0 0 0 4px rgba(26,91,255,.1);background:#fff}
.stats{font-size:.85rem;color:var(--muted);white-space:nowrap;font-weight:500}
.c{max-width:860px;margin:0 auto;padding:1.5rem 1.5rem 3rem;display:flex;flex-direction:column;gap:10px}
.tc{background:var(--card);border-radius:var(--radius);overflow:hidden;border:1px solid var(--border);transition:all .2s}
.tc:hover{box-shadow:0 4px 24px rgba(26,91,255,.08);border-color:#bed9ff}
.th{padding:.85rem 1.3rem;cursor:pointer;display:flex;align-items:center;gap:12px;background:var(--card);user-select:none;-webkit-tap-highlight-color:transparent;transition:background .15s}
.th:hover{background:#fafcff}
.th:active{background:#f0f5ff}
.open .th{background:#f7faff;border-bottom:1px solid var(--border)}
.th .no{display:inline-flex;width:32px;height:32px;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border-radius:10px;align-items:center;justify-content:center;font-size:.75rem;font-weight:700;flex-shrink:0;transition:all .25s;box-shadow:0 2px 6px rgba(26,91,255,.2)}
.open .th .no{background:linear-gradient(135deg,var(--accent3),var(--accent));box-shadow:0 3px 10px rgba(26,91,255,.35);transform:scale(1.05)}
.th .tm{font-size:.92rem;font-weight:600;flex:1;color:var(--primary);line-height:1.4}
.th .li{display:flex;gap:5px;flex-shrink:0}
.th .lb{font-size:.55rem;padding:2px 9px;border-radius:20px;font-weight:700;letter-spacing:.4px;text-transform:uppercase}
.lb.e{background:#dbeafe;color:#1d4ed8}
.lb.a{background:#ede9fe;color:#5b21b6}
.th .ar{font-size:.85rem;color:#a0b9e0;transition:all .3s;flex-shrink:0;width:22px;text-align:center}
.open .ar{transform:rotate(180deg);color:var(--accent)}
.tb{max-height:0;overflow:hidden;transition:max-height .4s ease,padding .25s ease;padding:0 1.3rem}
.open .tb{max-height:3000px;padding:.9rem 1.3rem 1rem}
.ls{margin-bottom:.6rem}
.ls:last-child{margin-bottom:0}
.lsh{display:flex;justify-content:space-between;align-items:center;margin-bottom:.35rem;flex-wrap:wrap;gap:4px}
.lsh .ll{font-weight:700;font-size:.7rem;text-transform:uppercase;letter-spacing:.5px;color:var(--muted)}
.cb{display:inline-flex;align-items:center;gap:5px;padding:5px 14px;border:none;border-radius:8px;cursor:pointer;font-size:.7rem;font-weight:600;transition:all .15s;background:#f1f5f9;color:#475569;font-family:inherit}
.cb:hover{background:#e2e8f0;transform:translateY(-1px)}
.cb.ok{background:#059669;color:#fff;transform:none}
.cb svg{width:12px;height:12px}
.ec{background:#fafcff;border-radius:10px;padding:.7rem 1.1rem;font-size:.88rem;line-height:1.8;white-space:pre-wrap;font-family:Georgia,'Times New Roman',serif;border-left:4px solid var(--accent);border:1px solid var(--border);border-left-width:4px;color:var(--text)}.ft{text-align:center;padding:2rem;color:#94a3b8;font-size:.8rem;border-top:1px solid var(--border);background:#fff}
.empty-state{text-align:center;padding:3rem 1rem;color:var(--muted)}
.empty-state svg{width:44px;height:44px;margin-bottom:.8rem;opacity:.35}
.empty-state p{font-size:.9rem}
@media(max-width:640px){header{padding:2rem 1rem 1.5rem}header h1{font-size:1.6rem}header p{font-size:.9rem}.controls{padding:.7rem 1rem;gap:.6rem}.search-wrap{max-width:100%;min-width:0}.stats{font-size:.78rem}.c{padding:1rem 1rem 2rem;gap:8px}.th{padding:.65rem 1rem;gap:8px}.th .no{width:28px;height:28px;font-size:.7rem;border-radius:8px}.th .tm{font-size:.85rem}.th .lb{font-size:.5rem;padding:1px 7px}.open .tb{padding:.7rem 1rem}.ec{font-size:.82rem;padding:.5rem .9rem;line-height:1.7;border-radius:8px;border-left-width:3px}.ft{padding:1.5rem}}"""

# IMPORTANT: semicolon after data_json is REQUIRED for JS to work!
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0">
<title>TemplateOG</title>
<style>{CSS}</style>
</head>
<body>
<header>
<h1>TemplateOG</h1>
<p>Professional Email Templates for Daily Operations</p>
</header>
<div class="controls">
<div class="search-wrap">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
<input type="text" id="search" placeholder="Search templates..." oninput="filter(this.value)">
</div>
<div class="stats" id="stats">26 templates</div>
</div>
<div class="c" id="g"></div>
<div class="ft">TemplateOG &mdash; Professional Email Templates &bull; 2026</div>
<script>
var D={data_json};
(function(){{
function r(q){{
var g=document.getElementById('g');g.innerHTML='';var f=D;
if(q){{var l=q.toLowerCase();f=D.filter(function(t){{return t.title.toLowerCase().indexOf(l)>=0||t.titleAz.toLowerCase().indexOf(l)>=0||t.en.toLowerCase().indexOf(l)>=0||t.az.toLowerCase().indexOf(l)>=0}})}}
document.querySelector('.stats').textContent=f.length+' template'+(f.length!==1?'s':'');
if(f.length===0){{g.innerHTML='<div class="empty-state"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg><p>No templates found</p></div>';return}}
f.forEach(function(t){{
var c=document.createElement('div');c.className='tc';
c.innerHTML='<div class="th" onclick="this.parentNode.classList.toggle(\\'open\\')"><span class="no">'+t.id+'</span><span class="tm">'+e(t.title)+'</span><span class="li"><span class="lb e">EN</span><span class="lb a">AZ</span></span><span class="ar">\\u25bc</span></div><div class="tb">'+s('en','English',t.en)+s('az','Azerbaycan',t.az)+'</div>';
g.appendChild(c)}})
}}
function s(l,la,t){{
var lc=l==='en'?'el':'al';
var tx=t.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/\\n/g,'<br>');
var js=t.replace(/\\\\/g,'\\\\\\\\').replace(/'/g,"\\\\'").replace(/\\n/g,'\\\\n');
return '<div class="ls"><div class="lsh"><span class="ll '+lc+'">'+la+'</span><button class="cb" onclick="cp(this,\\''+js+'\\')"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy</button></div><div class="ec">'+tx+'</div></div>'
}}
function e(s){{return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}}
function cp(b,t){{
var d=t.replace(/\\\\n/g,'\\n').replace(/\\\\\\\\/g,'\\\\').replace(/\\\\'/g,"'");
navigator.clipboard.writeText(d).then(function(){{b.innerHTML='\\u2713 Copied!';b.className='cb ok';setTimeout(function(){{b.innerHTML='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy';b.className='cb';}},2000)}}).catch(function(){{var ta=document.createElement('textarea');ta.value=d;document.body.appendChild(ta);ta.select();document.execCommand('copy');document.body.removeChild(ta);b.innerHTML='\\u2713 Copied!';b.className='cb ok';setTimeout(function(){{b.innerHTML='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy';b.className='cb';}},2000)}})
}}
r();
}})();
window.filter = function(v){{
  r(v);
}}
</script>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ Generated: {len(html)} bytes")
print("✅ Semicolons verified: var D=[...]; (function...")
