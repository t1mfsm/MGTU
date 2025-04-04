// pages/main/index.js
import { ProductPage } from "../product/index.js";

export class MainPage {
    constructor(parent) {
        this.parent = parent;
        this.currentIndex = 0; // текущий индекс отображаемой акции
    }

    getData() {
        return [
            {
                id: 1,
                src: "https://static.orgpage.ru/newsphotos/ff/ff945141ef1544739e5162995d272921.jpg",
                title: "Акция",
                text: "Такой акции вы еще не видели 1"
            },
            {
                id: 2,
                src: "https://ochisto.ru/images/5e6df0as-960.jpg",
                title: "Акция",
                text: "Такой акции вы еще не видели 2"
            },
            {
                id: 3,
                src: "https://kredit-on.ru/wp-content/uploads/5/e/e/5ee5c2b1c18c3f4f35e70f67cdeacc29.jpeg",
                title: "Акция",
                text: "Такой акции вы еще не видели 3"
            },
        ];
    }

    render() {
        const data = this.getData();
        this.renderProductPage(this.currentIndex, data);
    }

    renderProductPage(index, data) {
        const productPage = new ProductPage(this.parent, data[index], this.showNext.bind(this), this.showPrev.bind(this));
        productPage.render();
    }

    showNext() {
        const data = this.getData();
        this.currentIndex = (this.currentIndex + 1) % data.length;
        this.renderProductPage(this.currentIndex, data);
    }

    showPrev() {
        const data = this.getData();
        this.currentIndex = (this.currentIndex - 1 + data.length) % data.length;
        this.renderProductPage(this.currentIndex, data);
    }
}
