/*
export function someGetter (state) {
}
*/
import _ from 'lodash'

export function isAuthUser(state){
    return !_.isEmpty(state.user)
}

export function token(state) {
    return state.user.jwt
}

export function user(state) {
    return state.user
}

export function permissions(state){
    return state.user.permissions
}