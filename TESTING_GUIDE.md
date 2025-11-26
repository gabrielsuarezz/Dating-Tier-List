# Testing Guide - Image System Updates

## Quick Test (5 minutes)

### 1. Open the App
Simply open `index.html` in your web browser:
- **Option A**: Double-click `index.html` in File Explorer
- **Option B**: Right-click → "Open with" → Choose your browser (Chrome, Firefox, Edge, etc.)

### 2. Visual Check ✓
When the page loads, you should see:
- ✅ All 26 date cards in the "Unranked Dates" pool
- ✅ Each card has an image (no broken image icons)
- ✅ Images look relevant to their dates
- ✅ Cards are draggable to different tiers

### 3. Test Drag & Drop
- Drag a few cards to different tier rows (S, A, B, C, D)
- Cards should move smoothly
- Try dragging them back to the pool

### 4. Test Filters
Click the filter buttons at the top:
- **All Dates** - Shows all 26 cards
- **🎨 Art & Cute** - Shows only art-tagged dates
- **🏛️ History** - Shows only history-tagged dates
- **🎢 Fun & Silly** - Shows only fun-tagged dates
- **🌿 Healthy Eats** - Shows only food-tagged dates

## Detailed Image Testing (10 minutes)

### Test the Fallback System

To verify the fallback system actually works, let's intentionally break an image:

1. Open `index.html` in a text editor
2. Find any date (e.g., Vizcaya Museum around line 350)
3. Change the `img` URL to something broken:
   ```javascript
   img: 'https://fake-url-that-doesnt-exist.com/broken.jpg'
   ```
4. Save and refresh your browser
5. **Expected Result**: You should see a fallback image appear (not a broken icon)
6. The fallback will match the date's category (art/history/fun/food)
7. **Undo this change** when done testing!

### Check Specific Images

Open your browser's Developer Tools (press **F12**) and look at the Console tab.

**Good Signs:**
- No red error messages
- Images load without issues

**If you see warnings about images:**
- That's okay! The fallback system will handle it
- Check that the fallback image appears instead

### Test Individual Cards

Hover over each card and verify:
- ✅ Image appears and is relevant to the location
- ✅ Image zooms slightly on hover
- ✅ Drive time badge shows (with color: green < 30min, orange 30-60min, red 60+ min)
- ✅ Price shows ($, $$, or $$$)
- ✅ Tags show at bottom with colors

## Browser Compatibility Test

Test in multiple browsers if available:
- [ ] Chrome
- [ ] Firefox
- [ ] Edge
- [ ] Safari (if on Mac)

All should work identically.

## Network Test (Advanced)

Test how the app handles slow/bad connections:

1. Open Developer Tools (F12)
2. Go to "Network" tab
3. Change throttling to "Slow 3G" or "Offline"
4. Refresh the page
5. **Expected**: Images should eventually load (or show fallbacks)

## What Changed - Verification Checklist

Compare to the old version and verify:

### ✅ All Unsplash URLs Replaced
These dates should now have Wikimedia Commons images:
- [ ] Silverball Arcade (pinball machine)
- [ ] Yellow Green Market (farmers market veggies)
- [ ] The Redlander (vineyard)
- [ ] Superblue Miami (light installation)
- [ ] T.Y. Park (pedal boats)
- [ ] Good Luck Cat Cafe (cat photo)
- [ ] Mad Arts (neon lights)
- [ ] Knaus Berry Farm (cinnamon rolls)
- [ ] Puttshack / PopStroke (mini golf)
- [ ] Cauley Sq Tea Room (tea setting)
- [ ] Better Than Sex (chocolate cake)
- [ ] Naked Farmer (healthy salad)
- [ ] Las Olas Boulevard (boulevard photo)

### ✅ Existing Wikimedia Images Still Work
These should still display correctly:
- [ ] Vizcaya Museum
- [ ] Morikami Gardens
- [ ] Coral Castle
- [ ] Butterfly World
- [ ] Bonnet House
- [ ] Frost Science
- [ ] Robert Is Here
- [ ] Venetian Pool
- [ ] Lion Country Safari
- [ ] Oleta River Park
- [ ] SoundScape Park
- [ ] Wynwood Walls
- [ ] Gumbo Limbo Center

## Common Issues & Solutions

### ❌ Problem: Some images still not loading
**Solution**:
- Check your internet connection
- The fallback system should show a backup image
- Open browser console (F12) to see which URLs are failing

### ❌ Problem: Images look wrong/irrelevant
**Solution**:
- Note which dates have bad images
- Find better images on Wikimedia Commons
- Update the URL in `index.html`
- See `HOW_TO_ADD_DATES.md` for instructions

### ❌ Problem: Page is blank or broken
**Solution**:
- Open browser console (F12)
- Look for JavaScript errors (usually in red)
- Common causes:
  - Missing comma between date entries
  - Extra comma after last date entry
  - Mismatched quotes or brackets

### ❌ Problem: Drag and drop not working
**Solution**:
- This is unrelated to image changes
- Clear your browser cache (Ctrl+Shift+Delete)
- Try a different browser

## Performance Check

The app should load quickly. Check:
- Initial page load: < 3 seconds (on normal connection)
- All images visible: < 5 seconds
- Smooth dragging with no lag

## Success Criteria ✅

Your testing is complete when:
- ✅ All 26 date cards display with images
- ✅ No broken image icons visible
- ✅ Images are relevant to their dates
- ✅ Drag & drop works smoothly
- ✅ All filters work correctly
- ✅ No console errors in browser dev tools

---

## Quick Commands for Testing

### Open in Default Browser (Windows)
```bash
start index.html
```

### Open in Specific Browser
```bash
# Chrome
start chrome index.html

# Firefox
start firefox index.html

# Edge
start msedge index.html
```

---

## Next Steps After Testing

If everything works:
- ✅ You're all set! The image system is now stable and maintainable
- 📝 Use `HOW_TO_ADD_DATES.md` when adding new dates in the future

If you find issues:
- 📋 Make a list of which dates have problems
- 🔍 Check the browser console for specific error messages
- 🛠️ We can fix any remaining issues together
