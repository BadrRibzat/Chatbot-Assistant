import { signup, signin, signout } from '../../services/api'

export default {
  namespaced: true,
  state: {
    token: localStorage.getItem('token') || '',
    username: localStorage.getItem('username') || '',
    isAuthenticated: !!localStorage.getItem('token'),
    error: ''
  },
  mutations: {
    setAuth(state, { token, username }) {
      state.token = token
      state.username = username
      state.isAuthenticated = true
      state.error = ''
      localStorage.setItem('token', token)
      localStorage.setItem('username', username)
    },
    clearAuth(state) {
      state.token = ''
      state.username = ''
      state.isAuthenticated = false
      state.error = ''
      localStorage.removeItem('token')
      localStorage.removeItem('username')
    },
    setError(state, error) {
      state.error = error
    }
  },
  actions: {
    async signup({ commit }, { username, password }) {
      const data = await signup(username, password)
      if (data.token) {
        commit('setAuth', { token: data.token, username })
      } else {
        commit('setError', data.error)
      }
    },
    async signin({ commit }, { username, password }) {
      const data = await signin(username, password)
      if (data.token) {
        commit('setAuth', { token: data.token, username })
      } else {
        commit('setError', data.error)
      }
    },
    async signout({ commit, state }) {
      const data = await signout(state.token)
      if (data.message) {
        commit('clearAuth')
      } else {
        commit('setError', 'Failed to sign out')
      }
    }
  }
}
