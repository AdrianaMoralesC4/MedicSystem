/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: { DEFAULT: "#0ea5e9" },    /* sky-500 */
        accent:  { DEFAULT: "#22c55e" },    /* green-500 */
        danger:  { DEFAULT: "#ef4444" },    /* red-500 */
      },
      borderRadius: { xl2: "1rem" }
    },
  },
  plugins: [],
}
