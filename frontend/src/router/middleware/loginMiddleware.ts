export default function loginMiddleware(to, from, next) {
  if (to.meta.requiresAuth) {
    next('/login')
  } else {
    next()
  }
}
