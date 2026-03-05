# Dashboard Skill

Accessible HTML dashboards with JSON + localStorage.

## Features

- **Tabs** — navigation between sections
- **Checklists** — multiple choice
- **Text/Textarea** — auto-detected based on hint (commas/semicolons → textarea)
- **Priority fields** — numbered priorities
- **Progress** — completion tracking
- **localStorage** — saves progress in browser
- **Export/Import JSON** — share data

## Usage

```bash
# Generate dashboard with ZIP
python3 scripts/generate.py -z -o my-dashboard
```

This creates a ZIP with `dashboard.html` and `data.json`.

## Default Structure

8 tabs based on AI consulting brief:

1. About company
2. Sales
3. CRM
4. Documents
5. Marketing
6. Universities
7. Tools
8. Problems

## Accessibility

- Screen reader friendly
- Keyboard navigation
- Light/dark theme (prefers-color-scheme)

## License

MIT
