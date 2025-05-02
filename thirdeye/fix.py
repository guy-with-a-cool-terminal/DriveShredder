import os
import click
import shodan
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

# Load .env variables
load_dotenv()
SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")

console = Console()

# Check API key
if not SHODAN_API_KEY:
    console.print("[bold red]Error:[/bold red] SHODAN_API_KEY not found in .env")
    exit(1)

# Init Shodan
api = shodan.Shodan(SHODAN_API_KEY)


@click.command()
@click.option('--region', default="Kenya", help='Region or country to search (default: Kenya)')
@click.option('--query', default="port:554", help='Custom Shodan query (default: port:554)')
@click.option('--limit', default=10, help='Number of results to return')
def scan(region, query, limit):
    try:
        console.print(f"[bold green]Searching Shodan for:[/bold green] {query} in {region}")

        # Build query with region
        full_query = f"{query} country:{region}"
        results = api.search(full_query, limit=limit)

        if not results['matches']:
            console.print("[yellow]No results found.[/yellow]")
            return

        table = Table(title="ThirdEye Results")

        table.add_column("IP", style="cyan")
        table.add_column("Port", style="magenta")
        table.add_column("Org", style="green")
        table.add_column("Product", style="yellow")

        for result in results['matches']:
            ip = result.get('ip_str', 'N/A')
            port = str(result.get('port', 'N/A'))
            org = result.get('org', 'Unknown')
            product = result.get('product', 'Unknown')
            table.add_row(ip, port, org, product)

        console.print(table)

    except shodan.APIError as e:
        console.print(f"[bold red]Shodan API error:[/bold red] {e}")


if __name__ == '__main__':
    scan()
