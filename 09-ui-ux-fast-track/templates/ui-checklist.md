# UI Checklist — Ship a Professional-Looking App in 30 Minutes

You don't need a designer. You need this checklist and Tailwind CSS.

## Pre-Build: Set Up Your Design System (10 min)

### Colors (Pick ONE palette)

Copy this into your `tailwind.config.js` or `globals.css`:

```
Primary:    #2563EB (blue-600)   — buttons, links, active states
Secondary:  #7C3AED (violet-600) — accents, highlights
Success:    #16A34A (green-600)  — confirmations, positive feedback
Warning:    #EA580C (orange-600) — cautions, pending states
Error:      #DC2626 (red-600)    — errors, destructive actions
Gray:       #F9FAFB → #111827   — backgrounds to text (gray-50 through gray-900)
```

**Rule:** 3 colors max in your entire UI. One primary, one accent, one neutral. That's it.

### Typography (Don't Overthink It)

```
Headings:   Inter or Geist (both free on Google Fonts)
Body:       Same as headings — keep it simple
Mono:       JetBrains Mono (for code blocks only)

Sizes:
  h1: text-4xl font-bold tracking-tight
  h2: text-2xl font-semibold
  h3: text-lg font-medium
  body: text-base text-gray-600
  small: text-sm text-gray-400
```

**Rule:** Two font sizes for headings, one for body. No more.

### Spacing System

```
Page padding:      px-4 sm:px-6 lg:px-8
Section gaps:      space-y-8 (2rem between sections)
Card padding:      p-6
Input padding:     px-4 py-2
Button padding:    px-4 py-2 (small) or px-6 py-3 (large)
```

**Rule:** Everything is multiples of 4. If it looks off, it's probably a spacing issue.

## The 8-Item Essential Checklist

Check each item. If you skip one, your app looks amateur.

### 1. Hero Section (Above the Fold)

- [ ] One clear headline (6–10 words max)
- [ ] One subheadline (explains what the app does)
- [ ] One primary CTA button (contrasting color, large)
- [ ] No more than 2 elements in the hero
- [ ] Background: solid color or subtle gradient, NOT a busy image

**Copy-paste starter:**
```html
<section className="py-20 px-4 text-center">
  <h1 className="text-4xl font-bold mb-4">Build Faster, Ship Sooner</h1>
  <p className="text-gray-600 text-lg mb-8 max-w-xl mx-auto">
    The all-in-one platform that turns ideas into deployed apps.
  </p>
  <button className="bg-blue-600 text-white px-8 py-3 rounded-lg font-medium hover:bg-blue-700 transition">
    Get Started Free
  </button>
</section>
```

### 2. Main Action Visible Immediately

- [ ] Primary action is above the fold
- [ ] User knows what to do within 3 seconds
- [ ] No hamburger menu for core features
- [ ] CTA appears in hero AND sticky nav

### 3. Clean Spacing & Visual Hierarchy

- [ ] Consistent padding (use the 4px grid)
- [ ] Clear section separation (gray-50 backgrounds or dividers)
- [ ] Headings are visually distinct from body text
- [ ] No text smaller than `text-sm` (14px)
- [ ] Line height is 1.5–1.75 for body text

### 4. Mobile Layout (Test Now)

- [ ] Tap targets are at least 44×44px
- [ ] Text is readable without zooming
- [ ] Single column layout on mobile
- [ ] Forms stack vertically on small screens
- [ ] No horizontal scrolling

**Quick test:** Open Chrome DevTools, toggle device toolbar, check iPhone 14.

### 5. Loading State

- [ ] Skeleton screens, NOT spinners (modern look)
- [ ] Show within 200ms of user action
- [ ] Disable buttons while loading
- [ ] Show progress for operations > 2 seconds

**Copy-paste skeleton:**
```html
<div className="animate-pulse space-y-4">
  <div className="h-4 bg-gray-200 rounded w-3/4"></div>
  <div className="h-4 bg-gray-200 rounded w-1/2"></div>
  <div className="h-32 bg-gray-200 rounded"></div>
</div>
```

### 6. Success State

- [ ] Confirmation message after key actions
- [ ] Visual indicator (checkmark, color change, animation)
- [ ] Next step suggestion ("What to do next:...")
- [ ] No raw JSON dumps or server messages

### 7. Error State

- [ ] Human-readable error messages (not "Error 500")
- [ ] Suggestion for how to fix it
- [ ] Retry button where applicable
- [ ] Form validation with inline messages
- [ ] Network error handling ("Check your connection")

**Good error message:** "We couldn't save your changes. Check your connection and try again."
**Bad error message:** "Internal Server Error"

### 8. Screenshot-Ready

- [ ] No lorem ipsum anywhere
- [ ] No placeholder images (use Unsplash random or generated avatars)
- [ ] No console errors visible
- [ ] Favicon is set
- [ ] Page title is descriptive
- [ ] OG image is set (for social sharing links)

## Premium Look Shortcuts (5-Minute Wins)

These tiny details separate "hackathon project" from "real product":

### 1. Subtle Shadows Instead of Borders
```html
<!-- Instead of border -->
<div className="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
<!-- Better: just shadow -->
<div className="bg-white rounded-xl shadow-md p-6">
```

### 2. Rounded Corners Everywhere
```
Cards:    rounded-xl or rounded-2xl
Buttons:  rounded-lg
Inputs:   rounded-lg
Avatars:  rounded-full
```
No sharp corners. Ever. Sharp corners scream "2015."

### 3. Hover Transitions on Everything Interactive
```
className="transition duration-200 ease-in-out hover:shadow-lg hover:-translate-y-0.5"
```
Buttons, cards, links — everything clickable should respond to hover.

### 4. Gradient Backgrounds (One Accent Only)
```html
<div className="bg-gradient-to-br from-blue-500 to-violet-600 text-white p-8 rounded-2xl">
```
Use for hero sections or feature highlights. Never for the whole page.

### 5. Consistent Icon Library
Pick ONE and stick with it:
- **Lucide React** (recommended): `npm i lucide-react`
- **Heroicons** (Tailwind-native): `npm i @heroicons/react`
- **Phosphor Icons**: `npm i @phosphor-icons/react`

Size: 20px for inline, 24px for standalone, 32px for feature sections.

### 6. The "3-Second Rule" Polish Pass
Open your app fresh. Count to 3. Can you tell what it does? If not:
- Make the headline bigger
- Remove competing CTAs
- Add more whitespace around the hero

## Component Inventory (Copy-Paste Tailwind)

### Primary Button
```html
<button className="bg-blue-600 text-white px-6 py-2.5 rounded-lg font-medium
  hover:bg-blue-700 active:bg-blue-800 transition duration-200
  focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
  Button Text
</button>
```

### Secondary Button
```html
<button className="bg-white text-gray-700 px-6 py-2.5 rounded-lg font-medium
  border border-gray-300 hover:bg-gray-50 active:bg-gray-100 transition duration-200">
  Button Text
</button>
```

### Card
```html
<div className="bg-white rounded-2xl shadow-md p-6 hover:shadow-lg transition duration-200">
  <h3 className="text-lg font-semibold mb-2">Card Title</h3>
  <p className="text-gray-600 text-sm">Card description goes here.</p>
</div>
```

### Input Field
```html
<input
  type="text"
  placeholder="Enter your email"
  className="w-full px-4 py-2.5 rounded-lg border border-gray-300
    focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent
    text-sm placeholder:text-gray-400"
/>
```

### Badge / Tag
```html
<span className="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium
  bg-blue-100 text-blue-800">
  Badge Text
</span>
```

### Avatar
```html
<img
  src="https://i.pravatar.cc/150"
  alt="User"
  className="w-10 h-10 rounded-full object-cover"
/>
```

### Navbar
```html
<nav className="flex items-center justify-between px-6 py-4 bg-white border-b border-gray-100">
  <div className="text-xl font-bold">Logo</div>
  <div className="flex gap-6 text-sm text-gray-600">
    <a href="#" className="hover:text-gray-900 transition">Features</a>
    <a href="#" className="hover:text-gray-900 transition">Pricing</a>
    <a href="#" className="hover:text-gray-900 transition">Docs</a>
  </div>
</nav>
```

### Footer
```html
<footer className="bg-gray-50 border-t border-gray-100 py-12 px-6">
  <div className="max-w-6xl mx-auto text-center text-sm text-gray-500">
    © 2026 Your App. Built with ❤️ at [Hackathon Name].
  </div>
</footer>
```

## Responsive Breakpoints Quick Reference

```
Mobile:    default (< 640px)   — single column, stacked
Tablet:    sm: (640px+)        — side-by-side where needed
Desktop:   lg: (1024px+)       — full layout, sidebar optional
Wide:      xl: (1280px+)       — max-width containers

Container: max-w-6xl mx-auto px-4 sm:px-6 lg:px-8
Grid:      grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6
```

## Accessibility Quick Wins (10 min)

You don't need to be an expert. These 5 things cover 80% of issues:

1. **All images have alt text.** No exceptions.
2. **All form inputs have labels.** Use `<label htmlFor="id">`.
3. **Color contrast ratio ≥ 4.5:1.** Use [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/).
4. **Keyboard navigable.** Tab order works. Focus rings visible.
5. **Skip link for main content.** `<a href="#main" className="sr-only focus:not-sr-only">Skip to content</a>`

**Quick test:** Can you tab through your entire app using only your keyboard? If yes, you're 80% there.
