const BASE_URL = process.env.VUE_APP_BACKEND_URL || 'https://chatbot-backend-badr.fly.dev'

export const signup = async (username, password) => {
  const response = await fetch(`${BASE_URL}/chat/signup/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
  })
  return response.json()
}

export const signin = async (username, password) => {
  const response = await fetch(`${BASE_URL}/chat/signin/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
  })
  return response.json()
}

export const signout = async (token) => {
  const response = await fetch(`${BASE_URL}/chat/signout/`, {
    method: 'POST',
    headers: { 'Authorization': `Token ${token}`, 'Content-Type': 'application/json' }
  })
  return response.json()
}

export const sendMessage = async (message, token = null) => {
  const headers = token ? { 'Authorization': `Token ${token}`, 'Content-Type': 'application/json' } : { 'Content-Type': 'application/json' }
  const response = await fetch(`${BASE_URL}/chat/`, {
    method: 'POST',
    headers,
    body: JSON.stringify({ message })
  })
  return response.json()
}
