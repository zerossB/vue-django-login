// import something here

import { each } from "lodash";

// "async" is optional;
// more info on params: https://quasar.dev/quasar-cli/boot-files
export default async ({ Vue, store }) => {
  function can(permission, model){
    try {
      const permissions = store.getters['auth/permissions'];
      let listPermissions = permissions.find(item => item.model === model).list;
      let hasPermission = false;
      
      for(let i = 0; i < listPermissions.length; i++){
        let permission_name = listPermissions[i]
        if (permission_name.includes(permission)) {
          hasPermission = true;
          break;
        }
      }

      return hasPermission
    } catch (error) {
      return false
    }
  }

  Vue.prototype.$can = can
}
