import Vue from 'vue'
import axios from 'axios'

export default async ({Vue, store}) => {
    const token = store.getters['auth/token']
    axios.defaults.baseURL = process.env.APIHOST || 'http://localhost:8000/'

    // Headers
    if (token && typeof token === 'string') {
        axios.defaults.headers = {
            'Authorization': `JWT ${token}`
        }
    }

    Vue.prototype.$axios = axios
}
