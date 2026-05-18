"""
Multimodal Bandwidth Platform — Booking Reference Screen
Rotterdam & Antwerp Hinterland Corridor
Run: python mbp_booking_reference.py
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich.text import Text
from rich.rule import Rule
from rich import box

console = Console()

# ── Booking data ────────────────────────────────────────────────────────────
BOOKING = {
    "ref":          "MBP-4QR7W2",
    "status":       "Slot Confirmed",
    "mode":         "Barge (Inland Waterway)",
    "operator":     "Rhine Carrier III",
    "origin":       "Port of Rotterdam (RTM)",
    "destination":  "Port of Antwerp-Bruges (ANR)",
    "departure":    "Thu 5 Jun 2026 · 06:00",
    "arrival":      "Fri 6 Jun 2026 · 00:00",
    "transit":      "18h",
    "gate_open":    "Thu 5 Jun · 04:30",
    "cut_off":      "Thu 5 Jun · 05:30",
    "cargo_weight": "24,000 kg",
    "commodity":    "General freight",
    "cost_barge":   310,
    "cost_road":    420,
    "co2_saving":   "68%",
    "planner":      "Sophie van der Berg",
    "company":      "Geodis NL",
    "email":        "s.vanderberg@geodis.com",
    "booking_time": "47 seconds",
    "cancel_by":    "Wed 4 Jun 2026 · 18:00",
    "cancel_fee":   45,
    "slot_hold":    "17:00 today",
}


def header():
    console.print()
    console.rule("[bold green]Multimodal Bandwidth Platform[/bold green]", style="green")
    console.print(
        "[dim]Rotterdam & Antwerp Hinterland Corridor[/dim]",
        justify="center",
    )
    console.print()

    status = Text()
    status.append("✔  SLOT CONFIRMED", style="bold white on green")
    console.print(status, justify="center")
    console.print()

    ref = Text()
    ref.append("Booking Reference: ", style="dim")
    ref.append(BOOKING["ref"], style="bold cyan")
    console.print(ref, justify="center")
    console.print()


def mode_block():
    console.rule("[green]Mode booked[/green]", style="green dim")

    t = Table(box=None, show_header=False, padding=(0, 2))
    t.add_column(style="bold")
    t.add_column()

    t.add_row("🚢  Mode",     f"[bold green]{BOOKING['mode']}[/bold green]  [green][Recommended][/green]")
    t.add_row("   Operator",  BOOKING["operator"])

    console.print(t)
    console.print()

    # Cost / time / CO2 comparison mini-table
    cmp = Table(
        title="[dim]vs road comparison[/dim]",
        box=box.SIMPLE_HEAVY,
        show_header=True,
        header_style="dim",
        padding=(0, 2),
        title_justify="left",
    )
    cmp.add_column("", style="dim")
    cmp.add_column("Cost",        justify="right")
    cmp.add_column("Transit",     justify="right")
    cmp.add_column("CO2",         justify="right")

    cmp.add_row(
        "🚛  Road (default)",
        f"€ {BOOKING['cost_road']}",
        "4h",
        "baseline",
        style="dim",
    )
    cmp.add_row(
        "🚢  Barge [green][booked][/green]",
        f"[bold green]€ {BOOKING['cost_barge']}[/bold green]",
        f"[bold]{BOOKING['transit']}[/bold]",
        f"[bold green]−{BOOKING['co2_saving']}[/bold green]",
    )
    saving = BOOKING["cost_road"] - BOOKING["cost_barge"]
    cmp.add_row("", f"[green]Saves € {saving}[/green]", "", "")

    console.print(cmp)


def route_block():
    console.rule("[green]Route[/green]", style="green dim")

    route = Text()
    route.append("  Port of Rotterdam (RTM)", style="bold")
    route.append("  ──── 18h waterway ────▶  ", style="dim green")
    route.append("Port of Antwerp-Bruges (ANR)", style="bold")
    console.print(route)
    console.print()

    t = Table(box=None, show_header=False, padding=(0, 2))
    t.add_column(style="dim", width=22)
    t.add_column()

    t.add_row("Departure",  BOOKING["departure"])
    t.add_row("Arrival",    BOOKING["arrival"])
    t.add_row("Gate open",  BOOKING["gate_open"])
    t.add_row("Cut-off",    f"[bold yellow]{BOOKING['cut_off']}[/bold yellow]")

    console.print(t)
    console.print()


def shipment_block():
    console.rule("[green]Shipment[/green]", style="green dim")

    t = Table(box=None, show_header=False, padding=(0, 2))
    t.add_column(style="dim", width=22)
    t.add_column()

    t.add_row("Cargo weight", BOOKING["cargo_weight"])
    t.add_row("Commodity",    BOOKING["commodity"])

    console.print(t)
    console.print()


def planner_block():
    console.rule("[green]Booked by[/green]", style="green dim")

    t = Table(box=None, show_header=False, padding=(0, 2))
    t.add_column(style="dim", width=22)
    t.add_column()

    t.add_row("Planner",     BOOKING["planner"])
    t.add_row("Company",     BOOKING["company"])
    t.add_row("Confirm sent", BOOKING["email"])

    console.print(t)
    console.print()


def payment_block():
    console.rule("[green]Payment[/green]", style="green dim")

    saving = BOOKING["cost_road"] - BOOKING["cost_barge"]

    p1 = Panel(
        f"[bold]€ {BOOKING['cost_barge']}.00[/bold]\n[dim]incl. terminal handling[/dim]",
        title="[dim]Total charged[/dim]",
        border_style="green",
        expand=True,
    )
    p2 = Panel(
        f"[bold green]€ {saving}.00[/bold green]\n[dim]road would have been € {BOOKING['cost_road']}[/dim]",
        title="[dim]Saved vs road[/dim]",
        border_style="green",
        expand=True,
    )
    console.print(Columns([p1, p2]))


def slot_hold_block():
    console.print()
    console.print(
        Panel(
            f"⏳  Slot held until [bold yellow]{BOOKING['slot_hold']}[/bold yellow] — booking is already confirmed, no further action needed.",
            border_style="yellow",
            title="[yellow]Slot hold[/yellow]",
        )
    )


def cancellation_block():
    console.rule("[green]Cancellation policy[/green]", style="green dim")

    t = Table(box=None, show_header=False, padding=(0, 2))
    t.add_column(style="dim", width=28)
    t.add_column()

    t.add_row("Free cancellation until", f"[bold]{BOOKING['cancel_by']}[/bold]")
    t.add_row("Late cancellation fee",   f"€ {BOOKING['cancel_fee']}.00")

    console.print(t)
    console.print()


def journey_block():
    console.rule("[green]Booking journey[/green]", style="green dim")

    steps = Text()
    steps.append(" [1] Search ", style="bold white on dark_green")
    steps.append(" ▶ ", style="dim")
    steps.append(" [2] Compare ", style="bold white on dark_green")
    steps.append(" ▶ ", style="dim")
    steps.append(" [3] Confirm ", style="bold white on dark_green")
    steps.append(" ▶ ", style="dim")
    steps.append(" ✔ Booked ", style="bold white on green")
    console.print(steps)
    console.print()
    console.print(
        f"  Total booking time: [bold cyan]{BOOKING['booking_time']}[/bold cyan]  [dim](target: <90s)[/dim]"
    )
    console.print()


def co2_summary():
    console.print(
        Panel(
            f"[bold green]−{BOOKING['co2_saving']} CO2[/bold green] saved on this shipment vs road default.\n"
            "[dim]Export a CO2 report for sustainability accounting.[/dim]",
            title="[green]Environmental impact[/green]",
            border_style="green",
        )
    )
    console.print()


def footer():
    console.rule(style="dim")
    console.print(
        "[dim]Multimodal Bandwidth Platform · Breda University of Applied Sciences · 2025/2026[/dim]",
        justify="center",
    )
    console.print()


def main():
    header()
    mode_block()
    route_block()
    shipment_block()
    planner_block()
    payment_block()
    slot_hold_block()
    cancellation_block()
    journey_block()
    co2_summary()
    footer()


if __name__ == "__main__":
    main()
