<template>
  <div class="items-center no-wrap q-gutter-md row">
    <div v-if="isAuthUser" class="Layout-user row items-center q-mr-sm" :title="user.name || user.username">
      <avatar color="white" :image="user.gravatar" size="36px" :title="user.name" />
      <div class="Layout-userData cursor-pointer q-pl-xs q-pr-sm q-lh-sm">
        <div class="ellipsis">{{ user.name || user.givenName }}</div>
        <div class="text-caption ellipsis opacity-60 q-lh-sm">{{ user.email }}</div>
      </div>

      <q-menu>
        <div class="Layout-userMenu">
            <div class="q-pa-md text-center">
              <avatar color="white" :image="user.gravatar" size="75px" :title="user.name || user.username" />
              <div class="q-mt-md q-lh-sm text-subtitle1">{{ user.name || user.username }}</div>
              <div class="text-caption text-grey-6 q-truncate">{{ user.email }}</div>
            </div>
            <q-separator />
            <q-list>
              <q-item clickable @click="editProfile" v-if="canEditProfile">
                <q-item-section side>
                  <q-icon color="grey-6" name="account_box" size="20px" />
                </q-item-section>
                <q-item-section>Edit profile</q-item-section>
              </q-item>
            </q-list>
            <q-separator />
            <q-list>
              <q-item clickable @click="exitToApp">
                <q-item-section side>
                  <q-icon color="grey-6" name="exit_to_app" size="20px" />
                </q-item-section>
                <q-item-section>Exit</q-item-section>
              </q-item>
            </q-list>
        </div>
      </q-menu>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

import Avatar from './Avatar.vue'

export default {
  name: 'UserHeader',
  components:{
    Avatar
  },
  data () {
    return {}
  },
  methods:{
    exitToApp: function(){
      this.$router.push({name: "Logout"})
    },
    editProfile: function(){
      this.$router.push({name: "EditUser", params: { uuid: this.user.uuid }})
    },
  },
  computed: {
    ...mapGetters('auth', ['user', 'isAuthUser']),
    canEditProfile(){
      return this.$can('change', 'users')
    }
  }
}
</script>

<style lang="scss" scoped>
.Layout {
  background-color: $grey-1;
  &-toolbar {
    box-shadow: 0 0 15px rgba($grey-10, 0.25);
    height: 64px;
  }
  &-brand {
    height: 24px;
    margin-left: map-get($space-sm, x);
  }
  &-brandImage {
    height: 100%;
  }
  &-user {
    background-color: rgba(white, 0.1);
    border-radius: 500rem;
    padding-left: 5px;
    padding-right: 5px;
    transition: background-color $generic-hover-transition;
    &:focus,
    &:hover {
      background-color: rgba(white, 0.2);
    }
  }
  &-userData {
    max-width: 150px;
  }
  &-userMenu {
    max-width: 250px;
  }
  &-menuList {
    min-width: 100px;
  }
  @media (max-width: $breakpoint-xs) {
    &-userData {
      display: none;
    }
    &-brand--sm {
      height: 15px;
      margin-left: 0;
    }
  }
}
</style>