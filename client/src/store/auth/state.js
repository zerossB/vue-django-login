export default function () {
  const rawUser = localStorage.getItem('user')
  return {
    user: rawUser ? JSON.parse(rawUser) : {}
  }
}
