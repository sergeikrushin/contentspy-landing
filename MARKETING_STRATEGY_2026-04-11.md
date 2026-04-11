# ContentSpy Landing — Marketing Strategy Brief

**Дата:** 11 апреля 2026
**Автор:** Катя (как маркетолог, не как dev)
**Аудитория:** Сергей (decision maker), Даша (implementation)
**Цель документа:** Стратегическая структура лендоса, основанная на психологии посетителя, маркетинговых фреймворках и всём что мы проработали (Vaizle deep-dive, BYOK research, desktop economics, новые цены)

**Связанные документы:**
- `LAUNCH_PLAN_12W_2026.html` — общая стратегия запуска
- `TZ_LANDING_FIXES_2026-04-11.md` — детальные тех-правки (22 фикса)
- Этот документ — **СТРАТЕГИЧЕСКАЯ СТРУКТУРА**, должна читаться ПЕРЕД техническим ТЗ

---

## 0. Маркетинговая исходная точка

### Кто наш посетитель и откуда он пришёл?

ContentSpy получает трафик из 6 разных источников. У каждого источника свой mindset:

| Источник | Mindset посетителя | Что он ждёт от лендоса | % трафика (estimate) |
|---|---|---|---|
| **AppSumo deal page** | "Бой за best LTD deal. Покажи value за $59" | Сравнение с retail price, чёткие лимиты, отзывы | 40–60% (после go-live) |
| **ProductHunt** | "Что нового сегодня? Maker, расскажи историю" | Founder story, demo video, community feel | 10–15% (PH day) |
| **LinkedIn cold outreach** | "Кто-то прислал, посмотрю. Это для агентств?" | Agency-specific value, white-label proof | 15–20% |
| **Reddit (r/SMMA, etc)** | "Скрытая реклама? Покажи реальную пользу" | Honest mechanism, не PR-trash | 10–15% |
| **Google organic SEO** | "Ищу tool для competitor analysis" | Сравнение с альтернативами, цена | 5–10% |
| **Direct (word-of-mouth)** | "Друг порекомендовал, купить?" | Trust signals, отзывы, refund policy | 5% |

**Вывод #1:** Лендос должен работать на **3 разные аудитории одновременно** — solo freelancer, content team, agency owner. Не одна targeting persona, а **persona switching**.

**Вывод #2:** AppSumo трафик будет **самым большим** после launch. Лендос должен быть optimized под **deal-hunter mindset**: сравнения, лимиты, отзывы, цена, urgency.

**Вывод #3:** Direct sales трафик — это **высокоосознанные buyers**, которые хотят серьёзный продукт. Им нужен founder story, depth of features, не маркетинговый шум.

### Топ-7 вопросов которые посетитель задаёт за первые 10 секунд

В порядке приоритета (data из user research SaaS landing pages):

1. **Что это вообще?** (positioning) — должен быть ясен за 3 секунды
2. **Это для меня?** (audience match) — за 5 секунд
3. **Чем отличается от X?** (differentiation) — за 7 секунд (X = Sprout/ChatGPT/Iconosquare)
4. **Сколько стоит?** (pricing reality) — за 10 секунд (anchor)
5. **Можно доверять?** (trust) — на втором экране
6. **Что внутри?** (features) — на третьем экране
7. **Какие подводные камни?** (objections) — на четвёртом экране

**Если за первые 10 секунд visitor не получил ответы — он ушёл.** Bounce rate AppSumo deal pages: 60–70% за 15 секунд.

---

## 1. Маркетинговые фреймворки которые применяем

### 1.1 AIDA — структурный backbone

| Этап | Цель | Где на лендосе |
|---|---|---|
| **Attention** | Hook за 3 секунды | Hero (tagline + value prop) |
| **Interest** | Заинтересовать механизмом | How It Works + Features |
| **Desire** | Создать желание | Anchor pricing + Persona switcher + Vs competitors |
| **Action** | Конверсия | Pricing CTA + Lead magnet (для не-готовых) |

### 1.2 PAS — Problem / Agitation / Solution

Это вторая секция после Hero. Главная задача — **активировать существующую боль** посетителя, чтобы Solution выглядел естественным.

**Problem:** "Ты тратишь 3 часа в день на мониторинг конкурентов вручную"
**Agitation:** "К моменту когда ты понял что зашло — тренд уже умер. Sprout Social берёт $249/мес за vanity metrics. Iconosquare lock-in. Это всё не работает."
**Solution:** "ContentSpy скачивает видео конкурентов, транскрибирует каждое слово локально, вычисляет вирусный score и показывает точный паттерн виралки. Заплатил один раз. Работает офлайн. Privacy-first."

### 1.3 StoryBrand (Hero / Guide / Plan / Action)

- **Hero:** SMM-фрилансер / контент-команда / агентство (visitor)
- **Guide:** ContentSpy (продукт)
- **Plan:** 3 шага — установи / добавь конкурентов / получи insights
- **Action:** Start trial / Buy Pro / Become Founder

Visitor — герой, ContentSpy — Yoda. Сергей — НЕ герой. Это критично: лендос **не про Сергея**, он про visitor'а.

### 1.4 Anchor pricing (psychological pricing)

**Правило:** Сначала показать высокую цену конкурента, потом нашу низкую. Это создаёт perception of value.

```
Sprout Social: $2,988/year forever
Rival IQ: $2,868/year forever
Iconosquare: $948/year forever
                    ↓
ContentSpy: $189 once. Forever.
```

Это формула должна появиться **3 раза** на лендосе:
1. В Hero (anchor sentence)
2. В Vs Competitors таблице
3. В Pricing section header

### 1.5 Risk reversal (объект-handling)

**14-day money-back guarantee** + **7-day free trial** = **21 день полностью без риска**.

Должно быть:
- В Hero (small text под CTA)
- В каждой Pricing card
- В FAQ
- В Footer

Цель — сделать "не покупать" иррациональным выбором.

### 1.6 Social proof ladder

С самых сильных к самым слабым:

| Уровень | Что | У нас есть? |
|---|---|---|
| 1 | **Видео-отзывы реальных клиентов** | ❌ нет (получим после free giveaway) |
| 2 | **Названные case studies с цифрами** | ❌ нет |
| 3 | **Логотипы клиентских компаний** | ❌ нет |
| 4 | **Письменные отзывы с фото и должностью** | ❌ нет (есть FAKE — убираем!) |
| 5 | **Численная статистика продукта** | ✅ ДА (820 тестов, 2,319 reels, 66 профилей) |
| 6 | **Authority признание** (PH/AppSumo badges)** | 🟡 после launch |
| 7 | **Founder credentials** | ✅ ДА (Сергей's background) |

**Стратегия:** До получения уровней 1–4 — используем 5–7. **НЕ ВРЁМ.** Fake testimonials хуже отсутствия отзывов (палится 1-секундный поиск гуглом, AppSumo BD палит на review, AppSumo customers палят в комментах).

### 1.7 Scarcity (ethical urgency)

Два слоя:
1. **Founder Edition limited 100** — реальная ограниченность. Counter "87 of 100 left" должен быть **настоящим** (LemonSqueezy webhook → JS counter)
2. **Launch pricing window** — до 30 апреля цены X, после Y. Должен быть **реальным** (после 30 апреля цены повышаются на 10–20%)

Не делаем fake countdown timer на 24 часа который вечно перезапускается. Это **damage to trust**.

---

## 2. Структура лендоса — секция за секцией

Я расписал **13 секций** в порядке psychological flow. Каждая секция = 1 conversion goal + 1 главный вопрос visitor'а.

### Section 1 · HERO (above the fold)

**Goal:** Hook attention за 3 секунды + ответ на 3 вопроса (что / для кого / почему сейчас)
**Visitor question:** "Что это и зачем мне?"
**Conversion:** Click "Start Trial" или "Watch Demo" или scroll down

#### Components

```
[NAV: Logo · Features · Pricing · FAQ · "Get ContentSpy"]

╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║  [Platform badges: Instagram · TikTok · YouTube]          ║
║                                                           ║
║  H1 (BIG): Reverse-engineer every viral post             ║
║            in your competitor's niche.                    ║
║                                                           ║
║  H2 (sub): ContentSpy downloads competitor videos,       ║
║  transcribes every word locally, extracts viral hooks,   ║
║  and shows you the exact pattern that makes content      ║
║  explode.                                                 ║
║                                                           ║
║  ┌─────────────────────────────────────────────┐         ║
║  │ ✨ Includes 25 profile analyses/month       │         ║
║  │ Unlimited via free Apify account            │         ║
║  └─────────────────────────────────────────────┘         ║
║                                                           ║
║  [PRIMARY CTA: Start Free 7-Day Trial →]                 ║
║  [SECONDARY: Watch 60-Second Demo ▷]                     ║
║                                                           ║
║  Trust line: macOS + Windows · No credit card · 14d refund║
║                                                           ║
║  ┌──────────── ANCHOR PRICING ────────────┐              ║
║  │ Sprout Social: $2,988/yr forever       │              ║
║  │            ↓                            │              ║
║  │ ContentSpy: $189 once. Forever.        │              ║
║  └─────────────────────────────────────────┘              ║
║                                                           ║
║  [HERO VISUAL: animated GIF of actual UI                  ║
║   showing scrape → transcript → viral score]              ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

#### Copy specifics

**Tagline candidates (выбираем 1, A/B тест 2):**

| # | Tagline | Длина | Strength |
|---|---|---|---|
| A | **Reverse-engineer every viral post in your niche.** | 50 chars | Mechanism + benefit |
| B | Read every word your competitors say. See every frame they use. | 60 chars | Visceral, current |
| C | The competitor analysis tool that decodes virality, not vanity metrics. | 70 chars | Direct comparison |
| D | Stop guessing what's working in your niche. Start spying. | 56 chars | Action-oriented |

**Моя рекомендация: A.** Causes curiosity ("how do you reverse-engineer?"), promises mechanism, и benefit-driven. B — runner-up.

**Subtitle (ключевые слова):**
- "downloads" (visceral, конкретно)
- "transcribes every word locally" (privacy + completeness)
- "viral hooks" (что нужно)
- "exact pattern" (precision)
- "explode" (emotional)

**ВАЖНО про BYOK в Hero:** Front-loaded badge "✨ Includes 25 profile analyses/month" **сразу под subtitle**. Это снимает 70% BYOK-возражений до того как они появятся.

### Section 2 · PROBLEM AGITATION (PAS opener)

**Goal:** Активировать существующую боль visitor'а
**Visitor question:** "Это говорит про мою проблему?"
**Conversion:** Эмоциональный buy-in для следующих секций

#### Layout: 3 пунктом painpoint cards

```
┌─────────────────────┬─────────────────────┬─────────────────────┐
│ ⏱ 3 hours/day       │ 📉 Trends die      │ 💸 $249/month       │
│                     │                     │                     │
│ You spend 3 hours   │ By the time you've  │ Sprout Social wants │
│ every day watching  │ understood why a    │ $2,988/year for     │
│ competitor reels    │ video went viral,   │ vanity metrics. You │
│ manually. Spreadshe-│ the trend is        │ pay forever, you    │
│ ets, screenshots,   │ already over.       │ get likes counts.   │
│ notes — none of it  │                     │                     │
│ scales.             │                     │                     │
└─────────────────────┴─────────────────────┴─────────────────────┘

H2: There has to be a better way.
```

#### Copy guidance

- Каждый pain point = 30–40 слов (не больше)
- Used real numbers (3 hours, $249, $2,988)
- Conversational tone, не corporate
- Last line — bridge к solution

### Section 3 · SOLUTION INTRO (PAS closer)

**Goal:** Position ContentSpy как unique answer
**Visitor question:** "OK, как это решает мою проблему?"
**Conversion:** Visitor хочет узнать больше деталей

#### Layout

```
[Section tag: The Solution]

H2: ContentSpy is the only desktop app that
    decodes virality, not just measures it.

[3 line subtitle:
"Downloads competitor videos. Transcribes every word locally.
Extracts viral hooks. Scores virality. Shows you the exact
pattern that makes content explode. Pay once. Run privately.
Win competitively."]

[3 unique badges in a row:]
🎯 Word-for-word transcription · 🔥 Viral score (5×+) · 🎬 Frame-by-frame storyboard
```

### Section 4 · HOW IT WORKS (4 steps)

**Goal:** Reduce perceived complexity ("это сложно настроить?")
**Visitor question:** "Как быстро я смогу начать?"
**Conversion:** Снижение барьера к покупке

#### Layout: 4 cards с цифрами

```
┌──────┬──────┬──────┬──────┐
│  1   │  2   │  3   │  4   │
│ ⬇   │ ➕   │ 🔄   │ 🎯   │
│Install│ Add  │Sync  │Get   │
│ &   │compe-│Conte-│insig-│
│Setup │titors│ntSpy │hts   │
│2 min │paste │does  │AI    │
│      │URL   │work  │ana-  │
│      │      │24/7  │lysis │
└──────┴──────┴──────┴──────┘

[Below: Embedded 60-sec demo video, autoplay muted, looped]
```

#### Copy

- Step 1: "Download .dmg or .exe. Drag to Applications. 2-minute setup with master keys included."
- Step 2: "Paste any Instagram, YouTube, or TikTok profile URL. ContentSpy auto-detects platform."
- Step 3: "Background sync downloads videos, transcribes locally, computes viral scores. No active work."
- Step 4: "AI generates insights, hooks, content ideas, 30-day plans. Ready to use."

### Section 5 · 5 KEY FEATURES (визуальные блоки)

**Goal:** Показать 5 differentiating features с screenshots/GIFs
**Visitor question:** "Что именно я получаю?"
**Conversion:** Justification для цены

#### Структура: 5 alternating layout blocks (left/right text + visual)

| # | Feature | Hook line | Visual | Tier |
|---|---|---|---|---|
| 1 | **Word-for-word transcription** | "Read 50 reels in 5 minutes instead of 5 hours" | GIF: Reel → text appearing | All |
| 2 | **Viral Score (5×+)** | "Find videos that did 27× the average — automatically" | Screenshot: viral badge on reel | All |
| 3 | **Multi-Profile AI Chat** | "Chat with 5 competitors at once. AI cites them by @username" | GIF: chat with profile chips | Pro+ |
| 4 | **Frame-by-frame Storyboard** | "Decode the exact moment a video hooked millions" | GIF: video → frames + text | Pro+ |
| 5 | **Privacy-first desktop** | "Your data stays on your Mac. No cloud, no vendor lock-in" | Icon: lock + Mac silhouette | All |

#### Copy patterns

Каждая фича = одна **ОСНОВНАЯ строка benefit** + 3 bullet points с конкретикой:

```
H3: Read every word your competitors say.

Whisper AI transcribes every reel locally on your Mac.
Search across 40 profiles instantly. No cloud upload.

✓ Local Whisper transcription (no API costs)
✓ 20+ languages supported
✓ Search across all transcripts
```

### Section 6 · WHO IS THIS FOR? (Persona Switcher)

**Goal:** Self-qualification — visitor выбирает свою persona, лендос показывает relevant tier
**Visitor question:** "Это для меня или для кого-то другого?"
**Conversion:** Самоидентификация → emotional buy-in для соответствующего pricing tier

#### Layout: 3 (или 4) персона-карточки

```
H2: Built for content professionals at every stage

┌─────────────────┬─────────────────┬─────────────────┐
│   👤 Solo       │   👥 Team       │   🏢 Agency     │
│                 │                 │                 │
│ I'm a freelance │ I run content   │ I manage 10+    │
│ SMM specialist  │ for a brand     │ client accounts │
│                 │                 │                 │
│ • 5–20 profiles │ • 20+ profiles  │ • Unlimited     │
│ • Solo work     │ • All AI tools  │ • White-label   │
│ • $89 once      │ • $189 once     │ • $499 once     │
│                 │                 │                 │
│ [→ See Starter] │ [→ See Pro]     │ [→ See Agency]  │
└─────────────────┴─────────────────┴─────────────────┘
```

Click → smooth scroll to соответствующий tier in pricing section.

### Section 7 · VS COMPETITORS (anchor pricing visualisation)

**Goal:** Justify premium positioning, anchor против $249/мес tools
**Visitor question:** "Чем это лучше Sprout Social / Iconosquare?"
**Conversion:** Rational justification для clicking pricing

#### Layout: comparison table

```
H2: What other tools simply can't do

[Section tag: Why ContentSpy]

[Big intro paragraph: "SaaS dashboards show you vanity metrics.
ContentSpy gives you the actual intelligence — every word,
every frame, every winning pattern."]

┌─────────────────────────┬───────────┬──────────┬──────────┬──────────┐
│ Capability              │ContentSpy │Sprout    │Rival IQ  │Iconosquare│
│                         │ $189 once │$249/mo   │$239/mo   │$79/mo    │
├─────────────────────────┼───────────┼──────────┼──────────┼──────────┤
│ Full video transcription│    ✅    │   ❌    │   ❌    │   ❌    │
│ (Industry First)        │           │          │          │          │
├─────────────────────────┼───────────┼──────────┼──────────┼──────────┤
│ Frame-by-frame Storybd  │    ✅    │   ❌    │   ❌    │   ❌    │
│ (Industry First)        │           │          │          │          │
├─────────────────────────┼───────────┼──────────┼──────────┼──────────┤
│ AI multi-profile chat   │    ✅    │   ❌    │   ❌    │   ❌    │
├─────────────────────────┼───────────┼──────────┼──────────┼──────────┤
│ Viral score detection   │    ✅    │   ❌    │ ⚠️ basic │   ❌    │
├─────────────────────────┼───────────┼──────────┼──────────┼──────────┤
│ Track 40+ competitors   │    ✅    │ ⚠️5-10  │ ⚠️10-20 │ ⚠️ ltd  │
├─────────────────────────┼───────────┼──────────┼──────────┼──────────┤
│ 100% private (local)    │    ✅    │   ❌    │   ❌    │   ❌    │
├─────────────────────────┼───────────┼──────────┼──────────┼──────────┤
│ No monthly fee          │    ✅    │   ❌    │   ❌    │   ❌    │
├─────────────────────────┼───────────┼──────────┼──────────┼──────────┤
│ Lifetime price          │ $189 once │$2,988/yr │$2,868/yr │$948/yr  │
└─────────────────────────┴───────────┴──────────┴──────────┴──────────┘
```

### Section 8 · PROOF (build trust without fake testimonials)

**Goal:** Trust signals, even without real testimonials
**Visitor question:** "Можно ли этому доверять?"
**Conversion:** Снижает risk perception

#### Strategy: Honest stats, не fake reviews

Поскольку у нас нет реальных testimonials до free giveaway, используем **product proof**:

```
H2: Built in production. Tested in beta.

┌─────────────┬─────────────┬─────────────┬─────────────┐
│   2,319    │     820     │    66      │   v2.0     │
│   Reels   │    Tests   │  Profiles  │ Production│
│transcribed│  passing   │  in beta   │   ready   │
│  in beta  │            │            │            │
└─────────────┴─────────────┴─────────────┴─────────────┘

[After PH/AppSumo launches, add:]

🏆 Featured on Product Hunt — May 2026
⭐ 4.8★ on AppSumo (X reviews)
📊 Built by Sergey, indie founder · BYOK tools community
```

**После free giveaway 10 SMM-агентств** → добавить реальные testimonials (Section 8.5).

### Section 9 · BYOK FAQ (objection-handling front-loaded)

**Goal:** Kill #1 objection ("do I need API keys?") до того как visitor дойдёт до pricing
**Visitor question:** "Это требует настройки API ключей? Это работа?"
**Conversion:** Снимает блокер для AppSumo deal-hunters

#### Layout: Большая FAQ секция перед Pricing

**Это критическая секция.** На AppSumo refund rate напрямую коррелирует с тем, как чётко disclosed BYOK.

```
H2: No API keys to start. No surprises later.

[Big card with table:]

┌─────────────────────────────────┬──────────────┬─────────────────────┐
│ Feature                         │ Included     │ Optional BYOK       │
├─────────────────────────────────┼──────────────┼─────────────────────┤
│ Profile analyses (Apify)        │ 25/month     │ Unlimited via key   │
│ AI Profile Analytics            │ ✅ Unlimited │ Optional GPT-5      │
│ Multi-profile Chat              │ ✅ Unlimited │ Optional Claude     │
│ Hook generation                 │ ✅ Unlimited │ Optional            │
│ Local Whisper transcription     │ ✅ Free forever (runs on your Mac) │
│ Telegram Tag Bot, Viral Alerts  │ ✅ Free                              │
└─────────────────────────────────┴──────────────┴─────────────────────┘

Bottom line: You can use ContentSpy productively for life with $0 in API costs.
BYOK is for power users who need unlimited Apify scraping (e.g., agencies tracking 100+ profiles).
```

И ниже — стандартный FAQ accordion с топ-вопросами:

1. **Do I need any API keys to start?** ← FRONT-LOADED, must be #1
2. **What's included vs BYOK?** ← second
3. Mac or Windows? ← both available now
4. How does the trial work?
5. What's your refund policy?
6. Why not just use ChatGPT?
7. Is my data private?
8. Can I switch devices?

### Section 10 · PRICING (the actual purchase moment)

**Goal:** Конверсия. Реальная покупка.
**Visitor question:** "Какой tier мне подходит и сколько он стоит?"
**Conversion:** Click LemonSqueezy checkout button

#### Layout: 4 carded grid (responsive)

```
H2: One Payment. Lifetime Access. No Monthly Fees.

[Subtitle: "Launch pricing ends April 30. Prices go up 20% in May."]

[Optional: real countdown timer to April 30]

┌─────────┬─────────┬─────────┬─────────┐
│ Starter │   Pro   │ Agency  │ Founder │
│         │ ★ POP   │         │ ⏰ 100  │
│  $89   │  $189  │  $499  │  $899  │
│  once   │  once   │  once   │  once   │
│         │         │         │         │
│ 1 dev   │ 1 dev   │ 5 dev   │ 5 dev   │
│ 20 prof │ ∞ prof  │ ∞ prof  │ ∞ prof  │
│ Basics  │ +AI all │ +Reports│+Lifetime│
│         │         │         │+Discord │
│         │         │         │+1h call │
│         │         │         │         │
│[GET]   │[GET]   │[GET]   │[BECOME] │
│Try free│Best Val│5 device│Founder! │
└─────────┴─────────┴─────────┴─────────┘

🔒 14-day refund · 7-day free trial · Secure checkout via LemonSqueezy
```

#### Copy для buttons (CTA)

| Tier | Button text |
|---|---|
| Starter | "**Try Starter — 7 days free**" |
| Pro | "**Start Pro — Best Value**" |
| Agency | "**Get Agency — 5 devices**" |
| Founder | "**Become a Founder** — Limited 100" |

#### Founder Edition — особое внимание

```
┌──────────────────────────────────┐
│ ⏰ LIMITED TO 100 COPIES         │ ← orange glow, pulse animation
│                                   │
│      Founder Edition              │
│   For the first 100 believers     │
│                                   │
│        $899 once                  │
│      lifetime everything          │
│                                   │
│ ✅ Everything in Agency, plus:    │
│ ⭐ Lifetime updates ALL versions  │
│ ⭐ Beta channel — 2 weeks early   │
│ ⭐ Founder Discord access         │
│ ⭐ Your name in app credits       │
│ ⭐ 1-hour 1:1 strategy call       │
│                                   │
│ [BECOME A FOUNDER]                │
│                                   │
│ 🔥 87 of 100 left                │ ← REAL counter via webhook
└──────────────────────────────────┘
```

### Section 11 · LEAD MAGNET (capture non-buyers)

**Goal:** Email waitlist для тех кто не готов покупать сейчас
**Visitor question:** "Не готов купить, но интересно. Что-то бесплатное есть?"
**Conversion:** Email signup → ConvertKit drip → eventually buy / PH supporter

#### Layout: full-width section с visual

```
[Background: subtle gradient]

H2: Not ready to buy? Get the Free Viral Hook Swipe File.

[Subtitle: "50 hooks that drove 100M+ views. Real examples
from real Instagram, TikTok, and YouTube profiles. Extracted
by ContentSpy. Annotated by category and viral score."]

┌─────────────────────────────────────┬───────────────┐
│ ✅ 50 verified viral hooks          │   [PDF       │
│ ✅ Categorized by niche             │    cover     │
│ ✅ With viral score multiplier      │    image]    │
│ ✅ Annotated: why each one works    │              │
│                                      │              │
│ [email input] [Send Me the Hooks →] │              │
│                                      │              │
│ No spam. We'll also send launch     │              │
│ updates and 1 weekly tip.            │              │
└─────────────────────────────────────┴───────────────┘
```

### Section 12 · FINAL CTA + RISK REVERSAL

**Goal:** Last chance, make it impossible to say no
**Visitor question:** "Купить сейчас или подумать ещё?"
**Conversion:** Last-attempt purchase

#### Layout

```
H2: Stop Guessing. Start Spying.

[Subtitle: "Your competitors are posting right now.
Know what's working before they do."]

[Big primary CTA: Start Free 7-Day Trial →]
[Secondary: See Pricing]

[Trust line:
🔒 7-day free trial · 14-day money-back guarantee · 25 free analyses included
macOS + Windows · 820 tests passing · v2.0 production ready]
```

### Section 13 · FOOTER

```
ContentSpy 🔍                     PRODUCT          COMPANY         LEGAL
Built for creators who            Pricing          Founder Story  Privacy Policy
take content seriously.           Features         Blog (soon)    Terms of Service
                                  FAQ              Roadmap        Refund Policy
[Logo]                            Changelog        Affiliate
                                                                  
Twitter: minimal · IG: @contentspy_app · LinkedIn: ContentSpy

support@contentspy.co · © 2026 ContentSpy. All rights reserved.

[STICKY MOBILE CTA bottom: "ContentSpy from $89 once · [Get Started →]"]
```

---

## 3. Mobile-first considerations

AppSumo audience: **45–55% mobile**. Mobile experience должен быть first-class.

### Mobile-specific changes

| Element | Desktop | Mobile |
|---|---|---|
| Hero | 2-column (text + visual) | Stacked, visual under text |
| CTAs | Side-by-side | Stacked, full-width |
| Stats bar | 4 columns | 2x2 grid |
| Features | Alternating L/R | All centered, stacked |
| Persona switcher | 3 cards row | Swipe carousel |
| Comparison table | Full table | Horizontal scroll OR collapsed |
| Pricing | 4 cards row | 1 card per screen, swipe |
| FAQ | Full accordion | Same |
| Footer | Multi-column | Stacked accordion |
| Sticky CTA bar bottom | No | Yes (always visible) |

### Mobile copy adjustments

- Tagline shorter on mobile (max 8 words)
- Subtitle 2 lines max
- Feature descriptions 1 sentence each
- Pricing CTAs full-width buttons

---

## 4. Conversion optimization

### 4.1 Tracking что обязательно

| Tool | Что | Бесплатно? |
|---|---|---|
| **Plausible Analytics** | Page views, conversions, source | $9/мес или self-host |
| **Microsoft Clarity** | Heatmaps, session recordings | ✅ free |
| **LemonSqueezy webhooks** | Purchase events | ✅ free |
| **ConvertKit** | Email signup events | ✅ free до 1000 |
| **Hotjar** (alternative) | Funnels + recordings | $32/мес |

### 4.2 Conversion events (что трекаем)

```
1. landing_view (любой посетитель)
2. hero_cta_click (Start Trial / Watch Demo)
3. demo_video_played
4. demo_video_completed (50%+)
5. pricing_view (scrolled to pricing)
6. pricing_cta_click (Starter/Pro/Agency/Founder)
7. lead_magnet_signup
8. checkout_started
9. checkout_completed (purchase)
10. trial_started
11. trial_to_paid (28 days later)
```

### 4.3 KPI funnel goals

| Step | Conversion target |
|---|---|
| Landing → Pricing scroll | 35%+ |
| Pricing scroll → Pricing CTA click | 8%+ |
| Pricing CTA click → Checkout started | 60%+ |
| Checkout started → Completed | 70%+ |
| **Overall: Landing → Purchase** | **1.5–3%** |
| Lead magnet conversion | 5–8% of non-buyers |

### 4.4 A/B test priorities (после launch)

В порядке impact на conversion:

| # | Test | Hypothesis | Effort |
|---|---|---|---|
| 1 | Hero tagline (A vs B) | Different value framings | low |
| 2 | Primary CTA text ("Try Trial" vs "Get Pro") | Action verb impact | low |
| 3 | Pricing tier highlighting (Pro vs Agency featured) | Anchor effect | medium |
| 4 | Hero anchor pricing position (above CTA vs below) | Visual prominence | low |
| 5 | Founder Edition placement (4th card vs floating banner) | Scarcity prominence | medium |
| 6 | Persona switcher placement (after features vs before) | Self-qualification timing | medium |
| 7 | Lead magnet placement (after pricing vs before) | Last-resort capture | low |
| 8 | Demo video length (60s vs 90s vs 2min) | Engagement | high |

---

## 5. Что меняется в существующей структуре

Существующий лендос имеет: Nav → Hero → Stats → How → Features → VS → Proof → Pricing → FAQ → CTA → Footer.

**Это close to right.** Главные отличия от моей рекомендации:

| Текущее | Рекомендую | Зачем |
|---|---|---|
| Stats bar после Hero | **Удалить** или сделать честным (2,319 reels) | Текущие цифры (748M+) выглядят invented |
| Нет PROBLEM AGITATION | **Добавить** между Hero и How | PAS framework — ключевая воронка |
| Features раньше Pricing | OK | Стандартная структура |
| Нет PERSONA SWITCHER | **Добавить** между Features и VS | Self-qualification |
| FAQ ПОСЛЕ Pricing | **Перенести FAQ перед Pricing** | Killing objections до момента покупки |
| Pricing 3 tiers | **Pricing 4 tiers** + Founder Edition | Scarcity driver |
| FAKE testimonials | **Убрать** до real ones | Trust damage |
| Нет LEAD MAGNET | **Добавить** между Pricing и Final CTA | Капчинг для не-buyers |
| Хорошие OG/Schema | OK, оставить | Уже есть |

---

## 6. Финальная структура (TL;DR)

```
1. NAV (sticky, transparent → scrolled state)
2. HERO (tagline + subtitle + BYOK badge + dual CTA + anchor + visual)
3. PROBLEM AGITATION (3 painpoint cards) ← НОВОЕ
4. SOLUTION INTRO (1 H2 + 3 unique badges)
5. HOW IT WORKS (4 steps + demo video)
6. KEY FEATURES (5 alternating blocks)
7. PERSONA SWITCHER (3 cards Solo/Team/Agency) ← НОВОЕ
8. VS COMPETITORS (anchor table)
9. PROOF (honest stats, after launch — testimonials)
10. BYOK FAQ FRONT-LOADED (объект-handling) ← КРИТИЧНО
11. PRICING (4 tiers + Founder Edition)
12. LEAD MAGNET (Free Viral Hook Swipe File) ← НОВОЕ
13. FINAL CTA + RISK REVERSAL
14. FOOTER (4 columns)
15. STICKY MOBILE CTA (bottom bar)
```

---

## 7. Implementation priority для Даши

### Priority 1 (Critical для AppSumo submission 16 апреля)
- ✅ Section 1 (Hero) — обновить tagline + BYOK badge + anchor pricing
- ✅ Section 10 (Pricing) — 4 tiers с новыми лимитами + Founder Edition
- ✅ Section 9 (BYOK FAQ) — front-load disclosure
- ✅ Privacy/Terms pages

### Priority 2 (Важно для конверсии)
- Section 3 (Problem Agitation) — добавить
- Section 6 (Persona Switcher) — добавить
- Section 11 (Lead Magnet) — добавить
- Удалить fake testimonials
- Убрать сломанный countdown timer
- Conversion tracking setup

### Priority 3 (Nice to have)
- Founder Edition counter с реальным webhook
- Animated GIFs вместо статичных screenshots
- Heatmap setup (Microsoft Clarity)
- A/B testing infrastructure
- Russian translation (для CIS audience)

---

## 8. Брендинг и tone of voice

ContentSpy — **honest, direct, confident**, не corporate.

### Voice guidelines

- ✅ "Reverse-engineer every viral post" (action, confidence)
- ❌ "Empower your social media strategy with AI-driven insights" (corporate babble)
- ✅ "Stop guessing. Start spying." (direct, memorable)
- ❌ "Take your content marketing to the next level" (cliché)
- ✅ "Read every word your competitors say" (visceral, specific)
- ❌ "Comprehensive analytics solution" (generic)

### Что используем
- Прямые глаголы (read, decode, see, find, copy)
- Конкретные числа (20 profiles, 25 free analyses, 5x viral)
- Сравнения (vs Sprout Social $2,988/yr)
- "You" пишем часто
- Короткие предложения (10–15 слов)

### Что не используем
- "Solution" / "platform" / "ecosystem"
- "Empower" / "leverage" / "synergy"
- "Cutting-edge" / "revolutionary" / "innovative"
- "Best in class" / "industry leading"
- Длинные предложения с подчинениями

---

## 9. Checklist готовности к AppSumo submission (16 апреля)

- [ ] Hero updated с новой tagline + BYOK badge
- [ ] Pricing 4 tiers с правильными лимитами
- [ ] Founder Edition card с scarcity counter
- [ ] BYOK FAQ section front-loaded
- [ ] Anchor pricing visible 3 раза (Hero + VS + Pricing)
- [ ] Demo video 60-секундный (записан 15 апреля)
- [ ] Privacy Policy + Terms страницы созданы
- [ ] Sticky mobile CTA работает
- [ ] LemonSqueezy buttons активны и работают
- [ ] ConvertKit lead magnet form подключена
- [ ] Conversion tracking (Plausible/Clarity) настроен
- [ ] Real Microsoft SmartScreen mention для Windows
- [ ] Apple notarized DMG download link работает
- [ ] Mobile responsive протестирован на iPhone + Android
- [ ] Page speed >85 (Lighthouse)
- [ ] Социальные мета-теги (OG + Twitter cards) обновлены
- [ ] Sitemap.xml + robots.txt обновлены
- [ ] Schema.org SoftwareApplication обновлён с новыми ценами

---

## 10. Что я (Катя) сделаю дальше

1. **Передать этот документ Даше** вместе с TZ_LANDING_FIXES_2026-04-11.md
2. **Даша** делает Priority 1 fixes к 13 апреля 18:00
3. **NiKa** пишет copy для всех новых секций (PAS, Persona switcher, Lead magnet)
4. **Макс** записывает 60-сек demo video 15 апреля
5. **Я (Катя)** контролирую финал и делаю QA пасс перед AppSumo submission

---

**Документ согласован Катей (strategic ops + marketing thinking).**
**Связанные:**
- `TZ_LANDING_FIXES_2026-04-11.md` — implementation tasks
- `LAUNCH_PLAN_12W_2026.html` — общая стратегия
