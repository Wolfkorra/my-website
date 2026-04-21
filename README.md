# Abdullah Korra Portfolio Starter

This is a Quarto website starter for a professional portfolio that supports four things at once:

1. a recruiter-friendly landing page
2. a project portfolio
3. a polished sample analysis report
4. supporting materials such as a resume, statement, posters, and selected personal interests

## Pages

- `index.qmd` — home page
- `projects.qmd` — projects and poster presentations
- `analysis/telco-churn-report.qmd` — sample analysis report
- `resume.qmd` — resume page
- `statement.qmd` — statement page
- `contact.qmd` — contact page

## Assets already included

- placeholder headshot
- favicon
- social preview card
- placeholder resume PDF
- personal statement PDF
- two astronomy poster PDFs
- poster thumbnails
- one homepage cover image
- three ceramics photos for the lower-page gallery

## First edits to make

- replace `YOUR-USERNAME` and `YOUR-LINKEDIN`
- update `site-url` in `_quarto.yml`
- replace the placeholder headshot
- replace the placeholder resume PDF
- update email and contact links
- add the Kaggle churn CSV to `data/raw/` if you want a fully local render

## Local preview

Open the folder in Positron, then run:

```bash
quarto preview
```

To fully render the website:

```bash
quarto render
```

## Publish

When you are ready to deploy:

```bash
quarto publish gh-pages
```

## Notes on structure

The top of the home page is intentionally technical and recruiter-facing.

The lower sections add:
- poster presentations
- hobbies and personal interests
- ceramics and craft images

That keeps the first impression professional while still making the site feel like a real person made it.
