# Dark Mode and Theme System Documentation

## Overview
The Chat with Steve Jobs application features a comprehensive theme system with automatic dark mode detection and multiple theme options.

## Features

### 🌙 Dark Mode Support
- **Automatic Detection**: The app automatically detects your system's light/dark mode preference
- **Manual Override**: Users can manually select their preferred theme
- **Smooth Transitions**: All theme changes use smooth CSS transitions for a polished experience

### 🎨 Available Themes
1. **Auto** (Default) - Automatically follows your system's light/dark mode preference
2. **Light** - Classic light theme with clean, bright colors
3. **Dark** - Dark theme optimized for low-light environments
4. **Vibrant** - Purple/pink gradient theme with high contrast
5. **Minimalist** - Clean, minimal design with subtle colors
6. **Retro Apple** - Classic Apple-inspired gray theme

### 🔧 Technical Implementation

#### CSS Variables
The theme system uses CSS custom properties (variables) for consistent color management:
```css
:root {
    --bg-color: #f4f4f4;
    --text-color: #333;
    --chat-bg: white;
    --message-bg: #f0f0f0;
    /* ... more variables */
}
```

#### Auto Mode with System Detection
The auto mode uses CSS media queries to detect system preferences:
```css
@media (prefers-color-scheme: dark) {
    [data-theme="auto"] {
        /* Dark theme variables */
    }
}
```

#### JavaScript Integration
- Detects system preference changes in real-time
- Persists user theme preference in localStorage
- Updates theme button text dynamically
- Provides smooth transitions between themes

### 📱 Browser Compatibility
- ✅ Chrome (76+)
- ✅ Firefox (67+) 
- ✅ Safari (12.1+)
- ✅ Edge (79+)

### ♿ Accessibility Features
- High contrast ratios for all themes
- Respects system accessibility preferences
- Keyboard navigation support
- Screen reader friendly

### 💾 Persistence
Theme preferences are automatically saved to browser localStorage and restored on subsequent visits.

## Usage

### For Users
1. **Automatic**: The app starts in "Auto" mode, following your system preference
2. **Manual Selection**: Click the theme button in the top-right to cycle through available themes
3. **Persistence**: Your choice is remembered for future visits

### For Developers
The theme system is easily extensible. To add a new theme:

1. Define CSS variables for the new theme:
```css
[data-theme="my-theme"] {
    --bg-color: /* your color */;
    --text-color: /* your color */;
    /* ... other variables */
}
```

2. Add the theme to the JavaScript configuration:
```javascript
const themes = ['auto', 'light', 'dark', 'my-theme'];
const themeNames = {
    'my-theme': 'My Theme'
};
```

## Benefits

### For Users
- **Comfort**: Dark mode reduces eye strain in low-light environments
- **Choice**: Multiple themes to match personal preferences
- **Consistency**: Automatic sync with system preferences
- **Performance**: CSS-only theme switching with no JavaScript overhead

### For Accessibility
- Supports users with visual sensitivities
- Respects system accessibility settings
- Provides high contrast options
- Maintains readability across all themes

## Browser Support for System Detection
The `prefers-color-scheme` media query is supported in:
- Chrome 76+ (July 2019)
- Firefox 67+ (May 2019)
- Safari 12.1+ (March 2019)
- Edge 79+ (January 2020)

For older browsers, the app gracefully falls back to the light theme.