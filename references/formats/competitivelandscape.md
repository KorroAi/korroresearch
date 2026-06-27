# Competitive Landscape Matrix

## Automatic Competitor Matrix

Generates a comparison table of known competitors plus your custom entries.

### Default Competitors Tracked

| Name | Category | Funding | Key Feature | Weakness |
|---|---|---|---|---|
| GitHub Copilot | Code AI | $100M+ | Deep IDE integration | Slow, expensive |
| Cursor | Code AI | $60M+ | AI-native editor | Limited language support |
| Windsurf | Code AI | $30M+ | Real-time collaboration | New, unproven |
| Codeium | Code AI | $65M+ | Free tier | Limited features |
| Claude Code | Code AI | N/A | Full-stack agent | CLI-only |
| Gemini Code Assist | Code AI | N/A | Google ecosystem | Limited IDE support |

### Custom Entries

Add your own competitors:
```bash
python scripts/wizard.py --format pitch-deck --competitors "company1,company2,company3"
```

## Matrix Format

For each competitor, document:
1. **Name and URL**
2. **Funding raised** (if known)
3. **Key differentiator** (their main selling point)
4. **Primary weakness** (where you beat them)
5. **Target market** (enterprise, SMB, developer, consumer)
6. **Pricing model** (free, freemium, subscription, usage-based)
