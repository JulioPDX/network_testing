#!/usr/bin/env python3

from tcp_latency import measure_latency
from rich.progress import Progress
from rich.console import Console
from rich.table import Table

sites = [
    "en.wikipedia.org",
    "youtube.com",
    "amazon.com",
    "facebook.com",
    "twitter.com",
    "pinterest.com",
    "imdb.com",
    "reddit.com",
    "juliopdx.com",
    "404",
]

device_table = Table(title="TCP Latency Test")
device_table.add_column("Site Name", justify="center")
device_table.add_column("Results", justify="center")

with Progress() as progress:
    task1 = progress.add_task("[green]Testing Sites...", total=len(sites))
    for site in sites:
        test_results = measure_latency(host=site, runs=3)
        if None in test_results:
            device_table.add_row(f"[red underline]{site}[/]", f"[red]Not Found[/]")
        else:
            device_table.add_row(
                f"[dodger_blue3 underline]{site}[/]", f"[green]{test_results}[/]"
            )

        progress.update(task1, advance=1.0)

console = Console()
console.print(device_table)
