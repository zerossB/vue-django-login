<template>
  <q-page padding>
    <pre>
    {{ data.payload }}
    </pre>
  </q-page>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'IndexPage',
  mounted(){
    if(this.isAuthUser == false){
      this.$router.push({name: "Login"})
    }

    this.$axios.get("auth/user/").then((response) => {
        this.data = response.data
    })
  },
  data(){
    return {
      data: {}
    }
  },
  computed: {
    ...mapGetters('auth', ['user', 'isAuthUser', "permissions"])
  },
}
</script>
