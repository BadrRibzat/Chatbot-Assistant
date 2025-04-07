import { createApp } from 'vue'
import App from './App.vue'
import store from './store'
import './assets/tailwind.css'
import '@fortawesome/fontawesome-free/css/all.css'

const app = createApp(App)
app.use(store)
app.mount('#app')
