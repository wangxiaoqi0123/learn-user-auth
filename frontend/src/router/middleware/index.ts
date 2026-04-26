import loginMiddleware from './loginMiddleware'
import dataMiddleware from './dataMiddleware'
import authMiddleware from './authMiddleware'

const whitelist = ['/', '/401', '/404']
const middlewares = [loginMiddleware, dataMiddleware, authMiddleware]

const routerMiddleware = (to, from, next) => {
  const url = to.path
  if (whitelist.includes(url))  return next()

  const stack = [...middlewares]
  const _next = (...args: any[]) => {
    if (args.length > 0 || stack.length === 0) {
      return next(...args)
    }
    const middleware = stack.shift()
    middleware(to, from, _next)
  }
  _next()
}

export default routerMiddleware
