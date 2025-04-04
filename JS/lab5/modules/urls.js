import {version} from "./consts.js";

export class Urls {
    constructor(accessToken, groupId) {
        this.accessToken = accessToken
        this.groupId = groupId
        this.url = 'https://api.vk.com/method'
        this.commonInfo = `access_token=${accessToken}&v=${version}`
    }

    getUserInfo(userId) {
        return `${this.url}/users.get?user_ids=${userId}&fields=photo_400_orig&${this.commonInfo}`
    }

    getGroupMembers() {
        return `${this.url}/groups.getMembers?group_id=${this.groupId}&fields=photo_400_orig&${this.commonInfo}`
    }

    getGroupMembers() {
        return `${this.url}/groups.getMembers?group_id=${this.groupId}&fields=photo_400_orig&${this.commonInfo}`
    }

    postMessage(userId, message) {
        return `${this.url}/messages.send?user_id=${userId}&random_id=0&message=${message}&${this.commonInfo}`
    }
}