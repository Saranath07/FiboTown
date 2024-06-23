// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    "@nuxtjs/tailwindcss",
    "@pinia/nuxt",
    "@nuxtjs/mdc"
  ],
  app: {
    head: {
      link: [
        {
          rel: "stylesheet",
          href: "https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css"
        }
      ],
      script: [
        {
          src: "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML",
          async: true
        }
      ]
    }
  },
  mdc: {
    rehypePlugins: {
      'rehype-katex': {
        options:
        {
          output: 'html'
        }
      },
    },
    remarkPlugins:  {
      'remark-math': {},
    }
  }
})
