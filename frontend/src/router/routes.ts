
const baseRouter = [
  {
    path: "/",
    component: () => import("/@/layout/Layout.vue"),
    redirect: "/home",
    children: [],
  },
  {
    path: "/login",
    name: "login",
    component: () => import("/@/views/login/LoginView.vue"),
  },
  {
    path: "/401",
    name: "unauthorized",
    component: () => import("/@/views/status/UnauthorizedView.vue"),
  },
  {
    path: "/:pathMatch(.*)*",
    name: "not-found",
    component: () => import("/@/views/status/NotFoundView.vue"),
  },
];

const modules = import.meta.glob("./modules/**/*.ts", {
  eager: true,
  import: "default",
});

const getRoutes = (modules, baseRouter) => {
  const modulesRoutes = [];
  // 加入到路由集合中
  Object.keys(modules).forEach((key) => {
    const mod = modules[key] || {};
    const modList = Array.isArray(mod) ? [...mod] : [mod];
    for (let i = 0; i < modList.length; i++) {
      modulesRoutes.push(modList[i]);
    }
  });
  baseRouter[0].children = [...modulesRoutes, ...baseRouter[0].children];
  return baseRouter;
};

const routes = getRoutes(modules, baseRouter);

export default routes;
