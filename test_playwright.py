from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r"C:\Users\tahora\AppData\Local\ms-playwright\chromium-1228\chrome.exe",
        headless=False
    )

    page = browser.new_page()
    page.goto("https://example.com")
    print(page.title())

    input("Press Enter to close...")
    browser.close()