
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue'), name: 'Index' },
      { path: 'users/:uuid/edit', component: () => import('pages/users/EditUser.vue'), name: 'EditUser' }
    ]
  },

  {
    path: '/auth/',
    component: () => import('layouts/LoginLayout.vue'),
    children: [
      { path: 'login/', component: () => import('pages/auth/Login.vue'), name: "Login" },
      { path: 'logout/', component: () => import('pages/auth/Logout.vue'), name: "Logout" }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
