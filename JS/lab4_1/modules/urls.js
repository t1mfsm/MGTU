import {accessToken, version } from "./consts.js";

class Urls {
    constructor() {
        this.url = 'https://api.vk.com/method'
        this.commonInfo = `access_token=${accessToken}&v=${version}`
    }

    getUserInfo(userId) {
        return `${this.url}/users.get?user_ids=${userId}&fields=photo_200_orig,bdate,city,online,id,join_date&${this.commonInfo}`;
    }      

    getGroupMembers(groupId) {
        return `${this.url}/groups.getMembers?group_id=${groupId}&fields=photo_400_orig&${this.commonInfo}&access_token=${accessToken}`
    }

    getFriendsList(id) {
        const sortOrder = 'name'; 
        return `${this.url}/friends.get?user_id=${id}&access_token=${'vk1.a.e8f1yzxLD5qUZU2bZGbvUe_k-zaoC6vhmzmg_zyROmHsZfTub6bygcPxaTIBP6rLzWqA-yOTv2ZHONyemPFOOMgwInIyQK2-SB5OC7flhENjhiThBAqFxN0bTKc4A-77BxD3-w-yfQVdggTtxSPeozrpRfv5kt_Dem1J_4fM7QV0rjGsu75FjxBF1-3V0WfA8xcx34rLpuAxMjcA_FcLqQ'}&v=${version}&fields=nickname,domain,sex,city,photo_200_orig&order=${sortOrder}`;
    }
    
    // getGroupMembersFilter(groupId,ch) {
    //     return `${this.url}/groups.getMembers?group_id=${groupId}&filter=${ch}&fields=photo_400_orig&${this.commonInfo}`
    // }

    getGroupMembersSort(groupId, sort) {
        return `${this.url}/groups.getMembers?group_id=${groupId}&sort=${sort}&fields=photo_400_orig&${this.commonInfo}&access_token=${accessToken}`;
    }
    
}

export const urls = new Urls()