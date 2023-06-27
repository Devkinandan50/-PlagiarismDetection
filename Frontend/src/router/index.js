import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../Pages/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../Pages/AboutView.vue')
    },
    {
      path: '/how',
      name: 'how',
      component: () => import('../Pages/how.vue')
    }
  ]
})

export default router
