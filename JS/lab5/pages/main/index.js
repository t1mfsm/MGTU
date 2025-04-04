import {CardComponent} from "../../components/card/index.js";
import {ProductPage} from "../product/index.js";
import {Urls} from "../../modules/urls.js";
import {group_list} from "../../modules/consts.js"
import { GroupButtonsComponent } from "../../components/group-button/index.js";



export class MainPage {
    constructor(parent, group_number) {
        this.group_number = group_number
        this.accessToken = group_list[group_number][1]
        this.groupId = group_list[group_number][0]
        this.urls = new Urls(this.accessToken, this.groupId)
        this.parent = parent;
    }
    
    get pageRoot() {
        return document.getElementById('main-page')
    }
        
    getHTML() {
        return (
            `
                <div id="main-page" class="d-flex flex-wrap"><div/>
            `
        )
    }

    getData() {
            fetch(this.urls.getGroupMembers())
                .then(response => response.json())
                .then(data => this.renderData(data.response.items))
                .catch(error => console.error('Error:', error));
        //Отправить сообщениче через fetch
    }

    renderData(items) {
        items.forEach((item) => {
            const productCard = new CardComponent(this.pageRoot)
            productCard.render(item, this.clickCard.bind(this))
        })
    }

    clickCard(e) {
        const cardId = e.target.dataset.id
        console.log(`card id ${cardId}`)
        const productPage = new ProductPage(this.parent, cardId, this.group_number)
        productPage.render()
    }

    clickNewGroup(e) {
        const countID = e.target.dataset.id
        console.log(e.target.dataset.id)
        const new_mainPage = new MainPage(this.parent, countID)
        new_mainPage.render()
    }

    render() {
        this.parent.innerHTML = ''
        const html = this.getHTML()
        this.parent.insertAdjacentHTML('beforeend', html)
        const gr_list = new GroupButtonsComponent(this.pageRoot)
        gr_list.render(group_list, this.clickNewGroup.bind(this))
        this.getData()
    }
}