// pages/product/index.js
import { ProductComponent } from "../../components/product/index.js";
import { NextButtonComponent } from "../../components/next-button/index.js";
import { PrevButtonComponent } from "../../components/prev-button/index.js";

export class ProductPage {
    constructor(parent, data, nextListener, prevListener) {
        this.parent = parent;
        this.data = data;
        this.nextListener = nextListener;
        this.prevListener = prevListener;
    }

    getHTML() {
        return `
            <div id="product-page" class="product-page-container"></div>
        `;
    }

    render() {
        this.parent.innerHTML = '';
        const html = this.getHTML();
        this.parent.insertAdjacentHTML('beforeend', html);

        const prevButton = new PrevButtonComponent(this.pageRoot);
        prevButton.render(this.prevListener);

        const nextButton = new NextButtonComponent(this.pageRoot);
        nextButton.render(this.nextListener);

        const stock = new ProductComponent(this.pageRoot);
        stock.render(this.data);
    }

    get pageRoot() {
        return document.getElementById('product-page');
    }
}
