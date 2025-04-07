<template>
  <div class="max-w-lg mx-auto p-6 bg-gray-100 min-h-screen">
    <h1 class="text-3xl font-bold text-center mb-6">
      <i class="fas fa-robot mr-2"></i> Chatbot Assistant
    </h1>

    <AuthComponent v-if="!$store.state.auth.isAuthenticated" />
    <div v-else class="mb-6 flex justify-between items-center">
      <p class="text-gray-700">Logged in as <span class="font-semibold">{{ $store.state.auth.username }}</span></p>
      <button @click="$store.dispatch('auth/signout')" class="text-red-500 hover:text-red-700">
        <i class="fas fa-sign-out-alt mr-2"></i> Sign Out
      </button>
    </div>

    <div class="h-96 overflow-y-auto border p-4 bg-white rounded mb-6">
      <p v-for="(msg, index) in $store.state.chat.messages" :key="index" :class="msg.user ? 'text-right text-blue-600' : 'text-left text-gray-800'">
        <span class="inline-block p-2 rounded bg-gray-200">{{ msg.text }}</span>
      </p>
    </div>

    <div class="flex space-x-4">
      <input v-model="message" @keyup.enter="sendMessage" placeholder="Type a message..." class="flex-1 p-2 border rounded" />
      <button @click="sendMessage" class="bg-indigo-500 text-white p-2 rounded hover:bg-indigo-600">
        <i class="fas fa-paper-plane"></i>
      </button>
    </div>

    <p v-if="$store.state.auth.error" class="text-red-500 mt-4 text-center">{{ $store.state.auth.error }}</p>
    <p v-if="$store.state.chat.error" class="text-red-500 mt-4 text-center">{{ $store.state.chat.error }}</p>
  </div>
</template>

<script>
import AuthComponent from './AuthComponent.vue'

export default {
  components: { AuthComponent },
  data() {
    return {
      message: ''
    }
  },
  methods: {
    sendMessage() {
      this.$store.dispatch('chat/sendMessage', this.message)
      this.message = ''
    }
  }
}
</script>
