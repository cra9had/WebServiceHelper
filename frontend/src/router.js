import Vue from 'vue'
import Router from 'vue-router'
import Register from './components/Register'
import PageNotFound from './Views/NotFoundPage'
import Login from './Views/Login'
import UserPage from './components/UserPage'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [{
            path: '/register/:hash',
            component: Register,
            name: "RegisterPage"
        },
        {
            path: '/login',
            component: Login,
            name: "LoginPage"
        },
        {
            path: '/user/:username',
            component: UserPage,
            name: "UserPage"
        },
        {
            path: '/:pathMatch(.*)*',
            component: PageNotFound,
            name: "PageNotFound"
        }
    ]
})