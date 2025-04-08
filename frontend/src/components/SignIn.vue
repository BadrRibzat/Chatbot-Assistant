<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-100">
    <div class="w-full max-w-md p-6 bg-white rounded-lg shadow-lg">
      <h2 class="text-2xl font-bold text-center mb-6"><i class="fas fa-sign-in-alt mr-2"></i> Sign In</h2>
      <form @submit.prevent="signin" class="space-y-4">
        <input v-model="username" placeholder="Username" class="w-full p-2 border rounded focus:outline-none focus:ring-2 focus:ring-green-500" />
        <input v-model="password" type="password" placeholder="Password" class="w-full p-2 border rounded focus:outline-none focus:ring-2 focus:ring-green-500" />
        <button type="submit" class="w-full bg-green-500 text-white p-2 rounded hover:bg-green-600 transition duration-200">
          Sign In
        </button>
      </form>
      <p v-if="error" class="text-red-500 text-center mt-4">{{ error }}</p>
      <p class="text-center mt-4">Need an account? <router-link to="/signup" class="text-blue-500 hover:underline">Sign Up</router-link></p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      error: ''
    }
  },
  methods: {
    async signin() {
      const success = await this.$store.dispatch('auth/signin', { username: this.username, password: this.password })
      this.error = this.$store.state.auth.error
      if (success) {
        this.$router.push('/chat')
      }
      this.username = ''
      this.password = ''
    }
  }
}
</script>
