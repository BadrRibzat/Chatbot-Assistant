<template>
  <div class="max-w-lg mx-auto p-6 bg-gray-100 min-h-screen">
    <h1 class="text-3xl font-bold text-center mb-6">
      <i class="fas fa-robot mr-2"></i> Chatbot Assistant
    </h1>

    <!-- Auth Section -->
    <div v-if="!isAuthenticated" class="mb-6">
      <div class="flex space-x-4 mb-4">
        <input v-model="username" placeholder="Username" class="flex-1 p-2 border rounded" />
        <input v-model="password" type="password" placeholder="Password" class="flex-1 p-2 border rounded" />
      </div>
      <div class="flex space-x-4">
        <button @click="signup" class="bg-blue-500 text-white p-2 rounded hover:bg-blue-600 w-full">
          <i class="fas fa-user-plus mr-2"></i> Sign Up
        </button>
        <button @click="signin" class="bg-green-500 text-white p-2 rounded hover:bg-green-600 w-full">
          <i class="fas fa-sign-in-alt mr-2"></i> Sign In
        </button>
      </div>
    </div>
    <div v-else class="mb-6 flex justify-between items-center">
      <p class="text-gray-700">Logged in as <span class="font-semibold">{{ username }}</span></p>
      <button @click="signout" class="text-red-500 hover:text-red-700">
        <i class="fas fa-sign-out-alt mr-2"></i> Sign Out
      </button>
    </div>

    <!-- Chat Area -->
    <div class="h-96 overflow-y-auto border p-4 bg-white rounded mb-6">
      <p v-for="(msg, index) in messages" :key="index" :class="msg.user ? 'text-right text-blue-600' : 'text-left text-gray-800'">
        <span class="inline-block p-2 rounded bg-gray-200">{{ msg.text }}</span>
      </p>
    </div>

    <!-- Message Input -->
    <div class="flex space-x-4">
      <input v-model="message" @keyup.enter="sendMessage" placeholder="Type a message..." class="flex-1 p-2 border rounded" />
      <button @click="sendMessage" class="bg-indigo-500 text-white p-2 rounded hover:bg-indigo-600">
        <i class="fas fa-paper-plane"></i>
      </button>
    </div>

    <!-- Error Message -->
    <p v-if="error" class="text-red-500 mt-4 text-center">{{ error }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      token: localStorage.getItem('token') || '',
      isAuthenticated: !!localStorage.getItem('token'),
      message: '',
      messages: [],
      error: '',
    }
  },
  methods: {
    async signup() {
      const res = await fetch('https://chatbot-assistant-backend.onrender.com/chat/signup/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `username=${this.username}&password=${this.password}`
      })
      const data = await res.json()
      if (res.ok) {
        this.token = data.token
        localStorage.setItem('token', this.token)
        this.isAuthenticated = true
        this.error = ''
      } else {
        this.error = data.error
      }
    },
    async signin() {
      const res = await fetch('https://chatbot-assistant-backend.onrender.com/chat/signin/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `username=${this.username}&password=${this.password}`
      })
      const data = await res.json()
      if (res.ok) {
        this.token = data.token
        localStorage.setItem('token', this.token)
        this.isAuthenticated = true
        this.error = ''
      } else {
        this.error = data.error
      }
    },
    async signout() {
      const res = await fetch('https://chatbot-assistant-backend.onrender.com/chat/signout/', {
        method: 'POST',
        headers: { 'Authorization': `Token ${this.token}` }
      })
      if (res.ok) {
        this.token = ''
        localStorage.removeItem('token')
        this.isAuthenticated = false
        this.messages = []
        this.error = ''
      } else {
        this.error = 'Failed to sign out'
      }
    },
    async sendMessage() {
      if (!this.message.trim()) return
      const headers = this.isAuthenticated ? { 'Authorization': `Token ${this.token}`, 'Content-Type': 'application/x-www-form-urlencoded' } : { 'Content-Type': 'application/x-www-form-urlencoded' }
      const res = await fetch('https://chatbot-assistant-backend.onrender.com/chat/', {
        method: 'POST',
        headers,
        body: `message=${this.message}`
      })
      const data = await res.json()
      if (res.ok) {
        this.messages.push({ text: this.message, user: true })
        this.messages.push({ text: data.response, user: false })
        this.message = ''
        this.error = ''
      } else {
        this.error = data.error || 'Something went wrong'
      }
    }
  }
}
</script>
