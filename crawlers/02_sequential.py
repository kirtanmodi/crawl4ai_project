import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig, CacheMode
from typing import List


async def sequential_crawl(urls: List[str] = ["https://docs.crewai.com/introduction", "https://docs.crewai.com/installation"]):
    # Minimal browser config
    browser_config = BrowserConfig(
        # headless=False,
        # viewport={"width": 1920, "height": 1080},
        verbose=False,   # corrected from 'verbos=False'
        extra_args=["--disable-gpu",
                    "--disable-dev-shm-usage", "--no-sandbox"],
    )
    crawl_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)

    # Create the crawler instance
    crawler = AsyncWebCrawler(config=browser_config)
    await crawler.start()

    try:
        for url in urls:
            print(f"Crawling {url}...")

            result = await crawler.arun(
                url=url,
                config=crawl_config
            )

            if result.success:
                print(result.markdown)
            else:
                print("Failed:", result.url, "-", result.error_message)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await crawler.close()

if __name__ == "__main__":
    urls = [
        "https://resource.payrix.com/resources/",
        # "https://docs.crewai.com/installation", "https://docs.crewai.com/getting-started", "https://docs.crewai.com/core/agent",
        # "https://docs.crewai.com/core/agent/agent-class", "https://docs.crewai.com/core/agent/agent-class/agent-class-attributes", "https://docs.crewai.com/core/agent/agent-class/agent-class-methods"
    ]
    asyncio.run(sequential_crawl(urls))
