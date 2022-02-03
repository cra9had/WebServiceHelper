import Vue from 'vue'
import Router from 'vue-router'
import Register from './components/Register'
import PageNotFound from './Views/NotFoundPage'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [{
            path: '/register/:hash',
            component: Register,
            name: "HomePage"
        },
        {
            path: '/:pathMatch(.*)*',
            component: PageNotFound,
            name: "PageNotFound"
        }
    ]
})