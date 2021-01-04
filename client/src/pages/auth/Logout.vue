<template>
  <q-page padding>
    <div class="row items-center window-height">
      <div class="col-12 offset-md-3 col-md-6 text-center">
          <h1>Saindo do Sistema</h1>
          <h2>{{ countDown }}</h2>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'LogoutPage',
  created(){
    this.countDownTimer()
  },
  data(){
    return {
      countDown: 10
    }
  },
  methods: {
    countDownTimer() {
        if(this.countDown > 0) {
            setTimeout(() => {
                this.countDown -= 1
                this.countDownTimer()
            }, 1000)
        }else{
          this.$axios.get("auth/logout/").then((result) => {
            localStorage.removeItem("user")
            localStorage.removeItem("token")

            this.$router.push({name: "Login"})
          }).catch((error) => {
            localStorage.removeItem("user")
            localStorage.removeItem("token")

            this.$router.push({name: "Login"})
          })
        }
    }
  },
}
</script>
