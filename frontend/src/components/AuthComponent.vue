<template>
  <div class="mb-6">
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
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    signup() {
      this.$store.dispatch('auth/signup', { username: this.username, password: this.password })
      this.reset()
    },
    signin() {
      this.$store.dispatch('auth/signin', { username: this.username, password: this.password })
      this.reset()
    },
    reset() {
      this.username = ''
      this.password = ''
    }
  }
}
</script>
