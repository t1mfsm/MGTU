import {ProductComponent} from "../../components/product/index.js";
import {BackButtonComponent} from "../../components/back-button/index.js";
import {MainPage} from "../main/index.js";
import {Urls} from "../../modules/urls.js";
import {group_list} from "../../modules/consts.js";
import {InputComponent} from "../../components/input-message/index.js";


export class ProductPage {
    constructor(parent, id, group_number) {
        this.parent = parent
        this.group_number = group_number
        this.accessToken = group_list[group_number][1]
        this.groupId = group_list[group_number][0]
        this.urls = new Urls(this.accessToken, this.groupId)
        this.id = id
    }

    getData() {
        fetch(this.urls.getGroupMembers(this.id))
                .then(response => response.json())
                .then(data => this.renderData(data.response.items))
                .catch(error => console.error('Error:', error));
        
    }

    renderData(item) {
        const product = new ProductComponent(this.pageRoot)
        product.render(item[0])
    }

    get pageRoot() {
        return document.getElementById('product-page')
    }

    getHTML() {
        return (
            `
                <div id="product-page"></div>
            `
        )
    }
    clickBack() {
        console.log(`product return groupid ${this.group_number}`)
        const mainPage = new MainPage(this.parent, this.group_number)
        mainPage.render()
    }

    clickPost() {
        const messageInput = document.getElementById('message');
        const messageValue = messageInput.value;
        ajax.post(this.urls.postMessage(this.id, messageValue), (data) => {});
    }
    
    render() {
        this.parent.innerHTML = ''
        const html = this.getHTML()
        this.parent.insertAdjacentHTML('beforeend', html)
    
        const backButton = new BackButtonComponent(this.pageRoot)
        backButton.render(this.clickBack.bind(this))
        const inputmessage = new InputComponent(this.pageRoot)
        inputmessage.render(this.clickPost.bind(this))
        this.getData()
    }
}