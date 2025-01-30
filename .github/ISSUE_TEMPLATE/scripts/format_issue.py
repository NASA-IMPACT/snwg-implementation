import os
import json
from github import Github
from jinja2 import Template

# Initialize GitHub client
g = Github(os.environ['GITHUB_TOKEN'])
repo = g.get_repo(os.environ['GITHUB_REPOSITORY'])
issue_number = int(os.environ['GITHUB_EVENT_PATH']['issue']['number'])
issue = repo.get_issue(issue_number)

# Load the template
with open('.github/ISSUE_TEMPLATE/solution-status-template.md', 'r') as f:
    template_content = f.read()

template = Template(template_content)

# Parse form data from issue body
# This will need to be adjusted based on your form structure
form_data = parse_issue_body(issue.body)

# Render template with form data
formatted_content = template.render(**form_data)

# Update issue
issue.edit(body=formatted_content)

def parse_issue_body(body):
    # Add parsing logic here to convert the form submission
    # into a dictionary of values for the template
    return {
        'project_name': '...',
        'status': '...',
        # etc.
    }
