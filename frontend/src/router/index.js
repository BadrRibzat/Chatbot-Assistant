import { createRouter, createWebHistory } from 'vue-router'
import ChatDashboard from '../components/ChatDashboard.vue'
import SignUp from '../components/SignUp.vue'
import SignIn from '../components/SignIn.vue'

const routes = [
  { path: '/', redirect: '/chat' },
  { path: '/chat', component: ChatDashboard, meta: { requiresAuth: true } },
  { path: '/signup', component: SignUp },
  { path: '/signin', component: SignIn }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL || '/'),
  routes
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('token')
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/signin')
  } else {
    next()
  }
})

export default router
