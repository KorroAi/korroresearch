# Financial Model for Pitch Decks

## Required Metrics

| Metric | What It Means | Typical VC Expectation |
|---|---|---|
| CAC | Customer Acquisition Cost | < $100 for SaaS |
| LTV | Lifetime Value | > 3x CAC |
| Burn Rate | Monthly cash burn | Know your runway |
| Gross Margin | Revenue - COGS / Revenue | > 70% for SaaS |
| Runway | Months until cash runs out | > 18 months |
| MRR | Monthly Recurring Revenue | Growth trajectory |
| ARR | Annual Recurring Revenue | MRR x 12 |

## Financial Model Structure

1. **Revenue Model** - How you make money (subscription, usage-based, marketplace)
2. **Unit Economics** - Per-customer revenue and cost
3. **Growth Projections** - 3-year revenue forecast
4. **Burn and Runway** - Current cash, monthly spend, months remaining
5. **Key Assumptions** - What must be true for these numbers to work

## Spreadsheet Generation

```bash
python scripts/wizard.py --format pitch-deck --financial
```

Generates a CSV with formulas for CAC, LTV, Burn, Margin, Runway, and Revenue projections.
