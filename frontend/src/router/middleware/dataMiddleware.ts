export default function dataMiddleware(to, from, next) {
  if (to.meta.requiresAuth) {
    next('/login')
  } else {
    next()
  }
}
