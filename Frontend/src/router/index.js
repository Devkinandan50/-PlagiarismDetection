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
      path: '/checkplag',
      name: 'checkplag',
      component: () => import('../Pages/CheckPlag.vue')
    }
  ]
})

export default router
