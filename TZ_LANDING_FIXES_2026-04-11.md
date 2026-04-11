# ТЗ — Ревизия и фиксы лендоса ContentSpy

**Дата:** 11 апреля 2026
**Исполнитель:** Даша (landing agent)
**Заказчик:** Сергей (через Катю)
**Срок:** к 16 апреля (день AppSumo submission)
**Файлы:** `/Users/Shared/app sergei/contentspy-landing/`
**Production URL:** https://contentspy.co
**Связанные документы:** `/Users/Agent/workspace/products/contentspy/LAUNCH_PLAN_12W_2026.html`

---

## Контекст

Лендос существует, в целом структура хорошая (Nav → Hero → Stats → How → Features → VS → Proof → Pricing → FAQ → CTA → Footer). Скрипты, анимации, OG-теги, Schema.org — есть. **Полная переделка НЕ нужна — только targeted fixes.**

В рамках новой стратегии v3 (LAUNCH_PLAN_12W_2026.html):
- **AppSumo Select** = приоритет №1 (submission 16 апреля)
- **Новые цены** license-only с Founder Edition $899
- **Email waitlist** = ключевой канал для PH в июне (target 500 подписчиков к концу мая)
- **Apple notarization** = блокер для distribution

Это ТЗ — список **22 правок**, разбитых на 3 блока по приоритетам.

---

## 🔴 БЛОК 1 — КРИТИЧНОЕ (must fix к 16 апреля)

### Fix 1: Обновить ВСЕ цены + лимиты — Solo→Starter, новые суммы и tier limits

**Старые → Новые (UPDATED 11.04.2026 16:30):**
| Позиция | Было | Стало |
|---|---|---|
| Tier 1 имя | Solo | **Starter** |
| Tier 1 цена | $79 (was $99) | **$89** (was $129) |
| Tier 1 profiles limit | unlimited | **20 профилей** |
| Tier 1 devices | 1 | 1 |
| Tier 2 цена | $179 (was $249) | **$189** (was $249) |
| Tier 2 profiles limit | unlimited | **∞ (unlimited)** |
| Tier 2 devices | 1 | 1 |
| Tier 3 цена | $599 (was $799) | **$499** (was $799) |
| Tier 3 profiles limit | unlimited | **∞ (unlimited)** |
| Tier 3 devices | 3 | **5 устройств** |
| Tier 1 описание | "Track competitors" | "Track competitors" (оставить) |
| Tier 2 описание | "Understand why competitors win" | "Understand why competitors win" (оставить) |
| Tier 3 описание | "Turn insights into client work" | "Turn insights into client work" (оставить) |

**ВАЖНО про "lifetime updates" wording:**
- Starter: "12 months of updates (current major version)"
- Pro: "24 months of updates (current major version + all v2.x)"
- Agency: "Lifetime updates (current major version + all v2.x)"
- Founder Edition: "Lifetime updates including all future major versions" (ТОЛЬКО ДЛЯ ФАУНДЕРОВ)

**Зачем такое разделение:** Vaizle потерял репутацию из-за обещания "lifetime updates including all future versions" в LTD кампании. Когда они выпустили v3, AppSumo Sumolings были исключены. Каждый 1-star review до сих пор ссылается на это. **Это reputation damage permanent.** Используем защитную формулировку для всех кроме Founders.

**Файлы для правок:**
- `index.html:51-53` — Schema.org JSON-LD `offers` массив (Solo→Starter $79→$89, Pro $179→$189, Agency $599→$499)
- `index.html:405` — VS table header `from $79 one-time` → `from $89 one-time`
- `index.html:491-494` — VS table cost row, обновить $79 → $89, $599 → $499
- `index.html:564-641` — Pricing section, все 3 cards (Solo→Starter), новые лимиты профилей (20/∞/∞), Agency 3→5 devices
- `index.html:587` (Solo card) — добавить explicit "Up to **20 profiles**" в `<ul class="price-features">`
- `index.html:614` (Pro card) — добавить explicit "**Unlimited profiles**" 
- `index.html:638` (Agency card) — `<div class="price-device">3 devices</div>` → `<div class="price-device">5 devices</div>`
- `index.html:677` — comparison table `Devices` row: `1 / 1 / 3` → `1 / 1 / 5`
- `index.html:778` — Sticky mobile CTA `from $79 one-time` → `from $89 one-time`
- `style.css` — найти все `.price-tier` правила, проверить что Starter не сломал стиль

**Также добавить новые feature limits в comparison table** (`index.html:657-680`):
```html
<tr><td><strong>Profiles tracked</strong></td><td>20</td><td class="highlight-col">Unlimited</td><td>Unlimited</td></tr>
```
вставить как первую строку после `<thead>`

---

### Fix 2: Добавить НОВЫЙ 4-й tier — Founder Edition $899 (Limited 100)

**Куда:** `index.html:564-642` (pricing section), как 4-я карточка ПОСЛЕ Agency

**HTML код для вставки:**
```html
<!-- Founder Edition -->
<div class="price-card price-card-founder" data-animate>
    <div class="price-badge price-badge-limited">⏰ Limited to 100 copies</div>
    <div class="price-tier">Founder Edition</div>
    <div class="price-tagline">For the first 100 believers</div>
    <div class="price-amount">
        <span class="price-dollar">$</span>899
        <span class="price-old">$1,499</span>
    </div>
    <div class="price-period">one-time payment · lifetime everything</div>
    <ul class="price-features">
        <li class="included"><span class="check">✓</span> Everything in Agency, plus:</li>
        <li class="included highlight"><span class="check">⭐</span> <strong>Lifetime updates</strong> — including all major versions forever</li>
        <li class="included highlight"><span class="check">⭐</span> Beta channel — new features 2 weeks early</li>
        <li class="included highlight"><span class="check">⭐</span> Founder Discord — direct line to the team</li>
        <li class="included highlight"><span class="check">⭐</span> Your name in app credits</li>
        <li class="included highlight"><span class="check">⭐</span> 1-hour 1:1 strategy call with the founder</li>
        <li class="included"><span class="check">✓</span> Priority support 12h response</li>
    </ul>
    <div class="price-device">3 devices · founder license</div>
    <a href="LEMONSQUEEZY_URL_FOUNDER" class="btn btn-founder btn-block">Become a Founder</a>
    <p class="price-trust">🔥 <span id="founderCount">87</span> of 100 left · 14-day refund</p>
</div>
```

**CSS для нового стиля** (добавить в `style.css`):
```css
.price-card-founder {
    border: 2px solid #f97316;
    background: linear-gradient(135deg, rgba(249,115,22,0.05), rgba(249,115,22,0.02));
    position: relative;
}
.price-badge-limited {
    background: linear-gradient(135deg, #f97316, #dc2626);
    color: white;
    font-weight: 700;
    animation: pulse 2s infinite;
}
.btn-founder {
    background: linear-gradient(135deg, #f97316, #ea580c);
    color: white;
    font-weight: 700;
}
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.8; }
}
```

**Schema.org** (`index.html:51-53`) добавить 4-й offer:
```json
{ "@type": "Offer", "name": "Founder Edition", "price": "899", "priceCurrency": "USD" }
```

**Pricing grid** в CSS — поменять `grid-template-columns` с 3 на 4 колонки или сделать responsive grid (auto-fit).

---

### Fix 3: Сломанный countdown timer

**Проблема:** `script.js:135` — `deadline = new Date('2026-03-27T23:59:59');` уже прошёл.

**Решение:** Переменная deadline = **30 апреля 2026 23:59:59** (launch pricing window).

```javascript
const deadline = new Date('2026-04-30T23:59:59');
```

Заменить в `script.js:135`.

---

### Fix 4: Pricing CTA buttons — нерабочие

**Проблема:** Все href в pricing buttons = `href="#"`. Кнопки никуда не ведут.

**Решение:** Интегрировать LemonSqueezy checkout URLs.

**После того как Сергей закончит LemonSqueezy setup**, заменить:
- `index.html:588` (Solo button) → `href="https://contentspy.lemonsqueezy.com/checkout/buy/STARTER_VARIANT_ID"`
- `index.html:615` (Pro button) → `href="https://contentspy.lemonsqueezy.com/checkout/buy/PRO_VARIANT_ID"`
- `index.html:639` (Agency button) → `href="https://contentspy.lemonsqueezy.com/checkout/buy/AGENCY_VARIANT_ID"`
- Founder Edition button → `href="https://contentspy.lemonsqueezy.com/checkout/buy/FOUNDER_VARIANT_ID"`

**Также добавить data-attributes для analytics:**
```html
<a href="..." data-tier="starter" data-price="89" class="btn btn-outline btn-block">
```

---

### Fix 5: Email waitlist — НЕ работает

**Проблема:** `script.js:165-173` — windows waitlist form просто прячется при submit, **email никуда не отправляется**. Это потерянный канал лидгена.

**Решение:** Использовать **LemonSqueezy → Customer email collection** через built-in form, ИЛИ **Formspree** ($0 free tier 50 submissions/мес), ИЛИ **ConvertKit** (бесплатный до 1000 подписчиков).

**Рекомендую ConvertKit** — это лучший free tier для email маркетинга, дальше можно отправлять PH/AppSumo blast.

**HTML изменения** (`index.html:712-717`):
```html
<form class="waitlist-form" action="https://app.convertkit.com/forms/FORM_ID/subscriptions" method="post" data-uid="FORM_UID">
    <input type="email" name="email_address" placeholder="your@email.com" class="waitlist-input" required>
    <button type="submit" class="btn btn-sm btn-primary">Notify Me</button>
</form>
```

**Сергею задача:** создать ConvertKit account + получить FORM_ID, передать Даше.

---

### Fix 6: Добавить ЛЕНД МАГНИТ — "Free Viral Hook Swipe File"

**Контекст:** Это критично для PH запуска в июне. Нужно собрать 300–500 email подписчиков к концу мая. Lead magnet = "Free PDF: 50 viral hooks from top Instagram profiles, analyzed by ContentSpy".

**Куда вставить:** Новая секция между Hero и Stats Bar (новая полоса). Альтернатива — между Features и VS section.

**HTML код:**
```html
<!-- LEAD MAGNET -->
<section class="lead-magnet" id="lead-magnet">
    <div class="container">
        <div class="lead-magnet-card">
            <div class="lead-magnet-content">
                <span class="section-tag">🎁 Free Resource</span>
                <h2>Get the Viral Hook Swipe File<br><span class="gradient-text">— 50 hooks that drove 100M+ views</span></h2>
                <p class="lead-magnet-subtitle">A free PDF with 50 hooks ContentSpy extracted from top Instagram, TikTok and YouTube profiles. The exact words. The exact timing. Steal them.</p>
                <ul class="lead-magnet-bullets">
                    <li>✅ 50 verified viral hooks (real examples, not made-up)</li>
                    <li>✅ Categorized by niche (fitness, finance, food, education, lifestyle)</li>
                    <li>✅ With viral score multiplier (5x to 27x)</li>
                    <li>✅ Annotated: why each one works</li>
                </ul>
                <form class="lead-magnet-form" action="https://app.convertkit.com/forms/SWIPE_FILE_FORM_ID/subscriptions" method="post">
                    <input type="email" name="email_address" placeholder="your@email.com" required>
                    <button type="submit" class="btn btn-lg btn-primary">Send Me the Swipe File →</button>
                </form>
                <p class="lead-magnet-trust">No spam. Unsubscribe anytime. We'll also send you ContentSpy launch updates.</p>
            </div>
            <div class="lead-magnet-visual">
                <img src="img/swipe-file-preview.png" alt="Viral Hooks Swipe File Preview" loading="lazy">
            </div>
        </div>
    </div>
</section>
```

**CSS для секции** (новые правила в `style.css`):
```css
.lead-magnet {
    padding: 4rem 0;
    background: linear-gradient(135deg, rgba(249,115,22,0.08), rgba(220,38,38,0.04));
    border-top: 1px solid rgba(249,115,22,0.2);
    border-bottom: 1px solid rgba(249,115,22,0.2);
}
.lead-magnet-card {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    align-items: center;
}
.lead-magnet-form {
    display: flex;
    gap: 0.5rem;
    margin-top: 1.5rem;
}
.lead-magnet-form input {
    flex: 1;
    padding: 0.9rem 1.2rem;
    font-size: 1rem;
    border-radius: 8px;
    border: 1px solid rgba(255,255,255,0.2);
    background: rgba(0,0,0,0.3);
    color: white;
}
@media (max-width: 768px) {
    .lead-magnet-card { grid-template-columns: 1fr; }
    .lead-magnet-form { flex-direction: column; }
}
```

**Сергею задача:**
1. Сгенерировать сам swipe file через ContentSpy на твоих 66 профилях (1 час работы)
2. Сделать обложку PDF (можно через Canva или Figma)
3. Залить на ConvertKit как auto-deliver после подтверждения email

---

### Fix 7: Удалить FAKE TESTIMONIALS — заменить или скрыть

**Проблема:** `index.html:511-547` — 3 testimonials с инициалами Alex R., Maria K., Jake T. **Они выглядят invented** (initials only, generic results, no photos, no LinkedIn). Гугл это палит, AppSumo палит, опытные клиенты палят. Это вредит доверию.

**Решение А (рекомендую — скрыть):** До того как у Сергея будут реальные testimonials от free giveaway 10 SMM-агентств — **полностью скрыть секцию proof**.

```html
<!-- SOCIAL PROOF -->
<!-- HIDDEN until real testimonials collected from free giveaway 10 SMM agencies, target: May 2026 -->
<!--
<section class="proof" id="proof"> ... </section>
-->
```

**Решение Б (если нужен social proof):** Заменить на честные **product proof** (не testimonials):

```html
<section class="proof" id="proof">
    <div class="container">
        <div class="section-header">
            <span class="section-tag">Built For Real Work</span>
            <h2>What ContentSpy Has Already Analyzed</h2>
        </div>
        <div class="proof-stats-grid">
            <div class="proof-stat-card">
                <div class="proof-stat-num">66</div>
                <div class="proof-stat-label">Profiles tracked in beta</div>
            </div>
            <div class="proof-stat-card">
                <div class="proof-stat-num">2,319</div>
                <div class="proof-stat-label">Reels transcribed</div>
            </div>
            <div class="proof-stat-card">
                <div class="proof-stat-num">820</div>
                <div class="proof-stat-label">Tests passing</div>
            </div>
            <div class="proof-stat-card">
                <div class="proof-stat-num">v2.0</div>
                <div class="proof-stat-label">Production ready</div>
            </div>
        </div>
    </div>
</section>
```

**Рекомендую решение А** — полностью скрыть до реальных отзывов. Вакуум честнее лжи.

---

### Fix 8: Privacy Policy + Terms of Service — нет страниц

**Проблема:** `index.html:764-765` — ссылки `#privacy` и `#terms` ведут в никуда. **AppSumo и LemonSqueezy ОБЯЗАТЕЛЬНО требуют privacy policy и terms.**

**Решение:** Создать 2 файла:
- `/Users/Shared/app sergei/contentspy-landing/privacy.html`
- `/Users/Shared/app sergei/contentspy-landing/terms.html`

**Содержание:** Стандартный SaaS template, адаптированный под:
- ContentSpy LLC / PT INDOGIG HRTECH INDONESIA как entity
- Privacy: data processing локально (не на сервере), email через ConvertKit, payment через LemonSqueezy
- Terms: 14-day refund, license terms, BYOK ответственность пользователя
- GDPR compliance section
- Contact: support@contentspy.co

**Готовый template:** https://www.iubenda.com/en/help/19120-website-privacy-policy-template или генератор от LemonSqueezy для merchant'ов.

**Замена ссылок:**
- `index.html:764` → `<a href="privacy.html">Privacy Policy</a>`
- `index.html:765` → `<a href="terms.html">Terms of Service</a>`

---

### Fix 9: Windows update — устаревший FAQ

**Проблема:** `index.html:709-717` — FAQ "Mac or Windows?" говорит "Windows version is coming in v2.2 — launching Q3 2026". В новом плане Windows = Week 1 (16 апреля).

**Решение:**
```html
<div class="faq-item" data-animate>
    <button class="faq-q">Mac or Windows?</button>
    <div class="faq-a">
        <p><strong>Both available now.</strong> ContentSpy ships as native macOS app (.dmg) and Windows installer (.exe). Apple Silicon (M1/M2/M3), Intel, and Windows 10/11 supported.</p>
    </div>
</div>
```

**Также убрать** waitlist form внутри FAQ (Fix 5 заменяет его на главный lead magnet).

---

## 🟡 БЛОК 2 — ВАЖНОЕ (желательно к 16 апреля, можно до AppSumo go-live)

### Fix 10: Anchor pricing в Hero — усилить

**Проблема:** Hero (`index.html:146-182`) не показывает прямое сравнение vs Sprout Social. Это твой главный коммерческий аргумент.

**Решение:** Добавить под `hero-cta` блок с anchor:

```html
<div class="hero-anchor-pricing">
    <span class="anchor-cross">Sprout Social: <s>$2,988/year</s></span>
    <span class="anchor-arrow">→</span>
    <span class="anchor-us"><strong>ContentSpy: $189 once.</strong> Forever.</span>
</div>
```

**CSS:**
```css
.hero-anchor-pricing {
    display: flex;
    gap: 12px;
    align-items: center;
    margin-top: 2rem;
    padding: 12px 20px;
    background: rgba(0,217,126,0.08);
    border: 1px solid rgba(0,217,126,0.3);
    border-radius: 8px;
    font-size: 1rem;
}
.anchor-cross { color: var(--text-dim); }
.anchor-cross s { opacity: 0.6; }
.anchor-us strong { color: var(--accent); }
.anchor-arrow { color: var(--accent); font-weight: 700; }
@media (max-width: 640px) {
    .hero-anchor-pricing { flex-direction: column; align-items: flex-start; }
}
```

---

### Fix 11: API keys — front-load BYOK disclosure (КРИТИЧНО для AppSumo!)

**Контекст:** Research показал что AppSumo НЕ блочит BYOK deals (есть много precedents: AgenticFlow, Triplo AI, Merlin, Afforai, SheetMagic). НО **disclosure quality = #1 driver refund rate** для BYOK products. Прятать BYOK = катастрофа в reviews.

**Что меняется в коде ContentSpy:** Катя поднимает MASTER_APIFY_KEY quota с 5 до **25 analyses/мес** (по результатам benchmarks AppSumo Select deals). MASTER_AI_KEY (Anthropic Haiku) полностью включён, никогда не BYOK на AI слой.

**Проблема `index.html:706`:** FAQ про API keys говорит про BYOK ($3-5/month) сразу. Это барьер.

**Решение — front-load в HERO + переписать FAQ:**

#### A. Hero subtitle (новая строка под main subtitle)

`index.html:157-159` — добавить ПОД hero-subtitle:

```html
<p class="hero-subtitle">
    ContentSpy downloads competitor videos from Instagram, YouTube & TikTok — transcribes every word with AI, breaks down every frame with Storyboard, and shows you exactly why they win and how to replicate it.
</p>
<p class="hero-included">
    ✨ Includes <strong>25 profile analyses per month</strong> via our managed scraping. Want unlimited? Connect your free Apify account (5 min setup, free tier included).
</p>
```

CSS:
```css
.hero-included {
    margin-top: 1rem;
    padding: 12px 20px;
    background: rgba(0,217,126,0.08);
    border: 1px solid rgba(0,217,126,0.3);
    border-radius: 8px;
    font-size: 0.95rem;
    color: var(--text-dim);
    max-width: 700px;
}
.hero-included strong { color: var(--accent); }
```

#### B. FAQ #1 — переписать про API keys

```html
<div class="faq-item" data-animate>
    <button class="faq-q">Do I need any API keys to start?</button>
    <div class="faq-a">
        <p><strong>No setup required to use ContentSpy.</strong> Every license includes <strong>25 profile analyses per month</strong> through our managed scraping infrastructure — no API keys, no credit cards, no friction.</p>
        <p>For unlimited usage, you can connect your own free Apify account in 3 clicks (we'll show you exactly how — there's a Loom video in onboarding). Apify's free tier covers most use cases at $0/month.</p>
        <p>For AI features (analytics, chat, hooks), <strong>we cover the AI costs entirely</strong> — no OpenAI key needed. Power users can optionally connect their own OpenAI/Anthropic key for unlimited AI calls and access to GPT-5 / Claude Opus.</p>
        <p>Compare: Sprout Social charges $249/month and you have zero control over their AI spend. ContentSpy is one-time $89–$499.</p>
    </div>
</div>
```

#### C. FAQ #2 — новый: "What's included vs BYOK?"

Добавить второй FAQ item сразу после первого:

```html
<div class="faq-item" data-animate>
    <button class="faq-q">What's included vs Bring Your Own Key (BYOK)?</button>
    <div class="faq-a">
        <table style="width:100%;font-size:0.9rem;border-collapse:collapse;margin:0.5rem 0;">
            <thead>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.1);">
                    <th style="text-align:left;padding:8px;">Feature</th>
                    <th style="text-align:center;padding:8px;">Included</th>
                    <th style="text-align:center;padding:8px;">Optional BYOK</th>
                </tr>
            </thead>
            <tbody>
                <tr><td style="padding:8px;">Profile analyses (Apify scraping)</td><td style="text-align:center;">25/month</td><td style="text-align:center;">Unlimited via your Apify key</td></tr>
                <tr><td style="padding:8px;">AI Profile Analytics</td><td style="text-align:center;">✅ Unlimited (we pay)</td><td style="text-align:center;">Optional: your OpenAI/Anthropic for GPT-5</td></tr>
                <tr><td style="padding:8px;">Multi-profile Chat</td><td style="text-align:center;">✅ Unlimited (we pay)</td><td style="text-align:center;">Optional: your AI key</td></tr>
                <tr><td style="padding:8px;">Hook generation</td><td style="text-align:center;">✅ Unlimited (we pay)</td><td style="text-align:center;">Optional</td></tr>
                <tr><td style="padding:8px;">Local Whisper transcription</td><td style="text-align:center;">✅ 100% free (runs on your Mac)</td><td style="text-align:center;">N/A</td></tr>
                <tr><td style="padding:8px;">Telegram Tag Bot, Viral Alerts</td><td style="text-align:center;">✅ Free</td><td style="text-align:center;">N/A</td></tr>
            </tbody>
        </table>
        <p>Bottom line: <strong>You can use ContentSpy productively for life with $0 in API costs.</strong> BYOK is for power users who need unlimited Apify scraping (e.g., agencies tracking 100+ profiles).</p>
    </div>
</div>
```

#### D. Что НЕ говорить (запрещено)
- ❌ "BYOK" как голый акроним — заменить на "connect your free Apify account"
- ❌ Прятать API key requirement в footer fine print
- ❌ Mention только в TOS (юзеры это не читают)
- ❌ Обещать "unlimited Apify" в pricing tier — это враньё
- ❌ Скрывать что для unlimited нужен Apify

**Зачем это критично:** Common complaints в 1-star AppSumo reviews для BYOK products: *"Why not state that from the beginning then?"* (Content Boom). Юзеры accept BYOK, но punish скрытое disclosure. Front-loading = страховка от refund spike в weeks 1-2 кампании.

---

### Fix 12: CTA texts — слабые

**Проблема:** "Get Solo / Get Pro / Get Agency" — generic, не action-oriented.

**Решение:**
- Solo (Starter) button → "**Try Starter — 7 days free**"
- Pro button → "**Start Pro — Best Value**"
- Agency button → "**Get Agency — 3 devices**"
- Founder button → "**Become a Founder — Limited**"

Hero CTA: "Start Free 7-Day Trial" — оставить, это хорошо.

Final CTA section: добавить второй CTA "Or skip the trial — Get Pro $189"

---

### Fix 13: Hero micro — "no installation needed" неправда

**Проблема:** `index.html:169` — `<span class="hero-micro">No credit card required · No installation needed</span>`

ContentSpy = desktop app, **установка ОБЯЗАТЕЛЬНА** (DMG/EXE). Это противоречит реальности.

**Решение:**
```html
<span class="hero-micro">No credit card required · 2-minute setup · Cancel anytime</span>
```

---

### Fix 14: Stats bar — обосновать или скрыть

**Проблема:** `index.html:184-205` — статы `748M+ Views Analyzed`, `27.2× Peak Viral Score`, `3 Platforms`, `$0 Monthly Fee`. Цифры выглядят invented (особенно 748M+).

**Решение:** Обосновать или заменить на честные:

```html
<section class="stats-bar">
    <div class="container">
        <div class="stats-grid">
            <div class="stat-item" data-animate>
                <div class="stat-num" data-count="2319" data-suffix="+">0+</div>
                <div class="stat-label">Reels transcribed in beta</div>
            </div>
            <div class="stat-item" data-animate>
                <div class="stat-num" data-count="27.2" data-suffix="×" data-decimals="1">0×</div>
                <div class="stat-label">Peak viral score detected</div>
            </div>
            <div class="stat-item" data-animate>
                <div class="stat-num">3</div>
                <div class="stat-label">Platforms in one app</div>
            </div>
            <div class="stat-item" data-animate>
                <div class="stat-num">$0</div>
                <div class="stat-label">Monthly fee — ever</div>
            </div>
        </div>
    </div>
</section>
```

Цифра 2319 = реальное количество reels из CHANGELOG_v4 (rebuild-hooks migration).

---

### Fix 15: Поддержка email

**Проверить:** работает ли `hello@contentspy.co` (упоминается в footer `index.html:763`). Если домен только-только настроен — может быть не настроен MX.

**Решение:**
1. Сергею проверить MX записи на contentspy.co
2. Настроить через Cloudflare Email Routing → forward на личный gmail
3. Или Google Workspace ($6/мес) для real `support@contentspy.co`
4. Заменить `hello@contentspy.co` → `support@contentspy.co` (более профессионально)

---

### Fix 16: Добавить FAQ "What about ChatGPT/Claude?"

**Контекст:** В 2026 это будет частый вопрос — "почему я не могу просто спросить ChatGPT?"

**Решение:** Добавить новый FAQ item после "What is your refund policy?":

```html
<div class="faq-item" data-animate>
    <button class="faq-q">Why not just use ChatGPT or Claude?</button>
    <div class="faq-a">
        <p>ChatGPT and Claude don't have access to your competitors' actual videos. They can't transcribe Instagram Reels, can't extract real hooks from real content, and can't track viral patterns over time.</p>
        <p>ContentSpy <strong>downloads the actual videos</strong>, transcribes every word locally, and builds a searchable library across 40+ competitors. Then, you can use ChatGPT/Claude/Ollama (your choice) to chat with that real data — that's where ContentSpy's AI Chat feature comes in.</p>
        <p>It's not "instead of" — it's "with". ContentSpy is the data layer. AI is the interpretation layer.</p>
    </div>
</div>
```

---

### Fix 17: AppSumo soft mention (для будущего)

**Контекст:** Когда AppSumo одобрит deal (mid-May), нужно место для AppSumo banner. Сейчас просто подготовить место.

**Решение:** Добавить в footer hidden div, который потом активируется:

```html
<!-- APPSUMO BANNER (activated when AppSumo deal goes live) -->
<div class="appsumo-banner" id="appsumoBanner" style="display:none;">
    <p>🎉 We're live on AppSumo! Get ContentSpy for as low as $59 (limited time)</p>
    <a href="APPSUMO_URL" class="btn btn-primary">View AppSumo Deal →</a>
</div>
```

Сейчас просто скрыто, потом одной строкой включится через JavaScript.

---

## 🔵 БЛОК 3 — Nice to have (можно после AppSumo submission)

### Fix 18: Exit intent popup

**Цель:** Capture email от уходящих посетителей.

**Решение:** Добавить exit-intent popup с offer "Get the Viral Hook Swipe File before you go" → ConvertKit form. Простая JavaScript логика на `mouseleave` event window.

### Fix 19: Carousel в hero вместо одного screenshot

**Решение:** Auto-rotate между 3 screenshot'ами (dashboard, ai-analysis, hooks) каждые 4 секунды. Уже есть `floater` элементы, можно их использовать.

### Fix 20: Performance audit

**Действия:**
- Lighthouse run на текущей версии (target: 90+ Performance, 100 Accessibility)
- Проверить размер `demo-slideshow.mp4` (если >5MB — пережать)
- Lazy load для feature images (уже есть `loading="lazy"` в большинстве, проверить все)
- Preload критических ресурсов: `style.css`, `dashboard.png`

### Fix 21: Open Graph image

**Проблема:** OG image сейчас = `dashboard.png`. Это screenshot. Лучше — кастомный OG image 1200×630 с logo + tagline + product image.

**Решение:** Создать `img/og-card.png` 1200×630 через Figma/Canva. Обновить:
- `index.html:20` → `og:image`
- `index.html:28` → `twitter:image`

### Fix 22: A/B тест pricing — Founder Edition placement

**Идея:** Тестировать 2 варианта:
- A: Founder Edition как 4-я карточка справа
- B: Founder Edition как floating banner поверх pricing с "Limited 100 left" badge

Через 1 неделю смотрим конверсию. Решение — A (проще, без сложной логики).

---

## Summary

**Total fixes:** 22
**Block 1 (critical):** 9 fixes — обязательно к 16 апреля
**Block 2 (important):** 8 fixes — желательно к 16, можно до go-live
**Block 3 (nice-to-have):** 5 fixes — после AppSumo submission

**Estimated time для Даши:**
- Block 1: 6–8 часов
- Block 2: 4–6 часов
- Block 3: 4 часа

**Дедлайны:**
- **К 13 апреля 18:00** — все Block 1 fixes готовы
- **К 14 апреля 18:00** — все Block 2 fixes готовы
- **К 15 апреля 18:00** — financial QA, Lighthouse, mobile тест
- **16 апреля** — лендос финал live, готов к AppSumo submission

---

## Зависимости от Сергея

1. **LemonSqueezy URLs** для Starter/Pro/Agency/Founder checkout — после payout setup
2. **ConvertKit FORM_ID** — после регистрации account
3. **Swipe File PDF** — после генерации через ContentSpy + Canva обложку
4. **Privacy/Terms templates** — Сергей выбирает (iubenda generator или Termly)
5. **MX records** для contentspy.co — proverить и настроить email forwarding

## Зависимости от Кати (агента)

1. **MASTER_APIFY_KEY вшит** — иначе FAQ #11 текст про "5 free analyses" неправда
2. **Windows .exe готов и протестирован** — иначе FAQ #9 текст про Windows неправда
3. **Apple notarized DMG** — иначе при скачивании юзер увидит "ContentSpy is damaged"

## Контрольные точки

После каждого блока — отчёт в Telegram + push в git:
```bash
cd "/Users/Shared/app sergei/contentspy-landing"
git add . && git commit -m "Block 1: critical landing fixes (Starter $89, Founder Edition, lead magnet)"
git push
```

---

**Документ согласован Катей, передан Даше для исполнения.**
**Связанная стратегия:** `/Users/Agent/workspace/products/contentspy/LAUNCH_PLAN_12W_2026.html`
