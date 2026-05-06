---
name: PulseIQ
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#45464d'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#4648d4'
  on-secondary: '#ffffff'
  secondary-container: '#6063ee'
  on-secondary-container: '#fffbff'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#002113'
  on-tertiary-container: '#009668'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#e1e0ff'
  secondary-fixed-dim: '#c0c1ff'
  on-secondary-fixed: '#07006c'
  on-secondary-fixed-variant: '#2f2ebe'
  tertiary-fixed: '#6ffbbe'
  tertiary-fixed-dim: '#4edea3'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005236'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  display:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.02em
  h1:
    fontFamily: Inter
    fontSize: 30px
    fontWeight: '600'
    lineHeight: 38px
    letterSpacing: -0.01em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: 0em
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.02em
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
  xl: 32px
  2xl: 48px
  3xl: 64px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system is engineered for high-stakes business intelligence, prioritizing clarity, authority, and cognitive ease. The brand personality is "The Sophisticated Navigator"—reliable, intelligent, and forward-thinking. It bridges the gap between complex data science and actionable executive insights.

The visual style follows a **Corporate / Modern** aesthetic with a strong emphasis on **Minimalism**. It utilizes a "data-first" philosophy where the interface recedes to allow insights to take center stage. By employing generous whitespace and a restricted color palette, the system ensures that even the most information-dense dashboards remain scannable and stress-free.

## Colors

The palette is anchored by a deep navy primary, providing a sense of stability and professional gravity. The vibrant indigo is used exclusively for interactive elements and primary call-to-actions, acting as a beacon for the user's journey.

- **Primary (#0F172A):** Used for sidebars, primary headings, and high-level navigation backgrounds.
- **Accent (#6366F1):** Reserved for primary buttons, active states, and critical data highlights.
- **Success (#10B981):** Utilized for positive growth metrics, "on-track" statuses, and completed actions.
- **Background (#F8FAFC):** A cool, low-strain canvas that differentiates content areas without the harshness of pure white.
- **Border/Muted:** Use #E2E8F0 for subtle containment and #94A3B8 for secondary text.

## Typography

The design system utilizes **Inter** across all levels to maintain a systematic and utilitarian feel. The hierarchy is established through drastic weight shifts rather than just size changes.

- **Headings:** Use Semi-Bold (600) or Bold (700) for all H1-H3 levels to ensure strong section anchoring.
- **Data Points:** Large metrics should use a "Display" style with tight letter-spacing for a modern, high-density look.
- **Labels:** Use Medium (500) or Semi-Bold (600) at smaller sizes (12px-14px) for table headers and form labels to maintain readability at a glance.
- **Paragraphs:** Standard body text should remain at 16px with a generous 1.5x line height to support long-form report reading.

## Layout & Spacing

The system employs a **Fixed Grid** philosophy for dashboard layouts to maintain consistency in data visualization placement. A 12-column grid is standard, with 24px gutters providing ample breathing room between widgets.

- **Internal Padding:** Widgets and cards should use a minimum of 24px (lg) internal padding to prevent content from feeling cramped.
- **Rhythm:** Use a 4px base unit. All margins and paddings should be multiples of 4 (e.g., 8, 16, 24, 32).
- **Page Layout:** Sidebars are fixed at 280px, with the main content area utilizing a maximum width of 1440px for optimal readability on wide monitors.

## Elevation & Depth

To maintain a clean and professional look, this design system avoids heavy drop shadows in favor of **Tonal Layers** and **Ambient Shadows**.

- **Surface Levels:** 
    - Level 0: Background (#F8FAFC)
    - Level 1: Cards and main containers (White #FFFFFF)
    - Level 2: Overlays, Modals, and Dropdowns (White #FFFFFF + Shadow)
- **Shadow Profile:** Shadows should be highly diffused and low-opacity. Use a subtle Y-offset (4px-8px) with a large blur (15px-25px) and a very low alpha (e.g., `rgba(15, 23, 42, 0.08)`).
- **Separation:** Use 1px borders in #E2E8F0 for primary containment, reserving shadows exclusively for elements that sit "above" the main layout (like modals or active tooltips).

## Shapes

The shape language is defined by a **Rounded** philosophy, striking a balance between the rigidity of traditional finance tools and the approachability of modern SaaS.

- **Small Components:** Checkboxes and small tags use 4px (0.25rem).
- **Standard Components:** Buttons, input fields, and small cards use 8px (0.5rem).
- **Large Components:** Dashboard widgets and main containers use 12px (0.75rem) to 16px (1rem).
- **Interactive States:** Focus states should follow the container's radius exactly, with a 2px offset for clarity.

## Components

- **Buttons:** Primary buttons use the Indigo accent with white text. Secondary buttons use a transparent background with a 1px #E2E8F0 border.
- **Cards:** White background, 1px border (#E2E8F0), and 12px corner radius. Use a subtle shadow on hover to indicate interactivity.
- **Input Fields:** 8px radius, white background, 1px border. On focus, the border shifts to Indigo with a soft 3px outer glow in the same color (at 15% opacity).
- **Chips/Badges:** For status indicators (e.g., Success, Warning), use a light tint of the status color for the background and a high-contrast dark version for the text. 
- **Data Tables:** Row heights should be generous (min 48px). Use a subtle #F8FAFC zebra stripe or a 1px bottom border to separate rows.
- **Charts:** Use a refined palette for data viz that complements the Indigo and Emerald, introducing muted teals and slates to avoid visual clutter.