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
      try {
        const data = await signup(username, password)
        if (data.token) {
          commit('setAuth', { token: data.token, username })
          return true
        } else {
          commit('setError', data.error || 'Signup failed')
          return false
        }
      } catch (e) {
        commit('setError', 'Something went wrong')
        return false
      }
    },
    async signin({ commit }, { username, password }) {
      try {
        const data = await signin(username, password)
        if (data.token) {
          commit('setAuth', { token: data.token, username })
          return true
        } else {
          commit('setError', data.error || 'Signin failed')
          return false
        }
      } catch (e) {
        commit('setError', 'Something went wrong')
        return false
      }
    },
    async signout({ commit, state }) {
      try {
        await signout(state.token)
        commit('clearAuth')
        return true
      } catch (e) {
        commit('setError', 'Failed to sign out')
        return false
      }
    }
  }
}
