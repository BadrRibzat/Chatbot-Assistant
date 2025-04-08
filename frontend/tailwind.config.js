/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#4F46E5', // Indigo for buttons
        secondary: '#1F2937' // Dark gray for sidebar
      }
    }
  },
  plugins: []
}
