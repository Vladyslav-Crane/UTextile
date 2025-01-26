import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        catalog: "./catalog/static/src/Apps/Catalog/Catalog.jsx",
      },
      output: {
        entryFileNames: "[name].js",
      },
    },
  },
  plugins: [react()],
  base: "/staticfiles/", // Используется Django staticfiles
});
