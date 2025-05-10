import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()
    await page.goto("https://parabank.parasoft.com/parabank/index.html")

    ## Example get locator of element by text
    alt_text_example = page.get_by_alt_text("ParaBank")
    await alt_text_example.highlight()
    await page.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())