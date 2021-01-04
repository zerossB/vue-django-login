<template>
  <q-layout view="hHh LpR fFf">

    <q-header bordered class="bg-primary text-white">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="left = !left" />

        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo/svg/quasar-logo.svg">
          </q-avatar>
          Quasar Framework
        </q-toolbar-title>

        <UserHeader></UserHeader>
      </q-toolbar>
    </q-header>

    <q-drawer show-if-above v-model="left" side="left" bordered>
      <!-- drawer content -->
    </q-drawer>

    <q-page-container class="bg-grey-1">
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<script>
import UserHeader from '../components/UserHeader.vue'

export default {
  components: {
    UserHeader
  },
  data () {
    return {
      left: false
    }
  }
}
</script>