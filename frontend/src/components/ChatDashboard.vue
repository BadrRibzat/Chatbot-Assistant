<template>
  <div class="flex min-h-screen bg-gray-100">
    <!-- Sidebar -->
    <div class="w-1/4 bg-secondary text-white p-4 flex flex-col">
      <div class="flex items-center mb-6">
        <img src="../assets/logo.png" alt="Logo" class="w-10 h-10 mr-2 rounded-full" />
        <h2 class="text-xl font-bold">Chatbot</h2>
      </div>
      <div class="flex-1 overflow-y-auto">
        <h3 class="text-lg font-semibold mb-2">Chat History</h3>
        <ul class="space-y-2">
          <li v-for="(chat, index) in mockHistory" :key="index" class="p-2 bg-gray-700 rounded hover:bg-gray-600 cursor-pointer transition duration-200">
            {{ chat }}
          </li>
        </ul>
      </div>
      <div class="mt-4">
        <p class="text-sm">Logged in as <span class="font-semibold">{{ $store.state.auth.username }}</span></p>
        <button @click="handleSignout" class="mt-2 w-full bg-red-500 text-white btn hover:bg-red-600">
          <i class="fas fa-sign-out-alt mr-2"></i> Sign Out
        </button>
      </div>
    </div>

    <!-- Main Chat Area -->
    <div class="w-3/4 p-6 flex flex-col">
      <h1 class="text-3xl font-bold mb-6 text-primary"><i class="fas fa-robot mr-2"></i> Chatbot Assistant</h1>
      <div class="flex-1 overflow-y-auto bg-white p-4 rounded-lg shadow mb-6">
        <div v-for="(msg, index) in $store.state.chat.messages" :key="index" :class="msg.user ? 'flex justify-end' : 'flex justify-start'" class="mb-4">
          <span :class="msg.user ? 'bg-primary text-white' : 'bg-gray-200 text-gray-800'" class="inline-block p-3 rounded-lg max-w-md shadow-sm">
            {{ msg.text }}
          </span>
        </div>
      </div>
      <div class="flex space-x-4">
        <input v-model="message" @keyup.enter="sendMessage" placeholder="Type a message..." class="input focus:ring-primary" />
        <button @click="sendMessage" class="bg-primary text-white btn hover:bg-indigo-600">
          <i class="fas fa-paper-plane"></i>
        </button>
      </div>
      <p v-if="$store.state.chat.error" class="text-red-500 mt-4 text-center">
        {{ $store.state.chat.error }}
        <router-link v-if="$store.state.chat.error.includes('limit reached')" to="/signup" class="text-blue-500 hover:underline">Sign Up Now</router-link>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: '',
      mockHistory: [
        'Chat from 5 mins ago',
        'Yesterday’s Q&A',
        'Project Discussion',
        'Random Chat'
      ]
    }
  },
  methods: {
    async sendMessage() {
      if (!this.message.trim()) return
      await this.$store.dispatch('chat/sendMessage', this.message)
      if (this.$store.state.chat.error && this.$store.state.chat.error.includes('limit reached')) {
        this.$router.push('/signup')
      }
      this.message = ''
    },
    async handleSignout() {
      await this.$store.dispatch('auth/signout')
      this.$router.push('/signin')
    }
  }
}
</script>
