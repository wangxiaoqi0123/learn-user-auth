import { createRouter, createWebHistory } from 'vue-router'
import routes from './routes'
import routerMiddleware from './middleware'

const router = createRouter({
  history: createWebHistory('/'),
  routes,
  scrollBehavior: () => ({ left: 0, top: 0 })
})

router.beforeEach((to, from, next) => {
  routerMiddleware(to, from, next)
})

router.afterEach(() => {
  document.body.scrollTop = 0
})
export default router
