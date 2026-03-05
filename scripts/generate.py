#!/usr/bin/env python3
"""
Generate dashboard from JSON data file.
Usage: python3 generate.py --data my-data.json -z -o my-dashboard
"""

import argparse
import json
import re
import sys
from pathlib import Path

TEMPLATE_PATH = Path(__file__).parent.parent / "templates" / "dashboard.html"

def generate_dashboard(data_path=None, output_path=None):
    """Generate dashboard HTML from JSON data."""
    
    if not TEMPLATE_PATH.exists():
        return None, f"Template not found: {TEMPLATE_PATH}"
    
    # Read template
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Load data from JSON file
    json_data = None
    if data_path and Path(data_path).exists():
        with open(data_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
    
    # If JSON provided, inject data into template
    if json_data:
        # Replace DEFAULT_DATA
        data_json = json.dumps(json_data, ensure_ascii=False, indent=2)
        # Match DEFAULT_DATA block and replace
        pattern = r'const DEFAULT_DATA = \{[\s\S]*?\};'
        replacement = f'const DEFAULT_DATA = {data_json};'
        template = re.sub(pattern, replacement, template)
        
        # Update title if provided
        if 'title' in json_data:
            template = template.replace('>Бриф на ИИ<', f'>{json_data["title"]}<')
    
    if output_path is None:
        output_dir = Path.home() / ".agent" / "dashboards"
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / "dashboard.html"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template)
    
    return str(output_path), json_data


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
            zf.writestr('data.json', '{}')
    
    return str(output_path)


def main():
    parser = argparse.ArgumentParser(description="Generate dashboard")
    parser.add_argument("-d", "--data", help="JSON file with dashboard data")
    parser.add_argument("-o", "--output", help="Output file (without extension)")
    parser.add_argument("-z", "--zip", action="store_true", help="Create ZIP archive with HTML+JSON")
    
    args = parser.parse_args()
    
    if not args.data:
        print("Error: --data is required", file=sys.stderr)
        sys.exit(1)
    
    output_path, json_data = generate_dashboard(args.data, args.output)
    
    if output_path is None:
        print(f"Error: {json_data}", file=sys.stderr)  # json_data contains error message
        sys.exit(1)
    
    if args.zip:
        archive_path = create_archive(output_path, json_data, args.output)
        print(archive_path)
    else:
        print(output_path)


if __name__ == "__main__":
    main()
