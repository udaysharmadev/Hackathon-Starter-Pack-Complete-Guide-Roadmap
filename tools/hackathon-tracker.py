#!/usr/bin/env python3
"""
Hackathon Tracker — CLI tool to find, track, and manage hackathons.

Usage:
    python3 hackathon-tracker.py list                    List all tracked hackathons
    python3 hackathon-tracker.py add                     Add a new hackathon (interactive)
    python3 hackathon-tracker.py add --name "Name" --deadline "2026-03-15" --platform "Devfolio"
    python3 hackathon-tracker.py search "query"          Search hackathons by name/theme
    python3 hackathon-tracker.py upcoming                Show upcoming deadlines
    python3 hackathon-tracker.py stats                   Show statistics
    python3 hackathon-tracker.py export                  Export to CSV
    python3 hackathon-tracker.py delete <id>             Delete a hackathon entry
"""

import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "hackathons.json"


def load_hackathons():
    """Load hackathons from JSON file."""
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_hackathons(hackathons):
    """Save hackathons to JSON file."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(hackathons, f, indent=2)


def generate_id(hackathons):
    """Generate next available ID."""
    if not hackathons:
        return 1
    return max(h["id"] for h in hackathons) + 1


def cmd_list(hackathons):
    """List all tracked hackathons."""
    if not hackathons:
        print("\n  No hackathons tracked yet. Use 'add' to get started.\n")
        return

    print(f"\n  {'ID':<4} {'Name':<30} {'Deadline':<12} {'Platform':<15} {'Status':<12} {'Score':<6}")
    print("  " + "-" * 85)

    for h in hackathons:
        deadline = h.get("deadline", "TBD")
        status = h.get("status", "interested")
        score = h.get("score", "-")
        status_icon = {
            "interested": "📋",
            "applied": "✅",
            "registered": "🎯",
            "building": "🔨",
            "submitted": "🚀",
            "won": "🏆",
            "skipped": "⏭️"
        }.get(status, "📋")
        print(f"  {h['id']:<4} {h['name'][:28]:<30} {deadline:<12} {h.get('platform', 'N/A'):<15} {status_icon} {status:<10} {score:<6}")

    print(f"\n  Total: {len(hackathons)} hackathons\n")


def cmd_add(hackathons, args):
    """Add a new hackathon."""
    name = None
    deadline = None
    platform = None
    theme = None
    prize = None
    link = None

    i = 0
    while i < len(args):
        if args[i] == "--name" and i + 1 < len(args):
            name = args[i + 1]
            i += 2
        elif args[i] == "--deadline" and i + 1 < len(args):
            deadline = args[i + 1]
            i += 2
        elif args[i] == "--platform" and i + 1 < len(args):
            platform = args[i + 1]
            i += 2
        elif args[i] == "--theme" and i + 1 < len(args):
            theme = args[i + 1]
            i += 2
        elif args[i] == "--prize" and i + 1 < len(args):
            prize = args[i + 1]
            i += 2
        elif args[i] == "--link" and i + 1 < len(args):
            link = args[i + 1]
            i += 2
        else:
            i += 1

    if not name:
        name = input("  Hackathon name: ").strip()
        if not name:
            print("  Name is required.")
            return
        deadline = deadline or input("  Deadline (YYYY-MM-DD or TBD): ").strip() or "TBD"
        platform = platform or input("  Platform (Devfolio/Devpost/MLH/etc): ").strip() or "N/A"
        theme = theme or input("  Theme (AI/Health/Finance/etc): ").strip() or "N/A"
        prize = prize or input("  Prize pool: ").strip() or "N/A"
        link = link or input("  Link: ").strip() or "N/A"

    hackathon = {
        "id": generate_id(hackathons),
        "name": name,
        "deadline": deadline or "TBD",
        "platform": platform or "N/A",
        "theme": theme or "N/A",
        "prize": prize or "N/A",
        "link": link or "N/A",
        "status": "interested",
        "score": "-",
        "notes": "",
        "added": datetime.now().strftime("%Y-%m-%d")
    }

    hackathons.append(hackathon)
    save_hackathons(hackathons)
    print(f"\n  ✅ Added: {name} (ID: {hackathon['id']})\n")


def cmd_search(hackathons, query):
    """Search hackathons by name or theme."""
    query = query.lower()
    results = [h for h in hackathons if query in h["name"].lower() or query in h.get("theme", "").lower()]

    if not results:
        print(f"\n  No hackathons found matching '{query}'\n")
        return

    print(f"\n  Search results for '{query}':\n")
    for h in results:
        print(f"  [{h['id']}] {h['name']} — {h.get('platform', 'N/A')} — {h.get('deadline', 'TBD')}")
    print()


def cmd_upcoming(hackathons):
    """Show hackathons with upcoming deadlines."""
    upcoming = []
    for h in hackathons:
        deadline = h.get("deadline", "TBD")
        if deadline == "TBD":
            continue
        try:
            d = datetime.strptime(deadline, "%Y-%m-%d")
            days_left = (d - datetime.now()).days
            if days_left >= 0:
                upcoming.append((h, days_left))
        except ValueError:
            continue

    if not upcoming:
        print("\n  No upcoming deadlines found.\n")
        return

    upcoming.sort(key=lambda x: x[1])

    print(f"\n  {'Name':<30} {'Deadline':<12} {'Days Left':<10} {'Platform':<15}")
    print("  " + "-" * 70)

    for h, days in upcoming:
        urgency = "🔴" if days <= 7 else "🟡" if days <= 30 else "🟢"
        print(f"  {h['name'][:28]:<30} {h['deadline']:<12} {urgency} {days:<8} {h.get('platform', 'N/A'):<15}")

    print(f"\n  {len(upcoming)} upcoming hackathons\n")


def cmd_stats(hackathons):
    """Show statistics."""
    if not hackathons:
        print("\n  No data to show.\n")
        return

    total = len(hackathons)
    statuses = {}
    platforms = {}
    themes = {}

    for h in hackathons:
        s = h.get("status", "unknown")
        statuses[s] = statuses.get(s, 0) + 1
        p = h.get("platform", "N/A")
        platforms[p] = platforms.get(p, 0) + 1
        t = h.get("theme", "N/A")
        themes[t] = themes.get(t, 0) + 1

    print(f"\n  📊 Hackathon Statistics\n")
    print(f"  Total tracked: {total}\n")

    print("  By Status:")
    for s, c in sorted(statuses.items(), key=lambda x: -x[1]):
        bar = "█" * (c * 20 // total)
        print(f"    {s:<15} {c:>3}  {bar}")

    print("\n  By Platform:")
    for p, c in sorted(platforms.items(), key=lambda x: -x[1])[:5]:
        print(f"    {p:<15} {c:>3}")

    print("\n  By Theme:")
    for t, c in sorted(themes.items(), key=lambda x: -x[1])[:5]:
        print(f"    {t:<15} {c:>3}")

    print()


def cmd_export(hackathons):
    """Export to CSV."""
    if not hackathons:
        print("\n  No data to export.\n")
        return

    csv_path = DATA_FILE.parent / "hackathons_export.csv"
    with open(csv_path, "w") as f:
        f.write("id,name,deadline,platform,theme,prize,status,score,link,notes\n")
        for h in hackathons:
            name = h["name"].replace(",", ";")
            notes = h.get("notes", "").replace(",", ";")
            f.write(f"{h['id']},{name},{h.get('deadline', '')},{h.get('platform', '')},{h.get('theme', '')},{h.get('prize', '')},{h.get('status', '')},{h.get('score', '')},{h.get('link', '')},{notes}\n")

    print(f"\n  ✅ Exported to {csv_path}\n")


def cmd_delete(hackathons, hack_id):
    """Delete a hackathon entry."""
    try:
        hack_id = int(hack_id)
    except ValueError:
        print("  Invalid ID.")
        return

    original_len = len(hackathons)
    hackathons = [h for h in hackathons if h["id"] != hack_id]

    if len(hackathons) == original_len:
        print(f"  No hackathon found with ID {hack_id}")
        return

    save_hackathons(hackathons)
    print(f"\n  ✅ Deleted hackathon #{hack_id}\n")


def cmd_status(hackathons, hack_id, new_status):
    """Update hackathon status."""
    try:
        hack_id = int(hack_id)
    except ValueError:
        print("  Invalid ID.")
        return

    valid_statuses = ["interested", "applied", "registered", "building", "submitted", "won", "skipped"]
    if new_status not in valid_statuses:
        print(f"  Invalid status. Choose from: {', '.join(valid_statuses)}")
        return

    for h in hackathons:
        if h["id"] == hack_id:
            h["status"] = new_status
            save_hackathons(hackathons)
            print(f"\n  ✅ Updated #{hack_id} to '{new_status}'\n")
            return

    print(f"  No hackathon found with ID {hack_id}")


def main():
    hackathons = load_hackathons()

    if len(sys.argv) < 2:
        print(__doc__)
        return

    cmd = sys.argv[1]

    if cmd == "list":
        cmd_list(hackathons)
    elif cmd == "add":
        cmd_add(hackathons, sys.argv[2:])
    elif cmd == "search" and len(sys.argv) > 2:
        cmd_search(hackathons, " ".join(sys.argv[2:]))
    elif cmd == "upcoming":
        cmd_upcoming(hackathons)
    elif cmd == "stats":
        cmd_stats(hackathons)
    elif cmd == "export":
        cmd_export(hackathons)
    elif cmd == "delete" and len(sys.argv) > 2:
        cmd_delete(hackathons, sys.argv[2])
    elif cmd == "status" and len(sys.argv) > 3:
        cmd_status(hackathons, sys.argv[2], sys.argv[3])
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
