import { ProductCardComponent } from "../../components/product-card/index.js";
import { ProductComponent } from "../../components/product/index.js";
import { ProductPage } from "../product/index.js";
import { ajax } from "../../modules/ajax.js";
import { urls } from "../../modules/urls.js";
import {groupId} from "../../modules/consts.js";
import {userID} from "../../modules/consts.js";
import { SortSelect } from "../../components/sort-select/index.js";

export class MainPage {
    constructor(parent) {
        this.parent = parent;
    }

    getData(sortType = 'id_asc') {
        const url = urls.getGroupMembersSort(groupId, sortType);
    
        ajax.post(url, (data) => {
            this.renderData(data.response.items);
        });
    }

    getData2() {
        const url = urls.getFriendsList(userID);
    
        ajax.post(url, (data) => {
            this.renderData2(data.response.items);
        });
        
    }

    renderData(items) {
        items.forEach((item) => {
            const productCard= new ProductCardComponent(this.pageRoot)
            productCard.render(item, this.clickCard.bind(this))
        })
    }
    
    renderData2(items) {
        items.forEach((item) => {
            if ((item.city && item.city.title === "Москва") && item.sex === 2) {
                this.pageRoot.insertAdjacentHTML('beforeend', '<div></div>');
                const productComponent = new ProductComponent(this.pageRoot)
                productComponent.render(item)
            }
        });
    }
    
    

    get pageRoot() {
        return document.getElementById("main-page");
    }

    getHTML() {
        return `
            <div id="main-page" class="d-flex flex-wrap" style="width: 1000px;"></div>
        `;
    }

    clickCard(e) {
        const cardId = e.target.dataset.id;
        console.log("pressed ", cardId);

        const productPage = new ProductPage(this.parent, cardId);
        productPage.render();
    }

    handler(sortType) {
        Array.from(document.getElementsByClassName('card')).forEach((item) => {
            item.remove()
        })
        this.getData(sortType)
        this.getData2()
    }

    render() {
        this.parent.innerHTML = ''
        const html = this.getHTML()
        this.parent.insertAdjacentHTML('beforeend', html)

        const selectOption = new SortSelect(this.pageRoot);
        selectOption.render(this.handler.bind(this));

        this.getData()
        this.getData2()
    }   
}