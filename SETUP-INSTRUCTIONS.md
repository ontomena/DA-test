# DisplacementActivities Jekyll Site - Setup Instructions

## What I've Built

A clean Jekyll site with:
- **Homepage**: Literary intro text (adapted from your current site)
- **Commentarium**: 3-column grid layout (1 column on mobile) showing 9 dummy posts
- **Contact**: Your contact info + subscription options (RSS + Buttondown)
- **Typography**: Georgia serif, minimal design inspired by Sounds from Dangerous Places
- **Colour**: Subtle desaturated blue accent (#4a7c9e)
- **Categories**: sound, text, animation, video, archive, projects

## Files Included

```
DA-test/
├── _config.yml           # Site configuration
├── _layouts/
│   ├── default.html      # Main layout template
│   └── post.html         # Individual post template
├── _posts/               # 9 dummy blog posts
│   ├── 2025-03-21-geoambo.md
│   ├── 2024-10-10-tabularasa.md
│   └── ... (7 more)
├── assets/
│   ├── css/
│   │   └── style.css     # All styling
│   └── images/           # Placeholder images (blue squares)
├── index.md              # Homepage
├── commentarium.md       # Blog grid page
└── contact.md            # Contact page
```

## How to Deploy

### Option 1: Using the archive file (DA-test-site.tar.gz)

1. Download the .tar.gz file
2. Navigate to where you cloned DA-test locally
3. Extract: `tar -xzf DA-test-site.tar.gz`
4. This will create/overwrite files in your local DA-test folder
5. Open GitHub Desktop
6. It will show all the new files
7. Commit with a message like "Initial Jekyll site"
8. Push to GitHub

### Option 2: Manual copy (if archive doesn't work)

I can provide individual files for you to copy into your local DA-test folder.

## After Pushing

1. Go to https://github.com/ontomena/DA-test/settings/pages
2. Make sure GitHub Pages is still enabled (Source: main branch)
3. Wait 2-3 minutes for it to build
4. Visit: https://ontomena.github.io/DA-test/

## Next Steps

Once live, you can:
- Replace dummy posts with real content
- Swap placeholder images for actual images
- Tweak colors/fonts/spacing
- Add more posts
- Update the Buttondown username in contact.md

## Jekyll Post Format

Posts go in `_posts/` with filename: `YYYY-MM-DD-title.md`

Example:
```markdown
---
layout: post
title: "Your Post Title"
date: 2024-04-12
categories: [sound, text]
image: /assets/images/yourimage.jpg
excerpt: "Brief description for the grid"
---

Your post content here in markdown...
```

## Customizing

- **Colors**: Edit `:root` section in `assets/css/style.css`
- **Navigation**: Edit `_layouts/default.html`
- **Homepage text**: Edit `index.md`
- **Contact info**: Edit `contact.md`
