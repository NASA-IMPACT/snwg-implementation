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
- {% if item.complete %}[x]{% else %}[ ]{% endif %} {{ item.label }}
  {% if item.id == 'hq-kickoff' and hq_kickoff_url %}
  📎 [Documentation]({{ hq_kickoff_url }})
  {% endif %}
  {% if item.id == 'provider-kickoff' and provider_kickoff_url %}
  📎 [Documentation]({{ provider_kickoff_url }})
  {% endif %}
  {% if item.id == 'project-plan-draft' and project_plan_url %}
  📎 [Documentation]({{ project_plan_url }})
  {% endif %}
{% endfor %}

### Formulation Phase {% if formulation_complete %}✓{% endif %}
{% for item in formulation %}
- {% if item.complete %}[x]{% else %}[ ]{% endif %} {{ item.label }}
  {% if item.id == 'daac-summary' and daac_summary_url %}
  📎 [Documentation]({{ daac_summary_url }})
  {% endif %}
  {% if item.id == 'stakeholder-sessions' and stakeholder_sessions_url %}
  📎 [Documentation]({{ stakeholder_sessions_url }})
  {% endif %}
  {% if item.id == 'f2i-dg' %}
  {% if f2i_dg_presentation_url %}
  📎 [Presentation]({{ f2i_dg_presentation_url }})
  {% endif %}
  {% if f2i_dg_memo_url %}
  📎 [Memo]({{ f2i_dg_memo_url }})
  {% endif %}
  {% if f2i_dg_notes_url %}
  📎 [Meeting Notes]({{ f2i_dg_notes_url }})
  {% endif %}
  {% endif %}
{% endfor %}

### Implementation Phase {% if implementation_complete %}✓{% endif %}
{% for item in implementation %}
- {% if item.complete %}[x]{% else %}[ ]{% endif %} {{ item.label }}
  {% if item.id == 'operational-testing' and operational_testing_url %}
  📎 [Documentation]({{ operational_testing_url }})
  {% endif %}
  {% if item.id == 'orr' %}
  {% if orr_presentation_url %}
  📎 [Presentation]({{ orr_presentation_url }})
  {% endif %}
  {% if orr_memo_url %}
  📎 [Memo]({{ orr_memo_url }})
  {% endif %}
  {% if orr_notes_url %}
  📎 [Meeting Notes]({{ orr_notes_url }})
  {% endif %}
  {% endif %}
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

## 📑 Additional Documentation & Notes

### 📌 Milestone Documentation
{{ milestone_notes }}

{% if general_notes %}
### 📝 General Notes
{{ general_notes }}
{% endif %}

---
*Note: 🔒 Some linked documents may require additional access permissions.*
