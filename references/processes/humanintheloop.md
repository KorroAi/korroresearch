# Human-in-the-Loop Editing

## Professional Writing Workflow

One-shot generation is not how professionals write. Real documents evolve through:

### Phase 1: Outline Approval
1. AI generates document skeleton
2. User reviews structure and flow
3. User approves, modifies, or rejects
4. AI incorporates feedback
5. Repeat until outline is correct

### Phase 2: Section-by-Section Generation
1. AI writes Section 1
2. User reviews inline
3. Comments: "Add more detail here", "Remove this claim"
4. AI revises Section 1
5. User approves Section 1
6. Move to Section 2
7. Run consistency check between sections

### Phase 3: Global Review
1. All sections written
2. AI generates consistency report
3. User reviews for narrative arc
4. User adds/removes/modifies sections
5. AI runs review engine

### Phase 4: Polish
1. AI applies style engine
2. AI runs hallucination check
3. AI verifies all citations
4. User does final read-aloud
5. AI generates output

## Version History

Maintain numbered versions:
- `paper_v1_draft.md` - First complete draft
- `paper_v2_revised.md` - After user review
- `paper_v3_camera_ready.md` - Final

Never overwrite without a backup. Use `diff` between versions:
```bash
diff paper_v1_draft.md paper_v2_revised.md
```

## Inline Comments Convention

Format for AI-human communication:
```
[COMMENT: This claim needs a citation]
The proposed method achieves state-of-the-art results.
```

```
[TODO: Add ablation study results]
```

```
[NEEDS VERIFICATION: Is 3.2x the correct number?]
```
