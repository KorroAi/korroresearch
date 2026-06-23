# DOCX Format - Word Documents

Generate editable Word documents using python-docx.

## When to Use

- Grant proposals
- Internal reports needing collaboration
- Documents for non technical reviewers

## Prerequisites

```bash
pip install python-docx
```

## Python Script

```python
from docx import Document
from docx.shared import Inches, Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# Page setup
for section in doc.sections:
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)

# Title
title = doc.add_heading('Paper Title', level=0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Abstract
doc.add_heading('Abstract', level=1)
doc.add_paragraph('Abstract text here...')

# Save
doc.save('paper.docx')
```

## Style Standards

| Element | Font | Size | Bold |
|---------|------|------|------|
| Title | Times New Roman | 16pt | Yes |
| Heading 1 | Times New Roman | 14pt | Yes |
| Heading 2 | Times New Roman | 12pt | Yes |
| Body | Times New Roman | 11pt | No |
| Caption | Times New Roman | 9pt | No |

## Quality Checklist
- [ ] Times New Roman throughout
- [ ] Consistent heading hierarchy
- [ ] Tables formatted with simple borders
- [ ] Figures inserted at appropriate resolution
- [ ] Page numbers present
- [ ] No em dashes in text
