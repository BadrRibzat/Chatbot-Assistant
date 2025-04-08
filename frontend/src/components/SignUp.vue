<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-100">
    <div class="w-full max-w-md p-6 bg-white rounded-lg shadow-lg">
      <h2 class="text-2xl font-bold text-center mb-6"><i class="fas fa-user-plus mr-2"></i> Sign Up</h2>
      <form @submit.prevent="signup" class="space-y-4">
        <input v-model="username" placeholder="Username" class="w-full p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500" />
        <input v-model="password" type="password" placeholder="Password" class="w-full p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500" />
        <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600 transition duration-200">
          Sign Up
        </button>
      </form>
      <p v-if="error" class="text-red-500 text-center mt-4">{{ error }}</p>
      <p class="text-center mt-4">Already have an account? <router-link to="/signin" class="text-blue-500 hover:underline">Sign In</router-link></p>
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
    async signup() {
      const success = await this.$store.dispatch('auth/signup', { username: this.username, password: this.password })
      this.error = this.$store.state.auth.error
      if (success) {
        this.$router.push('/signin')
      }
      this.username = ''
      this.password = ''
    }
  }
}
</script>
