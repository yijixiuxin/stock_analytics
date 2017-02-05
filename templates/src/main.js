// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Vuex from 'vuex'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import VueResource from 'vue-resource'

Vue.use(VueResource);

Vue.use(ElementUI)
Vue.use(Vuex)

// 状态管理器
const store = new Vuex.Store({
    state: {
        code: null
    },
    mutations: {
        changeCode(state, payload) {
            state.code = payload.code
        }
    }
})

/* eslint-disable no-new */
new Vue({
    el: '#app',
    store,
    template: '<App/>',
    components: { App }
})