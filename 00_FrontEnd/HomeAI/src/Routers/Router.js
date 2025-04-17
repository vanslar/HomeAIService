import { createRouter, createWebHistory } from "vue-router";

const routes = [
    {
        path: "/HomeView",
        name: "HomeView",
        component: () => import("../Views/HomeView/HomeView.vue"),
    },

    {
        path: "/HomeViewTest",
        name: "HomeViewTest",
        component: () => import("../Views/HomeView/HomeView_test.vue"),
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router;