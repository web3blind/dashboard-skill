# Dashboard Skill

Accessible HTML dashboards with JSON + localStorage.

## Features

- **Tabs** — navigation between sections
- **Checklists** — multiple choice with progress tracking
- **Text/Textarea** — auto-detected based on hint (commas/semicolons → textarea)
- **Priority fields** — numbered priorities
- **Progress** — completion tracking per dashboard
- **localStorage** — unique key per dashboard (no conflicts)
- **Export/Import JSON** — share data

## Usage

```bash
# Generate dashboard from JSON file
python3 scripts/generate.py -d data.json -z -o my-dashboard
```

This creates a ZIP with `dashboard.html` and `data.json`.

## Workflow

1. Get data from user (file, description, or text)
2. Parse into JSON structure (see below)
3. Generate dashboard: `python3 scripts/generate.py -d data.json -z -o <name>`
4. Send ZIP archive to user

## JSON Structure

```json
{
  "title": "Dashboard Title",
  "tabs": [
    {
      "id": "tab1",
      "name": "1. Section Name",
      "items": [
        {
          "id": "1.1",
          "text": "1.1. Question or task",
          "hint": "Hint text (optional)",
          "type": "text|textarea|checklist|priority",
          "options": ["Option 1", "Option 2"],
          "checked": [],
          "value": ""
        }
      ]
    }
  ]
}
```

## Field Types

- **text** — single line input
- **textarea** — multi-line input
- **checklist** — checkboxes (options = choices)
- **priority** — numbered priorities (1, 2, 3...)

## Accessibility

- Screen reader friendly
- Keyboard navigation
- Light/dark theme (prefers-color-scheme)

## License

MIT
