---
name: Institutional Clarity
colors:
  surface: '#0b1326'
  surface-dim: '#0b1326'
  surface-bright: '#31394d'
  surface-container-lowest: '#060e20'
  surface-container-low: '#131b2e'
  surface-container: '#171f33'
  surface-container-high: '#222a3d'
  surface-container-highest: '#2d3449'
  on-surface: '#dae2fd'
  on-surface-variant: '#c4c5d5'
  inverse-surface: '#dae2fd'
  inverse-on-surface: '#283044'
  outline: '#8e909f'
  outline-variant: '#444653'
  surface-tint: '#b8c4ff'
  primary: '#b8c4ff'
  on-primary: '#002584'
  primary-container: '#1e40af'
  on-primary-container: '#a8b8ff'
  inverse-primary: '#3755c3'
  secondary: '#7bd0ff'
  on-secondary: '#00354a'
  secondary-container: '#00a6e0'
  on-secondary-container: '#00374d'
  tertiary: '#b9c8de'
  on-tertiary: '#233143'
  tertiary-container: '#3e4c5e'
  on-tertiary-container: '#adbcd2'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dde1ff'
  primary-fixed-dim: '#b8c4ff'
  on-primary-fixed: '#001453'
  on-primary-fixed-variant: '#173bab'
  secondary-fixed: '#c4e7ff'
  secondary-fixed-dim: '#7bd0ff'
  on-secondary-fixed: '#001e2c'
  on-secondary-fixed-variant: '#004c69'
  tertiary-fixed: '#d4e4fa'
  tertiary-fixed-dim: '#b9c8de'
  on-tertiary-fixed: '#0d1c2d'
  on-tertiary-fixed-variant: '#39485a'
  background: '#0b1326'
  on-background: '#dae2fd'
  surface-variant: '#2d3449'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  title-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
  mono-data:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 32px
---

## Brand & Style
The design system is engineered for high-stakes institutional finance, prioritizing precision, authority, and rapid data processing. The brand personality is stoic and reliable, evoking the stability of a legacy financial institution merged with the speed of a modern high-frequency trading platform.

The aesthetic follows a **Corporate / Modern** direction with a focus on high-contrast dark mode. It utilizes a layered surface architecture to manage complex information density without overwhelming the user. The emotional response should be one of absolute confidence and "quiet power"—where the interface recedes to let the data lead.

## Colors
This design system utilizes a "Deep Sea" palette. The foundation is a rich charcoal-navy (`#0f172a`), providing a stable, low-strain backdrop for extended professional use. 

- **Primary Blue:** A deep, authoritative blue used for brand presence and primary actions.
- **Accents:** Vibrant sky blue is reserved for interactive highlights and focus states to ensure they "pop" against the dark surfaces.
- **Semantic Colors:** Success, Warning, and Error states use high-chroma variants to ensure immediate recognition against the dark background, maintaining accessibility standards (WCAG AA).
- **Surface Tiering:** Depth is communicated through color luminance; higher-level containers use lighter navy shades (`#1e293b` and `#334155`) to appear closer to the user.

## Typography
The system relies exclusively on **Inter** for its systematic, utilitarian clarity and exceptional legibility at small sizes. 

- **Scale:** A tight typographic scale prevents layout bloat. 
- **Hierarchy:** Use `White (#FFFFFF)` for primary headings and `Slate 300 (#cbd5e1)` for body text to reduce visual vibration on dark backgrounds.
- **Data Display:** For financial tables and ticker data, use a monospaced font (JetBrains Mono) to ensure tabular figures align perfectly, allowing for easier vertical scanning of numbers.
- **Labels:** Small labels use medium weight with increased letter spacing for readability in dense dashboard environments.

## Layout & Spacing
The layout uses a **fixed-fluid hybrid grid**. 
- **Desktop:** 12-column grid with a max-width of 1440px for standard views, but allows for full-width fluid "Workstation" views for data-heavy dashboards.
- **Rhythm:** A strict 4px baseline grid ensures vertical rhythm. Spacing between related components should stay at `8px` or `16px`, while section-level separation uses `40px`.
- **Density:** Provide two density modes: "Compact" (for traders/analysts) which reduces padding to 4px/8px, and "Comfortable" (for reporting/admin) which uses 12px/16px padding.

## Elevation & Depth
In this dark-themed system, depth is conveyed through **Tonal Layering** and **Low-Contrast Outlines** rather than traditional shadows.

- **Level 0 (Background):** `#0f172a` — The lowest canvas layer.
- **Level 1 (Cards/Panels):** `#1e293b` — Primary containers. Use a subtle 1px border of `#334155` to define edges.
- **Level 2 (Modals/Popovers):** `#334155` — Elevated surfaces. These are the only elements that receive a soft, dark-tinted shadow (0px 8px 24px rgba(0,0,0,0.5)) to separate them from the grid.
- **Interactive States:** Use a "Inner Glow" effect for active elements, using a 10% opacity version of the primary blue to simulate a backlit physical control.

## Shapes
The shape language is controlled and professional. A standard radius of **8px (0.5rem)** is applied to buttons, input fields, and cards. This provides a modern feel that is "softer" than legacy financial software but retains more structure than a consumer-facing app. 

- **Small elements (Checkboxes):** 4px radius.
- **Buttons/Inputs:** 8px radius.
- **Large containers:** 12px radius.
- **Tabs:** Top-only 8px radius to maintain a structural connection to the content pane below.

## Components
- **Buttons:** Primary buttons use a solid `#1e40af` fill with white text. Secondary buttons use a ghost style with a `#334155` border and sky blue text.
- **Input Fields:** Darker than the container surface (`#0f172a`) to create an "inset" feel. On focus, the border transitions to the primary vibrant blue with a 2px outer glow.
- **Data Tables:** Zebra-striping is discouraged. Instead, use thin `1px` dividers in `#1e293b`. Row hover states should use a subtle highlight of `#334155`.
- **Chips/Badges:** For status indicators (e.g., "Active", "Pending"), use a "soft-tint" style: a 10% opacity background of the semantic color with a 100% opacity text color (e.g., Soft Green BG + Solid Green Text).
- **Cards:** Cards should have no shadow by default; they are defined by their surface color contrast and 1px border.
- **Charts:** Use a custom-tuned palette of 6 colors that are optimized for visibility on navy backgrounds, avoiding high-vibration oranges or yellows unless for alerts.