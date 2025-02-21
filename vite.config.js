import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        catalog: "./catalog/static/src/Apps/Catalog/App.jsx",
      },
      output: {
        entryFileNames: "[name].js",
        assetFileNames: "assets/[name].[ext]",
      },
    },
  },
  plugins: [react()],
  base: "/staticfiles/", // Используется Django staticfiles
});
