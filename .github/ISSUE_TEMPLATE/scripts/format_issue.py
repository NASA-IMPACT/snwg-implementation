import os
import json
import re
from github import Github
from jinja2 import Template

def parse_issue_body(body):
    """Parse the issue body form data into a structured dictionary"""
    # Create a pattern to match form fields
    pattern = r'### ([^\n]+)\s*(?:\r?\n(?:[ \t]*(?!\#\#\#)[^\n]*))*'
    
    # Find all form fields
    fields = re.findall(pattern, body)
    
    # Create dictionary to store parsed data
    data = {}
    
    # Current section trackers
    current_phase = None
    current_items = []

    for field in fields:
        label, content = field.split('\n', 1)
        content = content.strip()
        
        # Handle checkboxes
        if '[x]' in content or '[ ]' in content:
            items = []
            for line in content.split('\n'):
                if line.strip():
                    checked = '[x]' in line
                    label = line.split(']', 1)[1].strip()
                    items.append({'label': label, 'complete': checked})
            
            # Map to phase
            if 'Pre-Formulation' in label:
                data['pre_formulation'] = items
            elif 'Formulation' in label:
                data['formulation'] = items
            elif 'Implementation' in label:
                data['implementation'] = items
            elif 'Operations' in label:
                data['operations'] = items
            elif 'Closeout' in label:
                data['closeout'] = items
        else:
            # Handle regular fields
            key = label.lower().replace(' ', '_')
            data[key] = content
    
    return data

def main():
    # Initialize GitHub client
    g = Github(os.environ['GITHUB_TOKEN'])
    repo = g.get_repo(os.environ['GITHUB_REPOSITORY'])
    
    # Get event data
    with open(os.environ['GITHUB_EVENT_PATH']) as f:
        event = json.load(f)
    
    issue_number = event['issue']['number']
    issue = repo.get_issue(issue_number)
    
    # Load template
    with open('.github/ISSUE_TEMPLATE/solution-status-template.md', 'r') as f:
        template_content = f.read()
    
    template = Template(template_content)
    
    # Parse form data
    form_data = parse_issue_body(issue.body)
    
    # Add phase completion status
    for phase in ['pre_formulation', 'formulation', 'implementation', 'operations', 'closeout']:
        if phase in form_data:
            form_data[f'{phase}_complete'] = all(item['complete'] for item in form_data[phase])
    
    # Render template
    formatted_content = template.render(**form_data)
    
    # Update issue
    issue.edit(body=formatted_content)

if __name__ == '__main__':
    main()
