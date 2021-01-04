<template>
    <div class="row items-center window-height">
        <div class="col-12 offset-md-4 col-md-4">
            <q-card class="my-card">
                <q-card-section class="bg-primary text-white text-center">
                    <div class="text-h6">Login</div>
                </q-card-section>

                <q-card-section v-if="!isValidData" class="text-center">
                    <div class="negative" v-for="(error, index) in errors.data" :key="index">{{ error }}</div>
                </q-card-section>

                <q-card-section class="text-white">
                    <q-form>
                        <q-input color="purple-12" v-model="form.username" label="Username" type="text" :error="!isValidUsername">
                            <template v-slot:prepend>
                                <q-icon name="account_circle" />
                            </template>
                            <template v-slot:error>
                                <div v-for="(error, index) in errors.username" :key="index">{{ error }}</div>
                            </template>
                        </q-input>
                        <q-input color="purple-12" v-model="form.password" label="Password" type="password" :error="!isValidPassword">
                            <template v-slot:prepend>
                                <q-icon name="lock" />
                            </template>
                            <template v-slot:error>
                                <div v-for="(error, index) in errors.password" :key="index">{{ error }}</div>
                            </template>
                        </q-input>
                    </q-form>
                </q-card-section>

                <q-card-actions vertical>
                    <q-btn flat class="bg-primary" color="white" @click="login">Login</q-btn>
                    <hr>
                    <q-btn flat>Esqueceu sua senha?</q-btn>
                </q-card-actions>
            </q-card>
        </div>
    </div>
</template>

<script>
import _ from 'lodash'

export default {
    name: 'LoginPage',
    data(){
        return {
            form: {
                username: "",
                password: ""
            },
            errors: {}
        }
    },
    computed:{
        isValidUsername() {
            return _.isEmpty(this.errors.username)
        },
        isValidPassword() {
            return _.isEmpty(this.errors.password)
        },
        isValidData() {
            return _.isEmpty(this.errors.data)
        },
    },
    methods: {
        login: function() {
            this.cleanErrors();
            this.$axios.post('auth/login/', this.form).then((response) => {
                let data = response.data

                localStorage.setItem("user", JSON.stringify(data.payload))
                localStorage.setItem("token", JSON.stringify(data.token))

                setTimeout(() => {
                    this.$router.push({name: "Index"})
                }, 1000);
            }).catch((error) => {
                if (error.response) {
                    // Request made and server responded
                    this.errors = error.response.data
                    this.$q.notify({type: 'negative', message: this.errors.detail})
                } else {
                    // Something happened in setting up the request that triggered an Error
                    console.log('Error', error);
                }
            })
        },
        cleanErrors: function(){
            this.errors = {}
        }
    },
}
</script>

<style lang="scss" scoped>
.negative{
    color: $negative;
    font-weight: 600;
}
hr{
    height: 30px;
}
</style>