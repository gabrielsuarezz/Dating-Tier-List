# How to Add New Dates to the South Florida Date Ranker

This guide will help you safely add new dates to your tier list with proper, relevant images.

## Quick Start

1. Open `index.html`
2. Find the `dates` array (around line 342)
3. Add your new date object following the template below
4. Save and test

## Date Object Template

```javascript
{
    id: 'unique-id-here',              // Unique identifier (lowercase, no spaces)
    name: 'Display Name',              // The name shown on the card
    desc: 'Brief description here.',   // Short description (2-3 sentences max)
    price: '$$',                       // $ (cheap), $$ (moderate), $$$ (expensive)
    time: '45 min',                    // Drive time from North Perry Airport
    tags: ['art', 'fun'],              // Pick from: art, history, fun, food
    img: 'https://upload.wikimedia.org/...'  // Image URL (see below)
}
```

## Finding Good Images

### Option 1: Wikimedia Commons (RECOMMENDED - Most Stable)

1. Go to [Wikimedia Commons](https://commons.wikimedia.org)
2. Search for your location or activity (e.g., "butterfly garden", "japanese garden")
3. Click on an image you like
4. Look for "Use this file" or click the image to enlarge
5. Right-click → "Copy image address"
6. Paste the URL into the `img` field

**Pro tip:** Look for images with 500px-800px width for optimal loading speed

### Option 2: Local/Specific Location Images

If you have specific photos of the location:
- Upload to Wikimedia Commons (free account required)
- Or use any reliable image hosting service
- Make sure the image URL is stable and won't change

### What Makes a Good Image?

✅ **GOOD:**
- Clear, high-quality photos
- Directly represents the location/activity
- Stable URLs (Wikimedia Commons, official venue sites)
- Landscape orientation works best

❌ **AVOID:**
- Generic stock photos unrelated to the location
- URLs that might break or change
- Very large images (over 2MB)
- Portrait orientation (gets cropped oddly)

## Image Fallback System

Don't worry too much about broken images! The app has a built-in fallback system:

- If an image fails to load, it will automatically show a category-appropriate backup image
- Fallback images are based on the first tag in the `tags` array
- This means even if your image URL breaks, users will still see something relevant

## Tags Explained

Choose 1-2 tags that best describe the date:

- **art**: Museums, galleries, creative/aesthetic experiences
- **history**: Historical sites, cultural experiences, educational
- **fun**: Activities, entertainment, playful experiences
- **food**: Restaurants, markets, food-focused experiences

**Note:** The first tag is used for the fallback image, so put the most relevant one first!

## Drive Time Guidelines

Estimate from North Perry Airport (HWO):

- **Short**: < 30 minutes (green badge)
- **Medium**: 30-60 minutes (orange badge)
- **Long**: 60+ minutes (red badge)

Use Google Maps to estimate the drive time.

## Price Guidelines

- **$**: Under $20 per person
- **$$**: $20-$50 per person
- **$$$**: Over $50 per person

Include estimates for entry fees, typical meal costs, or activity pricing.

## Example: Adding a New Date

```javascript
{
    id: 'artdeco',
    name: 'Art Deco Historic District',
    desc: 'Walk through Miami Beach\'s famous pastel buildings. Architecture lovers dream, great for photos.',
    price: '$',
    time: '35 min',
    tags: ['history', 'art'],
    img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Art_Deco_District.jpg/500px-Art_Deco_District.jpg'
}
```

## Where to Add in the Code

1. Open `index.html`
2. Scroll to the `dates` array (starts around line 342)
3. Add a comma after the last date entry (after `lasolas`)
4. Paste your new date object
5. Make sure there's a comma between entries but NOT after the last one

```javascript
        {
            id: 'lasolas',
            name: 'Las Olas Boulevard',
            ...
        },  // ← Make sure there's a comma here
        {
            id: 'yournewdate',  // ← Your new date
            name: 'Your New Date',
            ...
        }  // ← NO comma after the last entry
        ];
```

## Testing Your Changes

1. Save `index.html`
2. Open it in a web browser
3. Check that:
   - Your new date appears in the pool
   - The image loads correctly
   - All text displays properly
   - Tags show the right colors
   - Drive time badge shows the correct color

## Troubleshooting

### Image not loading?
- Check that the URL is correct
- Try opening the image URL directly in a browser
- Make sure you copied the full URL
- The fallback system will show a backup image if needed

### Date not appearing?
- Check for JavaScript errors in browser console (F12)
- Make sure you have commas in the right places
- Verify the `id` is unique

### Weird formatting?
- Check that all quotes match (use straight quotes `'` not curly `'`)
- Make sure there are no extra commas or missing brackets

## Need Help?

If you run into issues:
1. Check the browser console for errors (press F12)
2. Compare your new entry to existing ones
3. Make sure all brackets `{}` and quotes `''` are properly closed

---

**Remember:** The system is designed to be forgiving! Even if an image breaks later, the fallback system will handle it gracefully.

##Tesing comments and commits

