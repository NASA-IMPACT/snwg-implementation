# 📊 {{ project_name }} Project Status Report

## 📈 Project Overview
**Status:** {{ status }}  
**Funded Until:** {{ funded_until }}

## 👥 Leadership Structure

### Core Team
| Role | Name | Organization |
|------|------|--------------|
| 👨‍💼 Implementation Lead | {{ implementation_lead }} | {{ implementation_org }} |
| 🔬 Project Scientist | {{ project_scientist }} | {{ scientist_org }} |
| 🤝 Partner Organization | {{ partner_org }} | - |

## 📋 Management Assessment

### Performance Metrics
- **Assessment Cycle:** {{ assessment_cycle }}
- **Stakeholder Survey:** 📝 [Stakeholder Assessment]({{ stakeholder_survey }})

### Project Deliverables
**Primary Product:** 🔗 [{{ product_name }}]({{ product_url }})  
*{{ product_description }}*

## 🔄 Project Lifecycle Status

### Pre-Formulation Phase {% if pre_formulation_complete %}✓{% endif %}
{% for item in pre_formulation %}
- {% if item.complete %}[x]{% else %}[ ]{% endif %} {{ item.label }} {% if item.url %}
  📎 [Documentation]({{ item.url }}){% endif %}
{% endfor %}

### Formulation Phase {% if formulation_complete %}✓{% endif %}
{% for item in formulation %}
- {% if item.complete %}[x]{% else %}[ ]{% endif %} {{ item.label }} {% if item.url %}
  📎 [Documentation]({{ item.url }}){% endif %}
{% endfor %}

### Implementation Phase {% if implementation_complete %}✓{% endif %}
{% for item in implementation %}
- {% if item.complete %}[x]{% else %}[ ]{% endif %} {{ item.label }} {% if item.url %}
  📎 [Documentation]({{ item.url }}){% endif %}
{% endfor %}

### Operations Phase {% if operations_complete %}✓{% endif %}
{% for item in operations %}
- {% if item.complete %}[x]{% else %}[ ]{% endif %} {{ item.label }} {% if item.url %}
  📎 [Documentation]({{ item.url }}){% endif %}
{% endfor %}

### Closeout Phase {% if closeout_complete %}✓{% endif %}
{% for item in closeout %}
- {% if item.complete %}[x]{% else %}[ ]{% endif %} {{ item.label }} {% if item.url %}
  📎 [Documentation]({{ item.url }}){% endif %}
{% endfor %}

{% if fact_sheet == "Yes" %}
## 📄 Fact Sheet
[View Fact Sheet]({{ fact_sheet_url }})
{% endif %}

---
*Note: 🔒 Some linked documents may require additional access permissions.*
