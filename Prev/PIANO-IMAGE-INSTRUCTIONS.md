# Piano Strip Image - Manual Step Required

## What I Did
I created a placeholder piano strip image because I can't download from your site due to network restrictions.

The placeholder is at: `/assets/images/piano-strip.jpg`

## What You Need to Do

1. **Download the original piano image** from your current site:
   - Go to: https://www.displacementactivities.org/assets/images/logo2.jpg
   - Save it locally

2. **Crop it to bottom half:**
   - Open in any image editor (Preview on Mac, Photoshop, GIMP, etc.)
   - Crop to show ONLY the bottom half/portion of the piano keys
   - Keep it wide (full width) but short height - around 60-80px tall
   - The CSS expects it to be cropped to bottom portion

3. **Save as:** `piano-strip.jpg`

4. **Replace the placeholder:**
   - Copy your cropped `piano-strip.jpg` into `/assets/images/`
   - Overwrite the placeholder I created
   - Commit and push

## How It Works

The image appears between the header title and navigation on ALL pages.

**Homepage:** CSS applies `filter: saturate(0.5)` to desaturate it
**Commentarium & other pages:** Shows at full saturation

This is controlled in the CSS - no need for two separate image files.
