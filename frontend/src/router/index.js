import { createRouter, createWebHistory } from "vue-router";

import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import Dashboard from "../views/Dashboard.vue";
import UpdateUser from "../views/UpdateUser.vue";

const routes = [
  {
    path: "/",
    name: "Login",
    component: Login,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
  },
  {
    path: "/update/:id",
    name: "UpdateUser",
    component: UpdateUser,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
