#!/usr/bin/env python3
"""Public Atlas: offline, privacy-bounded browser smoke in Chromium.

Two local-file viewports; verifies real search/mark/reset and keyboard use.
No login, external requests, downloads, telemetry or public deployment.
This smoke does not certify accessibility, history/rights or hosted Pages.
"""
from pathlib import Path
import sys

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
URL = (ROOT / "index.html").as_uri()

class SmokeFail(Exception):
    pass

def demand(condition, label):
    if not condition:
        raise SmokeFail(label)

def verify(page, mode):
    stage = "initial"
    outbound = []
    js_errors = []
    page.on("pageerror", lambda _error: js_errors.append("page-error"))
    page.on("request", lambda req: outbound.append("external-request")
            if req.url.startswith(("https://", "http://")) else None)
    try:
        response = page.goto(URL, wait_until="load", timeout=20000)
        demand(response is not None, "navigation-missing")
        demand(page.title() == "CISSP Domain Atlas — Explore the Eight Domains", "title")
        cards = page.locator("article.domain")
        demand(cards.count() == 8, "eight-cards")
        demand(page.locator("#visible-count").inner_text() == "8 domains in view", "initial-count")
        demand(page.locator("#explored-count").inner_text() == "0 of 8", "initial-progress")
        stage = "search"
        field = page.locator("#domain-search")
        field.fill("identity")
        demand(page.locator("article.domain:not([hidden])").count() == 1, "search-visible")
        demand(page.locator("#visible-count").inner_text() == "1 domain in view", "search-count")
        stage = "mark"
        marked = page.locator("article.domain:not([hidden]) button.mark")
        demand(page.get_by_role("button", name="Mark explored Identity and Access Management").count() == 1,
               "accessible-name-before-mark")
        marked.click()
        demand(marked.get_attribute("aria-pressed") == "true", "mark-pressed")
        demand(page.get_by_role("button", name="Explored ✓ Identity and Access Management").count() == 1,
               "accessible-name-after-mark")
        demand(page.locator("#explored-count").inner_text() == "1 of 8", "mark-count")
        stage = "clear"
        page.locator("#clear-search").click()
        demand(field.input_value() == "", "clear-input")
        demand(page.locator("#visible-count").inner_text() == "8 domains in view", "clear-visible")
        demand(page.locator("#explored-count").inner_text() == "1 of 8", "session-mark")
        demand(page.evaluate("document.activeElement.id") == "domain-search", "focus-return")
        stage = "zero-state"
        field.fill("no-match-12345")
        demand(page.locator("article.domain:not([hidden])").count() == 0, "zero-results")
        demand(page.locator("#visible-count").inner_text() == "0 domains in view", "zero-count")
        demand(page.locator("#empty-state").is_visible(), "empty-state-visible")
        page.locator("#clear-search").click()
        demand(page.locator("#empty-state").is_hidden(), "empty-state-cleared")
        stage = "viewport"
        demand(page.evaluate("document.documentElement.scrollWidth <= window.innerWidth + 2"),
               "horizontal-overflow")
        demand(page.evaluate("matchMedia('(prefers-reduced-motion: reduce)').matches"),
               "reduced-motion-respected")
        demand(not outbound, "unexpected-external-request")
        demand(not js_errors, "javascript-error")
    except SmokeFail as exc:
        raise SmokeFail(mode + ":" + str(exc)) from None
    except Exception:
        raise SmokeFail(mode + ":" + stage + "-interaction-unverified") from None

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            for mode, size in (
                ("desktop", {"width": 1440, "height": 900}),
                ("mobile", {"width": 390, "height": 844}),
            ):
                context = browser.new_context(viewport=size, reduced_motion="reduce",
                                              accept_downloads=False, service_workers="block")
                try:
                    verify(context.new_page(), mode)
                    print("PASS: offline Atlas " + mode + " browser interaction", flush=True)
                finally:
                    context.close()
        finally:
            browser.close()
    print("PASS: 2/2 offline viewport browser smoke; no hosted-site assertion")

if __name__ == "__main__":
    try:
        main()
    except SmokeFail as err:
        print("NOT VERIFIED: " + str(err), file=sys.stderr)
        sys.exit(2)
    except Exception:
        print("NOT VERIFIED: browser environment or execution unavailable", file=sys.stderr)
        sys.exit(2)
