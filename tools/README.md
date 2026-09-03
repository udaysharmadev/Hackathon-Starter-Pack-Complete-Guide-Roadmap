# Tools

CLI tools to help you plan, score, and prepare for hackathons.

## Available Tools

### 📋 hackathon-tracker.py

Track hackathons you're interested in, applied to, or building for.

```bash
# Add a hackathon
python3 tools/hackathon-tracker.py add --name "SIH 2026" --deadline "2026-09-15" --platform "Devfolio"

# Add interactively
python3 tools/hackathon-tracker.py add

# List all
python3 tools/hackathon-tracker.py list

# Show upcoming deadlines
python3 tools/hackathon-tracker.py upcoming

# Update status
python3 tools/hackathon-tracker.py status 1 building

# Search
python3 tools/hackathon-tracker.py search "AI"

# Show stats
python3 tools/hackathon-tracker.py stats

# Export to CSV
python3 tools/hackathon-tracker.py export
```

### 🎯 idea-scorer.py

Score your hackathon idea against a 7-factor rubric (max 35 points).

```bash
# Interactive scoring
python3 tools/idea-scorer.py

# Score with name
python3 tools/idea-scorer.py --name "Campus Lost & Found"
```

**Scoring dimensions:**
1. Pain Score — How painful is this problem?
2. Frequency — How often does it occur?
3. Urgency — How urgently does it need solving?
4. Clarity — How clear is the problem statement?
5. Buildability — Can you build an MVP in time?
6. Demo Strength — Will the demo impress judges?
7. Judge Appeal — Will judges care about this?

**Decision thresholds:**
- 28-35: 🔥 STRONG — Pursue this idea
- 20-27: 🟡 GOOD — Refine and strengthen
- 13-19: 🟠 WEAK — Consider pivoting
- 7-12: 🔴 SKIP — Not worth the time

### 🎤 pitch-timer.py

Analyze your pitch script for timing, word count, and pacing.

```bash
# Interactive mode
python3 tools/pitch-timer.py

# From file
python3 tools/pitch-timer.py --file my-pitch.txt

# From clipboard
cat pitch.txt | python3 tools/pitch-timer.py
```

**Targets:**
- 30-second pitch: 75-90 words
- 60-second pitch: 150-180 words
- 2-minute pitch: 300-360 words
- 3-minute pitch: 450-540 words

## Requirements

All tools use Python 3 standard library only. No external dependencies needed.

```bash
python3 --version  # Requires Python 3.6+
```

## Data

The `hackathon-tracker.py` tool stores data in `data/hackathons.json`. This file is gitignored.
