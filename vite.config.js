import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        catalog: "./catalog/static/src/Catalog.jsx",
      },
      output: {
        entryFileNames: "static/[name].js",
      },
    },
  },
  plugins: [react()],
  base: "/staticfiles/", // Используется Django staticfiles
});
