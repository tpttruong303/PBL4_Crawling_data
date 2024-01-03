import { createRouter, createWebHistory } from "vue-router"

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: "/",
            redirect: "/mainjob", 
        },
        {
            path: "/mainjob",
            component: () => import("../views/mainjob/index.vue"),
            meta: {
                layout: "default",
            },
        },
        {
            path: "/login",
            component: () => import("../views/login/index.vue"),
        },
        {
            path: "/register",
            component: () => import("../views/register/index.vue"),
        },
        {
            path: "/user",
            component: () => import("../views/user/index.vue"),

        },
        {
            path: "/admin",
            component: () => import("../views/admin/index.vue"),

        },
        {
            path: '/mainjob/:id',
            name: 'JobDetail',
            component: () => import("../views/jobdetails/index.vue"),
            props: true 
        }
        
    ],
})

export default router
