# src/cli/commands/ping.py
import typer
from rich import print
from rich.markdown import Markdown
from rich.panel import Panel

# imports
from mcp.messages.ping.send_messages import send_ping

# app
app = typer.Typer(help="Ping commands")

@app.command("run")
async def ping_run(server_streams: list):
    """Ping all connected servers."""
    print("[cyan]\nPinging Servers...[/cyan]")
    for i, (r_stream, w_stream) in enumerate(server_streams):
        if await send_ping(r_stream, w_stream):
            print(Panel(Markdown(f"## Server {i+1} is up!"), style="bold green"))
        else:
            print(Panel(Markdown(f"## Server {i+1} failed to respond."), style="bold red"))
