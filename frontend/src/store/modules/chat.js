import { sendMessage } from '../../services/api'

export default {
  namespaced: true,
  state: {
    messages: [],
    messageCount: 0,
    error: ''
  },
  mutations: {
    addMessage(state, message) {
      state.messages.push(message)
      if (message.user) state.messageCount++
    },
    clearMessages(state) {
      state.messages = []
      state.messageCount = 0
      state.error = ''
    },
    setError(state, error) {
      state.error = error
    }
  },
  actions: {
    async sendMessage({ commit, state, rootState }, message) {
      if (!message.trim()) return
      const token = rootState.auth.token
      const data = await sendMessage(message, token)
      if (data.response) {
        commit('addMessage', { text: message, user: true })
        commit('addMessage', { text: data.response, user: false })
      } else if (data.error && data.error.includes('limit reached')) {
        commit('setError', 'You’ve reached the 10-message limit. Sign up for unlimited access!')
      } else {
        commit('setError', data.error || 'Something went wrong')
      }
    }
  }
}
