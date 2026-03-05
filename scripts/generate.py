#!/usr/bin/env python3
"""
Generate dashboard from data/description.
Usage: python3 generate.py "description or data" [-o output.html]
"""

import argparse
import json
import sys
from pathlib import Path

TEMPLATE_PATH = Path(__file__).parent.parent / "templates" / "dashboard.html"

def generate_dashboard(data=None, output_path=None):
    """Generate dashboard HTML from data structure."""
    
    if not TEMPLATE_PATH.exists():
        return None, f"Template not found: {TEMPLATE_PATH}"
    
    # Read template
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = f.read()
    
    if output_path is None:
        output_dir = Path.home() / ".agent" / "dashboards"
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / "dashboard.html"
    
    # For now, use default template
    # In future, could customize based on data
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template)
    
    return str(output_path), None


def create_archive(html_path, json_data=None, output_path=None):
    """Create ZIP archive with HTML and JSON."""
    import zipfile
    
    if output_path is None:
        output_path = Path(html_path).with_suffix('.zip')
    
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Add HTML
        zf.write(html_path, 'dashboard.html')
        
        # Add JSON
        if json_data:
            zf.writestr('data.json', json.dumps(json_data, ensure_ascii=False, indent=2))
        else:
            # Try to extract default data from HTML
            zf.writestr('data.json', '{}')
    
    return str(output_path)


def main():
    parser = argparse.ArgumentParser(description="Generate dashboard")
    parser.add_argument("data", nargs="?", help="Data or description for dashboard")
    parser.add_argument("-o", "--output", help="Output HTML file")
    parser.add_argument("-z", "--zip", action="store_true", help="Create ZIP archive with HTML+JSON")
    
    args = parser.parse_args()
    
    output_path, error = generate_dashboard(args.data, args.output)
    
    if error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
    
    if args.zip:
        archive_path = create_archive(output_path)
        print(archive_path)
    else:
        print(output_path)


if __name__ == "__main__":
    main()
