from playwright.sync_api import sync_playwright
import time

def take_screenshots():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 800})
        base = "/Users/Shared/workspace/products/contentspy/landing/img"

        # Dashboard
        page.goto("http://localhost:5055")
        page.wait_for_load_state("networkidle")
        time.sleep(2)
        page.screenshot(path=f"{base}/dashboard.png")
        print("dashboard done")

        # Content Hub
        page.evaluate("""
            let els = Array.from(document.querySelectorAll('[onclick]'));
            for (let e of els) {
                if (e.textContent.includes('Контент') && e.textContent.includes('⭐')) {
                    e.click(); break;
                }
            }
        """)
        time.sleep(2)
        page.screenshot(path=f"{base}/content-hub.png")
        print("content-hub done")

        # Back to profiles, open first profile detail
        page.evaluate("""
            let els = Array.from(document.querySelectorAll('[onclick]'));
            for (let e of els) {
                if (e.textContent.includes('Профили')) {
                    e.click(); break;
                }
            }
        """)
        time.sleep(2)

        # Click first profile card
        page.evaluate("""
            let cards = document.querySelectorAll('[class*=profile]');
            if (cards.length > 0) cards[0].click();
        """)
        time.sleep(2)

        # Overview (default)
        page.screenshot(path=f"{base}/profile-overview.png")
        print("profile-overview done")

        # Tab navigation helper
        def click_tab(label):
            page.evaluate(f"""
                let els = Array.from(document.querySelectorAll('[onclick]'));
                for (let e of els) {{
                    let t = e.textContent.trim();
                    if (t.startsWith('{label}')) {{ e.click(); break; }}
                }}
            """)
            time.sleep(2)

        # Growth
        click_tab("📈 Growth")
        page.screenshot(path=f"{base}/growth.png")
        print("growth done")

        # AI Analysis
        click_tab("🤖 AI Analysis")
        page.screenshot(path=f"{base}/ai-analysis.png")
        print("ai-analysis done")

        # Hooks
        click_tab("🪝 Hooks")
        page.screenshot(path=f"{base}/hooks.png")
        print("hooks done")

        # Reels
        click_tab("🎬 Reels")
        page.screenshot(path=f"{base}/reels.png")
        print("reels done")

        # Chat
        click_tab("💬 Chat")
        page.screenshot(path=f"{base}/ai-chat.png")
        print("ai-chat done")

        # Statistics page
        page.evaluate("""
            let els = Array.from(document.querySelectorAll('[onclick]'));
            for (let e of els) {
                if (e.textContent.includes('Статистика')) {
                    e.click(); break;
                }
            }
        """)
        time.sleep(2)
        page.screenshot(path=f"{base}/statistics.png")
        print("statistics done")

        browser.close()
        print("ALL DONE")

take_screenshots()
